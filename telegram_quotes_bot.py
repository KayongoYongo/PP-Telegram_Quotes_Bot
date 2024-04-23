import os
from dotenv import load_dotenv
import telebot
from quotes import get_quotes

# load environmental variables
load_dotenv()

# Access the variables
BOT_TOKEN = os.getenv("API_TOKEN")
username = os.getenv("USERNAME")

# Create an instance of the Telebot class
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """
    This function will handle welcoming the user

    Args:
        message: This will be the text that will trigger the function
    """
    # This messsage loads when the bot is started
    bot.reply_to(message, f"Hello! Want to see a quote? Enter /mode to continue")

@bot.message_handler(commands=['mode'])
def mode_handler(message):
    """
    This function will handle the mode of the quote

    Args:
        message: This will be the text that will trigger the function
    """
        
    text = "What category do you like?\nChoose one: *today*, *random* or *image*."

    # sends a message from the bot to the chat
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")

    # register next step handler with lambda function to pass mode argument
    bot.register_next_step_handler(sent_msg, lambda msg: fetch_quotes(msg, mode=None))

def fetch_quotes(message, mode):
    """
    This function will handle the fetching of the quotes

    Args:
        category: This will be the text that will trigger the function
    """
    mode = message.text.lower()
    data = get_quotes(mode)

    # The returned response is a JSON Array
    quote_data = data[0]

    # Retrieve the data from the array
    quote = quote_data["q"]
    author = quote_data["a"]

    print(author)
    print(quote)
    joke_message = f"*Quote:* {quote}\n*Author:* {author}"
    bot.send_message(message.chat.id, "Here's the quote and author:")
    bot.send_message(message.chat.id, joke_message, parse_mode="Markdown")

# starts the bot and continuously polls for new messages from users.
bot.infinity_polling()