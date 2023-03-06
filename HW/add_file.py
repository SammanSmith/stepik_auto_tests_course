from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.dirname(__file__)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    fn.send_keys('Jack')
    ln = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    ln.send_keys('Sparrow')
    email = browser.find_element(By.XPATH, '//input[@name="email"]')
    email.send_keys('JSparrow@mail.ru')

    file = browser.find_element(By.ID, 'file')
    full_path = os.path.join(current_dir, 'text.txt')
    file.send_keys(full_path)

    btn = browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()