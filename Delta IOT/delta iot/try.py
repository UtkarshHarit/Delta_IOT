import requests

url = "https://weather.com/weather/hourbyhour/l/Kendall+FL+USFL0240:1:US"

page = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.text)

#right_table=soup.find_all('table')

aa = soup.find('tr class="clickable open" classname ="clickable open"')

print (aa)




