from selenium import webdriver
import time
import math

#def calc(x,y):
#    return str(x + y)

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    find_x = browser.find_element_by_id("num1")
    x = find_x.text
    print(find_x)
    print(x)

    find_y = browser.find_element_by_id("num2")
    y = find_y.text
    print(find_y)
    print(y)

    exam = str(int(x) + int(y))
    print(exam)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector('option[value=\"exam\"]').click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()