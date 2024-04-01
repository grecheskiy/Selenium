# Импорт необходимых библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Установка веб-драйвера
driver = webdriver.Chrome()

# Переход на веб-сайт DuckDuckGo
driver.get("https://duckduckgo.com/")

# Поиск строки поиска и ввод поискового запроса
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("Selenium books")

# Поиск кнопки поиска и нажатие на нее
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

# Поиск выпадающего меню "Время" и щелчок по нему
time_dropdown = driver.find_element(By.XPATH, "//*[@id='links_wrapper']/div[1]/div[1]/div/div[3]/a")
time_dropdown.click()

# Поиск опции "За последний месяц" в выпадающем меню времени и щелчок по ней
time_last_month = driver.find_element(By.XPATH, "*//a[@data-value='m']")
time_last_month.click()
more_btn = driver.find_element(By.XPATH, "//button[@id='more-results']")
more_btn.click()

# Поиск всех результатов на странице
results = driver.find_elements(By.XPATH, "//div[@class='ikg2IXiCD14iVX7AdZo1']")
result_data = []

# Извлечение заголовка и URL каждого результата
for result in results:
    result_title = result.find_element(By.XPATH, ".//h2/a/span").text
    result_url = result.find_element(By.XPATH, ".//h2/a").get_attribute("href")
    result_data.append([result_title, result_url])

driver.quit()

# Запись данных в файл CSV
with open("duckduckgo2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Result Title", "URL"])
    writer.writerows(result_data)