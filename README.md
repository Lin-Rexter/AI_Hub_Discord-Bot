[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)]()

<div align="center">

# AI_Hub_Discord_Bot
**ChatGPT、 BingGPT、 Image Creator、 DALL·E、 Other AI Application with Discord Bot.**

</div>

---

## Features
- **[ChatGPT](https://github.com/acheong08/ChatGPT)**<br>
- **[EdgeGPT](https://github.com/acheong08/EdgeGPT#image-generator)**<br>
- **[Bing Image Creator](https://github.com/acheong08/EdgeGPT#chatbot)**<br>
- **[DALL·E](https://platform.openai.com/docs/api-reference/images)**<br>
- **More...**

<details>
  <summary>

## Commands

  </summary>

```
[ChatGPT]:
	/gpt:
	   + <prompts [對話]>
	   + <api_key [OpenAI的API Key]>
	   + <role [用戶(默認), 系統, 助手]>
	   + <engine [gpt-3.5-turbo(默認), gpt-4, gpt-4-32k]>
	   + <top_p>
	   + <temperature>
	   + <presence_penalty>
	   + <frequency_penalty>
	   + <reply_count>
	   + coming soon...
	Ex1: /gpt 系統 Hello~
	Ex2: /gpt Please give me the table of xxx

[EdgeGPT]:
	/gpt4:
	   + <prompts [對話]>
	   + <role [創意, 平衡(默認), 精確]>
	Ex1: /gpt4 精確 Let me know what's hot in Taiwan today
	Ex2: /gpt4 Implement the Caesar Cipher using Python

[Bing Image Creator]:
	/img:
	   + <prompts [圖片描述]>
	   + <width>
	   + <height>
	Ex1: /img An owl spitting fire

[DALL·E]:
	/dall:
	   + <prompts [圖片描述]>
	   + <api_key [OpenAI的API Key]>
	   + <parameter>
	   + <size>

More...
```

</details>

<details>
  <summary>

## Supported languages

  </summary>

- **Chinese**
- **English** (coming soon...)

</details>

<details>
  <summary>
  
## How to use

  </summary>

**1. [Set Environment Variables(not necessary)](https://github.com/Lin-Rexter/AI_Hub_Discord-Bot/blob/ea98ad2d15728017ecd56fe7e5e870f7e76dd1eb/.env)**<br>
**2. [Install Poetry](https://python-poetry.org/docs/)**<br>
**3. Run `poetry shell`**<br>
**4. Run `poetry install`**<br>
**5. Run `python ./bot.py` or `poetry run python ./bot.py`**<br>

</details>

