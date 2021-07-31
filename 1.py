from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_css_selector('div.first_block input.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('div.first_block input.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('div.first_block input.third')
    input3.send_keys("zalup@gmail.com")
 #   input4 = browser.find_element_by_css_selector('')
 #   input4.send_keys("")
 #   input5 = browser.find_element_by_css_selector('')
 #   input5.send_keys("")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()