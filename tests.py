from selenium import webdriver
import time # wait antil
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
"""
	открывает страницу в вк отправляет первому в друзьях сообщение
	
"""
#s = Service(executable_path='geckodriver.exe')
browser = webdriver.Firefox('aaa')
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла




try:


    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    a = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    send = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
    answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)



    chislo = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    res = calc(chislo)


    answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
    answer.send_keys(res)

    send2 = browser.find_element(By.XPATH, '//button[@id="solve"]').click()

    #alert = browser.switch_to.alert
    #alert.accept()
    #time.sleep(30)

    # res = calc(a)         btn btn-primary
    # input = browser.find_element(By.XPATH, '//input[@id="answer"]')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    # input.send_keys(res)
    # i_am_robots = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    #
    # robots_rule = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    # robots_rule.click()
    # send = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

    #browser.execute_script("return arguments[0].scrollIntoView(true);", send)
    # for i in  driver.find_elements(By.XPATH,'//input[@type="text"]'):
    #     i.send_keys('name')
    # z = driver.find_element(By.CSS_SELECTOR, "button.btn")
    # z.click()
    # time.sleep(1)
    # welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt

    # assert "Congratulations! You have successfully registered!" == welcome_text, '\033[31m{}'.format('Тест 1 проверка аутентификации ошибка')
    # print('\033[32m{}'.format('Тест 1 проверка аутентификации успешно'))


except AttributeError as ex:
    print(ex)
finally:
    pass

    time.sleep(50)
    browser.close()
    browser.quit()


