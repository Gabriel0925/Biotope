from ressources import *

def generateur_id_monde():
    pass

def save_monde(monde_name, monde_date_last_connexion):
    id_monde = 1
    monde_date_creation = date_actuelle

    iden = pandas.read_csv("data_base.csv")
    pass

save_monde("monde_name", "monde_date_last_connexion")

def creation_bdd(entetes):
    try:
        with open('data_base.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=entetes)
            writer.writeheader()
        # J'ai enlevé "writer.writerows()" parce que il faut absolument un dico mais la une liste suffit

    # Je met "as e" c'est pour récupérer l'erreur mais je l'affiche pas parce que l'utilisateur s'en fou de savoir l'erreur exacte
    # si probleme lors du dev et qu'il faut l'erreur exacte alors : "print(f"Biotop n'arrive pas à créer la base de données, il faut accorder les permissions à Biotop ! {e}")"
    except PermissionError as e:
        print("Biotop n'arrive pas à créer la base de données, il faut accorder les permissions à Biotop !")
        return
    except Exception as e:
        print("Une erreur inattendu s'est produite, veuillez réessayer !")
        return
