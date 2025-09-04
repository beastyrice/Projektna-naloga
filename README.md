# <p align="center">ANALIZA Official Singles Chart UK Top 40</p>

V svoji projektni nalogi za predmet **Uvod v programiranje** sem se odločil analizirati podatke iz [Official Singles Chart UK Top 40](https://www.officialcharts.com/charts/singles-chart/).  
Podatke sem pridobil s spletne strani, jih pretvoril v csv datoteko in nato analiziral z uporabo Pythona in Jupyter Notebooka.

## NAVODILA
Če želite sami pridobiti podatke iz interneta in jih pretvoriti v csv datoteko, poženite `glavni.py`.  
S tem se:
- prenesejo html datoteke tedenskih lestvic v mapo `uk_charts`,  
- iz njih izluščijo podatki o pesmih in izvajalcih,  
- shrani vse skupaj v datoteko `uk_top_40.csv`.

Analiza podatkov je dostopna v datoteki `analiza-uk-top40.ipynb`.

## PRIDOBIVANJE PODATKOV
- V datoteki `pridobivanje_spletne_strani.py` je funkcija, ki prenese html datoteke lestvic.  
- V datoteki `izluscevanje_podatkov.py` so funkcije, ki iz html datotek izluščijo podatke o naslovu pesmi, izvajalcu, poziciji, številu tednov na lestvici in najvišji poziciji.  
- V datoteki `shranjevanje_podatkov.py` se podatki zapišejo v csv datoteko.  
- Vse funkcije se poženejo prek `glavni.py`.

## ANALIZA
V datoteki `analiza-uk-top40.ipynb` so prikazani različni pregledi in vizualizacije:
- **Top izvajalci** glede na število pojavitev,  
- **Pesmi z največ tedni** na lestvici,  
- **Pesmi z najboljšo najvišjo pozicijo**,  
- **Pesmi za izbranega izvajalca**,  
- **Največji tedenski skoki in padci**,  
- **Trajektorije izbranih pesmi skozi čas**,  
- **Porazdelitev trajanja pesmi na lestvici** (pie chart).

Nekatere funkcije, uporabljene pri analizi, so shranjene v datoteki `analiza_funkcije.py`, da je v notebooku manj kode in bolj čista struktura.

## UGOTOVITVE
Analiza pokaže:
- kateri izvajalci so se v zadnjih 5 letih največkrat pojavili na lestvici,  
- katere pesmi so se na lestvici obdržale najdlje,  
- kakšni so tipični vzorci trajanja pesmi na lestvici (večina se zadrži le nekaj tednov, redke pa več deset tednov),  
- primerjave med posameznimi tedni razkrijejo največje skoke in padce v pozicijah.  

Projekt tako lepo pokaže priljubljenosti pesmi in omogoča hiter in enostaven vpogled v glasbene trende v Združenem kraljestvu v zadnjih 5 letih.
