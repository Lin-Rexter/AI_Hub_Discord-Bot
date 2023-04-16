# coding=utf-8
import os
import sys
import time
import datetime
import random
import json
import asyncio
import numpy as np
from typing import List
from dotenv import load_dotenv

# py-cord
import discord
from discord.ext import commands, tasks

# OpenAI(ChatGPT, DALL·E-2)
from src.OpenAI import (
        ChatGPT_Reply,
        DALL_E_Reply
    )

# Microsoft(Bing ChatGPT, Bing Image Creator)
from src.Microsoft import (
        EdgeGPT_Reply,
        Image_Creator_Reply
    )

# Google(Bard)
from src.Google import Bard_Reply

# Translator
from deep_translator import GoogleTranslator


# take environment variables from .env
env_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".env")

load_dotenv(env_path)

# take Discord Bot token from environment variables
Discord_Token = os.getenv('DISCORD_TOKEN') or None

# take Discord Administrator ID from environment variables
Administrator_ID = os.getenv('DISCORD_ADMIN_ID') or None

if Discord_Token is None:
    sys.exit("\nError❗: Please set the DISCORD_TOKEN environment variable in the .env file\n請在.env檔設置DISCORD_TOKEN環境變量。\n")

if Administrator_ID is None:
    print("\n⚠️ You did not set Administrator_ID in .env file\n⚠️ .env檔尚未設置Administrator_ID\n")

# Discord Bot Intents(權限設置)
intents = discord.Intents.default()
intents.message_content = True # discord.ext
intents.members = True

# py-cord, 創建Bot物件
client = discord.Bot(intents=intents)

# Discord Administrator ID
global Admin_ID
Admin_ID = Administrator_ID


@tasks.loop(seconds=random.randint(2, 6))
async def change_status():
    new_status = random.choice(
                [
                    "I want more...",
                    "You can't stop me!",
                    "Hello World!",
                    "YOU!!!",
                    "Life game..."
                ]
            )

    await client.change_presence(status = discord.Status.online, activity = discord.Game(new_status))


@client.event # 呼叫event函式庫
async def on_ready(): # 當bot完成啟動時
    change_status.start()

    print(f'We have logged in as {client.user}')


# /help 幫助
@client.slash_command(description="查看指令")
async def help(ctx):
    embed = discord.Embed(
        title="指令表",
        description="各種指令用法介紹",
        color=discord.Colour.blurple()
    )

    embed.add_field(name="🤖 /gpt [ChatGPT]", value="✅ <prompts[對話]>\n✅ <api_key[OpenAI的API Key]>\n✅ <role[system, user(Default), assistant]>\n✅ <engine[gpt-3.5-turbo(Default), gpt-4, gpt-4-32k]>\n✅ <top_p>\n✅ <temperature>\n✅ <presence_penalty>\n✅ <frequency_penalty>\n✅ <reply_count>\n✅ <rollback[Rollback the conversation by n messages]>\n✅ <reset[Reset the conversation]>", inline=False)
    embed.add_field(name="🤖 /gpt4 [Bing ChatGPT]", value="✅ <prompts[對話]>\n✅ <style[creative, balanced(Default), precise]>", inline=False)
    embed.add_field(name="🤖 /bard [Google Bard]", value="✅ <prompts[對話]>\n✅ <token[SESSION('__Secure-1PSID' cookie]>", inline=False)
    embed.add_field(name="", value="> **Join the waitlist for Bard: [https://bard.google.com](https://bard.google.com)**", inline=False)
    embed.add_field(name="🎨 /img [Bing Image Creator]", value="✅ <prompts[圖片描述]>\n✅ <width>\n✅ <height>\n✅ <auth_cookies>", inline=False)
    embed.add_field(name="", value="> **<width>跟<height>: 1024px**", inline=False)
    embed.add_field(name="🎨 /dall [DALL·E 2]", value="✅ <prompts[圖片描述]>\n✅ <api_key>\n✅ <size>\n✅ <parameter[The number of images to generate(1 ~ 10)]>", inline=False)
    embed.add_field(name="", value="> **Ex: sk-xxx 1 256/512/1024 cute cat**", inline=False)
    embed.add_field(name="", value="-----------------------------------------", inline=False)
    embed.add_field(name="⚠️ Notice: ", value="> **<>、[]括號不用打，默認表示未指定模式時所採用。**", inline=False)
    embed.add_field(name="", value="> **各指令有專屬頻道以及教學。**", inline=False)
 
    now = datetime.datetime.now()
    embed.set_footer(text=f"@Wen Jin | AI-Hub-ChatGPT\nAI-Hub-ChatGPT Github: https://github.com/Lin-Rexter/AI_Hub_Discord-Bot\nTime: {now.strftime('%H:%M')}")
    embed.set_author(name="AI-Hub-ChatGPT", icon_url="https://forklog.com/wp-content/uploads/OpenAI-min.webp")
    embed.set_thumbnail(url="https://forklog.com/wp-content/uploads/OpenAI-min.webp")
    embed.set_image(url="https://forklog.com/wp-content/uploads/OpenAI-min.webp")
 
    await ctx.respond(f"Hello {ctx.author.mention} 這是指令表", embed=embed)


