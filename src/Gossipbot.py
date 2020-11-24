from random import randrange, sample
from time import sleep
from json import load
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



#Variables
base = Path.cwd().parent

config_path = base / "settings/Config.json"
random_phrases_path = base /"settings/Random Phrases.txt"



# FUNCTIONS
def login(username, password, url):
    driver.get(url)

    # no campo de email, escrever o username definido no arquivo "config.json"
    email = driver.find_element_by_name("email")
    email.send_keys(username)

    # no campo password, envia a senha definida no arquivo "config.json"
    pwd = driver.find_element_by_name("password")
    pwd.send_keys(password)
    pwd.send_keys(Keys.ENTER)



def get_config():
    with open(config_path, "r", encoding="utf-8") as file:
        config = load(file)

        return config




def print_message (phrase):
    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"\a\t{current_time}: {phrase}")



def send_phrase(phrase):
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div.content-98HsJk > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div')))
    input_field=driver.find_element_by_css_selector('#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div.content-98HsJk > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div')

    input_field.click()
    input_field.send_keys(phrase)
    input_field.send_keys(Keys.ENTER)



def random_phrase():

    while True:
        settings = get_config()
        pause_interval = settings.get("pauseinterval")

# pega as frases do arquivo "random_phrases.txt" e as coloca numa lista
        with open(random_phrases_path, "r", encoding="utf-8") as file:
            random_phrases = file.read().splitlines()

            # pega uma frase aleaatoriamente da lista e envia no chat da sala
        phrase=sample(random_phrases, len(random_phrases)).pop()
        send_phrase(phrase)

        print_message(phrase)
        sleep(randrange(pause_interval, 2*pause_interval))






# MAIN
# configurando o chrome para que ele opere de forma headless
chrome_options=Options()
chrome_options.headless=True

driver=webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(20)
wait=WebDriverWait(driver, 20)

# pega as configurações definidas no arquivo "config.json"
settings = get_config()

# pega o username, password e a url para a sala do discord
username = settings.get("username")
password = settings.get("password")
url = settings.get("url")

# por fim, loga no discord
login(username=username, password=password, url=url)

# gerando as frases randomicamente e enviando no chat
random_phrase()