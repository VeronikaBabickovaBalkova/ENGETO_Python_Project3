"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Veronika Balková
email: veronika.balkova@rohde-schwarz.com
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv

def main():
    # Kontrola, zda byly zadány správné argumenty při spuštění skriptu
    if len(sys.argv) != 3:
        print("Usage: python main.py <URL> <output_filename>")
        sys.exit(1)

    # Uložení URL a názvu výstupního souboru z argumentů
    url = sys.argv[1]
    output_filename = sys.argv[2]

    # Kontrola, zda URL začíná správným adresářem
    if not url.startswith("https://www.volby.cz/"):
        print("Invalid URL. Please provide a valid URL from volby.cz.")
        sys.exit(1)

    # Stažení dat z daného URL
    raw_data = download_data(url)
    # Extrakce odkazů na jednotlivé obce z stažených dat
    links = extract_links(raw_data)
    all_data = []
    all_party_names = []  # Použijeme seznam pro zachování pořadí názvů stran
    # Pro každou obec zpracujeme data
    for code, location, link in links:
        obec_data, party_names = process_obec_data(code, location, link)
        all_data.append(obec_data)
        if not all_party_names:  # Pokud seznam názvů stran je prázdný, přidáme názvy z první obce
            all_party_names = party_names
    # Generování CSV souboru s výsledky
    generate_csv(all_data, output_filename, all_party_names)

def download_data(url):
    # Stažení HTML obsahu z daného URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to download data")

def extract_links(raw_data):
    # Parsování HTML obsahu pomocí BeautifulSoup
    soup = BeautifulSoup(raw_data, 'html.parser')
    links = []
    # Najdeme všechny tabulky s třídou 'table'
    tables = soup.find_all('table', class_='table')
    for table in tables:
        # Pro každou tabulku projdeme řádky, kromě prvních dvou (hlavičky)
        for row in table.find_all('tr')[2:]:
            cols = row.find_all('td')
            # Zkontrolujeme, zda máme alespoň dva sloupce
            if len(cols) >= 2:
                code = cols[0].text.strip()  # Kód obce
                location = cols[1].text.strip()  # Název obce
                link_tag = cols[0].find('a')
                # Získáme odkaz na podstránku s detailními daty
                if link_tag and link_tag.get('href'):
                    href = link_tag.get('href')
                    full_url = f"https://www.volby.cz/pls/ps2017nss/{href}"
                    links.append((code, location, full_url))
    return links

def process_obec_data(code, location, url):
    # Stažení HTML obsahu z podstránky pro konkrétní obec
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Najdeme tabulku s ID 'ps311_t1', která obsahuje základní údaje
        table1 = soup.find('table', id='ps311_t1')
        if table1 is None:
            print(f"Table1 not found for URL: {url}")
            return [code, location, None, None, None], []
        
        row1 = table1.find_all('tr')[2]
        cols1 = row1.find_all('td')
        registered = cols1[3].text.strip()  # Počet registrovaných voličů
        envelopes = cols1[4].text.strip()   # Počet vydaných obálek
        valid = cols1[7].text.strip()       # Počet platných hlasů

        # Extrahujeme data z tabulek stran
        party_votes = {}
        party_names = []
        tables = soup.find_all('table', class_='table')[1:]  # Najdeme všechny tabulky s třídou 'table' kromě první
        for table2 in tables:
            for row in table2.find_all('tr')[2:]:
                cols2 = row.find_all('td')
                party_name = cols2[1].text.strip()  # Název strany
                votes = cols2[2].text.strip()       # Počet hlasů pro stranu
                party_votes[party_name] = votes
                party_names.append(party_name)

        # Kombinujeme základní údaje s údaji o stranách
        return [code, location, registered, envelopes, valid] + [party_votes[name] for name in party_names], party_names
    else:
        raise Exception("Failed to download data for obec")

def generate_csv(data, filename, party_names):
    # Definujeme hlavičku CSV souboru
    header = ["code", "location", "registered", "envelopes", "valid"] + party_names
    
    # Uložení dat do CSV souboru s kódováním UTF-8 s BOM
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Zapíšeme hlavičku
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    main()
