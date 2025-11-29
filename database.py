from ressources import *

def generateur_id_monde():
    try:
        iden = pandas.read_csv("data_base.csv")
        existing_ids = iden['id_monde']
    except Exception as e:
        messagebox.showerror("Erreur de base de données","Erreur lors de la connexion à la base de données lors de l'enregistrement du monde.")
        return
    
    random_id = random.randint(1000, 9999) #l'id ce sera 4 chiffres random 
    # Initialisation de la variable
    compteur = 0
    while random_id in existing_ids: # tant que l'id généré existe déjà dans la colonne id_monde on en génère un nouveau
        random_id = random.randint(1000, 9999)
        if compteur >= 1000:
            messagebox.showerror("Erreur de répétition","Biotop n'a pas réussi à générer votre monde.")
            break
        compteur += 1

    return random_id    

def exist_monde_name(monde_name):
    with open(nom_fichier_bdd, 'r') as fichier:
        reader = csv.DictReader(fichier)  # DictReader ça permet de traiter chaque ligne du csv comme un dico avec le header
        for row in reader:
            # "row["monde_name"]" ça permet d'avoir accès au data grâce au nom des headers
            if monde_name in row["monde_name"]:
                messagebox.showwarning("Erreur","Ce nom de monde est déjà utilisé, essayez en un autre.")
                # Je le met en True dès qu'il y a une "erreur" en gros
                return True
    return False

def creer_monde(monde_name, monde_date_last_connexion):
    id_monde = generateur_id_monde() # on utilise la fonction pour générer un id unique
    monde_date_creation = date_actuelle

    nb_limite_caractere = 60
    if len(monde_name) >= nb_limite_caractere:
        messagebox.showwarning("Erreur",f"Le nom du monde est trop long ! Il ne doit pas dépasser {nb_limite_caractere} caractères.")
        return
    if monde_name.lower() in li_mots_sensible:
        messagebox.showwarning("Erreur de sensibilité","Le nom du monde est jugé sensible par Biotope. Essayez un autre nom.")
        return
    
    verif_stop_fonction = exist_monde_name(monde_name)

    if verif_stop_fonction == True:
        return
    # ça c'est le truc pour écrire dans le csv, posez pas de questions
    write_data = pandas.DataFrame([{
        "id_monde": id_monde,
        "monde_name": monde_name,
        "monde_date_creation": monde_date_creation,
        "monde_date_last_connexion": monde_date_last_connexion
    }])
    write_data.to_csv(nom_fichier_bdd, mode='a', index=False, header=False)
    messagebox.showinfo(f"Création de {monde_name}",f"Le monde '{monde_name}' a été créé avec l'ID {id_monde}.")
    return

def creation_bdd(entetes):
    try:
        with open(nom_fichier_bdd, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=entetes)
            writer.writeheader()
        # J'ai enlevé "writer.writerows()" parce que il faut absolument un dico mais la une liste suffit

    # Je met "as e" c'est pour récupérer l'erreur mais je l'affiche pas parce que l'utilisateur s'en fou de savoir l'erreur exacte
    # si probleme lors du dev et qu'il faut l'erreur exacte alors : "print(f"Biotope n'arrive pas à créer la base de données, il faut accorder les permissions à Biotope ! {e}")"
    except PermissionError as e:
        messagebox.showerror("Erreur de permission","Biotope n'arrive pas à créer la base de données, il faut accorder les permissions à Biotope !")
        return
    except Exception as e:
        messagebox.showerror("Erreur","Une erreur inattendu s'est produite, veuillez réessayer !")
        return

