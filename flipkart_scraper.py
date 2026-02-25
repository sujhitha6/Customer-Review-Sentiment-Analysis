import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = uc.Chrome()

reviews = []
ratings = []

for page in range(1, 4):

    url = f"https://www.flipkart.com/product-reviews/MOBH8G3PZGYF9GED?page={page}"
    driver.get(url)

    time.sleep(6)

    review_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'ZmyHeo')]")
    rating_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'XQDdHH')]")

    print("Reviews found:", len(review_elements))

    for r in review_elements:
        reviews.append(r.text)

    for rt in rating_elements:
        ratings.append(rt.text)

data = pd.DataFrame({
    "Review": reviews,
    "Rating": ratings
})

data.to_csv("flipkart_reviews.csv", index=False)

print("Scraping Completed ✅")
print("Total Reviews:", len(data))

driver.quit()