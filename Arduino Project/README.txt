Arduino-anturi + FastAPI + HTML-dashboard

Tämä projekti toteuttaa reaaliaikaisen lämpötila- ja kosteusvalvonnan Arduino-antureilla (DHT11 ja LM35). Mittaustiedot lähetetään Python-backendille ja esitetään visuaalisesti verkkoselaimessa.


Käytetyt teknologiat

- Arduino UNO + DHT11 + LM35 (sarjaliikenteen kautta)
- Python 3.11+
- FastAPI (sensoritietojen vastaanotto ja palvelu)
- Chart.js (kaaviot selaimessa)
- HTML + JavaScript (frontend käyttöliittymä)





Asennusohjeet:

 - Kloonaa tai kopioi koodi koneellesi:

bash
git clone <tähän oma repo-osoite>
cd "Arduino Project"

- Luo virtuaaliympäristö (suositeltu)

python -m venv venv
venv\Scripts\activate

- Asenna tarvittavat kirjastot

pip install fastapi uvicorn jinja2 pyserial
arduino IDE:ssä suosittelen lataa seuraavia kirjastoja:
Adafruit Unified Sensor
DHT sensor library
SimpleDHT


- Ja tarvittaessa jos ilmestyy ongelmia serjaportin yhdistämisessä voit lataa CH340 ajurin
linkki ltaussivuun (ensimmäinen latauslinkki): https://sparks.gogo.co.nz/ch340.html?srsltid=AfmBOopoafn--AzB7arNhUZsq5RO1DB-amKgH6rQ8VuuqWhZP7g5YTaO



Projektin käynnistys: 

 Varmista Arduino-yhteys

- Yhdistä Arduino USB:llä tietokoneeseen
- Lue sensorin dataa sarjaportilta (DHT11 ja LM35)
- Esimerkki johdotuksesta:

| Anturi | 5V | GND | Signaali |
| ------ | -- | --- | -------- |
| DHT11  | ✔️ | ✔️  | D2       |
| LM35   | ✔️ | ✔️  | A0       |


Kopioi arduinoIDE_code.txt- koodi ja lataa arduinoon. 

2. Käynnistä FastAPI-backend

uvicorn main:app --reload

Jos kaikki toimii, näet:

Uvicorn running on http://127.0.0.1:8000
Avaa selaimessa:
➡️ http://127.0.0.1:8000

3. Lähetä Arduino-data send_data.py-tiedostolla

python send_data.py


Sivussa näet: 
uusimman mitatun lämpötilan ja kosteuden

historiakaaviot (viimeiset 50 mittausta):

-DHT11 lämpötilan
-DHT11 kosteuden
-Ja LM35 lämpötilan

Kaaviot päivittyvät automaattisesti 5 sekunnin välein.




Vinkkejä jatkoon: 
Lisää tallennus tietokantaan (esim. SQLite, PostgreSQL)

Lisää käyttöliittymästä ajanjakson valinta

Tee sensorilukemista CSV/Excel-vienti

Lisää tunnistus/loki virheellisille mittauksille


Yt. Ivan Kotsalainen :)

