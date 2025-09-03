import pandas as pd
import matplotlib.pyplot as plt

def top_n_izvajalci(df, n = 10):
    vc = df['izvajalec'].value_counts().head(n)
    return vc.rename_axis('izvajalec').reset_index(name='stevilo_pojavitev')

def top_pesmi_po_tednih(df, n = 20):
    izhod = df.sort_values('tedni_na_lestvici', ascending=False)
    vrstice = ['datum','pozicija','naslov','izvajalec','tedni_na_lestvici','najvisja_pozicija']
    return izhod[vrstice].drop_duplicates(subset=['naslov','izvajalec'], keep='first').head(n)

def top_pesmi_po_najvisji(df, n = 20):
    izhod = df.sort_values('najvisja_pozicija', ascending=True)
    vrstice = ['datum','pozicija','naslov','izvajalec','tedni_na_lestvici','najvisja_pozicija']
    return izhod[vrstice].drop_duplicates(subset=['naslov','izvajalec'], keep='first').head(n)

def pesmi_izvajalca(df, izvajalec: str):
    d = df[df['izvajalec'].str.contains(izvajalec, case=False, na=False)]
    if d.empty:
        return pd.DataFrame()
    return (d.groupby('naslov', as_index=False)
              .agg(pojavitve=('pozicija','count'),
                   povp_poz=('pozicija','mean'),
                   najvisja=('najvisja_pozicija','min'),
                   max_tedni=('tedni_na_lestvici','max'))
              .sort_values(['najvisja','povp_poz','pojavitve']))

def najvecji_skoki(df, datum):
    trenutni = df[df['datum'] == pd.to_datetime(datum)].copy()
    prejsnji = df[df['datum'] == (pd.to_datetime(datum) - pd.Timedelta(days=7))].copy()
    m = pd.merge(trenutni, prejsnji, on=['naslov','izvajalec'], suffixes=('_cur','_prev'))
    m['sprememba'] = m['pozicija_prev'] - m['pozicija_cur']
    narascujoci = m.sort_values('sprememba', ascending=False).head(10)[['naslov','izvajalec','pozicija_prev','pozicija_cur','sprememba']]
    padajoci = m.sort_values('sprememba', ascending=True).head(10)[['naslov','izvajalec','pozicija_prev','pozicija_cur','sprememba']]
    return narascujoci, padajoci

def trajektorija_pesmi(df, title_substr: str):
    vrstice = df[df['naslov'].str.contains(title_substr, case=False, na=False)].copy()
    if vrstice.empty:
        print('Ni zadetkov.')
        return
    vrstice = vrstice.sort_values('datum')
    plt.figure(figsize=(9,4))
    plt.plot(vrstice['datum'], vrstice['pozicija'])
    plt.gca().invert_yaxis()
    plt.title(f'Trajektorija: {title_substr}')
    plt.xlabel('Datum')
    plt.ylabel('Pozicija (nižja je boljša)')
    plt.tight_layout()
    plt.show()
