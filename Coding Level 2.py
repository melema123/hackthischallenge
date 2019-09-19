# This code solves "Coding Level 2" challenge from HackThis website using python and selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Provide path to your chrome driver
chromedriver="C:\Python37\drivers\chromedriver.exe"
driver=webdriver.Chrome(chromedriver)

# Login into your HackThis account
driver.get("https://www.hackthis.co.uk/")
driver.find_element_by_name("username").send_keys("yourusername")
driver.find_element_by_name("password").send_keys("yourpassword")
driver.find_element_by_name("username").send_keys(Keys.ENTER)


# Load "Coding Level 2" page
driver.get('https://www.hackthis.co.uk/levels/coding/2')

# Get the encrypted content to be decypted ( from the textbox )
question=driver.find_element_by_xpath("//textarea[1]").get_attribute('value').split(",")

# Key in the decypted answer in the Textbox provided -> this compressed list is the one decrypting [ " " if q == " " else chr(127 - ((int(q)-32) + 1)) for q in question]
driver.find_element_by_name("answer").send_keys([ " " if q == " " else chr(127 - ((int(q)-32) + 1)) for q in question ])

# Click Submit button
driver.find_element_by_xpath("//input[@class='button']").click()
