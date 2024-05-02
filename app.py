import requests
import dotenv
import os
dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={"chat_id": chat_id, "text": "Hello, World!"})
print("Message sent!")
print('Finished!')