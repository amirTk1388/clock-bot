from datetime import datetime

print("ربات ساعت فعال شد")

while True:
    now = datetime.now()
    print(now.strftime("%H:%M:%S"))
