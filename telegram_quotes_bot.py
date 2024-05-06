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
        # List of categories
    categories = [
        "age", "alone", "amazing", "anger", "architecture", "art", "attitude", "beauty", "best", "birthday",
        "business", "car", "change", "communication", "computers", "cool", "courage", "dad", "dating", "death",
        "design", "dreams", "education", "environmental", "equality", "experience", "failure", "faith", "family",
        "famous", "fear", "fitness", "food", "forgiveness", "freedom", "friendship", "funny", "future", "god",
        "good", "government", "graduation", "great", "happiness", "health", "history", "home", "hope", "humor",
        "imagination", "inspirational", "intelligence", "jealousy", "knowledge", "leadership", "learning", "legal",
        "life", "love", "marriage", "medical", "men", "mom", "money", "morning", "movies", "success"
    ]

    # Generate options text dynamically
    categories_text = ", ".join(categories)

    text = f"What category do you like?\nChoose one: *today*, *random*, *image*, or *category* ({categories_text})."

    # sends a message from the bot to the chat
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")

    # register next step handler with lambda function to pass mode argument
    bot.register_next_step_handler(sent_msg, lambda msg: fetch_quotes(msg, mode=None))

def fetch_quotes(message, mode):
    """
    This function will handle the fetching of the quotes

    Args:
        message: The message object from telegram
        mode: This will determine whether to fetch a quote or an image
    """
    mode = message.text.lower()

    # This list shows the expected output as shown above
    expected_list = [
        "today","random", "image", "age", "alone", "amazing", "anger", "architecture", "art", "attitude", "beauty", "best", "birthday",
        "business", "car", "change", "communication", "computers", "cool", "courage", "dad", "dating", "death",
        "design", "dreams", "education", "environmental", "equality", "experience", "failure", "faith", "family",
        "famous", "fear", "fitness", "food", "forgiveness", "freedom", "friendship", "funny", "future", "god",
        "good", "government", "graduation", "great", "happiness", "health", "history", "home", "hope", "humor",
        "imagination", "inspirational", "intelligence", "jealousy", "knowledge", "leadership", "learning", "legal",
        "life", "love", "marriage", "medical", "men", "mom", "money", "morning", "movies", "success"
    ]

    # Generate options text dynamically
    categories_text = ", ".join(expected_list)

    # Handle the case of no provided information
    if mode not in expected_list:
        bot.send_message(message.chat.id, "The bot cannot retrieve the provided category. Please select one from the provided list")
        bot.send_message(message.chat.id, f"List: {categories_text}")

    if mode == 'random' or mode == 'today':
        data = get_quotes(mode)

        # Checks if the data is a list
        if isinstance(data, list) and data:  # Check if data is a non-empty list
            # Select a quote from the list
            quote_data = data[0]

            # Use .get() method to handle missing keys
            quote = quote_data.get("q") 
            author = quote_data.get("a")

            if quote and author:
                quote_message = f"*Quote:* {quote}\n*Author:* {author}"
                bot.send_message(message.chat.id, "Here's the quote and author:")
                bot.send_message(message.chat.id, quote_message, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, "Failed to fetch quote data.")
        else:
            bot.send_message(message.chat.id, "Failed to fetch quote data.")
    
    elif mode == 'image':
        image_content = get_quotes(mode)

        # Send the image to the user
        bot.send_message(message.chat.id, "Here's the image of the quote and author:")
        bot.send_photo(message.chat.id, image_content)
    
    else:
        category_data = get_quotes(mode)

        # Check if data is a list and not empty
        if isinstance(category_data, list) and category_data:
            # retrieve the JSON from the list
            quoted_data = category_data[0]

            # Check if data is a dictionary
            if isinstance(quoted_data, dict):
                # Assign the retrieved data to variables
                quote = quoted_data.get('quote')
                author = quoted_data.get('author')

                # Handles the case of existing quote and author
                if quote and author:
                    quote_message = f"*Quote:* {quote}\n*Author:* {author}"
                    bot.send_message(message.chat.id, "Here's the quote and author:")
                    bot.send_message(message.chat.id, quote_message, parse_mode="Markdown")
                else:
                    bot.send_message(message.chat.id, "Failed to fetch quote data.")
            else:
                bot.send_message(message.chat.id, "Failed to fetch quote data.")      

# starts the bot and continuously polls for new messages from users.
bot.infinity_polling()