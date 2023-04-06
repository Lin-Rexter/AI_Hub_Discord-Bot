import json
from ImageGen import ImageGen


def Image_Creator_Reply(prompt, width=None, height=None, cookie_file='./src/Microsoft/Bing_Image_Creator/cookies.json', Output_dir=None) -> list:
    # Get auth cookie
    U = None
    if cookie_file == None:
        U = "1Waa56EwjvqfTBEdBHJGuA9xHc6n6zd-ab-FFsXKQ9oajesEjP-EXM70AAyfjO4VRHj2GrmQb-JWtyg8WjlUadtqTdmZBDnCxLDZhtnsbme9XjNfNTkphSsbot-qhT746roy3GS9XTXi8nS6_S8xq9GeqdOkMe9BldiCPt35qc94Nd0OPBScHhkzYEP0_IQDqf0_dhtToBp5HAC5mFr2tMXn85eLf2XeE7m4dxgcaNuI"
    else:
        with open(cookie_file, encoding="utf-8") as file:
            cookie_json = json.load(file)
            for cookie in cookie_json:
                if cookie.get("name") == "_U":
                    U = cookie.get("value")
                    break

    if U is None:
        raise Exception("Could not find auth cookie")

    print(f"\n圖片寬度: {width}")
    print(f"圖片長度: {height}\n")

    try:
        # Create image generator
        image_generator = ImageGen(U)
        images_list = image_generator.get_images(prompt)

        if len(images_list) != 0 or images_list != None:
            # 設置圖片大小
            images_reply = [link + f'?w={width}&h={height}' for link in images_list]
        else:
            images_reply = "Oops❗ 沒有圖片，請嘗試移除較敏感字眼!"

        print(images_reply)
        return [prompt, images_reply]
    except Exception as e:
        print("\nError:", e)
        images_reply = "Oops❗ 沒有圖片，請嘗試移除較敏感字眼!"
        return [prompt, images_reply]