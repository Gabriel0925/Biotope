import pygame as pg # Il faut faire un pip install
import csv
import ctypes
import pygame_gui as pg_gui # Il faut faire un pip install
from datetime import date
import pandas

# Couleur de Biotop (je met en majuscule pour la lisibilité)
COLOR_ACCENT = "#355E3B"
COLOR_ACCENT_HOVER = "#447B4C"

COLOR_BACKGROUND = "#101010"
COLOR_BACKGROUND_CARD = "#252525"
COLOR_BACKGROUND_CARD_HOVER = "#2F2F2F"

COLOR_TEXT_PRINCIPAL = "#E0E0E0"
COLOR_TEXT_SECONDAIRE = "#A0A0A0"

# Caractéristiques composants
CORNER = 20
WIDTH_BUTTON = 250
HEIGHT_BUTTON = 50

date_actuelle = date.today()

# J'ai rajouté "monde_date_creation" pour le moment ou le monde a été crée
entetes_colonne_bdd = ['id_monde','monde_name','monde_date_creation','monde_date_last_connexion']