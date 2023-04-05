import asyncio
from EdgeGPT import Chatbot, ConversationStyle

bot = Chatbot(cookiePath='./src/Microsoft/Bing_EdgeGPT_4/cookies.json')

gpt4_style = {
    "創意": ConversationStyle.creative,
    "平衡": ConversationStyle.balanced,
    "精確": ConversationStyle.precise
} 

async def EdgeGPT_Reply(Texts, role=None) -> str:
    style = gpt4_style[role]

    print("\n風格: " + role)

    reply_dict = await bot.ask(prompt=Texts, conversation_style=style)
    reply_text = reply_dict["item"]["messages"][1]["text"]
    #await bot.close()
    #print(reply_text)
    return reply_text