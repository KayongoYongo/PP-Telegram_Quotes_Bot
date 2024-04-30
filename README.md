# Telegram Quotes Bot
A simple telegram bot which shares inspirational quotes based off the user's prompts.

# Description
A telegram bot which shares inspirational quotes based off the user's prompts. The bot can return quotes from various categories such as happiness,
age, architechture etc. Additionally, there's an option of returning an image with quotes.

# If you want to just use the bot, here's the link:
Look up the name of the bot: (https://t.me/sam_telegram_quotes_bot).

## Instructions:
To get started with the bot, use the `/start` command.
Note: In order to get the quotes, use `/mode` then the `category`. Otherwise, the bot will not work.

# If you are getting started from scratch, here are the instructions:
## 1. Bot father
If you are interested in running tha applcation in you own environment, you'll need to follow these instructions:
1. First, start `Bot Father` in Telegram.
2. Assign a `name` to the bot.
3. Lastly, assign a `bot username`. Make sure the username ends with `bot`. After all the steps have been followed, you will be provided with an `API TOKEN`.

## 2. API-Ninja
In order to use the API, a user will need to create an account. There, you'll be provided with an `API KEY` that will
track the number of requests made to the API.

## 3. Security
Store the `API KEY` and the `API token` in a **`.env`** file in order to preserve privacy. Additionally, add the `.env` file to `.gitignore` so
as to make them private

## 4. Installation
To get started with the bot, two things need to be installed. The python telegram bot and python.
Run these two commands in the terminal so as to get started:
```
pip install python-telegram-bot
```
```
sudo apt-get update
sudo apt-get install python3
```

## 5. Running the app
In order to run the app, just type this command: `python telegram_bot_quotes.py`

## Features
### 1. Bot Interaction
To get started with the app, use the commands `start` or `hello`. To continue, use the command `mode`.
This will show the various categories and modes that the bot supports.

### 2. Third party API integration
The Bot utilises two third party APIs: 
1. `https://zenquotes.io/api/`. This API is responsible for retrieving a JSON array on **today**, **random** and **image**.
2. `https://api.api-ninjas.com/v1/quotes?category={}`. This API is responsible for retrieving quotes based off categories.

### 3. Error Handling
The bot returns errors if the following instances take place:
1. If it fails to retrieve data from the thirdparty API's
2. If the user provides data which is not supported from the prompts.
3. If the structure of the JSON response of the API has been altered.
4. Since the bot is built using a synchronous mode of programming, expect concurrency issues when **multiple** requests are processed at the same time.
5. If the bot takes too long to respond to a user's message or an API request, Telegram may timeout the connection, resulting in a timeout error

When entering information, the bot has been modified so as to covert each string into lowercase.

### 4. Scalability.
Since the bot is built using synchronous programming, it will struggle to deal with multiple concurrent requests.

# Visuals
Here is a sample on quotes for **today**:
![image](https://github.com/KayongoYongo/PP-Telegram_Quotes_Bot/assets/111020589/fe4ae4fd-807f-4d5d-8399-bb32d272d3e4)

Here is a sample on quotes for **image**:
![image](https://github.com/KayongoYongo/PP-Telegram_Quotes_Bot/assets/111020589/893e9c59-2acc-44cb-a579-a6d1e64e2518)

Here is a sample on quotes for a random category such as **computers**:
![image](https://github.com/KayongoYongo/PP-Telegram_Quotes_Bot/assets/111020589/52a3f3c0-fbd9-42f8-a6a1-9b02fef4558c)

Lastly, here is a sample on providing a category that does not exist:
![image](https://github.com/KayongoYongo/PP-Telegram_Quotes_Bot/assets/111020589/b1854d63-f159-477a-8b47-61c9e2d00137)

# Authors and acknowledgement
**Kayongo Samuel Yongo**