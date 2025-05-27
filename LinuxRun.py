import openai
from Whatsapp.Whatsapp import Whatsapp
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# Load your OpenAI API key
openai.api_key = openai_api_key

bot = Whatsapp(silent=True, headless=False, user_data_dir="UserData")

async def func(element, msg):
    # Use ChatGPT to generate reply
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=msg[2],
        max_tokens=2048,
        temperature=0.5
    )
    reply = response.choices[0].text
    print(f"ChatGPT reply: {reply}")
    bot.replyTo(element, reply)

bot.login()
print("Reading messages now !")
bot.getChats()
bot.hookIncomming("Jelius ", func)