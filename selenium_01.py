from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
# driver.back()
# driver.forward()
# driver.refresh()
# print(driver.title)
# print(driver.current_url)

search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys("laptops")
search_box.submit()

assert "laptops" in driver.title

div_element = driver.find_element(By.XPATH, '//div[@data-asin="B0B2D77YB8"]/div/div/span/div/div/div/div[2]/div/div/div[@data-cy="title-recipe"]/h2/a/span')
print(div_element.text)
print(div_element.get_attribute("class"))