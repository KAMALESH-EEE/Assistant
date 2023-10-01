import requests
from bs4 import BeautifulSoup
url = "https://github.com/KAMALESH-EEE"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# Example: Extract the text of a specific element with a CSS selector
element = soup.select_one("/e-Mail_Writing")
if element:
    information = element.text
else:
    information = "Information not found"
print(information)