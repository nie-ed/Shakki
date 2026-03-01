#  Chess AI

This project contains a Chess AI, that uses the minimax-algorithim with alpha-beta pruning.

The project uses Python, Poetry, Robotframework, Pylint, Pytest, Coverage and autopep8.

The UI platform is provided by the school. The AI and movements of the pieces I have implemented myself.

The UI platform can be found here: https://algolabra-hy.github.io/aiplatform-en.

You can also play the game directly via terminal. Navigate to the root folder of the project and run 

```bash
poetry run python3 src/index.py
```
You can move a piece with for example "MOVE:e2e3". You need to write "PLAY:" for the AI to make the next move.

Unit tests can be done by:

```bash
poetry run pytest
```

Robotframework tests:

```bash
poetry run robot src/tests
```

Test coverage:

```bash
poetry run coverage run --branch -m pytest src; coverage html
```
**More detailed information of the project can be found in Finnish below:**

# Shakki

## Dokumentaatio
[Määrittelydokumentti](./dokumentaatio/määrittelydokumentti.md)

[Toteutusdokumentti](./dokumentaatio/toteutusdokumentti.md)

[Testausdokumentti](./dokumentaatio/testausdokumentti.md)

[Käyttöohje](./dokumentaatio/käyttöohje.md)


## Viikkoraportit
[Viikko 1](./dokumentaatio/viikkoraportit/viikkoraportti1.md)

[Viikko 2](./dokumentaatio/viikkoraportit/viikkoraportti2.md)

[Viikko 3](./dokumentaatio/viikkoraportit/viikkoraportti3.md)

[Viikko 4](./dokumentaatio/viikkoraportit/viikkoraportti4.md)

[Viikko 5](./dokumentaatio/viikkoraportit/viikkoraportti5.md)

[Viikko 6](./dokumentaatio/viikkoraportit/viikkoraportti6.md)

[Loppuraportti viikot 7 ja 8](./dokumentaatio/viikkoraportit/loppuraportti.md)
