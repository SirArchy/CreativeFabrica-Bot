# import module
from selenium import webdriver
import time

# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.
driver = webdriver.Chrome(r"./driver/chromedriver")

# get https://www.geeksforgeeks.org/
driver.get("https://www.geeksforgeeks.org/")

# Maximize the window and let code stall
# for 10s to properly maximise the window.
time.sleep(5)

# Obtain button by link text and click.
button1 = driver.find_element_by_link_text("Sign In")
button2 = driver.find_element_by_link_text("Sign In")
button3 = driver.find_element_by_link_text("Sign In")
button1.click()
button2.click()
button3.click()

