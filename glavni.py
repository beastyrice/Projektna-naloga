from datetime import datetime, timedelta
import pridobivanje_spletne_strani 
import izluscevanje_podatkov
import shranjevanje_podatkov
import sys

# za zadnjih 5 let
zacetek = datetime.now() - timedelta(days=5 * 365)
konec = datetime.now()

shranjevanje_podatkov.shrani_tedenske_htmlje(zacetek, konec)
skladbe = izluscevanje_podatkov.izlusci_osnovne_podatke()
skladbe = izluscevanje_podatkov.izlusci_dodatne_podatke(skladbe)

shranjevanje_podatkov.shrani_skladbe(skladbe)
shranjevanje_podatkov.shrani_izvajalce(skladbe)
shranjevanje_podatkov.shrani_najuspesnejse(skladbe)