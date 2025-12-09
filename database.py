from ressources import *

try:
    con = sqlite3.connect("data_base.db")
    curseur = con.cursor()
except sqlite3.Error as e:
    messagebox.showerror("Erreur", "Erreur de base de données lors de la connexion à la base de données !")
except Exception as e:
    messagebox.showerror("Erreur", "Une erreur inattendu s'est produite, réessaye !")  

def creer_monde(monde_name, monde_date_last_connexion):
    monde_date_creation = date_actuelle

    nb_limite_caractere = 60
    if len(monde_name) >= nb_limite_caractere:
        messagebox.showwarning("Erreur",f"Le nom du monde est trop long ! Il ne doit pas dépasser {nb_limite_caractere} caractères.")
        return False
    if monde_name.lower() in li_mots_sensible:
        messagebox.showwarning("Erreur de sensibilité","Le nom du monde est jugé sensible par Biotope. Essayez un autre nom.")
        return False
    try:
        curseur.execute(f"INSERT INTO Caract_monde (monde_name, monde_date_creation, monde_date_last_connexion) VALUES (?, ?, ?)", (monde_name, monde_date_creation, monde_date_last_connexion))
        con.commit()
        messagebox.showinfo(f"Création de {monde_name}",f"Le monde '{monde_name}' vient d'être créé.")
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Erreur de base de donnée", f"Une erreur est survenue lors de la création du monde.{e}")
        return False
    except Exception:
        messagebox.showerror("Erreur","Une erreur inattendu s'est produite, veuillez réessayer !")
        return False

def creation_bdd():
    try:
        # Identifiant du monde
        curseur.execute("CREATE TABLE IF NOT EXISTS Caract_monde (" \
                "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                "monde_name TEXT UNIQUE NOT NULL," \
                "monde_date_creation TEXT NOT NULL, " \
                "monde_date_last_connexion TEXT NOT NULL)")
    except sqlite3.Error as e:
        messagebox.showerror("Erreur de base de données","Une erreur est survenue lors de la création de la base de données.")
        return
    except Exception as e:
        messagebox.showerror("Erreur","Une erreur inattendu s'est produite, veuillez réessayer !")
        return

