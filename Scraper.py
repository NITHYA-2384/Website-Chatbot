import requests
from bs4 import BeautifulSoup

url = "https://www.apexisys.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text(separator=" ", strip=True)

# SAVE CORRECTLY
with open("data/website_data.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Data saved!")