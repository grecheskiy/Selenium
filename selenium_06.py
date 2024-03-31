# Импорт необходимых библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Установка веб-драйвера
driver = webdriver.Chrome()

# Переход на веб-сайт DuckDuckGo
driver.get("https://rtvi.us/")

# Поиск кнопки поиска и нажатие на нее
search_button = driver.find_element(By.XPATH, "//div[@class='container-footer']/div/div[2]/a[@href][6]")
search_button.click()

# Поиск всех результатов на странице
results = driver.find_elements(By.XPATH, "//div[@class='w-layout-grid section-block-grid']")
result_info = []

# Извлечение date и news-title каждого результата
for result in results:
    result_date = result.find_element(By.XPATH, ".//div").text
    result_news = result.find_element(By.XPATH, ".//a[@class='news-title-section']").text
    result_link = result.find_element(By.XPATH, ".//a").get_attribute("href")
    result_info.append([result_date, result_news, result_link])

driver.quit()

# Запись данных в файл CSV
with open("list_news.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "News-title", "Link"])
    writer.writerows(result_info)