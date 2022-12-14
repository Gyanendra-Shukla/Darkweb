from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="Downloads\chromedriver_win32")
driver.get("https://medium.com/tag/technology")
data = driver.page_source
alldata = ''.join(data)
soup = BeautifulSoup(alldata, 'html.parser')
head = []
link = []
content = []

heading = soup.find_all('h2', class_='be ek kk kl km kn eo ko kp kq kr es ks kt ku kv ew kw kx ky kz fa la lb lc ld fe ff fg fh fj fk bj')

hr = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/div/div/article/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a')

for a in range(len(heading)):
    head.append(heading[a].string)
for l in range(len(hr)):
    link.append(hr[l].get_attribute('href'))
for p in Link:
    driver.get(p)
    ta = driver.page_source
    aldata = ''.join(ta)
    soup = BeautifulSoup(aldata, 'html.parser')
    D = soup.find_all('div', id="root")
    temp = ""
    for m in range(len(D)):
        temp += D[m].get_text()
    content.append(temp)
# print(len(content))
# print(len(link))
# print(len(head))

w = pd.DataFrame({'Heading': Head, 'Link': Link, 'Content': Content})
w.to_csv('mediumtech.csv', index=False)
print(w)
