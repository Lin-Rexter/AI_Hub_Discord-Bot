import os
# 官方API
import openai
from pathlib import Path
# 讀取.env檔
from dotenv import load_dotenv

# 讀取.env檔環境變量
env_path = Path(__file__).resolve().parents[3] / '.env'
load_dotenv(env_path)

# 獲取OpenAI Api的Key
Openai_API_Key = os.getenv('OPENAI_API_KEY', None)


size_dict = {
    256: "256x256",
    512: "512x512",
    1024: "1024x1024"
}

def DALL_E_Reply(prompts, parameter=None, size=None, API_Key=None) -> list:
    try:
        openai.api_key = API_Key or Openai_API_Key or None
        
        if openai.api_key == None:
            return ["Error", "Oops❗ 尚未指定API Key"]
        else:
            image_list = []
            image = openai.Image.create(
                prompt = prompts,       # 圖片描述
                n = parameter,          # 圖片數量
                size = size_dict[size]  # 圖片大小 256x256, 512x512, 1024x1024 pixels
            )

            for Dict in image['data']:
                image_list.append(str(Dict['url']))

            return [prompts, image_list]
    except openai.error.APIError as e:
        print("\n", e)
        return ["Error", "Oops❗ OpenAI的伺服器出了問題，請短暫等待後重試!"]
    except openai.error.TryAgain as e:
        print("\n", e)
        return ["Error", "Oops❗ 請再重新試一次!"]
    except openai.error.Timeout as e:
        print("\n", e)
        return ["Error", "Oops❗ 請求超時，有可能是網路問題，請再重新試一次!"]
    except openai.error.APIConnectionError as e:
        print("\n", e)
        return ["Error", "Oops❗ 無法與OpenAI連線，有可能是網路問題，請再重新試一次!"]
    except openai.error.InvalidRequestError as e:
        print("\n", e)
        return ["Error", "Oops❗ 發送的數據不完整或缺少了參數，請查看API Key是否正確!"]
    except openai.error.AuthenticationError as e:
        print("\n", e)
        return ["Error", "Oops❗ 你的API Key似乎無效或過期，你可能需要再重新生成一個或是重新輸入正確的API Key!"]
    except openai.error.RateLimitError as e:
        print("\n", e)
        return ["Error", "Oops❗ 慢一點，發送的速率過快!"]
    except openai.error.ServiceUnavailableError as e:
        print("\n", e)
        return ["Error", "Oops❗ OpenAI的伺服器無法處理請求，目前可能流量過高，請稍後再重試!"]
    except UnicodeEncodeError as e:
        print("\n", e)
        return ["Error", "Oops❗ 請確認輸入的API Key格式是否正確!"]
    except Exception as e:
        print("\n", e)
        return ["Dangerous", "Oops❗ 發生了例外錯誤..."]