import requests
from bs4 import BeautifulSoup

with open("data.html", "r") as htmldata:
  bs4data = BeautifulSoup(htmldata, "html.parser")

  table_data = bs4data.find("table", attrs={"class": "table"})

  # print(table_data)

  print("NHL Hockey Teams since 1990:")
  for tr in table_data.find_all("tr", attrs={"class": "team"}):
    hockey_team = tr.find("td", attrs={"class": "name"}).get_text().strip()
    year = tr.find("td", attrs={"class": "year"}).get_text().strip()
    wins = tr.find("td", attrs={"class": "wins"}).get_text().strip()
    losses = tr.find("td", attrs={"class": "losses"}).get_text().strip()

    print(f"{year} {hockey_team}, {wins}W/{losses}L")
