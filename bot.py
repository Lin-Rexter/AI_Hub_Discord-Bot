# coding=utf-8
import os
import sys
import time
import random
import json
import asyncio
import numpy as np
from typing import List

# py-cord
import discord
from discord.ext import commands, tasks

# Google - Bard AI聊天
from src.Google.Bard_Chat import Bard_Reply

# OpenAI - ChatGPT(ChatGPT-3.5) AI聊天
from src.OpenAI.ChatGPT_3 import ChatGPT_Reply

# Microsoft - EdgeGPT(ChatGPT-4) AI聊天
from src.Microsoft.Bing_EdgeGPT_4 import EdgeGPT_Reply

# OpenAI - DALL·E 2 AI生成圖像
from src.OpenAI.DALL_E import DALL_E_Reply

# Microsoft - Bing Image Creator(結合DALL-E) AI生成圖像
from src.Microsoft.Bing_Image_Creator import Image_Creator_Reply

# 翻譯器
from deep_translator import GoogleTranslator

# 讀取.env檔
from dotenv import load_dotenv

# 讀取.env檔環境變量
load_dotenv('.env')

# 獲取Line Bot的TOKEN、 SECRET
Discord_Token = os.getenv('DISCORD_TOKEN', None)

if not Discord_Token:
    raise Exception('\nPlease set the DISCORD_TOKEN environment variable in the .env file.\n請在.env檔設置DISCORD_TOKEN環境變量。\n')
    sys.exit(1)


# Discord Bot 權限設置(Intents)
intents = discord.Intents.default()
intents.messages  = True
intents.message_content = True # discord.ext
intents.members = True

# 創建Bot物件
client = discord.Bot(intents=intents) # py-cord


# Your Discord ID(if you are the manager of this discord bot, modify it or delete)
global Admin_ID
Admin_ID = 824171370228744232

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

    embed.add_field(name="🤖 /gpt", value="✅ <prompts[對話]>\n✅ <api_key[OpenAI的API Key]>\n✅ <role[用戶(默認), 系統, 助手]>\n✅ <engine[gpt-3.5-turbo(默認), gpt-4, gpt-4-32k]>\n✅ <top_p>\n✅ <temperature>\n✅ <presence_penalty>\n✅ <frequency_penalty>\n✅ <reply_count>", inline=False)
    embed.add_field(name="🤖 /gpt4", value="✅ <創意, 平衡(默認), 精確>\n✅ <對話>", inline=False)
    embed.add_field(name="🎨 /img", value="✅ <圖片描述>\n✅ <width>\n✅ <height>", inline=False)
    embed.add_field(name="", value="> **<width>跟<height>默認都為1024**", inline=False)
    embed.add_field(name="🎨 /dall", value="✅ <api_key>\n✅ <parameter>\n✅ <size>\n✅ <圖片描述>", inline=False)
    embed.add_field(name="", value="> **Ex: sk-xxx 1 256/512/1024 cute cat**", inline=False)
    embed.add_field(name="", value="-----------------------------------------", inline=False)
    embed.add_field(name="⚠️ Notice: ", value="> **<>括號不用打，默認表示未指定模式時所採用。**", inline=False)
    embed.add_field(name="", value="> **各指令有專屬頻道以及教學。**", inline=False)
 
    embed.set_footer(text="@Wen Jin | AI-Hub-ChatGPT")
    embed.set_author(name="AI-Hub-ChatGPT", icon_url="https://forklog.com/wp-content/uploads/OpenAI-min.webp")
    embed.set_thumbnail(url="https://forklog.com/wp-content/uploads/OpenAI-min.webp")
    embed.set_image(url="https://forklog.com/wp-content/uploads/OpenAI-min.webp")
 
    await ctx.respond(f"Hello {ctx.author.mention} 這是指令教學", embed=embed)


# ChatGPT-3
@client.slash_command(description="與ChatGPT-3.5、 4聊天")
async def gpt(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="你要與ChatGPT聊的內容"),
        api_key: discord.Option(str, description="OpenAI的API Key") = None,
        role: discord.Option(str, choices=["用戶", "系統", "助手"], default="用戶", description="ChatGPT的角色，預設為: 用戶") = None,
        engine: discord.Option(str, choices=["gpt-3.5-turbo", "gpt-4", "gpt-4-32k"], default="gpt-3.5-turbo", description="GPT模型，預設為: gpt-3.5-turbo") = None,
        top_p: discord.Option(float, choices=[x/10 for x in range(0, 11)], default=1.0, description="過濾生成的詞彙，保留最有可能的回答，數值越高過濾越少，預設值為: 1.0") = None,
        temperature: discord.Option(float, choices=[x/10 for x in range(0, 11)], default=0.5, description="控制回答生成的多樣性和隨機性，數值越高越隨機，預設值為: 0.5") = None,
        presence_penalty: discord.Option(float, default=0, description="設置生成的現有詞彙懲罰程度，數值越高重複性降低、多樣性提高，預設值為:0，範圍: -2.0~2.0") = None,
        frequency_penalty: discord.Option(float, default=0, description="設置生成的詞彙頻率懲罰程度，數值越高生成的內容裡重複詞彙越少，預設值為:0，範圍: -2.0~2.0") = None,
        reply_count: discord.Option(int, default=1, description="回答的次數，預設值: 1") = None
    ):

    # 延遲
    await ctx.defer()

    # 使用者完整命令
    commands = {
        "user_id": ctx.author.id,
        "prompts": prompts,
        "role": role,
        "engine": engine,
        "top_p": temperature,
        "temperature": temperature,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "reply_count": reply_count
    }

    print(f"\n\n使用者完整命令: /gpt \n{beauty_dict(data=commands, indent_value=2, utf_8=True)}")

    result = ChatGPT_Reply(*list(commands.values())[1:], api_key) # 不傳入user_id

    if(isinstance(result, list)):
        if(result[0] == "Error"):
            result = f"⚠️ {result[1]}"
        elif(result[0] == "Dangerous"):
            result = f"⚡🚧⚡ {result[1]} \n <@{Admin_ID}>已排入修復行程!"

    print(f"\n命令結果: {result}") # 命令結果

    await ctx.respond(result, ephemeral=True)


