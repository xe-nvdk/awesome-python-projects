from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import telepot
import time

bot = telepot.Bot('1624440848:AAGgldpB2jsI5hrURScaGuI5GOPLLeCCzf8')

driver_options = Options()
driver_options.add_argument('--headless')
driver_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver', options=driver_options)
driver.get('https://dolarhoy.com')

class dolar:
    def compra():
        precio_compra = driver.find_element_by_class_name('compra')
        bot.sendMessage(-1001448256778, "Cotización Dolar Blue: %s" %(precio_compra.text))

    def venta():
        precio_venta = driver.find_element_by_class_name('venta')
        bot.sendMessage(-1001448256778, "Cotización Dolar Blue: %s" %(precio_venta.text)) 

    compra()
    venta()
