from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://svts10182803.wordpress.com/")
#driver.maximize_window()
driver.find_element(By.ID, 'g2-name').send_keys("name")
driver.find_element(By.ID, 'g2-email').send_keys("1234@gmail.com")
driver.find_element(By.ID, 'contact-form-comment-g2-message').send_keys("hello")
driver.find_element(By.CLASS_NAME, 'pushbutton-wide').submit()




driver.implicitly_wait(10)

driver.close()