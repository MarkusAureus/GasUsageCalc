# GasUsage Calculator

Jednoduchá desktopová aplikácia na výpočet spotreby plynu, ktorá konvertuje metre kubické (m³) na kilowatthodiny (kWh) a následne vypočíta cenu v eurách.

![GasUsage Calculator Screenshot](/images/background.png)

## Funkcie

- Prevod z metrov kubických (m³) na kilowatthodiny (kWh)
- Výpočet ceny v eurách na základe aktuálnej sadzby
- Prehľadné užívateľské rozhranie
- Možnosť vymazať zadané hodnoty

## Technické špecifikácie

- Jazyk: Python 3.x
- GUI Framework: Tkinter
- Konverzný faktor: 40 * 1.02264 / 3.6
- Sadzba za kWh: 0.0292 €

## Inštalácia

1. Uistite sa, že máte nainštalovaný Python 3.x
2. Stiahnite všetky súbory z repozitára
3. Vytvorte priečinok `images` a umiestnite do neho súbor `background.png`

## Spustenie aplikácie

```bash
python gas_calculator.py
```

## Použitie

1. Zadajte hodnotu spotreby v metroch kubických (m³)
2. Kliknite na tlačidlo "Result" pre výpočet
3. Aplikácia zobrazí:
   - Prepočítanú hodnotu v kWh
   - Cenu v eurách
4. Pomocou tlačidla "Clear" môžete vymazať všetky hodnoty

## Štruktúra projektu

```
GasUsage-Calculator/
├── gas_calculator.py
├── README.md
├── README_SK.md
├── images/
│   └── background.png
└── LICENSE
│   
└── thumbnail.jpg
```

## Autor

Marek Kožuch

## Licencia

Tento projekt je open-source softvér distribuovaný pod MIT licenciou. To znamená, že:
- Môžete softvér voľne používať, upravovať a distribuovať
- Softvér je dostupný zdarma
- Jediná požiadavka je zachovanie informácie o autorských právach a licencie

## Poznámky k vývoju

- Aplikácia je určená výhradne pre PC (stolné počítače a notebooky)
- Aplikácia používa fixnú veľkosť okna (602x400 pixelov)
- Používateľské rozhranie je optimalizované pre čitateľnosť s použitím fontov Roboto a Helvetica
- Implementované validácie vstupov pre bezpečné používanie
