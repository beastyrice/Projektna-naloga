import izluscevanje_podatkov
import shranjevanje_podatkov
import pridobivanje_spletne_strani
import sys
from datetime import datetime, timedelta

do_datuma = datetime.now()
od_datuma = do_datuma - timedelta(days=5*365)

mapa = "uk_charts" if len(sys.argv) < 2 else sys.argv[1]
try:
    TOP_N = int(sys.argv[2]) if len(sys.argv) >= 3 else 40
except:
    TOP_N = 40

pridobivanje_spletne_strani.shrani_tedenske_htmlje(od_datuma, do_datuma, mapa)

osnovni = izluscevanje_podatkov.izlusci_osnovne_podatke(mapa, top_n=TOP_N)
skladbe = izluscevanje_podatkov.izlusci_dodatne_podatke(osnovni)

shranjevanje_podatkov.shrani_skladbe(skladbe, "uk_top_40.csv")
