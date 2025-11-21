from ressources import *

# la liste des data c mieux de le mettre dans ressources au moins on y a accès partout

def creation_bdd(entetes):
    try:
        with open('biotope.csv', 'w') as f:
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
    
