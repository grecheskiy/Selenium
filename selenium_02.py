from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top")

movie_title_elements = driver.find_elements(By.CSS_SELECTOR, "a.ipc-title-link-wrapper h3")
rating_elements = driver.find_elements(By.CSS_SELECTOR, "div.sc-e2dbc1a3-0 span.ipc-rating-star--imdb")

titles = [element.text for element in movie_title_elements]
ratings = [element.text for element in rating_elements]

for i in range(10):
    print("Rating {}: {} ({})".format(i + 1, titles[i], ratings[i]))

driver.quit()