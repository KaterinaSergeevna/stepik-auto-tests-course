from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_x = browser.find_element_by_id("num1")
    x = find_x.text
    print(x)

    find_y = browser.find_element_by_id("num2")
    y = find_y.text
    print(y)

    exam = str(int(x) + int(y))
    print(exam)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(exam)

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    time.sleep(3)
    browser.quit()