# ChatGPT-3.5, 4
@client.slash_command(description="與ChatGPT-3.5, ChatGPT-4聊天")
async def gpt(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="你要與ChatGPT聊的內容"),
        api_key: discord.Option(str, description="OpenAI的API Key") = None,
        role: discord.Option(str, choices=["用戶", "系統", "助手"], default="用戶", description="ChatGPT的角色，預設為: 用戶") = None,
        model: discord.Option(str, choices=["gpt-3.5-turbo", "gpt-4", "gpt-4-32k"], description="GPT模型，預設: gpt-3.5-turbo") = None,
        top_p: discord.Option(float, choices=[x/10 for x in range(0, 11)], default=1.0, description="過濾生成的詞彙，保留最有可能的回答，數值越高過濾越少，預設值為: 1.0") = None,
        temperature: discord.Option(float, choices=[x/10 for x in range(0, 11)], default=0.5, description="控制回答生成的多樣性和隨機性，數值越高越隨機，預設值為: 0.5") = None,
        presence_penalty: discord.Option(float, default=0, description="設置生成的現有詞彙懲罰程度，數值越高重複性降低、多樣性提高，預設值為:0，範圍: -2.0~2.0") = None,
        frequency_penalty: discord.Option(float, default=0, description="設置生成的詞彙頻率懲罰程度，數值越高生成的內容裡重複詞彙越少，預設值為:0，範圍: -2.0~2.0") = None,
        reply_count: discord.Option(int, default=1, description="回答的次數，預設值: 1") = None,
        rollback: discord.Option(int, default=0, description="要退回的對話次數，預設值: 0") = None,
        reset: discord.Option(bool, default=False, choices=[True, False], description="重置所有對話") = None
    ):

    # 延遲
    await ctx.defer()

    # 使用者完整命令
    Commands = {
        "user_id": ctx.author.id,
        "prompts": prompts,
        "api_key": api_key,
        "role": role,
        "model": model,
        "top_p": temperature,
        "temperature": temperature,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "reply_count": reply_count,
        "rollback": rollback,
        "reset": reset
    }

    await Commands_Hub(ctx, Commands, ChatGPT_Reply, True, "chat")


# Bing ChatGPT(GPT-4)
@client.slash_command(description="與Bing ChatGPT(GPT-4)聊天")
async def gpt4(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="你要與Bing ChatGPT聊的內容"),
        style:discord.Option(str, choices=["創意", "平衡", "精確"], description="對話風格，預設: 平衡") = None
    ):

    # 延遲
    await ctx.defer()

    # 使用者完整命令
    Commands = {
        "user_id": ctx.author.id,
        "prompts": prompts,
        "style_name": style
    }

    await Commands_Hub(ctx, Commands, EdgeGPT_Reply, True, "chat")


# Google Bard
@client.slash_command(description="與Google Bard聊天")
async def bard(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="你要與Google Bard聊的內容"),
        token = None
    ):

    # 延遲
    await ctx.defer()

    # 使用者完整命令
    Commands = {
        "user_id": ctx.author.id,
        "prompts": prompts,
        "bard_token": token
    }

    await Commands_Hub(ctx, Commands, Bard_Reply, False, "chat")


