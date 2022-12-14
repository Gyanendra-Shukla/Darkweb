from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="Downloads\chromedriver_win32")
driver.get("https://medium.com/tag/technology")
data = driver.page_source
alldata = ''.join(data)
soup = BeautifulSoup(alldata, 'html.parser')
Head = []
Link = []
Content = []

A = soup.find_all('h2', class_='be ek kk kl km kn eo ko kp kq kr es ks kt ku kv ew kw kx ky kz fa la lb lc ld fe ff fg fh fj fk bj')

C = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/div/div/article/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a')

for a in range(len(A)):
    Head.append(A[a].string)
for l in range(len(C)):
    Link.append(C[l].get_attribute('href'))
for o in Link:
    driver.get(o)
    ta = driver.page_source
    aldata = ''.join(ta)
    soup = BeautifulSoup(aldata, 'html.parser')
    D = soup.find_all('div', id="root")
    tem = ""
    for m in range(len(D)):
        tem += D[m].get_text()
    Content.append(tem)
print(len(Content))
print(len(Link))
print(len(Head))

w = pd.DataFrame({'Heading': Head, 'Link': Link, 'Content': Content})
w.to_csv('mediumtech.csv', index=False)
print(w)