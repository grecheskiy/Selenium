# Импорт необходимых библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Установка веб-драйвера
driver = webdriver.Chrome()

# Переход на веб-сайт DuckDuckGo
driver.get("https://www.amazon.com/")

# Поиск строки поиска и ввод поискового запроса
search_bar = driver.find_element(By.NAME, "field-keywords")
search_bar.send_keys("chronicles nba basketball card")

# Поиск кнопки поиска и нажатие на нее
search_button = driver.find_element(By.XPATH, "//input[@type='submit']")
search_button.click()

# # Поиск выпадающего меню "Время" и щелчок по нему
# time_dropdown = driver.find_element(By.XPATH, "//span[@class='a-dropdown-container']/span/span/i")
# time_dropdown.click()

# # Поиск опции "За последний месяц" в выпадающем меню времени и щелчок по ней
# time_last_month = driver.find_element(By.XPATH, "//div[@class='a-popover-wrapper']/div/ul/li[6]/a[@href]")
# time_last_month.click()

# Поиск всех результатов на странице
results = driver.find_elements(By.XPATH, "//div[@class='a-section a-spacing-base']")
result_data = []

# Извлечение заголовка и URL каждого результата
for result in results:
    result_title = result.find_element(By.XPATH, ".//div[2]/div/h2/a/span").text
    result_url = result.find_element(By.XPATH, ".//div[2]/div[2]/div/div/a/span/span").text
    result_data.append([result_title, result_url])

driver.quit()

# Запись данных в файл CSV
with open("cards.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Result Title", "URL"])
    writer.writerows(result_data)