# Bing Image Creator
@client.slash_command(description="使用Bing Image Creator AI繪圖")
async def img(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="圖片的描述"),
        width: discord.Option(int, choices=[w for w in range(1024, 1, -41)], min_value=1, max_value=1024, default=1024, description="圖片寬度") = None,
        height: discord.Option(int, choices=[h for h in range(1024, 1, -41)], min_value=1, max_value=1024, default=1024, description="圖片高度") = None,
        auth_cookies: discord.Option(str, description="_U auth cookie") = None
    ):

    # 延遲
    await ctx.defer()

    # 使用者完整命令
    Commands = {
        "user_id": ctx.author.id,
        "prompts": prompts,
        "width": width,
        "height": height,
        "auth_cookies": auth_cookies
    }

    await Commands_Hub(ctx, Commands, Image_Creator_Reply, True, "image")


# OpenAI DALL-E 2
@client.slash_command(description="使用OpenAI DALL·E-2 AI繪圖")
async def dall(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="圖片的描述"),
        api_key: discord.Option(str, description="OpenAI的API Key") = None,
        parameter: discord.Option(int, description="指定生成的圖片數量，預設值: 1", default=1) = None,
        size: discord.Option(int, description="圖片的大小: 256x256, 512x512, 1024x1024， 預設值: 256x256", choices=[256, 512, 1024], default=256) = None
    ):

    # 延遲
    await ctx.defer()

    # 使用者完整命令
    Commands = {
        "user_id": ctx.author.id,
        "api_key": api_key,
        "prompts": prompts,
        "parameter": parameter,
        "size": size
    }

    await Commands_Hub(ctx, Commands, DALL_E_Reply, False, "image")


# translate languages
def translate(prompts, source_lang, target_lang):
    translated = GoogleTranslator(source=source_lang, target=target_lang).translate(prompts)
    print("\n翻譯結果: " + translated + "\n")
    return translated


# prints nicely formatted dictionary
def beauty_dict(data:dict, indent_value:int, utf_8:bool, sort:bool = False):
    if(utf_8):
        return json.dumps(data, indent=indent_value, ensure_ascii=False, sort_keys=sort).encode('utf8').decode()
    else:
        return json.dumps(data, indent=indent_value, sort_keys=sort)


# commands 處理
async def Commands_Hub(Ctx, Commands_Dict:dict, Function_Name:str, Async:bool, Reply_Type:str):
    hidden_key = ['user_id', 'api_key', 'bard_token', 'auth_cookies']
    print(f"\n\n使用者輸入: \n{beauty_dict(data={k: v for k, v in Commands_Dict.items() if k not in hidden_key}, indent_value=2, utf_8=True)}")

    if Async:
        result = await Function_Name(**dict(list(Commands_Dict.items())[1:]))
    else:
        result = Function_Name(**dict(list(Commands_Dict.items())[1:]))

    if(result[0] == 'Success'):
        if Reply_Type == "chat":
            result = f"<@{Commands_Dict['user_id']}>\n{result[1]}"
        elif Reply_Type == 'image':
            embed_list = []

            img_list = result[1]
            
            Title_Dict = {
                DALL_E_Reply: "DALL·E - 2",
                Image_Creator_Reply: "Bing Image_Creator"
            }

            for img in img_list:
                embed_list.append(discord.Embed(
                        title=f"🎨 {Title_Dict[Function_Name]}",
                        description="生成結果",
                        color=discord.Colour.random(),
                        url="https://forklog.com/wp-content/uploads/OpenAI-min.webp").set_image(url=img)
                    )

            result = embed_list
    elif(result[0] == "Error"):
        result = f"<@{Commands_Dict['user_id']}>\n⚠️ {result[1]}"
    elif(result[0] == "Dangerous"):
        result = f"⚡🚧⚡ {result[1]} \n <@{Admin_ID}>已排入修復行程!"

    # 命令結果
    if Reply_Type == 'chat':
        print(f"\n命令結果: {result}")
        await Ctx.respond(result, ephemeral=True)
    elif Reply_Type == 'image':
        print(f"\n命令結果: {img_list}")
        await Ctx.respond(embeds=embed_list, ephemeral=True)


if __name__ == "__main__":
    client.run(Discord_Token) # Run Discord Bot
    asyncio.run(Commands_Hub())