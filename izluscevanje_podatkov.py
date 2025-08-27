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
                    
                    sales_ujemanje = vzorec_prodaja.search(vsebina[ujemanje.start():ujemanje.end() + 1000])
                    prodaja = sales_ujemanje.group(1) if sales_ujemanje else "/"
                    
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
