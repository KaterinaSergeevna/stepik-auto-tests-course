from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//div[@class="first_block"]/div[1]/input')
    input1.send_keys("Iv")
    input2 = browser.find_element_by_xpath('//div[@class="first_block"]/div[2]/input')
    input2.send_keys("Pet")
    input3 = browser.find_element_by_xpath('//div[@class="first_block"]/div[3]/input')
    input3.send_keys("Smo")
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