# BingGPT(GPT-4)
@client.slash_command(description="與BingGPT(GPT-4)聊天")
async def gpt4(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="你要與Bing ChatGPT聊的內容"),
        role:discord.Option(str, choices=["創意", "平衡", "精確"], default="平衡") = None
    ):

    await ctx.defer()
    print(f"\n\n使用者完整命令: /gpt4 {prompts} {role}") # 使用者完整命令
    print(f"\n命令的值: {prompts}") # 命令的值

    result = await EdgeGPT_Reply(prompts, role)
    print(f"\n命令結果: {result}") # 命令結果

    await ctx.respond(result, ephemeral=True)


# Google Bard
@client.slash_command(description="與Google Bard聊天")
async def bard(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="你要與Google Bard聊的內容"),
        token: discord.Option(str, description="Google Bard的Token")
    ):

    await ctx.defer()
    print(f"\n\n使用者完整命令: /bard {prompts}") # 使用者完整命令

    result = Bard_Reply(prompts)
    if(isinstance(result, list)):
        if(result[0] == "Error"):
            result = f"⚠️ {result[1]}"

    print(f"\n命令結果: {result}") # 命令結果

    await ctx.respond(result, ephemeral=True)


# Bing Image Creator
@client.slash_command(description="使用Bing Image Creator AI繪圖")
async def img(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="圖片的描述"),
        width:discord.Option(int, choices=[w for w in range(1024, 1, -41)], min_value=1, max_value=1024, default=1024) = None,
        height:discord.Option(int, choices=[h for h in range(1024, 1, -41)], min_value=1, max_value=1024, default=1024) = None
    ):

    await ctx.defer()
    print(f"\n\n使用者完整命令: /img {prompts}") # 使用者完整命令
    print(f"\n命令的值: {prompts}") # 命令的值

    result = Image_Creator_Reply(prompts, width, height)
    img_list = result[1]

    print(f"\n命令結果: {img_list}") # 命令結果

    if(isinstance(result[1], list)):
        embed_list = []
        for img in img_list:
            embed_list.append(discord.Embed(
                    title="🎨 Bing Image Creator",
                    description="生成結果",
                    color=discord.Colour.random(),
                    url="https://forklog.com/wp-content/uploads/OpenAI-min.webp").set_image(url=img)
                )

        await ctx.respond(embeds=embed_list, ephemeral=True)
    else:
        await ctx.respond(result[1], ephemeral=True)


# OpenAI DALL-E 2
@client.slash_command(description="使用OpenAI DALL·E-2 AI繪圖")
async def dall(
        ctx:discord.ApplicationContext,
        prompts: discord.Option(str, description="圖片的描述"),
        api_key: discord.Option(str, description="OpenAI的API Key"),
        parameter: discord.Option(int, description="指定生成的圖片數量，預設值: 1", default=1) = None,
        size: discord.Option(int, description="圖片的大小: 256x256, 512x512, 1024x1024， 預設值: 256x256", choices=[256, 512, 1024], default=256) = None
    ):

    # 延遲
    await ctx.defer()

    # 使用者完整命令
    commands = {
        "user_id": ctx.author.id,
        "prompts": prompts,
        "parameter": parameter,
        "size": size
    }

    print(f"\n\n使用者完整命令: /dall \n{beauty_dict(data=commands, indent_value=2, utf_8=True)}")

    result = DALL_E_Reply(*list(commands.values())[1:], api_key) # 不傳入user_id

    if(result[0] == "Error"):
        await ctx.respond(f"⚠️ {result[1]}", ephemeral=True)
    elif(result[0] == "Dangerous"):
        await ctx.respond(f"⚡🚧⚡ {result[1]} \n <@{Admin_ID}>已排入修復行程!", ephemeral=True)
    else:
        img_list = result[1]
        embed_list = []

        for img in img_list:
            embed_list.append(discord.Embed(
                    title="🎨 DALL·E - 2",
                    description="生成結果",
                    color=discord.Colour.random(),
                    url="https://forklog.com/wp-content/uploads/OpenAI-min.webp").set_image(url=img)
                )

        print(f"\n命令結果: {img_list}") # 命令結果

        await ctx.respond(embeds=embed_list, ephemeral=True)

# 翻譯處理
def translate(texts):
    translated = GoogleTranslator(source='auto', target='en').translate(texts)
    print("\n翻譯結果: " + translated + "\n")
    return translated

# 排版dict
def beauty_dict(data:dict, indent_value:int, utf_8:bool):
    if(utf_8):
        return json.dumps(data, indent=indent_value, ensure_ascii=False).encode('utf8').decode()
    else:
        return json.dumps(data, indent=indent_value)


if __name__ == "__main__":
    client.run(Discord_Token)