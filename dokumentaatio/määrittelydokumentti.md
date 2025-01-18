# Määrittelydokumentti
Olen tietojenkäsittelytieteen kandidaatti (TKT) Helsingin yliopistossa.

## Aihe ja toteutus
Toteutan shakkipelille tekoälyn. Algoritmina käytän minimax-algoritmia, tehostetulla alpha-beta-karsinnalla.

Syötteinä ohjelma saa korkeuden johon saakka halutaan tutkia tulevia siirtoja, tämän hetken solmun ja tiedon onko tällä hetkellä kyseessä maximipelaajan vai minimipelaajan vuoro.

Algoritmissa tekoäly yrittää löytää polun, jossa on mahdollisimman suuri taattu arvo, ja olettaa, että vastustaja valitsee itselleen optimiratkaisun seuraavissa siirrossa. Solmut käydään rekursiivisesti läpi ja luodaan kaikista mahdollisista seuraavista siirroista koostuva pelipuu, kunnes ollaan saavutettu raja, johon lopetetaan, eli annettu korkeus. Joka askeleella algoritmi käy läpi tämän hetken solmun lapset (kaikki mahdolliset tilanteet joihin voi päästä seuraavan laillisen siirron seurauksena).

Kun ollaan saavutettu haluttu korkeus, algoritmi laskee luodun puun alimmille solmuille jotkin arvot. Arvot lasketaan esim. pelaajan oman nappuloiden määrän, vastustajan nappuloiden määrän ja nappuloiden laudalle sijoittumisen perusteella. Sitten algoritmi palauttaa arvon edelliselle tasolle, jossa riippuen siitä onko pelaaja maksimipelaaja vai minimipelaaja, verrataan palautunutta arvoa edelliseen maksimi/minimi arvoon ja korvataan tarvittaessa. Maksimipelaaja (tekoäly) valitsee aina suurimman mahdollisen arvon, minimipelaaja (vastustaja) pienimmän. 

Lisäksi, kun algoritmia tehostetaan, tulee algoritmille myös syötteenä alpha-beta-karsinnalle tarpeelliset alpha ja beta arvot.

Aikavaativuustavoitteena on O(b^d) ja tilavaativuustavoitteena on O(bd), missä b on suurin yhden solmun mahdollisten valintojen määrä ja d on puun korkeus.

Aikavaativuusarviossa jätämme vakion huomioita, tällöin arvio on b^d, koska oletetaan, että alimmalla puun tasolla d on b määrä solmuja käytävä läpi. Funktio on f(d)=SUM(i=1,...,d){b^i}.

Tilavaativuustavoite saadaa, koska algoritmissa mennään ensin rekursiivisesti puun alimmalle tasolle, valitsemalla matkalla jokaiselta tasolta yksi solmu, jonka lapset lisätään muistiin ja valitaan taas niistä yksi solmu, jonka lapset lisätään muistiin jne. Kun ollaan saavutettu alin taso, käydään kaikki tämän vanhemman solmun lapset läpi ja löydetään vanhemmalle arvo. Tämän jälkeen tämän vanhemman läpi käydyt lapset poistaa muistista. Näin ollen, tulee jokaisella tasolla olemaan b solmua muistissa, joka hetkellä, eli muistivaativuudeksi tulee b*d.

## Ohjelmointikieli

Ohjelmointikieli on Python. Mielellään vertaisarvioisin muita Pythonilla toteutettuja töitä, mutta osaan myös hieman Javaa, mikäli tarve.

## Ydin
Aiheeni ydin on tekoälyn. Eli tekoälyn toteuttaminen shakkipelille. 

## Lähteet
- https://en.wikipedia.org/wiki/Minimax
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
- https://www.youtube.com/watch?v=l-hh51ncgDI
- https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/tirakirja-2020k.pdf
- https://jyx.jyu.fi/bitstream/handle/123456789/58204/1/URN%3ANBN%3Afi%3Ajyu-201805292875.pdf
- https://stackoverflow.com/questions/2080050/how-do-we-determine-the-time-and-space-complexity-of-minmax