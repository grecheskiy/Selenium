# Импорт необходимых библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Установка веб-драйвера
driver = webdriver.Chrome()

# Переход на веб-сайт DuckDuckGo
driver.get("https://www.amazon.com/")

# Использование явного ожидания, при котором выполняется неблокирующее ожидание продолжительностью 10 секунд до тех пор, 
# пока не будет найден требуемый веб-элемент (с использованием его атрибута ID)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "field-keywords"))       
    )
except:
    print('some error happen !!!')
          
# Поиск строки поиска и ввод поискового запроса
search_bar = driver.find_element(By.NAME, "field-keywords")
search_bar.send_keys("chronicles nba basketball card")

# Поиск кнопки поиска и нажатие на нее
search_button = driver.find_element(By.XPATH, "//input[@type='submit']")
search_button.click()

# Поиск всех результатов на странице
results = driver.find_elements(By.XPATH, "//div[@class='a-section a-spacing-base']")
result_data = []

# Извлечение названия и цены каждого результата
for result in results:
    result_name = result.find_element(By.XPATH, ".//div[2]/div/h2/a/span").text
    result_price = result.find_element(By.XPATH, ".//div[2]/div[2]/div/div/a/span").text
    result_data.append([result_name, result_price])

driver.quit()

# Запись данных в файл CSV
with open("Selenium_homework/cards.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price"])
    writer.writerows(result_data)