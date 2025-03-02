import os
import requests
import threading

import dotenv

dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

text_send ="hello python"
chat_id=1878669270

list_of_users = [1878669270, 325011602]
def send_message(chat_id,text_send):
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text_send}"
    )
    print(response.json())



list_of_threads=[]
for userid in list_of_users:
    for i in range(10):
        g=threading.Thread(target=send_message,args=(userid,text_send))
        list_of_threads.append(g)
        g.start()

for thread in list_of_threads:
    thread.join()