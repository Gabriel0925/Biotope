import csv

entetes = ['id_monde','monde_name','monde_date','last_connexion_date']

data = [
        {'id_monde':'','monde_name':'','monde_date':'','last_connexion_date':''},
        {'id_monde':'','monde_name':'','monde_date':'','last_connexion_date':''},
        {'id_monde':'','monde_name':'','monde_date':'','last_connexion_date':''},
    ]

def fichier_csv(entetes, data):
    with open('biotope.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=entetes)
        writer.writeheader()
        writer.writerows(data)

fichier_csv(entetes, data)