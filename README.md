# ru2cn_trenslate_bot_py
Here is an example of a simple Telegram bot written in Python that can translate text from Russian to Chinese using the Google Translate API

In this code, we import the requests library to make the API call to Google Translate, the json library to parse the API response,
and the telegram.ext library to create a Telegram bot. We define the function translate_text() which takes in the bot, 
update and the arguments entered by the user. We use the join() function to join the input text into a single string, 
then set the source and target languages as "ru" for Russian and "zh" for Chinese. Then we use the google translate API to translate the text, 
passing the source language, target language and the text as parameters. We parse the response received from the API and extract the translated text. 
Finally, we use the update.message.reply_text() function to send the translated text back to the user.

It is important to note that, to use the Google Translate API, you need to have an API key, and this code is just an example
and it is not guaranteed to work as is. You should check the documentation of Google translate API to get the key and to know the usage limit and pricing.

Also, the code uses the python-telegram-bot library, you may need to install it before running the code by running pip install python-telegram-bot on your command line.
