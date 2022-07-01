from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Create the webdriver object
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'E:\Cricut Free Stuff'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

# get website link
driver.get('https://www.creativefabrica.com/daily-gifts/')

# wait for 1s to properly load website
time.sleep(1)

# Obtain buttons by class name and click all of them
close_modal = driver.find_element(By.CLASS_NAME,'close-modal').click()
close__notification_modal = driver.find_element(By.ID,'onesignal-slidedown-cancel-button').click()
signin_button = driver.find_element(By.ID ,'menu-item-icon-login').click()
username_field = driver.find_element(By.NAME ,'username').send_keys('wnbemail456@gmail.com')
pw_field = driver.find_element(By.NAME ,'password').send_keys('Motgk1491')
login_button = driver.find_element(By.NAME, 'login').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 730)") 
for buttons in driver.find_elements(By.CLASS_NAME, 'product-download-button'):
    buttons.click()
    time.sleep(3)
    driver.find_element(By.ID, 'promo-upsell-popup-freebie-close').click()
input('Press Enter to Continue…')
driver.quit()
