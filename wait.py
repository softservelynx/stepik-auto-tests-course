from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
# Br0wser

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Wait for #Price and click

WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
browser.find_element_by_id("book").click()

# Math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

# Answer

input = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(y)

# Submit

submit = browser.find_element_by_css_selector("button.btn[type='submit']")
submit.click()