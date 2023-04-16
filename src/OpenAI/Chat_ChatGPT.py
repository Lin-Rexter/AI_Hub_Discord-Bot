import os
from pathlib import Path
from dotenv import load_dotenv
# https://github.com/acheong08/ChatGPT#v3-official-chat-api
from revChatGPT.V3 import Chatbot

# take environment variables from .env
env_path = os.path.join(Path(__file__).resolve().parents[2],'.env')

load_dotenv(env_path)

# take OpenAI API Key from environment variables
Openai_API_Key = os.getenv('OPENAI_API_KEY') or None

# take ChatGPT's default model from environment variables
ChatGPT_Model= os.getenv('CHATGPT_MODEL') or None

chatbot = Chatbot(
        api_key = Openai_API_Key
    )

async def ChatGPT_Reply(**kwargs) -> list:
    try:
        for key, value in kwargs.items():
            globals()[key] = value

        chatbot.api_key = api_key or Openai_API_Key or None
        chatbot.engine = model or ChatGPT_Model or None
        chatbot.top_p: float = top_p                         # 0.0 ~ 1.0, https://platform.openai.com/docs/api-reference/chat/create#chat/create-top_p
        chatbot.temperature: float = temperature             # 0.0 ~ 2.0, https://platform.openai.com/docs/api-reference/chat/create#chat/create-temperature
        chatbot.presence_penalty: float = presence_penalty   # -2.0 ~ 2.0, https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty
        chatbot.frequency_penalty: float = frequency_penalty # -2.0 ~ 2.0, https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty
        chatbot.reply_count: int = reply_count               # 1~, https://platform.openai.com/docs/api-reference/completions/create#completions/create-n

        # Rollback the conversation
        if rollback > 0:
            chatbot.rollback(rollback)

        # Reset the conversation
        if reset:
            chatbot.reset()

        GPT_Role = {
            "系統": "system",
            "用戶": "user",
            "助手": "assistant"
        }

        Role = GPT_Role[role]

        if chatbot.api_key is None:
            reply = ['Error', "Oops❗ 尚未指定API Key"]
        else:
            if chatbot.engine is None:
                print("\nError❗ .env檔尚未指定模型名稱，因此使用預設模型gpt-3.5-turbo")
                chatbot.engine = "gpt-3.5-turbo"
            elif chatbot.engine not in ["gpt-3.5-turbo", "gpt-4", "gpt-4-32k"]:
                print("\nError❗ wrong ChatGPT model name in .env file.\n錯誤❗ .env檔設定的ChatGPT model名稱錯誤，因此使用預設模型gpt-3.5-turbo")
                chatbot.engine = "gpt-3.5-turbo"

            reply_text = await chatbot.ask_async(prompts, role=Role)
            reply = ['Success', reply_text]

        return reply
    except Exception as e:
        print("\nError: ", e)
        if "pop from empty list" in str(e):
            return ['Error', "Oops❗ 退回的次數超過對話總次數，如要退回所有次數，請使用reset指令"]
        else:
            return ['Error', "Oops❗ 你的API Key似乎無效或過期，你可能需要再去重新生成或重新輸入正確的API Key"]