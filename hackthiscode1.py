from selenium import webdriver

from selenium.webdriver.common.keys import Keys

chromedriver="C:\Python37\drivers\chromedriver.exe"
driver=webdriver.Chrome(chromedriver)

driver.get("https://www.hackthis.co.uk/")
driver.find_element_by_name("username").send_keys("dydydyd")
driver.find_element_by_name("password").send_keys("mnbvcxz")
driver.find_element_by_name("username").send_keys(Keys.ENTER)

driver.get('https://www.hackthis.co.uk/levels/coding/1')
# Make the tests...
question=driver.find_element_by_xpath("//textarea[1]").get_attribute('value').split(", ")
question.sort()
driver.find_element_by_name("answer").send_keys([ q+", " if question.index(q) != (len(question)-1)  else q for q in question])
driver.find_element_by_xpath("//input[@class='button']").click()