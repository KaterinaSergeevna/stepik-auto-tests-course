from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_class.name("nowrap")
    x = x_element.text
    y = calc(x)

    fil = browser.find_element_by_id("answer")
    fil.send_keys(y)

    che = browser.find_element_by_id("robotCheckbox")
    che.click()

    rob = browser.find_element_by_id("robotsRule")
    rob.click()

    sub = browser.find_element_by_css_selector('type["submit"]')
    sub.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()




