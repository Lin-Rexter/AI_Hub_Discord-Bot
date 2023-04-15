import os
import contextlib
import json
from pathlib import Path
from dotenv import load_dotenv
from ImageGen import ImageGen

# take environment variables from .env
env_path = os.path.join(Path(__file__).resolve().parents[2], '.env')

# check whether .env file exists
is_env_exist = os.path.exists(env_path) and os.path.isfile(env_path)

if is_env_exist:
    load_dotenv(env_path)

    # take AUTH_COOKIE path from environment variables
    env_auth_cookie = os.getenv('AUTH_COOKIE', None)

# take cookies.json path
cookie_path = os.path.join(Path(__file__).resolve().parents[2], 'cookies.json')


async def Image_Creator_Reply(**kwargs) -> list:
    for key, value in kwargs.items():
        globals()[key] = value

    # check whether cookies.json file exists
    is_cookies_exist = os.path.exists(cookie_path) and os.path.isfile(cookie_path)

    # Load auth cookie
    if is_cookies_exist:
        with contextlib.suppress(Exception):
            with open(cookie_path, encoding="utf-8") as file:
                cookie_json = json.load(file)
                for cookie in cookie_json:
                    if cookie.get("name") == "_U":
                        cookie_U = cookie.get("value")
                        break

    # auth cookie
    U = auth_cookies or cookie_U or env_auth_cookie or None

    if U is None:
        '''
        raise Exception("Could not find auth cookie")
        '''
        return ["Error", "Oops❗ 尚未設定auth cookie!"]

    try:
        # Create image generator
        image_generator = ImageGen(auth_cookie=U)
        images_list = image_generator.get_images(prompts)

        if len(images_list) != 0:
            # Setting images size
            reply = [link + f'?w={width}&h={height}' for link in images_list]
            return ["Success", reply]
        else:
            reply = "Oops❗ 沒有圖片，請嘗試移除較敏感字眼!"
            return ["Error", reply]

    except Exception as e:
        print("\nError:", e)
        return ["Dangerous", "Oops❗ 發生例外錯誤!"]