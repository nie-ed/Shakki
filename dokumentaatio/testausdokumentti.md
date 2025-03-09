# Testausdokumentti

## Kattavuusraportti

## Mitä on testattu

Projektissa on testattu pelinappuloiden liikkeiden oikeellisuus yksikkötesteillä unittest-kirjaston avulla. Yksikkötestit testaavat kansion *src/movement_of_pieces* tiedostoja. Lisäksi yksikkötestejä on koko flowlle alkaen minimax.py tiedostosta. Testit käsittelevät tiedostoja *board.py*, *get_legal_moves.py*, *is_king_threatened.py*, *minimax.py* ja *point_evaluation.py*. Tiedostot *index.py* sekä *moves.py* jätettiin pois testikattavuudesta, koska ne käsittelevät erityisesti käyttöliittymän kanssa kommunikointia ja minimax-algoritmin aloitusarvojen antoa, mikä tehtiin suoraan testeissä.

Lisäksi projektissa on robotframework testejä flowlle alkaen minimax.py tiedostosta. Nämä testit käsittelevät tiedostoja *board.py*, *get_legal_moves.py*, *is_king_threatened.py*, *minimax.py* ja *point_evaluation.py*.

## Testien syötteet

Useimpiin testeihin annettiin syötteenä erilaisia pelilaudan tilanteita. Nappuloiden siirron testeihin annettiin myös kyseisen nappulan rivi ja sarake. Nappuloiden liikkeiden tarkastukseen annettiin myös riippuen testistä esim. oliko max vai min pelaajan vuoro tai omien tai vastustajan nappuloiden aakkosmerkit.

Testeihin jotka käsittelivät sovelluksen toiminnan flowta pidemmälle annettiin syötteenä usein pelilaudan tilanne, Minimax olio, hakusyvyys, oliko min vai max pelaajan vuoro sekä alpha ja beta arvot. 

Pelilaudan perusteella tarkastettiin, tuleeko odotettu lista laillisia liikkeitä ulos, mitä mahdollisia liikkeitä kukin nappula voi tehdä, tuleeko True vai False kuninkaan uhan tarkastuksessa ja mitä arvoja saadaan ulos shakkimatti tilanteessa.

## Testien tulokset

On testattu, että nappuloiden bishop, knight, pawn, queen ja rook liike on toimivaa. Nappulalle king on saatu testikattavuus 94%, eli sen liike on testattu 94%. 

On testattu, että kuninkaan uhan arviointi toimii.

On testattu, että sovellus osaa karsia laittomat siirrot siirtojen listalta.

On testattu, että tekoäly osaa tehdä oikeat siirrot shakkimattiin, kun se on 1, 2, 3, ja 4 siirron päässä. On todettu, sttä siirrolle palautuu oikea arvo (-1000000 tai 1000000).


## Testien toisto

Yksikkötestit voidaan toistaa komentoriviltä syötteellä 

```bash
poetry run pytest
```

Robotframework testit voidaan toistaa komentiriviltä komennolla

```bash
poetry run robot src/tests
```

Testikattavuusraportin saat komennolla:

```bash
poetry run coverage run --branch -m pytest src; coverage html
```

## Coverage report

![Coverage report](../images/coverage_report.png)

## Viitteet
https://chesspuzzlesonline.com/chess-tactics/chess-puzzles-mate-in-4/