# Raportti Arctic järjestelmäprojektin edistymisestä

##20.02.2017 

Projektin aluksi kasasimme kaikki projektiin tarvittavat laitteet kasaan (Rasperry Pi 3 Model B, Web-kamera, 16 Gb MicroSD, Xubuntu 16.04.01 LTS kannettava ja kannettavan kortinlukija ja aloitimme työt. Koodi ja dokumentaatio sovittiin tallennettavaksi Joona Leppälahden Github repository:n. Arctic ryhmän jäsenet ovat: Jori Laine, Joona Leppälahti, Eero Kolkki ja Jarkko Koski.

Raspberry Pi ohjelmoidaan ottamaan kameralla kuvia, jotka se lähettää palvelimelle. Palvelin prosessoi kuvat videoiksi, jotka käyttäjä voi katsoa verkkokäyttöliittymästä. 

![alt text](https://github.com/joonaleppalahti/arctic-raspicam/blob/master/images/kaavio.png "Infrastruktuurikaavio")

###Raspberry Pi asennus
Ensimmäiseksi asensimme ohjelman GDDRescue tietokoneeseen, jolla asensimme Ubuntu Mate käyttöjärjestelmän Raspberry Pi 3 Model B:n muistikortille. Asennuksessa käytimme https://ubuntu-mate.org/raspberry-pi/ ohjeita ja komentoja. Asennuksen valmistuttua liitimme Raspberryn televisioon HDMI-kaapelilla ja tarkastelimme asennuksen tuloksia. Ubuntu Mate asentui onnistuneesti ja web-kamera toimi kun yhdistimme sen Raspberryyn.

Päätimme aluksi kokeilla Kim Salmen opinnäytetyönä tekemää falldetector python ohjelmaa joka löytyy täältä: https://github.com/infr/falldetector-public/tree/master/fall-detector-v2. Asensimme ohjelman Kim Salmen ohjeiden mukaisesti ja se toimi niinkuin pitikin. 

###Python ohjelma
Seuraavaksi aloimme tutkimaan Kim Salmen tekemää koodia ja miettimään millaisen koodin tarvitsemme omaan ohjelmaamme. Otimme koodista sellaisia palasia joista uskoimme olevan apua projektissa ja muokkasimme niitä. Tämän jälkeen lisäsimme omat koodinpätkät väliin. 

Tämä ei kuitenkaan toiminut kuten ajattelimme koska ryhmällämme ei ollut riittäviä Python ohjelmointi- ja koodinlukutaitoja. Seuraava päivä käytetty opiskellen Pythonia CodeAcademyn Python harjoitusten avulla.

##22.02.2017

OpenCV:n asennus ja Python koodin kirjoitus alusta. Seurasimme OpenCV dokumentaatiota https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html ja ongelmakohdissa konsultoimme Stack Overflow:ta. Kim salmen opinnäytetyön koodista päädyimme käyttämään kuvan vertailu osaa eli liiketunnistusta. 

Kun Raspberry oli saatu näkemään ja tunnistamaan liikettä, seuraavaksi se piti saada ottamaan kuvia. Alkuun koodimme sai aikaan sen, että Raspi otti kuvan 24:n frame:in välein joten kuvia tuli fps:n sidottuun tahtiin. https://github.com/joonaleppalahti/arctic-raspicam/commit/b50800e175d33676976a61394b5c6177b9aca508

Koodi kuitenkin toimi ja kuvia syntyi, joten seuraava vaihe oli sen uudelleen kirjoittaminen jotta se ottaisi vähemmän kuvia, kuvan otto nopeudeksi tuli kuva per sekuntti.https://github.com/joonaleppalahti/arctic-raspicam/blob/master/capture.py

Tämä koodi toimi halutulla tavalla.

###Muuta
Python ohjelman lisäksi projektia varten tehtiin bash-skripti joka siirtää web-kameran ottamat kuvat palvelimelle.

