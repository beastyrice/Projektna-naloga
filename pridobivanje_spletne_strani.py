import requests
import os
import time # moral dodati, ker me je strežnik blokiral....
import random # enako
from datetime import datetime, timedelta # enako

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def shrani_tedenske_htmlje(od_datuma, do_datuma, mapa="uk_charts"):
    os.makedirs("uk_charts", exist_ok=True) # da samodejno naredi mapo
    
    trenutni_datum = od_datuma
    delta = timedelta(weeks=1)
    
    while trenutni_datum <= do_datuma:
        datum_str = trenutni_datum.strftime("%Y%m%d")
        url = f"https://www.officialcharts.com/charts/singles-chart/{datum_str}/"
        
        try:
            odgovor = requests.get(url, headers=headers)
            odgovor.raise_for_status()
            
            with open(os.path.join("uk_charts", f"teden_{datum_str}.html"), "w", encoding="utf-8") as dat:
                dat.write(odgovor.text)
            
            print(f"Shranjeno za {datum_str}") # dodal, ker nisem vedel ali sploh kaj dela ali je zamrznilo
            time.sleep(random.uniform(0.5, 1)) # da spletna stran ne zazna "bot activity"
            
        except Exception as e:
            print(f"Napaka pri {datum_str}: {str(e)}") # da vem če kje ni delalo
        
        trenutni_datum += delta