import os
from pathlib import Path
# 讀取.env檔
from dotenv import load_dotenv
from Bard import Chatbot

# 讀取.env檔環境變量
env_path = Path(__file__).resolve().parents[3] / '.env'
load_dotenv(env_path)

# 獲取Bard的Token
Bard_Token = os.getenv('BARD_TOKEN', None)

def Bard_Reply(Texts) -> str:
    try:
        chatbot = Chatbot(Bard_Token)

        return chatbot.ask(Texts)
    except Exception as e:
        print("\n", e)
        return ['Error', "請確認Bard Token是否正確"]