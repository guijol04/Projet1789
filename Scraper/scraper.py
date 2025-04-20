import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

OUTPUT_PATH = "1789.csv"
NB = 20
NOTNEWFILE = False

if os.path.isfile(OUTPUT_PATH):
    output = pd.read_csv(OUTPUT_PATH)
    NOTNEWFILE = True
else:
    output = pd.DataFrame()
liste = []
file = open("liste1789.txt", "r")
for line in file:
    liste.append(line.strip().replace("/sycomore/fiche/(num_dept)/", ""))
file.close()

start = time.time()

for nb, i in enumerate(liste):
    if NOTNEWFILE:
        if int(i) in output.id.values:
            print(f"Skipping {i}")
            continue
    
    
    url = "https://www2.assemblee-nationale.fr/sycomore/fiche/(num_dept)/"
    

    #Empecher erreur Timeout 504
    essai = 0 
    max_essai = 3
    wait = 10
    while tries < max_essai:
        try:
            page = urllib.request.urlopen(f"{url}{i}")
            break
        except urllib.error.URLError:
            tries += 1 
            print(f"{essai}/{max_essai} Reessai dans {wait}s")
            time.sleep(wait) 
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    donnees = dict()
    
    donnees["id"] = i
    

    #Ruban
    donnees["nom"] = soup.h1.string.strip()
    if soup.find('p', class_="deputy-healine-sub-title") != None:
        donnees["annees"] = soup.find('p', class_="deputy-healine-sub-title").string.strip()
    infos_generales = soup.find("dl", class_="sycomore-infos-generales").find("dd").find("ul").find_all("li")
    if infos_generales[0].string != None:
        donnees["naissance"] = infos_generales[0].string.strip().replace("\t", "").replace("\r", "").replace("\n", "")
    if len(infos_generales) > 1:
        donnees["deces"]= infos_generales[1].string.strip().replace("\t", "").replace("\r", "").replace("\n", "")


    #Bio
    articles = soup.find_all("article")
    for article in articles[2:]:
        if article.find(id="bio") != None:
            if article.h3 != None:
                donnees["notice_bio"] = article.h3.string.strip()
            else:
                donnees["notice_bio"] = article.a.string.strip()
            donnees["bio"]= article.p.get_text().strip().replace("\t", "").replace("\n","\\n").replace("\r","\\r")


    #Postes
    presidence_count = 0
    mandat_count = 0
    postes = articles[1].find_all("dl")
    for poste in postes:
        infos = poste.find_all("dd")
        titres =poste.find_all("dt")
        if "Présidence" in titres[0].string:
            for presidences in titres:
                donnees[f"presidencetitre{presidence_count}"] = titres[presidence_count].string.strip()
                donnees[f"presidenceannees{presidence_count}"] = infos[presidence_count].string.strip()
                presidence_count += 1
        elif infos[1].a.string == None:
            pass
        else:
            donnees[f"regime{mandat_count}"] = infos[0].string.strip()
            donnees[f"legislature{mandat_count}"] = infos[1].a.string.strip()
            if infos[2].b != None:
                donnees[f"mandat{mandat_count}"] = infos[2].b.string.strip()
            else:
                donnees[f"mandat{mandat_count}"] = infos[2].get_text().strip()
            if len(infos) > 3:
                donnees[f"location{mandat_count}"] = infos[3].string.strip()
            if len(infos) > 4:
                donnees[f"groupe{mandat_count}"] = infos[4].string.strip()
            mandat_count += 1

    df = pd.DataFrame([donnees])

    #df.to_csv(OUTPUT_PATH, mode="a",index=False)
    output = pd.concat([output, df])

    time_step = time.time()
    print(f"{donnees["id"]} fait - {nb+1}/{len(liste)} en {round(time_step - start, 2)}s")

    output.to_csv(OUTPUT_PATH, mode="w",index=False)

    
    
    
    

