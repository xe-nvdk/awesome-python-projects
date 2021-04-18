import json
import time
import telepot
import requests
from win10toast import ToastNotifier

bot = telepot.Bot('paste-here-your-token')
url = "https://api.binance.com/api/v1/ticker/24hr?symbol=DOGEUSDT"

def doge():
    
    r = requests.get(url)
    p = r.json()['lastPrice']
    c = r.json()['priceChangePercent']

    toast = ToastNotifier()
    toast.show_toast("Dogecoin price - ToTheMoon", f"Price: ${p} - Change (24h): {c}%", duration=10, icon_path="doge.ico")
    
    bot.sendMessage(paste-here-chat-id, f"Price: ${p} - Change (24h): {c}%")

    time.sleep(60)

while True:
    doge()
