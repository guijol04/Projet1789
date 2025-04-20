Project de visulalisation de l'élection des États-Généraux de 1789  
Dans le cadre du cours HST2007-A-H25  
https://hst2007joly.weebly.com/  

Les Données sont pour la réalisation de projections avec Flourish Studio

Le code assume que tout les fichiers sont dans le même folder, donc les folders doivent être retirés pour que le Python marche; les folders sont pour organiser les fichiers après-coup.

Explication du code/des fichiers:  
- Linkgetter : Scraper la liste des députés à scraper
    - linkgetter.py : Code
    - liste1789.txt : Output
- Scraper : Scraper les députés dans liste1789.txt et mettre leurs infos en csv
    - scraper.py : Code, input liste1789.txt
    - 1789.csv: Output
    - 1789tweak.csv: Modification manuelle de 1789.csv; Sont corrigés les erreurs que j'ai repéré (voir casspeciaux.txt)
- Uncapitalize : Change le nom des bailliages/location titled
    - uncapitalize.py : Code, input noms.txt
    - noms.txt : liste des locations, vient des shapefiles (geojson)
    - nomstitled.txt : Output
- Ordres : Obtient le nombre de députés par état par bailliage
    - bailliages_ordres.py : Code , input nomstitled.txt et 1789tweaks.csv
    - Nbparetats.csv : Output
- Rename : Rennomme les locations de députés pour être équivalents à celles de la carte
    - Rename.py : Code , input nomstitled.txt et 1789tweaks.csv
    - new1789.csv : Output
- casspeciaux.txt : Recense des anomalies dans les données lors du travail
- fini100m3.geojson : Regionfiles; vient de https://doi.org/10.7910/DVN/T8UXHK et traité/combiné/simplifié avec QGIS