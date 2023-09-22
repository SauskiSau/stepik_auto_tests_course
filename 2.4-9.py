from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"






browser = webdriver.Chrome()
browser.get(link)
WebDriverWait(browser, "15").until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))  #Задаем счетчик ожидания
btn = browser.find_element(By.ID, "book") #Объявляем кнопку
btn.click()                   #Ипрокликиваем


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_in_text = browser.find_element(By.ID, "input_value")
x_value = x_in_text.text

# считаем значение x
first_answer = calc(x_value)
# скроллим страницу до появления на ней поля ввода в зоне видимости
first_input = browser.find_element(By.ID, "answer")

# вводим ответ в поле ввода

first_input.send_keys(first_answer)

btn1 = browser.find_element(By.ID, "solve")
btn1.click()

time.sleep(15)
browser.quit()
