import os
from bs4 import BeautifulSoup

def izlusci_osnovne_podatke(mapa='.', od=None, do=None, top_n=40):
    pesmi, datumi = [], []
    if od is None or do is None:
        for ime in os.listdir(mapa):
            if ime.startswith('teden_') and ime.endswith('.html'):
                try:
                    datumi.append(int(ime[6:14]))
                except:
                    pass
        datumi.sort()
    else:
        datumi = list(range(od, do))

    for datum in datumi:
        pot = os.path.join(mapa, f'teden_{datum}.html')
        if not os.path.isfile(pot):
            continue
        with open(pot, encoding='utf-8', errors='ignore') as fh:
            soup = BeautifulSoup(fh.read(), 'html.parser')

        vrstice = []
        for it in soup.select('.chart-item'):
            pos = it.select_one('.position .chart-key strong')
            title = it.select_one('.chart-name')
            artist = it.select_one('.chart-artist')
            weeks = it.select_one('li.weeks span')
            peak = it.select_one('li.peak span')
            if not (pos and title and artist):
                continue
            try:
                poz = int(pos.get_text(strip=True))
            except:
                continue

            naslov = title.get_text(strip=True)
            if naslov.upper().startswith('NEW'):
                naslov = naslov[3:].strip()
            izvajalec = artist.get_text(strip=True)
            wtxt = weeks.get_text(strip=True) if weeks else ""
            ptxt = peak.get_text(strip=True) if peak else ""
            tedni = int(wtxt) if wtxt.isdigit() else None
            naj = int(ptxt) if ptxt.isdigit() else None

            vrstice.append((poz, naslov, izvajalec, datum, tedni, naj))

        vrstice.sort(key=lambda r: r[0])
        if isinstance(top_n, int) and top_n > 0:
            vrstice = vrstice[:top_n]

        pesmi.extend([(n, i, p, d, t, naj) for (p, n, i, d, t, naj) in vrstice])

    pesmi.sort(key=lambda t: (t[3], t[2]))
    return pesmi

def izlusci_dodatne_podatke(osnovni):
    pesmi_info = []
    for (naslov, izvajalec, pozicija, datum, tedni, najvisja) in osnovni:
        pesmi_info.append({
            'naslov': naslov,
            'izvajalec': izvajalec,
            'pozicija': pozicija,
            'datum': datum,
            'tedni_na_lestvici': tedni,
            'najvisja_pozicija': najvisja
        })
    return pesmi_info
