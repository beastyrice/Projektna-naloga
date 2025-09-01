import csv
import os

def shrani_skladbe(skladbe, pot="uk_top_40.csv"):
    mapa = os.path.dirname(pot)
    if mapa:
        os.makedirs(mapa, exist_ok=True)

    with open(pot, "w", newline="", encoding="utf-8") as dat:
        w = csv.writer(dat)
        w.writerow(["datum", "pozicija", "naslov", "izvajalec", "tedni_na_lestvici", "najvisja_pozicija"])
        for s in skladbe:
            w.writerow([
                s.get("datum"),
                s.get("pozicija"),
                s.get("naslov"),
                s.get("izvajalec"),
                s.get("tedni_na_lestvici"),
                s.get("najvisja_pozicija"),
            ])
