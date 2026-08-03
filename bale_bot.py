import requests
import time
from datetime import datetime

TOKEN = "1454769491:F8G5qPO-9eLrHqKTaauKXCyV0LdZUEuSDl8"
URL = f"https://tapi.bale.ai/bot{TOKEN}/"

offset = 0

while True:
try:
r = requests.get(URL + "getUpdates", params={"offset": offset}, timeout=30).json()

if r.get("ok"):  
        for update in r["result"]:  
            offset = update["update_id"] + 1  

            if "message" in update:  
                chat_id = update["message"]["chat"]["id"]  
                text = update["message"].get("text", "")  

                if text == "/start":  
                    requests.post(URL + "sendMessage", json={  
                        "chat_id": chat_id,  
                        "text": "سلام 👋\nربات ساعت فعال است.\nبرای دیدن ساعت /time را بفرست."  
                    })  

                elif text == "/time":  
                    now = datetime.now().strftime("%H:%M:%S")  
                    requests.post(URL + "sendMessage", json={  
                        "chat_id": chat_id,  
                        "text": f"🕒 ساعت فعلی:\n{now}"  
                    })  

except Exception as e:  
    print(e)  

time.sleep(1)
