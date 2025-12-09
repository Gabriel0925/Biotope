import pygame as pg # Il faut faire un pip install
import sys #pour fermer proprement les fenêtres
import sqlite3
import time
import ctypes
import pygame_gui as pg_gui # Il faut faire un pip install
from datetime import date
import pandas # Il faut faire un pip install (parce que moi je l'avais pas)
from tkinter import messagebox # il faut faire un pip install

# Couleur de Biotope (je met en majuscule pour la lisibilité)
COLOR_MAIN_ACCENT = "#355E3B"

COLOR_BACKGROUND = "#000000"
COLOR_BACKGROUND_CARD = "#232323"
COLOR_BACKGROUND_CARD_HOVER = "#353535"

MAIN_COLOR_TEXT = "#E0E0E0"
COLOR_TEXT_SECONDAIRE = "#7B7B7B"
COLOR_MAIN_HOVER = "#0DE52A"

#couleur a trouver :
BACK_COLOR = "red"
BACK_HOVER_COLOR = "#650F0F"
COLOR_BACK_ACCENT = "#BD8320"

# Taille et Police
H1 = 50
H2 = 38
H3 = 30
P = 26
P_SMALL = 24 

# Caractéristiques composants
CORNER = 20
WIDTH_MAIN_BUTTON = 250
HEIGHT_MAIN_BUTTON = 50
WIDTH_HEIGHT_SETTING_BUTTON = 50

date_actuelle = date.today()

# Lors de la création du monde
li_mots_sensible = [
    # Insultes et propos haineux
    "connard", "pute", "salaud", "enfoiré", "bâtard", "merde", "nique", "fils de pute",
    "enculé", "trou du cul", "abrutis", "débile", "imbécile", "crétin", "idiot", "nul",
    "chienne", "ta gueule", "ferme ta gueule", "va te faire foutre", "dégage", "casse-toi",
    "racaille", "sous-merde", "pourriture", "ordure", "minable", "lâche", "fumier",

    # Contenu sexuel/explicite
    "sexe", "baise", "nique ta mère", "branlette", "fellation", "cunnilingus", "porno",
    "éjaculation", "orgasme", "pénis", "vagin", "cul", "anale", "violation", "pédophile",
    "prostitution", "putain", "salope", "chatte", "bite", "couilles", "érotique", "hardcore",

    # Violence et extrémisme
    "meurtre", "tuer", "assassinat", "terroriste", "bombe", "attentat", "guerre", "viol",
    "suicide", "massacre", "génocide", "nazisme", "hitler", "kkk", "daech", "islamiste",
    "extrémiste", "radical", "arme", "fusillade", "sang", "mort", "torture", "lynchage",

    # Drogues et substances illicites
    "drogue", "cocaine", "héroïne", "cannabis", "weed", "shit", "mdma", "ecstasy", "lsd",
    "amphetamine", "meth", "overdose", "dealer", "toxicomane", "shoot", "sniffer", "fumer",

    # Discrimination
    "nègre", "bougnoule", "juif", "arab", "noir", "blanc", "asiatique", "pédé", "gouine",
    "trans", "handicapé", "retardé", "feminazi", "islam", "christianisme", "raciste", "xénophobe",
    "homophobe", "antisémite", "supremaciste","hitler","nazi"

    # Piratage et triche
    "hack", "pirate", "cheat", "triche", "exploit", "virus", "malware", "phishing", "ddos",
    "backdoor", "rootkit", "crack", "warez", "torrent", "leak", "vol", "fraude",

    # Souffrance animale/environnementale
    "tuer des animaux", "chasse", "braconnage", "abattage", "pollution", "déforestation",
    "espèce en voie de disparition", "cruauté animale", "expérimentation animale",
    "viande", "fourrure", "peau", "ivoire", "corne de rhinocéros",

    # Autres termes inappropriés
    "spam", "arnaque", "escroquerie", "fake", "deepfake", "propagande", "désinformation",
    "complot", "illuminati", "reptilien", "qanon", "vaccin", "covid", "5g", "nouvel ordre mondial","caca","pipi"
]