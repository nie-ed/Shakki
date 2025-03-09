# Käyttöohje

## Asennus ja käynnistys

### Tekoälyalustan käyttöönotto

Sovellus on suunniteltu käytettäväksi tekoälyalustan kanssa. 
Tarkemmat ohjeet tekoälyalustan lataamisesta ja käyttöönotosta löydät osoitteesta [text](https://algolabra-hy.github.io/aiplatform-fi). Alla lyhyt kuvaus tekoäyalustan käyttöönotosta.

Lataa tekoälyalustan releasen zip tiedosto osoitteesta [text](https://github.com/game-ai-platform-team/tira-ai-local/releases).

Kloonaa tämä Shakki repositorio koneellesi. Koneellesi pitää olla asennettuna poetry, jotta seuraavat askeleet onnistuvat. Asenna riippuvuudet kloonatun repositorion juurihakemistossa komennolla.

```bash
poetry install
```
Pura aiemmin lataamasi tekoälyalustan zip tiedosto ja siirry purettuun kansioon terminaalissa. Käynnistä tekoälyalusta komennolla "./tira-ai-local".

Tekoälyalusta käynnistyy ikkunaan, jonka ylä vasemmassa on nappi "Chess". Klikkaa sitä. Raahaa shakkirepositorion kansio tai klikkaa tekstiä "Click or Drag & Drop Folder Here" ja etsi kyseinen kansio. Klikkaa "Submit". Pelisi pitäisi alkaa.

### Terminaalin käyttö

Peliä voi myös pelata suoraan terminaalista. Navigoi sovelluksen juurihakemistoon ja anna komento:

```bash
poetry run python3 src/index.py
```

Pelin käynnistyessä tulostuu terminaaliin pelin alkutilan lauta. Olet laudalla isot kirjaimet ja tekoäly on pienet. Voit tehdä siirron laudalla komennolla "MOVE:xxxx", esim. "MOVE:e2e3". Jotta tekoäly tekee seuraavan siirron, pitää terminaalissa kirjoittaa "PLAY:".

## Testit

Yksikkötestit voidaan toistaa komentoriviltä syötteellä 

```bash
poetry run pytest".
```

Robotframework testit voidaan toistaa komentiriviltä komennolla

```bash
poetry run robot src/tests
```

Testikattavuusraportin saat komennolla:

```bash
poetry run coverage run --branch -m pytest src; coverage html
```

## Pelin pelaaminen

Tekoälyalustalla voit pelata peliä siirrellen valkoisia nappuloita. Tekoäly on mustat nappulat. Peli alkaa aina sinun vuorolla. 

Suoraan terminaalin kautta pelatessa, olet nappulat merkittynä isoilla kirjaimilla ja tekoäly on nappulat merkittynä pienimmä kirjaimilla.

Voit tehdä siirron laudalla komennolla "MOVE:xxxx", jossa ensimmäiset kaksi "xx" merkkiä sisältäää sarakkeen kirjaimen ja rivin numeron jolla nappula jota haluat siirtää on sijoitettuna laudalla esim. e2. Toisen "xx" sisältävät sarakkeen kirjaimen ja rivin numeron jolle kohtaa haluat siirtää kyseisen nappulan esim. e3. Rivien numerot ovat 1-8 ja sarakkeiden kirjaimet ovat a-h. Eli esim. "MOVE:e2e3" alkutilanteessa:
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]

siirtää nappulaa niin, että lauta näyttää seuraavalta:
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", "P", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]

Jotta tekoäly oman siirtosi jälkeen tekee seuraavan siirron, pitää terminaalissa kirjoittaa "PLAY:".