from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Path to the chrome driver for selinium
chromedriver="\path\to\driver"
driver=webdriver.Chrome(chromedriver)

# Logging into HackThis Account
driver.get("https://www.hackthis.co.uk/")
driver.find_element_by_name("username").send_keys("yourusername")
driver.find_element_by_name("password").send_keys("yourpassword")
driver.find_element_by_name("username").send_keys(Keys.ENTER)

# Opening "Coding Level 1" page
driver.get('https://www.hackthis.co.uk/levels/coding/1')

# Getting the content to be sorted from TextBox
question=driver.find_element_by_xpath("//textarea[1]").get_attribute('value').split(", ")

# Sorting the content
question.sort()

# Submitting the answer
driver.find_element_by_name("answer").send_keys([ q+", " if question.index(q) != (len(question)-1)  else q for q in question])
driver.find_element_by_xpath("//input[@class='button']").click()