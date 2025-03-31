Project de visulalisation de l'élection des États-Généraux de 1789
Dans le cadre du cours HST2007-A-H25
https://hst2007joly.weebly.com/


Explication du code:
linkgetter.py crée une liste de lien à scraper, output liste1789.txt
scraper.py input liste1789.txt, lit la liste de pages a scraper, scrape le html et convertit l'information en csv, output 1789.csv
1789.csv est l'output de scraper.py
1789tweak.csv contient des modifations manuelles à 1789.csv
casspeciaux.txt liste manuellement des pages webs anormales (ce qui est édité dans 1789tweak.csv)
baillages.geojson contient les shapefiles pour Flourish Studio