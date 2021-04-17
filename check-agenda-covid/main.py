from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import telepot
import time

bot = telepot.Bot('bot-telegram-token')

driver_options = Options()
driver_options.add_argument('--headless')
driver_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=driver_options)
driver.get('https://agenda.vacunacioncovid.gub.uy/')

def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)

def ci():
    ci = driver.find_element_by_id('numberCID')
    slow_typing(ci, 'ci_number')

def db():
    daybirth = driver.find_element_by_name('dateBirth[day]')
    slow_typing(daybirth, 'xx')

def mb():
    monthbirth = Select(driver.find_element_by_id('mes'))
    monthbirth_selected = monthbirth.select_by_visible_text("noviembre")

def yb():
    daybirth = driver.find_element_by_name('dateBirth[year]')
    slow_typing(daybirth, 'xxxx')

def sb():
    submit = driver.find_element_by_id('btnCheckData')
    submit.click()
    
def screenshot():
    time.sleep(3)
    screenshot = driver.save_screenshot("screenshot.png")

def message():
    bot.sendMessage(-chat_id, 'Acabo de chequear si puedes vacunarte')
    bot.sendPhoto(-chat_id, photo=open('screenshot.png', 'rb'))
    
ci()
db()
mb()
yb()
sb()
screenshot()
message()