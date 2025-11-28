from ressources import *

def generateur_id_monde():  #l'id ce sera 4 chiffres random 
    random_id = random.randint(1000, 9999)
    iden = pandas.read_csv("data_base.csv")
    existing_ids = iden['id_monde']
    while random_id in existing_ids: # tant que l'id généré existe déjà dans la colonne id_monde on en génère un nouveau
        random_id = random.randint(1000, 9999)
    return random_id    

def creer_monde(monde_name, monde_date_last_connexion):
    id_monde = generateur_id_monde() # on utilise la fonction pour générer un id unique
    monde_date_creation = date_actuelle

    # ça c'est le truc pour écrire dans le csv, posez pas de questions
    write_data = pandas.DataFrame([{
        "id_monde": id_monde,
        "monde_name": monde_name,
        "monde_date_creation": monde_date_creation,
        "monde_date_last_connexion": monde_date_last_connexion
    }])
    write_data.to_csv("data_base.csv", mode='a', index=False, header=False)
    print(f"Le monde '{monde_name}' a été créé avec l'ID {id_monde}.")



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

