import os
import requests
import threading
import dotenv

# Load environment variables from a .env file
dotenv.load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")

# Message to be sent
text_send = "hello python"

# List of user IDs to send messages to
list_of_users = [1878669270, 325011602]

# Function to send a message to a specific chat ID
def send_message(chat_id, text_send):
    # Make a GET request to the Telegram API to send a message
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text_send}")
    # Print the response from the API
    print(response.json())

# List to keep track of threads
list_of_threads = []

# Create and start threads for each user ID
for userid in list_of_users:
    for i in range(10):
        # Create a new thread to send a message
        g = threading.Thread(target=send_message, args=(userid, text_send))
        # Add the thread to the list of threads
        list_of_threads.append(g)
        # Start the thread
        g.start()

# Wait for all threads to complete
for thread in list_of_threads:
    thread.join()