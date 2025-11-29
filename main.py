from ressources import *
# Quand ce n'est pas un fichier ressource le mieux c'est d'indiquer ce qu'on veut
from database import creer_monde, creation_bdd

pg.init()

# J'ai mis le bouton dans une class au moins on peut tout le temps le réutilliser
class Button:
    def __init__(self, text, width, height, position, screen, entry1):
        # Initialisation des attributs
        self.pressed = False

        # Création du rectangle pour button
        self.top_rectangle = pg.Rect(position, (width, height))
        self.top_color = COLOR_ACCENT
        self.font = pg.font.Font(None, H3)
        self.text_surface = self.font.render(text, True, COLOR_TEXT_PRINCIPAL)
        # On doit créer un rectangle pour mettre du text dans un bouton
        self.text_rectangle = self.text_surface.get_rect(center=self.top_rectangle.center)
        self.entry1 = entry1

    def dessiner(self, screen):
        pg.draw.rect(screen, self.top_color, self.top_rectangle, border_radius=CORNER)
        screen.blit(self.text_surface, self.text_rectangle)
        self.check_click()

    def check_click(self):
        mouse_position = pg.mouse.get_pos()
        # En gros dès que que la position de la souris est sur le rectangle (qu'on a definie dans init) alors on execute qqch
        if self.top_rectangle.collidepoint(mouse_position):
            # Dès que la souris passe sur le bouton
            if pg.mouse.get_pressed():
                self.top_color = COLOR_ACCENT_HOVER
            # Dès que souris délivrent un clic
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    monde_name = self.entry1.get_text()
                    if monde_name and monde_name != self.entry1.placeholder:
                        creer_monde(monde_name, date_actuelle)
                    self.pressed = False
        else:
            self.top_color = COLOR_ACCENT

# Pour entry users c pygame_gui qui gère tout
class EntryUsers:
    def __init__(self, x, y, width, height, default_text=""):
        self.placeholder = default_text
        self.cleared = False       # Indique si le placeholder a été effacé
        self.had_focus = False     # Pour détecter perte de focus (en gros si t'es pas en train d'ecrire)
        self.text = ""
        self.text_input = pg_gui.elements.UITextEntryLine(
            relative_rect=pg.Rect((x, y), (width, height))
        )
        self.text_input.set_text(default_text)  # On affiche le placeholder au départ

    def get_text(self):
        return self.text_input.get_text()

    def handle_event(self, event):
        # Effacer le placeholder quand on clique dans la zone
        if event.type == pg.MOUSEBUTTONDOWN:
            # Il faut vérifier d'abord si self.text_input n'est pas à None
            # Le get_abs_rect() ça permet de recup la position du clique sur l'écran et pas la position dans le parent
            if self.text_input and self.text_input.get_abs_rect().collidepoint(event.pos):
                if not self.cleared:
                    self.text_input.set_text("")
                    self.cleared = True

        # Quand on valide la saisie (Enter ou clic ailleurs)
        if event.type == pg_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == self.text_input:
                txt = event.text.strip()

                # Si rien n'est écrit, on remet le placeholder
                if txt == "" or txt == self.placeholder:
                    self.text_input.set_text(self.placeholder)
                    self.cleared = False
                    self.text = ""
                else:
                    self.text = txt
                #creer_monde(monde_name, monde_date_last_connexion)

    # Vérifie le focus pour remettre le placeholder si la zone est vide
    def update(self, manager):
        has_focus = (manager.focused_set == {self.text_input})

        # Si on perd le focus et que le champ est vide, on remet le placeholder
        if self.had_focus and not has_focus:
            txt = self.text_input.get_text().strip()
            if txt == "" or txt == self.placeholder:
                self.text_input.set_text(self.placeholder)
                self.cleared = False
                self.text = ""

        # Mise à jour de l'état du focus
        self.had_focus = has_focus

class Game:
    def __init__(self):
        pg.init()
        self.screen_size = ((1050, 600))
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("Biotope")
        # C'est pour l'icône de l'app j'en ai fais une relativement simple mais au moins on a tt les droits d'auteur !
        icone_Biotope = pg.image.load("Asset/Logo Biotope.png")
        pg.display.set_icon(icone_Biotope)
        self.manager = pg_gui.UIManager(self.screen_size)

        # Texte Bienvenue
        self.font_txt_bienvenue = pg.font.Font(None, H1)
        self.txt_bienvenue = self.font_txt_bienvenue.render("Bienvenue sur Biotope", True, COLOR_TEXT_PRINCIPAL)
        self.text_bienvenue = self.txt_bienvenue.get_rect(topleft=(25, 25))

    # Cette fonction tourne en permanence pour que dès qu'on referme la fenetre soit "detruit" proprement l'app
    def run(self):
        running = True
        
        entry1 = EntryUsers(400, 200, WIDTH_BUTTON, HEIGHT_BUTTON, "Nom du monde")
        bouton1 = Button("Créer le monde", WIDTH_BUTTON, HEIGHT_BUTTON, (400, 275), self.screen, entry1)

        while running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    # ça permet que quand on fait un "control" "w" ça ferme la fenetre
                    if event.key == pg.K_w and event.mod & pg.KMOD_CTRL:
                        running = False
                        
                entry1.handle_event(event)
                self.manager.process_events(event)

            self.screen.fill(COLOR_BACKGROUND)

            self.manager.update(0)
            self.screen.blit(self.txt_bienvenue, self.text_bienvenue)
            # On dessine le champs Entry
            entry1.update(self.manager)  # c'est important ca, sinon le placeholder ne revient pas
            self.manager.draw_ui(self.screen)
            bouton1.dessiner(self.screen)

            pg.display.flip() # C pour rafraîchir l'écran

# ⬇️ ça permet que le code commence ici 
if __name__ == "__main__":
    creation_bdd(entetes_colonne_bdd)
    game = Game()
    game.run()
