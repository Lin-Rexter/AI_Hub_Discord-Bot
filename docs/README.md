[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)]()

<div align="center">

## 🤖AI-Hub-Discord-Bot🤖
**Deploy your own multi-AI application Discord bot.**

<img src="https://user-images.githubusercontent.com/84280745/230615435-2c90c882-f34d-46e4-a140-8d0f69461bd1.gif" alt="Demo">

#### **[English] [[中文]](./README_zh-tw.md)**
</div>

---

## Features💡
- **🤖[ChatGPT](https://github.com/acheong08/ChatGPT#v3-official-chat-api)**<br>
- **🤖[Bing ChatGPT](https://github.com/acheong08/EdgeGPT#chatbot)**<br>
- **🤖[Google Bard](https://github.com/acheong08/Bard)**<br>
- **🎨[Bing Image Creator](https://github.com/acheong08/EdgeGPT#image-generator)**<br>
- **🎨[DALL·E](https://platform.openai.com/docs/api-reference/images)**<br>
- **[More(coming soon...)](https://replicate.com/explore)**

<details>
  <summary>

## Example🕹️
	  
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

## Commands🤖

  </summary>

```
[ChatGPT]:
	/gpt:
	   + <prompts [message]>
	   
	   + <api_key [OpenAI API Key]>
	   
	   + <model [System, User(Default), Assistant]>
	   
	   + <engine [gpt-3.5-turbo(Default), gpt-4, gpt-4-32k]> # GPT model
	   
	   + <top_p [0.0~1.0, https://platform.openai.com/docs/api-reference/chat/create#chat/create-top_p]>
	   
	   + <temperature [0.0~2.0, https://platform.openai.com/docs/api-reference/chat/create#chat/create-temperature]>
	   
	   + <presence_penalty [-2.0 ~ 2.0, https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty]>
	   
	   + <frequency_penalty [-2.0 ~ 2.0, https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty]>
	   
	   + <reply_count [Defaults: 1, https://platform.openai.com/docs/api-reference/completions/create#completions/create-n]>
	   
	   + <rollback> [Rollback the conversation by n messages]
	   
	   + <reset> [Reset the conversation]
	   
	   + coming soon...

[Bing ChatGPT]:
	/gpt4:
	   + <prompts [message]>
	   
	   + <style [Creative, Balanced(Default), Precise]> # Conversation style

[Bard]:
	/bard:
	   + <prompts [message]>
	   
	   + <token [SESSION("__Secure-1PSID" cookie, https://github.com/acheong08/Bard#authentication)]>

[Bing Image Creator]:
	/img:
	   + <prompts [image description]>
	   
	   + <width> # Image width
	   
	   + <height> # Image height
	   
	   + <auth_cookies [_U cookie, https://github.com/acheong08/BingImageCreator#getting-authentication]>

[DALL·E]:
	/dall:
	   + <prompts [image description]>
	   
	   + <api_key [OpenAI API Key]>
	   
	   + <parameter [1~10, https://platform.openai.com/docs/api-reference/images/create#images/create-n]>
	   
	   + <size [256x256, 512x512, 1024x1024]>

[Command Description]:
	/help

More...
```

</details>
	
<details>
  <summary>

## Supported languages🌎

  </summary>

- **Chinese**
- **English** (coming soon...)

</details>

<details>
  <summary>

## How to create and deploy🚀

  </summary>

- ### Deploy on Cloud
	#### 1. [Railway (Last updated: 2023/04/16)](https://railway.app?referralCode=CCqlpO)
	**[Free Plan](https://docs.railway.app/reference/plans#starter-plan):** $5.00 of usage each month with an execution time limit of 500 hours. 512MB of RAM, 2 vCPU and 1GB of Disk.
	> [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/9XWCtT?referralCode=CCqlpO)

- ### Local Deployment
	#### 1. Clone this Repository
	> ```bash
	> git clone https://github.com/Lin-Rexter/AI_Hub_Discord-Bot.git
	> ```

	#### 2. Set Environment Variables
	> **2-1. Rename the file .env.example to .env**
	
	> **2-2.**
	> ```env
	> # Discord:
	> # Discord Bot token # https://discord.com/developers/applications
	> DISCORD_TOKEN = ""
	> # Discord Administrator ID(Administrator ID to mention when an unexpected error occurred in executing the command)
	> DISCORD_ADMIN_ID = ""
	>
	> # ChatGPT(Official)、 DALL·E:
	> # [ChatGPT,DALL·E authentication](OpenAI API key) # https://platform.openai.com/account/api-keys
	> OPENAI_API_KEY = ""
	> # Default ChatGPT_Model(gpt-3.5-turbo, gpt-4, gpt-4-32k)
	> CHATGPT_MODEL = "gpt-3.5-turbo"
	>
	> # Bing ChatGPT:
	> # Default Bing ChatGPT response style(creative, balanced, precise)
	> RESPONSE_STYLE = "balanced"
	>
	> # Bing Image Creator:
	> # Bing Image Creator authentication(_U cookie) # https://github.com/acheong08/BingImageCreator#getting-authentication
	> # If you use cookies.json(Step 3), you do not need to set
	> AUTH_COOKIE = ""
	>
	> # Google Bard:
	> # Google Bard authentication[SESSION("__Secure-1PSID" cookie)] # https://github.com/acheong08/Bard#authentication
	> BARD_TOKEN = ""
	>
	> ### "OPENAI_API_KEY", "AUTH_COOKIE", "BARD_TOKEN", "CHATGPT_MODEL", "RESPONSE_STYLE": The value returned from the command will be used first.
	> ```

	#### 3. [Bing ChatGPT authentication](https://github.com/acheong08/EdgeGPT#getting-authentication-required)
	> **3-1. Rename** the file **cookies.example.json** to **cookies.json**

	> **3-2. Paste cookies** into cookies.json

	#### 4. [Running via Poetry](https://python-poetry.org/docs/#installation)
	> **3-1. Edit [poetry config settings](https://python-poetry.org/docs/cli/#config)**
	> If you prefer to have the virtual environment in the project directory
	> ```bash
	> poetry config virtualenvs.in-project true
	> ```

	> **3-2. [Installs the dependencies specified in pyproject.toml](https://python-poetry.org/docs/cli/#install)**
	> ```bash
	> poetry install
	> ```

	> **3-3. [Activating the virtual environment](https://python-poetry.org/docs/cli/#shell)**
	> * Use **default** Python version
	> ```bash
	> poetry shell
	> ```
	>
	> * If you want to **[specify Python version](https://python-poetry.org/docs/managing-environments/#switching-between-environments)**
	> ```bash
	> poetry env use 3.9
	> ```

	> **3-4. Run Bot**
	> * If you use `poetry shell`
	> ```bash
	> python ./bot.py
	> ```
	>
	> * If you **not use** `poetry shell`
	> ```bash
	> poetry run python ./bot.py
	> ```

</details>

## License
**[MIT](https://github.com/Lin-Rexter/AI_Hub_Discord-Bot/blob/1902f8e112c3e682ab041c39864d8bb8c7f78a24/LICENSE)**