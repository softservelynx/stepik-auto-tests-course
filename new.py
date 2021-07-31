from selenium import webdriver
import math
import time

brlink = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(brlink)

try:

  browser.find_element_by_css_selector("button.btn[type='submit']").click()

  browser.switch_to.window(browser.window_handles[1])

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)

  input = browser.find_element_by_css_selector('#answer')
  input.send_keys(y)

finally:
    submit = browser.find_element_by_css_selector("button.btn[type='submit']")
    submit.click()
    time.sleep(10)
    browser.quit