# Telegram Bot

This repository contains a simple Telegram bot that sends a message to two users using the Telegram Bot API. The bot is implemented without using any third-party libraries for interacting with the Telegram API.

## Features

- Sends a predefined message to a list of user IDs.
- Uses threading to send messages concurrently.

## How It Works

1. The bot token is loaded from an environment variable (`BOT_TOKEN`).
2. A list of user IDs is defined in the script.
3. The bot sends a message to each user using the Telegram Bot API.

## Prerequisites

- Python 3.x installed on your system.
- A `.env` file containing your bot token in the following format:

## How to Run

1. Clone this repository.
2. Create a `.env` file in the root directory and add your bot token.
3. Run the script:
 ```bash
 python bot.py

 NOTES:

1. The bot uses the Telegram Bot API directly via HTTP requests.
2. Ensure that the user IDs in the script are valid and that the bot 
   has permission to send messages to them.

Disclaimer

This bot is for educational purposes only. Use responsibly and ensure compliance with Telegram's terms of service. ```