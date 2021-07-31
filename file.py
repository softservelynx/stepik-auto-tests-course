from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element_by_css_selector("input[name='firstname']").send_keys("Firstname")
browser.find_element_by_css_selector("input[name='lastname']").send_keys("Lastname")
browser.find_element_by_css_selector("input[name='email']").send_keys("Email")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt') 

browser.find_element_by_id("file").send_keys(file_path)

browser.find_element_by_css_selector("button.btn[type='submit']").click()