from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://google.com")
#driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("abc")

print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))
print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

driver.find_element(By.NAME, "btnK").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
assert "ABC Home Page - ABC.com" in driver.title

driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
driver.implicitly_wait(10)
# Find el Dancing
driver.find_element(By.XPATH, "//a[@class='AnchorLink fitt-tracker']//img[@class='aspect-ratio--child']").click()
driver.find_element(By.XPATH, "//a[@href='/shows/dancing-with-the-stars/episode-guide/season-28']").click()
assert "Dancing with the Stars Full Episodes | Watch Online | ABC" in driver.title

driver.close()