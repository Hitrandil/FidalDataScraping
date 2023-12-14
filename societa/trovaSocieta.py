import json
from bs4 import BeautifulSoup
import re

# Funzione per estrarre il codice identificativo dalla stringa tra parentesi
def extract_code(text):
    match = re.search(r'\((.*?)\)', text)
    if match:
        return match.group(1)
    else:
        return None

# Apre il file HTML
with open('societa.html', 'r') as file:
    html_content = file.read()

# Parsing del file HTML con BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Crea una lista per salvare i dati
societa_list = []

# Estrai i dati e aggiungili alla lista
divs = soup.find_all('div', style='min-height: 100px')
for div in divs:
    b_tag = div.find('b')
    a_tag = div.find('a')
    if b_tag and a_tag:
        nome = b_tag.text
        link = a_tag['href']
        codice = extract_code(nome)
        if codice:
            nome = nome.replace(f" ({codice})", "") 
            societa = {  
                'codice': codice,
                'nome': nome,
                'link': link
            }
            societa_list.append(societa)

# Salva la lista come file JSON
with open('societa.json', 'w', encoding='utf-8') as json_file:
    json.dump(societa_list, json_file, ensure_ascii=False, indent=4)

print("Dati salvati in societa.json.")
