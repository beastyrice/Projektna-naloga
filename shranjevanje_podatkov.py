import csv

def shrani_skladbe(skladbe):
    leta = {}
    for skladba in skladbe:
        leto = skladba['datum'][:4]  
        if leto not in leta:
            leta[leto] = []
        leta[leto].append(skladba)

    with open("uk_top_40.csv", "w", newline="", encoding="utf-8") as dat:
        writer = csv.writer(dat)
        writer.writerow([
            "datum", "pozicija", "naslov", "izvajalec", 
            "tedni_na_lestvici", "gibanje", "najvisja_pozicija",
            "tedni_na_1", "prodaja"
        ])
        
        for skladba in skladbe:
            writer.writerow([
                skladba["datum"],
                skladba["pozicija"],
                skladba["naslov"],
                skladba["izvajalec"],
                skladba["tedni_na_lestvici"],
                skladba["gibanze"],
                skladba["najvisja_pozicija"],
                skladba["tedni_na_1"],
                skladba["prodaja"]
            ])

def shrani_izvajalce(skladbe):
    izvajalci = set()
    for skladba in skladbe:
        izvajalci.add((skladba["izvajalec"],))
    
    with open("uk_izvajalci.csv", "w", newline="", encoding="utf-8") as dat:
        writer = csv.writer(dat)
        writer.writerow(["izvajalec"])
        writer.writerows(izvajalci)

def shrani_najuspesnejse(skladbe):
    uspesnost = {}
    for skladba in skladbe:
        kljuc = (skladba["naslov"], skladba["izvajalec"])
        if kljuc not in uspesnost:
            uspesnost[kljuc] = {
                "tedni_na_1": skladba["tedni_na_1"],
                "najvisja_pozicija": skladba["najvisja_pozicija"],
                "skupni_tedni": 0
            }
        uspesnost[kljuc]["skupni_tedni"] += 1
    
    with open("uk_najuspesnejse.csv", "w", newline="", encoding="utf-8") as dat:
        writer = csv.writer(dat)
        writer.writerow(["naslov", "izvajalec", "tedni_na_1", "najvisja_pozicija", "skupni_tedni"])
        
        for (naslov, izvajalec), podatki in uspesnost.items():
            writer.writerow([naslov, izvajalec, podatki["tedni_na_1"], 
                           podatki["najvisja_pozicija"], podatki["skupni_tedni"]])