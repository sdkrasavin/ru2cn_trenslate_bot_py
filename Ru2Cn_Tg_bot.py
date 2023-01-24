import requests
import json
from telegram.ext import Updater, CommandHandler

# Replace with your Telegram token
TOKEN = "YOUR_TELEGRAM_TOKEN"

def translate_text(bot, update, args):
    # Join the input text into a single string
    text = " ".join(args)

    # Set the source and target languages
    source_language = "ru"
    target_language = "zh"

    # Use the Google Translate API to translate the text
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_language}&tl={target_language}&dt=t&q={text}"
    response = requests.get(url)
    translation = json.loads(response.text)[0][0][0]
  
    # Send the translated text back to the user
    update.message.reply_text(translation)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("translate", translate_text, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
