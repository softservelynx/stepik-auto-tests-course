from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

brlink = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(brlink)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

try:
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    check = browser.find_element_by_css_selector("#robotCheckbox")
    check.click() 

    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    time.sleep(3)

    submit = browser.find_element_by_css_selector("button.btn[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
    


