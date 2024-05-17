"""from time import sleep
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
login_url = 'http://172.16.1.3:8090/httpclient.html'
"""

def connect_to_wifi(ssid, password):
    try:
        result = subprocess.run(
            ['nmcli', 'device', 'wifi', 'connect', ssid,"password",password],
            check=True,
            capture_output=True,
            text=True
        )
        print("Connected to Wi-Fi successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to Wi-Fi: {e.stderr}")

connect_to_wifi("MMMUT_Ramanujam","")
sleep(1)
"""
#path where browser is installed
service = Service(executable_path='./geckodriver')
driver = webdriver.Firefox(service=service)

driver.get(url=login_url)

XPATH_username='//*[@id="username"]'
XPATH_password='//*[@id="password"]'
XPATH_click='//*[@id="loginbutton"]'
XPATH_status='//*[@id="statusmessage"]'

driver.find_element(By.XPATH,XPATH_username).send_keys('c2221123')
driver.find_element(By.XPATH,XPATH_password).send_keys('23')
driver.find_element(By.XPATH,XPATH_click).click()

if (len(driver.find_element(By.XPATH,XPATH_status).text)==0):
    print("Login successfully.")
else:
    print(driver.find_element(By.XPATH,XPATH_status).text)
driver.quit()
"""