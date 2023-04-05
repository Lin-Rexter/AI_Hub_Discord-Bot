import os
#import openai
from pathlib import Path
# 讀取.env檔
from dotenv import load_dotenv
#第三方作者包裝的官方API
from revChatGPT.V3 import Chatbot


# 讀取.env檔環境變量
env_path = Path(__file__).resolve().parents[3] / '.env'
load_dotenv(env_path)

# 獲取OpenAI Api的Key
Openai_API_Key = os.getenv('OPENAI_API_KEY', None)
ChatGPT_Model= os.getenv('CHATGPT_MODEL', None)

'''
if not Openai_Api_Key:
    raise Exception('Please set the OPENAI_API_KEY environment variable in the .env file.\n請在.env檔設置OPENAI_API_KEY環境變量。\n')
    sys.exit(1)
'''

chatbot = Chatbot(
        api_key = Openai_API_Key
    )

gpt_role = {
    "用戶": "user",
    "系統": "system",
    "助手": "assistant"
}

def ChatGPT_Reply(Texts, role=None, engine=None,top_p=None, temperature=None, presence_penalty=None, frequency_penalty=None, reply_count=None, API_Key=None) -> str:
    try:
        chatbot.api_key = API_Key or Openai_API_Key or None
        chatbot.engine = engine or ChatGPT_Model or None
        chatbot.top_p: float = top_p               # 0.0 ~ 1.0
        chatbot.temperature: float = temperature   # 0.0 ~ 2.0，數值越高越多樣化
        chatbot.presence_penalty: float = presence_penalty     # -2.0 ~ 2.0
        chatbot.frequency_penalty: float = frequency_penalty   # -2.0 ~ 2.0
        chatbot.reply_count: int = reply_count   # 回應次數 1~

        Role = gpt_role[role]

        print("\n角色: " + Role)

        if chatbot.api_key == None:
            reply_text = ['Error', "尚未指定API Key"]
        elif chatbot.engine == None:
            reply_text = ['Error', "尚未指定模型名稱"]
        else:
            reply_text = chatbot.ask(Texts, role=Role)

        return reply_text
    except UnboundLocalError as e:
        print("\n", e)
        return ['Dangerous', "Oops❗ 發生了例外錯誤..."]
    except Exception as e:
        print("\n", e)
        return ['Error', "請確認Api Key或是模型名稱是否正確"]

"""
#官方API
openai.api_key = Openai_Api_Key

gpt_role = {
    "用戶": "user",
    "系統": "system",
    "助手": "assistant"
}

def ChatGPT_Reply(Ask) -> str:
    role_name = Ask.split(" ")[0].strip() # ChatGPT角色

    if role_name in gpt_role:
        Ask_prompt = Ask.split(" ")[1].strip() # 使用者輸入的對話
        role = gpt_role[role_name]
    else:
        Ask_prompt = Ask
        role = "user"

    print("\n角色: " + role)

    completion = openai.ChatCompletion.create(
        model=ChatGPT_Model,
        messages=[
            {"role": role, "content": Ask_prompt}
        ]
    )

    return completion.choices[0].message["content"].encode().decode('utf-8')
"""
