from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4  import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('./chromedriver')

depths=[] #List to store depths

driver.get("https://github.com/login?client_id=")

username = driver.find_element_by_id("login_field")

password = driver.find_element_by_id("password")

login = driver.find_element_by_name("commit")

username.send_keys("")
password.send_keys("")

login.click()

driver.get("https://adventofcode.com/2021/day/1/input")


soup = BeautifulSoup(driver.page_source)

pre = soup.select_one('pre').text

results = []

for line in pre.split('\n')[1:-1]:
        if '--' not in line:
            row = [line[i:i+7].strip() for i in range(0, len(line), 7)]
            results.append(row)

df = pd.DataFrame(results)
#print(df)

prev_value = 9999

up_count = 1

for (index_label, row_series) in df.iterrows():
    print(index_label, ":", row_series, " : ", up_count)
        
    if int(row_series) > int(prev_value):
        
        up_count = up_count+1
        
    
    prev_value = int(row_series)

print(up_count)