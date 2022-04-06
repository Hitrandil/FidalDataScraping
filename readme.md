# Fidal Data Scraping

 [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg) [![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg) [![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![Visual Studio Code](https://img.shields.io/badge/--007ACC?logo=visual%20studio%20code&logoColor=ffffff)](https://code.visualstudio.com/) 

Il progetto nasce con l'intento di ricreare il database della Fidal lombardia popolato con tutti i dati già pubblici e consultabili in maniera libera sul sito <a href="https://fidal.it" target="_blank" rel="noopener noreferrer"> FIDAL Italia. </a>

#### Il software è ancora in fase di sviluppo. 

#### Consulta qua lo stato attuale del progetto:

Dato l'url di una società, passata alla funzione `getLinkAtleti(urlSocieta)` la funzione recupera dalla pagina tutti i link degli atleti tesserati nell'anno corrente in quella società, man mano che trova i link li passa alla funzione `getDatiAtleta(urlAtleta)` la quale estrae e inserisce nel dict `datoGara[]` i seguenti dati:

* Nome Cognome
* Data Nascita (se presente)
* Data prestazione
* Disciplina
* Prestazione
* Società di tesseramento al momento della prestazione

Per ogni prestazione trovata tutta questa stringa viene passata alla funzione `insert(dato)` la quale carica in maniera grezza i dati sul db.

#### Miglioramenti logici nel codice:

* Rendere versatili tutte le funzioni, costruire dizionario per ognuna e gestire l'intero dizionario come dato in ingresso.

#### Todo:

* Progettazione db e relativo caricamento corretto;Visual Studio Code
* polivalenza nell'utilizzo, possibilità di salvare su file di diversi formati i dati prelevati dallo scraping;
* recuperare i dati degli atleti *in pensione*, attualmente se un atleta non è tesserato in nessuna società non si riesce a recuperare la sua pagina, se non manualmente;
* recuperare elenco di tutte le società italiane con relativo indirizzo link;
* visualizzare stato di avanzamento del caricamento;

<hr>

### ~~Come usarlo?~~

* Clonare la repository
* Creare un DB (da zero oppure utilizzando il file `database.sql*`)  che rispetti il modello er
* Modificare il file `.env` con la stessa struttura del `modello presente*`  nella repository inserendo gli estremi di accesso al database
* Eseguire lo script `main.py` per popolare il database o per aggiornarlo

##### ~~Automatizzare l'update del db (linux SO):~~

* Inserire nel crontab la seguente stringa:

### Compatibilità

Essendo scritto in python è compatibile ovunque questo venga installato. La guida per l'automatizzazione dello script è compatibile solamente con dispositivi Linux.

### Contattami

Mi puoi contattare su Telegram: <a href="https:t.me/hitrandil">@Hitrandil </a>

### Credits 

Il software è pensato e creato da <a href = "https://github.com/Hitrandil/">@hitrandil </a>.

<span style = "font-size: 10px;"> *i file contrassegnati con asterisco non sono ancora stati creati </span>



