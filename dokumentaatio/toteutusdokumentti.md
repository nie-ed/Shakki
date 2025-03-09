# Toteutusdokumentti

## Ohjelman yleisrakenne

Projektissa on toteutettu tekoäly shakkipelille. Projektin käyttöliittymänä on käytetty annettua tekoälyalustaa. Sovellusta voi käyttää tekoälyalustan kautta, liikuttamalla valkoisia nappuloita, jonka jälkeen tekoäly tekee vuorollaan siirron mustalla nappulalla.

Projektin minimax-algoritmi sekä heuristiikkafunktio sijaitsevat minimax kansiossa. Nappuloiden siirtojen etsintä funktiot sijaitsevat movement_of_pieces kansiossa. Testit sijaitsevat tests kansiossa. Muut tiedostot sijaitsevat juurikansiossa.

Sovelluksen käynnistää index.py tiedosto, joka kommunikoi tekoälykäyttöliittymän kanssa sekä kutsuu funktiota, joka käynnistää minimax-algoritmin toiminnan. Luokan Minimax kautta toteutuu minimax-algoritmi sekä kutsutaan liikkeiden etsinnän ja tarkastuksen funktioita. 

Projekti on toteutettu Python kielellä. Tekoälyn toteutukseen on käytetty minimax-algoritmia sekä alpha-beta karsintaa.

## Aika- ja tilavaativuudet

Aikavaativuus on O(b^d) koska oletetaan, että alimmalla puun tasolla d on b määrä solmuja käytävä läpi.

Tilavaativuus on O(bd), missä b on suurin yhden solmun mahdollisten valintojen määrä ja d on puun korkeus. Algoritmissa mennään ensin rekursiivisesti puun alimmalle tasolle, valitsemalla matkalla jokaiselta tasolta yksi solmu, jonka lapset lisätään muistiin ja valitaan taas niistä yksi solmu, jonka lapset lisätään muistiin jne. Kun ollaan saavutettu alin taso, käydään kaikki tämän vanhemman solmun lapset läpi ja löydetään vanhemmalle arvo. Tämän jälkeen tämän vanhemman läpi käydyt lapset poistaa muistista. Näin ollen, tulee jokaisella tasolla olemaan b solmua muistissa, joka hetkellä, eli muistivaativuudeksi tulee b*d.

Alpha-beta karsinnalla on mahdollisuus pienentää aika- ja tilavaativuutta, kuitenkaan se ei ole taattu, että se tapahtuu.

## Työn mahdolliset puutteet ja parannusehdotukset

Projektia voisi refaktoroida siistimmäksi. 
Tällä hetkellä projektissa ei ole toimitoja erikoissiirroille tai -tilanteille, kuten tornitukselle, ohestalyönnille, sotilaan korotukselle eikä toistuvaan asemaan perustuvalle tasapelille. Näitä voisi toteuttaa tulevaisuudessa.

## Laajojen kielimallien käyttö.

Työssä ei ole käytetty laajoja kielimalleja.

## Viitteet

- https://www.quora.com/What-are-some-heuristics-for-quickly-evaluating-chess-positions
- https://jyx.jyu.fi/jyx/Record/jyx_123456789_12488?sequence=1&isAllowed=y
- https://stackoverflow.com/questions/2080050/how-do-we-determine-the-time-and-space-complexity-of-minmax