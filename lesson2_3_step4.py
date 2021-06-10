from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_class_name("btn.btn-primary").click()
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)
    
    browser.get("http://suninjuly.github.io/alert_redirect.html?")
    find_x = browser.find_element_by_id("input_value")
    x = find_x.text
    print("value x:", x)
    y = calc(x)
    print(y)

    sent_value = browser.find_element_by_id("answer")
    sent_value.send_keys(y)

    browser.find_element_by_class_name("btn.btn-primary").click() 

    alert = browser.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    answer = alert_text[-1]
    print("answer:", answer)

    browser.get("https://stepik.org/catalog?auth=login&language=ru")   
    time.sleep(8)

    browser.find_element_by_id("id_login_email").send_keys("klimova.ek.ser@yandex.by")
    browser.find_element_by_id("id_login_password").send_keys("QWas12ed34")
    
    browser.find_element_by_class_name('sign-form__btn').click()  
    time.sleep(3)
    browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    time.sleep(3)  

    answer_input = browser.find_element_by_css_selector('textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)

    button = browser.find_element_by_class_name('submit-submission')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()
 
finally:
    time.sleep(3)
  #  browser.quit()