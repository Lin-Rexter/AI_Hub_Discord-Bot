[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)]()

<div align="center">

## 🤖AI-Hub-Discord-Bot🤖
**部署你自己的多AI應用Discord Bot**

<img src="https://user-images.githubusercontent.com/84280745/230615435-2c90c882-f34d-46e4-a140-8d0f69461bd1.gif" alt="Demo">

#### **[[English]](./README.md) [中文]**
</div>

---

## 功能💡
- **🤖[ChatGPT](https://github.com/acheong08/ChatGPT#v3-official-chat-api)**<br>
- **🤖[Bing ChatGPT](https://github.com/acheong08/EdgeGPT#chatbot)**<br>
- **🤖[Google Bard](https://github.com/acheong08/Bard)**<br>
- **🎨[Bing Image Creator](https://github.com/acheong08/EdgeGPT#image-generator)**<br>
- **🎨[DALL·E](https://platform.openai.com/docs/api-reference/images)**<br>
- **[More(coming soon...)](https://replicate.com/explore)**

<details>
  <summary>

## 新消息

  </summary>

**[2023/04/16 10:56]**
- **不小心提交了重要文件，因此刪除了所有提交歷史(79). . .**

**[2023/04/16]**
1. **指令**:
	- /gpt [ChatGPT]:
		* 新增 **`rollback`** 和 **`reset`**, 可以**退回**或**重置**對話
	- /img [Bing Image Creator]:
		* 新增 **`auth_cookies`**, 可以使用自己的cookies
	- /help [指令說明]
		* 更新說明

2. **代碼重構及優化**

</details>

<details>
  <summary>

## 範例🕹️
	  
  </summary>

- ### **🤖ChatGPT**
> ```
> /gpt
> ```
>> <img src="https://user-images.githubusercontent.com/84280745/230544952-6342c67b-e7d6-4fa6-85db-924ed5d4b0da.gif" alt="ChatGPT">

- ### **🤖Bing ChatGPT**
> 
> ```
> /gpt4
> ```
>><img src="https://user-images.githubusercontent.com/84280745/230545509-29f5cb29-9598-4884-b06f-bfcf0bb4d62e.gif" alt="Bing ChatGPT">

- ### **🎨Bing Image Creator**
> ```
> /img
> ```
>><img src="https://user-images.githubusercontent.com/84280745/230546595-5c16f4d7-338c-4793-960e-500981f360bc.gif" alt="Bing Image Creator">

</details>

<details>
  <summary>

## 指令🤖

  </summary>

```
[ChatGPT]:
	/gpt:
	   + <prompts [對話]>
	   
	   + <api_key [OpenAI的API Key]>
	   
	   + <role [系統, 用戶(預設), 助手]>
	   
	   + <model [gpt-3.5-turbo(預設), gpt-4, gpt-4-32k]> # GPT模型
	   
	   + <top_p [0.0~1.0, https://platform.openai.com/docs/api-reference/chat/create#chat/create-top_p]>
	   
	   + <temperature [0.0~2.0, https://platform.openai.com/docs/api-reference/chat/create#chat/create-temperature]>
	   
	   + <presence_penalty [-2.0 ~ 2.0, https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty]>
	   
	   + <frequency_penalty [-2.0 ~ 2.0, https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty]>
	   
	   + <reply_count [Defaults: 1, https://platform.openai.com/docs/api-reference/completions/create#completions/create-n]>
	   
	   + <rollback> [退回n次對話]
	   
	   + <reset> [重置對話]
	   
	   + 更多功能敬請期待...

[Bing ChatGPT]:
	/gpt4:
	   + <prompts [對話]>
	   
	   + <style [創意, 平衡(預設), 精確]> # 對話風格

[Bard]:
	/bard:
	   + <prompts [對話]>
	   
	   + <token [SESSION("__Secure-1PSID" cookie, https://github.com/acheong08/Bard#authentication)]>

[Bing Image Creator]:
	/img:
	   + <prompts [圖片描述]>
	   
	   + <width> # 指定圖片寬度
	   
	   + <height> # 指定圖片高度
	   
	   + <auth_cookies [_U cookie, https://github.com/acheong08/BingImageCreator#getting-authentication]>

[DALL·E]:
	/dall:
	   + <prompts [圖片描述]>
	   
	   + <api_key [OpenAI的API Key]>
	   
	   + <parameter [1~10, https://platform.openai.com/docs/api-reference/images/create#images/create-n]>
	   
	   + <size [256x256, 512x512, 1024x1024]>

[指令說明]:
	/help

More...
```

</details>
	
<details>
  <summary>

## 支持的語言🌎

  </summary>

- **中文**
- **English** (敬請期待...)

</details>

<details>
  <summary>

## 如何創建及部署Discord Bot🚀

  </summary>

- ### 雲端部署
	#### 1. [Railway (最後更新: 2023/04/16)](https://railway.app?referralCode=CCqlpO)
	**[免費計畫](https://docs.railway.app/reference/plans#starter-plan):** 每月提供5.00美元的使用額度、500小時的運行時間(至少20天左右)、512MB的記憶體空間、2顆vCPU和1GB的儲存空間。
	> [![部署至Railway](https://railway.app/button.svg)](https://railway.app/template/9XWCtT?referralCode=CCqlpO)

- ### 本地部署
	#### 1. 拉取此儲存庫
	> ```bash
	> git clone https://github.com/Lin-Rexter/AI_Hub_Discord-Bot.git
	> ```

	#### 2. [設置環境變數](https://github.com/Lin-Rexter/AI_Hub_Discord-Bot/blob/582b427e0e58e4848fab4bf5233fca6936fc18ea/.env)
	> **重新命名 .env.example 檔案為 .env**
	> ```env
	> # Discord:
	> # Discord Bot token # https://discord.com/developers/applications
	> DISCORD_TOKEN = ""
	> # Discord Administrator ID(當使用指令發生例外錯誤時，tag管理者)
	> DISCORD_ADMIN_ID = ""
	>
	> # ChatGPT(官方)、 DALL·E:
	> # [ChatGPT,DALL·E 授權](OpenAI API key) # https://platform.openai.com/account/api-keys
	> OPENAI_API_KEY = ""
	> # 預設 ChatGPT 模型(gpt-3.5-turbo, gpt-4, gpt-4-32k)
	> CHATGPT_MODEL = "gpt-3.5-turbo"
	>
	> # Bing ChatGPT:
	> # 預設 Bing ChatGPT 對話風格(創意, 平衡, 精確)
	> RESPONSE_STYLE = "balanced"
	>
	> # Bing Image Creator:
	> # Bing Image Creator 授權(_U cookie) # https://github.com/acheong08/BingImageCreator#getting-authentication
	> # 如果有設置cookies.json則可以不用設置，設置部分請查看步驟3
	> AUTH_COOKIE = ""
	>
	> # Google Bard:
	> # Google Bard 授權[SESSION("__Secure-1PSID" cookie)] # https://github.com/acheong08/Bard#authentication
	> BARD_TOKEN = ""
	>
	> ### "OPENAI_API_KEY", "AUTH_COOKIE", "BARD_TOKEN", "CHATGPT_MODEL", "RESPONSE_STYLE": 將會首先使用從指令返回的設置
	> ```

	#### 3. [Bing ChatGPT 授權](https://github.com/acheong08/EdgeGPT#getting-authentication-required)
	>1. **重新命名** **cookies.example.json** 檔案為 **cookies.json**
	>2. **將cookies貼到[cookies.json](https://github.com/Lin-Rexter/AI_Hub_Discord-Bot/blob/0c34825b1a26bb47f56c4114cf6947aa53e03719/cookies.json)**

	#### 4. [使用Poetry運行](https://python-poetry.org/docs/#installation)
	> **4-1. 編輯 [poetry 設定檔](https://python-poetry.org/docs/cli/#config)**
	>> 如果你偏好將虛擬空間配置在專案目錄底下
	> ```bash
	> poetry config virtualenvs.in-project true
	> ```

	> **4-2. [安裝套件及依賴](https://python-poetry.org/docs/cli/#install)**
	> ```bash
	> poetry install
	> ```

	> **4-3. [啟用虛擬環境](https://python-poetry.org/docs/cli/#shell)**
	> * 使用 **預設** Python 版本
	> ```bash
	> poetry shell
	> ```
	>
	> * 如果你想 **[指定 Python 版本](https://python-poetry.org/docs/managing-environments/#switching-between-environments)**
	> ```bash
	> poetry env use 3.9
	> ```

	> **4-4. 運行Discord Bot**
	> * 如果上一個步驟有使用 `poetry shell`
	> ```bash
	> python ./bot.py
	> ```
	>
	> * 如果上一個步驟 **沒有使用** `poetry shell`
	> ```bash
	> poetry run python ./bot.py
	> ```

</details>

## License
**[MIT](https://github.com/Lin-Rexter/AI_Hub_Discord-Bot/blob/1902f8e112c3e682ab041c39864d8bb8c7f78a24/LICENSE)**