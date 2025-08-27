import re
import os

def izlusci_osnovne_podatke():
    vzorec_skladb = re.compile(
        r'<span class="position">(\d+)</span>.*?'
        r'<div class="title">.*?<a.*?>(.*?)</a>.*?'
        r'<div class="artist">.*?<a.*?>(.*?)</a>.*?'
        r'<span class="weeks-on-chart">(\d+)</span>.*?'
        r'<span class="movement (up|down|new|non-mover)">.*?(\d+|NEW).*?</span>',
        re.DOTALL # da '.' ujame tudi novo vrstico
    )

    vzorec_peak = re.compile(r'Peak.*?<span class="value">(\d+)</span>')
    vzorec_prodaja = re.compile(r'Sales.*?<span class="value">([\d,]+)</span>')

    skladbe = []
    for ime_datoteke in os.listdir("uk_charts"):
        if ime_datoteke.startswith("teden_") and ime_datoteke.endswith(".html"):
            datum = ime_datoteke[6:-5]
            
            with open(os.path.join("uk_charts", ime_datoteke), "r", encoding="utf-8") as dat:
                vsebina = dat.read()
                
                for ujemanje in vzorec_skladb.finditer(vsebina):
                    
                    peak_match = vzorec_peak.search(vsebina[ujemanje.start():ujemanje.end() + 1000])
                    peak_pozicija = peak_match.group(1) if peak_pozicija else ujemanje.group(1)
                    
                    prodaja_ujemanje = vzorec_prodaja.search(vsebina[ujemanje.start():ujemanje.end() + 1000])
                    prodaja = prodaja_ujemanje.group(1) if prodaja_ujemanje else "/"
                    
                    skladbe.append({
                        "datum": datum,
                        "pozicija": int(ujemanje.group(1)),
                        "naslov": ujemanje.group(2).strip(),
                        "izvajalec": ujemanje.group(3).strip(),
                        "tedni_na_lestvici": int(ujemanje.group(4)),
                        "gibanje": ujemanje.group(6),
                        "najvisja_pozicija": int(peak_pozicija),
                        "prodaja": prodaja
                    })
    
    return skladbe

def izlusci_dodatne_podatke(skladbe):
    skladbe_na_1 = {}
    for skladba in skladbe:
        kljuc = f"{skladba['naslov']}_{skladba['izvajalec']}"
        if skladba['pozicija'] == 1:
            if kljuc not in skladbe_na_1:
                skladbe_na_1[kljuc] = 0
            skladbe_na_1[kljuc] += 1
    
    for skladba in skladbe:
        kljuc = f"{skladba['naslov']}_{skladba['izvajalec']}"
        skladba['tedni_na_1'] = skladbe_na_1.get(kljuc, 0)
    
    return skladbe
