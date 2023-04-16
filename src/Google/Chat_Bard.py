import os
from pathlib import Path
from dotenv import load_dotenv
from Bard import Chatbot

# take environment variables from .env
env_path = os.path.join(Path(__file__).resolve().parents[2],'.env')

load_dotenv(env_path)

# take Bard token("__Secure-1PSID" cookie) from environment variables
env_bard_token = os.getenv('BARD_TOKEN') or None


def Bard_Reply(**kwargs) -> list:
    try:
        for key, value in kwargs.items():
            globals()[key] = value

        session = bard_token or env_bard_token or None

        if session is None:
            return ["Error", "Oops❗ 尚未指定Bard token"]
        
        chatbot = Chatbot(session)

        reply = chatbot.ask(message = prompts)['content']

        return ["Success", reply]
    except Exception as e:
        print("\nError: ", e)
        return ['Error', "Oops❗ 請確認Bard token是否有效或格式無誤"]