# import bs4, requests, webbrowser

# FIDAL_VA129 = 'https://www.fidal.it/societa/Pol--Olonia/VA129'
# PRE_ATLETA = 'https://www.fidal.it/atleta/'
# ATLETA_ESEMPIO = 'https://www.fidal.it/atleta/Matilde-Silanos/drKRk5WncGU'

# response = requests.get(ATLETA_ESEMPIO) #ottiene la pagina html
# response .raise_for_status() #genera eccezione se la richiesta non è andata a buon fine
# soup = bs4.BeautifulSoup(response.text, 'html.parser'); #salvo in soup l'html della pagina
# div_competions = soup.find('div', class_='table-responsive') #trova tutti i div delle diverse discipline

# result_gare = div_competions.find_all('form')
# result_data = []
# for result_gare in result_gare:
#     result_data = str(div_competions.get(''))


import requests, re, json, mysql.connector, os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from mysql.connector import Error

conn = None
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host=os.getenv("HOST"),
                                       database=os.getenv("NAME_DB"),
                                       user=os.getenv("USER_DB"),
                                       password=os.getenv("PSW_DB"),
                                       auth_plugin='mysql_native_password')
        if conn.is_connected():
            print('Connected to MySQL database')
            return(conn)

    except Error as e:
        print('Connection error');
        print(e)
    

def insert(datoGara):
    mycursor = conn.cursor()
    if 'dataNascita' in datoGara:
        sql = "INSERT INTO prova (nome_cognome, data_nascita, data_prestazione, disciplina, prestazione, societa_prestazione) VALUES (%s, STR_TO_DATE(%s, '%d-%m-%Y'), STR_TO_DATE(%s, '%d/%m/%Y'), %s, %s, %s)"
        val = (datoGara['nomeCognome'], datoGara['dataNascita'], datoGara['data'], datoGara['disciplina'], datoGara['prestazione'], datoGara['societaPrestazione'])
    else:
        sql = "INSERT INTO prova (nome_cognome, data_prestazione, disciplina, prestazione, societa_prestazione) VALUES (%s,  STR_TO_DATE(%s, '%d/%m/%Y'), %s, %s, %s)"
        val = (datoGara['nomeCognome'], datoGara['data'], datoGara['disciplina'], datoGara['prestazione'], datoGara['societaPrestazione'])
    mycursor.execute(sql, val)

    conn.commit()

    print(mycursor.rowcount, "record inserted.")

def getLinkAtleti(urlSocieta):
    listAtleti = []
    PREFIX_ATL = "https://www.fidal.it/atleta/"
    SUFF_SOC = "#tab2"
    
    r = requests.get(urlSocieta)
    soup = BeautifulSoup(r.text, 'html.parser')

    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            for col in row.find_all('td'):
                links = col.find_all('a')
                if len(links)>0:
                    if PREFIX_ATL in links[0]['href']:
                        getDatiAtleta(links[0]['href'])
                        listAtleti.append(links[0]['href'])
    if SUFF_SOC in urlSocieta:
        return listAtleti
    return listAtleti + getLinkAtleti(urlSocieta + "#tab2")

def salvaSuFile(dato):
    fileJson = open('datiAtleti.json','a')
    fileJson.write(json.dumps(dato))

def getDatiAtleta(urlAtleta):
    """Ottiene i dati dell'atleta presenti nella pagina Fidal dello stesso, non tutti gli atleti hanno la dataNascita
    :param urlAtleta: url dell'atleta dal quale scaricare i dati 
    """
    date_extract_pattern = "[0-9]{1,2}\-[0-9]{1,2}\-[0-9]{4}"

    r = requests.get(urlAtleta)
    soup = BeautifulSoup(r.text, 'html.parser')
    atleta = []
    datoGara = {}

    datoGara["nomeCognome"] = soup.find_all('h1', limit = 1)[0].text
    dataNascita = soup.find_all(style='float:left;')
   
    dataNascita = re.findall(date_extract_pattern, dataNascita[1].text)
    if len(dataNascita)>0:
        datoGara["dataNascita"] = dataNascita[0]
    #todo tirare fuori società con link

    #?estraggo dati gare
    for table in soup.find_all('table', class_ ="table"):
        if len(table.find_all('form', method="post"))>0:
            for form in table.find_all('form', method="post"):
                #todo aggiungere luogo prestazione
                datoGara["data"] = form.find_all('input', attrs={"name": "titleDate"})[0]['value']
                datoGara["disciplina"] = form.find_all('input', attrs={"name": "titleSportType"})[0]['value']
                datoGara["prestazione"] = form.find_all('input', attrs={"name": "titleTime"})[0]['value'].strip()
                datoGara["societaPrestazione"] = form.find_all('input', attrs={"name": "titleN"})[0]['value']
                insert(datoGara)
                #!print(datoGara)

load_dotenv()
conn = connect()
#getDatiAtleta("https://www.fidal.it/atleta/Paolo-Colombo/drKRkpWnaWs%3D")i
getLinkAtleti("https://www.fidal.it/societa/POL--OLONIA/VA129")
#*----------link utili----------------------------------
#atleta senza data nascita: https://www.fidal.it/atleta/Paolo-Colombo/drKRkpWnaWs%3D
#atleta con data nascita: https://www.fidal.it/atleta/Laura-Cortesi/drKRk5iobmw%3D
#società: https://www.fidal.it/societa/POL--OLONIA/VA129
#*-------------------------------------------------------
