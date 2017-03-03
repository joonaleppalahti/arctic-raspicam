# Raportti Arctic järjestelmäprojektin edistymisestä

##Sprint 1

Projektin aluksi kasasimme kaikki projektiin tarvittavat laitteet kasaan (Rasperry Pi 3 Model B, Web-kamera, 16 Gb MicroSD, Xubuntu 16.04.01 LTS kannettava ja kannettavan kortinlukija ja aloitimme työt. Koodi ja dokumentaatio sovittiin tallennettavaksi Joona Leppälahden Github repository:n. Arctic ryhmän jäsenet ovat: Jori Laine, Joona Leppälahti, Eero Kolkki ja Jarkko Koski.

Raspberry Pi ohjelmoidaan ottamaan kameralla kuvia, jotka se lähettää palvelimelle. Palvelin prosessoi kuvat videoiksi, jotka käyttäjä voi katsoa verkkokäyttöliittymästä. 

![alt text](https://github.com/joonaleppalahti/arctic-raspicam/blob/master/images/kaavio.png "Infrastruktuurikaavio")
**Kuva 1** Raspberry Pi ottaa kuvia webcamista, kun se havaitsee liikettä. Raspberryssä ajetaan Pythonin avulla OpenCV konenäköä, joka analysoi kuvaa ja tallentaa kuvia liikettä havaitessaan. Tallennetut kuvat Raspberry lähettää tietyin väliajoin Ubuntu palvelimelle, joka koostaa niistä videoita. Videot ovat katseltavissa Apachella toimivalla websivulla. Ubuntu palvelin toimii XenServerin päällä, jolla on muitakin käyttöjärjestelmiä.

###Raspberry Pi asennus
Ensimmäiseksi asensimme ohjelman GDDRescue tietokoneeseen, jolla asensimme Ubuntu Mate käyttöjärjestelmän Raspberry Pi 3 Model B:n muistikortille. Asennuksessa käytimme https://ubuntu-mate.org/raspberry-pi/ ohjeita ja komentoja. Asennuksen valmistuttua liitimme Raspberryn televisioon HDMI-kaapelilla ja tarkastelimme asennuksen tuloksia. Ubuntu Mate asentui onnistuneesti ja web-kamera toimi kun yhdistimme sen Raspberryyn.

![alt text](https://github.com/joonaleppalahti/arctic-raspicam/blob/master/images/raspi.png "Raspberry Pi")

**Kuva 2** Raspberry ja siihen liitetyt piuhat.

Päätimme aluksi kokeilla Kim Salmen opinnäytetyönä tekemää falldetector python ohjelmaa joka löytyy täältä: https://github.com/infr/falldetector-public/tree/master/fall-detector-v2. Asensimme ohjelman Kim Salmen ohjeiden mukaisesti ja se toimi niinkuin pitikin. 

###Python ohjelma
Seuraavaksi aloimme tutkimaan Kim Salmen tekemää koodia ja miettimään millaisen koodin tarvitsemme omaan ohjelmaamme. Otimme koodista sellaisia palasia joista uskoimme olevan apua projektissa ja muokkasimme niitä. Tämän jälkeen lisäsimme omat koodinpätkät väliin. 

Tämä ei kuitenkaan toiminut kuten ajattelimme koska ryhmällämme ei ollut riittäviä Python ohjelmointi- ja koodinlukutaitoja. Seuraava päivä käytetty opiskellen Pythonia CodeAcademyn Python harjoitusten avulla.

##Sprint 2

OpenCV:n asennus ja Python koodin kirjoitus alusta. Seurasimme OpenCV dokumentaatiota https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html ja ongelmakohdissa konsultoimme Stack Overflow:ta. Kim salmen opinnäytetyön koodista päädyimme käyttämään kuvan vertailu osaa eli liiketunnistusta. 

Kun Raspberry oli saatu näkemään ja tunnistamaan liikettä, seuraavaksi se piti saada ottamaan kuvia. Alkuun koodimme sai aikaan sen, että Raspi otti kuvan 24:n frame:in välein joten kuvia tuli fps:n sidottuun tahtiin. https://github.com/joonaleppalahti/arctic-raspicam/commit/b50800e175d33676976a61394b5c6177b9aca508

Koodi kuitenkin toimi ja kuvia syntyi, joten seuraava vaihe oli sen uudelleen kirjoittaminen jotta se ottaisi vähemmän kuvia, kuvan otto nopeudeksi tuli kuva per sekuntti.https://github.com/joonaleppalahti/arctic-raspicam/blob/master/capture.py

Tämä koodi toimi halutulla tavalla.

###Muuta
Python ohjelman lisäksi projektia varten tehtiin bash-skripti joka siirtää web-kameran ottamat kuvat palvelimelle. Scripti laitettiin ajettavaksi automaattisesti Cron:illa alkuun 1 minuutin välein.

##ToDo-lista
* Web-käyttöliittymä
* Videoiden koostaminen kuvista
* Python koodin hiominen
* Ohjelman automaattinen ajaminen Raspberryn käynnistyessä
* Kuvien ohjaaminen Arctic:n palvelimelle
* Projektin esittelymateriaali
* Asennusohjeiden laatiminen

##Asennusohjeet (Tämän ohjeen on todettu toimivan Ubuntu Mate käyttöjärjestelmässä)
1. Muistikortin alustus ja käyttöjärjestelmän asennus
Liitä muistikortti tietokoneeseen, lataa Ubuntu Mate (https://ubuntu-mate.org/download/) ja aja seuraavat komennot.

sudo apt-get install gddrescue xz-utils
unxz ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz
sudo ddrescue -D --force ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img /dev/sdx 
(sdx tilalle tulee muistikorttia vastaava laite. Esim meidän tapauksessa mmcblk0.)

kun muistikortti on valmis voi sen asentaa raspiin.

Kytke Raspberry Pi HDMI-liitännällä näyttöön, kytke myös webbikamera, hiiri ja näppäimistö.
Käynnistä Raspberry Pi ja asenna Ubuntu Mate seuraten asennusohjelman antamia ohjeita ja vastaten sen tietopyyntöihin.

2. Kameran asentaminen Raspberryyn 
Avaa komentorivi (terminal) ja aja ensin sudo apt-get update.

Asenna seuraavat ohjelmat sudo apt-get install komennolla: libopencv-dev ja python-opencv
sudo apt-get install libopencv-dev python-opencv.

Sitten asennetaan numpy pythonin avulla, asennus saattaa kestää hetken.
pip install numpy

sitten asennetaan git
sudo apt-get install git

gitin asennuttua voidaan kloonata git repo jossa on kameran koodit valitse haluamasi kansio ja kloonaa repo komennola
git clone https://github.com/joonalepppalahti/arctic-raspicam.git

tässä vaiheessa voi kokeilla että kamera toimii mene arctic-raspicam kansioon ja anna komento
python test.py
kameran pitäisi käynnistyä ja siinä pitäisi näkyä kameran näkemät kuvat.

luodaan kuville tallenuskansio komennolla 
mkdir /home/$(whoami)/img

kuvien lähettämiseksi palvelimelle, muokataan upload.sh tiedostosta käyttäjänimi ja ip osoite samaksi kuin palvelimella.

Ajastetaan kuvien siirto palvelimelle komennolla:
crontab -e

Lisää dokumentin loppuun:
@reboot python /home/käyttäjänimi/arctic-raspicam/capture.py
*/1 * * * * /home/käyttäjänimi/arctic-raspicam/upload.sh

Seuraavaksi luodaan ssh-avaimet komennolla ssh-keygen -t rsa. Lähetä sitten avaimet palvelimelle komennolla ssh-copy-id käyttäjä@IP-osoite

lopuksi käynnistä kamera
python capture.py



