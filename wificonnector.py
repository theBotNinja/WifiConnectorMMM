from time import sleep
import csv
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
login_url = 'http://172.16.1.3:8090/httpclient.html'

def connect_to_wifi(ssid, password):
    try:
        command = f"netsh wlan connect name={ssid} ssid={ssid} interface=Wi-Fi"
        subprocess.run(command, check=True, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

def Login(user_profiles):
    driver = webdriver.Chrome()
    try:
        sleep(0.5)
        driver.get(login_url)
        XPATH_username='//*[@id="username"]'
        XPATH_password='//*[@id="password"]'
        XPATH_click='//*[@id="loginbutton"]'
        XPATH_status='//*[@id="statusmessage"]'  
        for user_profile in user_profiles:
            driver.find_element(By.XPATH,XPATH_username).clear()
            driver.find_element(By.XPATH,XPATH_username).send_keys(user_profile[0])
            driver.find_element(By.XPATH,XPATH_password).clear()
            driver.find_element(By.XPATH,XPATH_password).send_keys(user_profile[1])
            driver.find_element(By.XPATH,XPATH_click).click()
            sleep(1)
            if (len(driver.find_element(By.XPATH,XPATH_status).text)==0):
                print(user_profile,driver.find_element(By.XPATH,XPATH_status).text)
                break
        else:
            print("no profiles free")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


# Usage
if __name__ == "__main__":
    user_profiles = []
    wifi_profiles = []

    with open('userProfiles.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
                user_profiles.append(lines)
    with open('wifiNetworkProfile.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            wifi_profiles.append(lines)
    
    for wifi_profile in wifi_profiles:
        if connect_to_wifi(wifi_profile[0], wifi_profile[1]):
            print("Connected to WiFi successfully!")
            if (wifi_profile[0] == "MMMUT_Ramanujam"):
                Login(user_profiles)
            break
    else:
        print("Failed to connect to WiFi.")    