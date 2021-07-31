from selenium import webdriver
import time
import math 

# Browser
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# Math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

# Input field
input = browser.find_element_by_id("answer")
input.send_keys(y)

# Scroll I am a robot
check = browser.find_element_by_css_selector("#robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click() 

# Scroll Robots rule
radio = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

# Submit
submit = browser.find_element_by_css_selector("button.btn[type='submit']")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()

time.sleep(5)

browser.quit