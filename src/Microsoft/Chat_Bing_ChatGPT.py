import os
import sys
#import contextlib
from dotenv import load_dotenv
from pathlib import Path
from EdgeGPT import Chatbot, ConversationStyle

# take cookies.json path
cookie_path = os.path.join(Path(__file__).resolve().parents[2], 'cookies.json')

env_cookies = os.getenv('BING_CHAT_COOKIES') or None

# take environment variables from .env
env_path = os.path.join(Path(__file__).resolve().parents[2],'.env')

load_dotenv(env_path)

env_response_style = os.getenv('RESPONSE_STYLE') or None

'''
if not is_exist:
    sys.exit("\nError: Could not find cookies.json(Bing CgatGPT)\n")

if os.path.getsize(cookie_path) <= 0:
    sys.exit("\nError: cookies.json(Bing CgatGPT) can't empty\n")
'''

'''
# https://docs.python.org/zh-cn/3.8/library/contextlib.html#contextlib.suppress
# 錯誤抑制
with contextlib.suppress(Exception):
'''

bot = Chatbot(cookiePath = cookie_path or env_cookies)

async def EdgeGPT_Reply(**kwargs) -> list:
    try:
        for key, value in kwargs.items():
            globals()[key] = value

        Translator_Style = {
            "CREATIVE": "創意",
            "BALANCED": "平衡",
            "PRECISE": "精確"
        }

        Response_Style = {
            "創意": ConversationStyle.creative,
            "平衡": ConversationStyle.balanced,
            "精確": ConversationStyle.precise
        }
        
        choice_style = style_name or None

        if choice_style is None:
            if env_response_style not in Translator_Style.keys():
                choice_style = "平衡"
            else:
                choice_style = Translator_Style[env_response_style.upper()]

        style = Response_Style[choice_style]

        reply_dict = await bot.ask(prompt=prompts, conversation_style=style)
        reply = reply_dict["item"]["messages"][1]["text"]

        return ["Success", reply]
    except Exception as e:
        print("\nError:", e)
        return ["Dangerous", "Oops❗ 發生例外錯誤! 有可能是未設置cookies.json的關係"]