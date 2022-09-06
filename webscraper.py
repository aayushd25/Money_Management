import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:/Users/User/Downloads/chromedriver.exe')
driver.get('https://www.incharge.org/financial-literacy/budgeting-saving/how-to-make-a-budget/')
result = []
content = driver.page_sources
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs="<a href="#Budget_Calculator">Budget Calculator</a>"):
    name = element.find('href')
    if name not in results: 
        results.append(name.text)
df = pd.DataFrame({"Names": results})
df.to_csv('names.csv', index=False, encoding="utf-8")