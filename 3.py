from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

brlink = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(brlink)

num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text

x = int(num1)
y = int(num2)

z = str(x + y)

try:
   select = Select(browser.find_element_by_id("dropdown"))
   select.select_by_visible_text(z)

   

finally:
    print(z)
    submit = browser.find_element_by_css_selector("button.btn[type='submit']")
    submit.click()
    
    browser.quit