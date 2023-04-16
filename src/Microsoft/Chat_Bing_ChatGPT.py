import os
import sys
from pathlib import Path
from EdgeGPT import Chatbot, ConversationStyle

# take cookies.json path
cookie_path = os.path.join(Path(__file__).resolve().parents[2], 'cookies.json')

# check whether cookies.json file exists
is_exist = os.path.exists(cookie_path) and os.path.isfile(cookie_path)

if not is_exist:
    sys.exit("\nError: Could not find cookies.json(Bing CgatGPT)\n")

if os.path.getsize(cookie_path) <= 0:
    sys.exit("\nError: cookies.json(Bing CgatGPT) can't empty\n")

bot = Chatbot(cookiePath=cookie_path)

async def EdgeGPT_Reply(**kwargs) -> list:
    try:
        for key, value in kwargs.items():
            globals()[key] = value

        Response_Style = {
            "創意": ConversationStyle.creative,
            "平衡": ConversationStyle.balanced,
            "精確": ConversationStyle.precise
        } 

        style = Response_Style[style_name]

        reply_dict = await bot.ask(prompt=prompts, conversation_style=style)
        reply = reply_dict["item"]["messages"][1]["text"]

        return ["Success", reply]
    except Exception as e:
        print("\nError:", e)
        return ["Dangerous", "Oops❗ 發生例外錯誤!"]