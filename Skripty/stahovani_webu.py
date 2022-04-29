# scraping

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
URL = "https://en.wikipedia.org/wiki/List_of_Olympic_records_in_athletics"
page = requests.get(URL, headers=header)

soup = BeautifulSoup(page.content, "html.parser")

tabulky = soup.find("table", class_ = "wikitable sortable plainrowheaders")

radky = tabulky.find("tbody")

i = 0
vysledna_tabulka = []
for radek in radky.find_all("tr"):
    data_v_radku = []
    
    for kazde_th in radek.find_all("th"):
        prvni_bunka_data = kazde_th
        if prvni_bunka_data != "" and prvni_bunka_data is not None:
            text_v_prvni_bunce = prvni_bunka_data.text.rstrip()
            text_v_prvni_bunce = text_v_prvni_bunce.replace(",", "")
            data_v_radku.append(text_v_prvni_bunce)
            
    for kazde_td in radek.find_all("td"):
        bunka_data = kazde_td
        if bunka_data != "" and bunka_data is not None:                
            text_v_bunce = bunka_data.text.replace("\u2666", "*")
            k = text_v_bunce.rfind("\n")
            text_v_bunce = text_v_bunce[:k]
            text_v_bunce = text_v_bunce.replace(",", "")
            data_v_radku.append(text_v_bunce)
    
    if data_v_radku != []:
        vysledna_tabulka.append(data_v_radku)

import csv

with open('./stazena_data.csv', 'w', newline='') as f:
    data_writer = csv.writer(f)
    data_writer.writerows(vysledna_tabulka)