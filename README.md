Project de visulalisation de l'élection des États-Généraux de 1789  
Dans le cadre du cours HST2007-A-H25  
https://hst2007joly.weebly.com/  

Les Données sont pour la réalisation de projections avec Flourish Studio


Sources/Documentation:
- Principales
    - Les regionfiles proviennent des bailliages de https://doi.org/10.7910/DVN/T8UXHK. Ceux-ci ont étés modifiés par la suite manuellement.
    - Les informations des députés proviennent de https://www2.assemblee-nationale.fr/sycomore/recherche. Cette source prend ses informations du Dictionnaire des parlementaires français (1789-1889) d'Adolphe Robert, publié en 1889-1891 https://gallica.bnf.fr/ark:/12148/bpt6k837081. 

- Supplémentaires
    - La liste wikipedia des députés de 1789, https://fr.wikipedia.org/wiki/Liste_des_d%C3%A9put%C3%A9s_aux_%C3%89tats_g%C3%A9n%C3%A9raux_de_1789, citant les Archives parlementaires https://gallica.bnf.fr/ark:/12148/bpt6k49516q, fut très utile quand est venu le temps de modifier les bailliages avec QGIS et de standardiser les données entre les députés et les regionfiles.



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

Le code assume que tout les fichiers sont dans le même dossier, donc les dossierss doivent être retirés pour que le code Python fonctionne; les dossiers sont pour organiser et catégoriser les étapes après-coup.