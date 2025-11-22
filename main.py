from ressources import *
from database import *

pg.init()

# J'ai mis le bouton dans une class au moins on peut tout le temps le réutilliser
class Button:
    def __init__(self, text, width, height, position, screen):
        # Initialisation des attributs
        self.pressed = False

        # Création du rectangle pour button
        self.top_rectangle = pg.Rect(position, (width, height))
        self.top_color = COLOR_ACCENT
        self.font = pg.font.Font(None, 30)
        self.text_surface = self.font.render(text, True, COLOR_TEXT_PRINCIPAL)
        # On doit créer un rectangle pour mettre du text dans un bouton
        self.text_rectangle = self.text_surface.get_rect(center=self.top_rectangle.center)

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
                    print("Tu viens de cliquer")
                    self.pressed = False
        else:
            self.top_color = COLOR_ACCENT

# Pour entry users c pygame_gui qui gère tout
class EntryUsers:
    def __init__(self, x, y, width, height, default_text=""):
        self.text_input = pg_gui.elements.UITextEntryLine(relative_rect=pg.Rect((x, y), (width, height)))
        self.text_input.set_text(default_text)
        self.text = default_text

    def get_text(self):
        return self.text_input.get_text()

    def handle_event(self, event):
        # pygame_gui permet de gèrer auto. le clic et la saisi
        if event.type == pg_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == self.text_input:
                self.text = event.text
                print(f"Tu viens d'écrire : {self.text}") 

class Game:
    def __init__(self):
        pg.init()
        self.screen_size = ((1050, 600))
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("Biotope")
        # C'est pour l'icône de l'app j'en ai fais une relativement simple mais au moins on a tt les droits d'auteur !
        icone_Biotop = pg.image.load("Asset/Logo_Biotop.png")
        pg.display.set_icon(icone_Biotop)
        self.manager = pg_gui.UIManager(self.screen_size)

    # Cette fonction tourne en permanence pour que dès qu'on referme la fenetre soit "detruit" proprement l'app
    def run(self):
        running = True
        
        entry1 = EntryUsers(400, 200, WIDTH_BUTTON, HEIGHT_BUTTON, "Veuillez entrer qqch")
        bouton1 = Button("Créer le monde", WIDTH_BUTTON, HEIGHT_BUTTON, (400, 275), self.screen)

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
            # On dessine le champs Entry
            self.manager.draw_ui(self.screen)
            bouton1.dessiner(self.screen)

            pg.display.flip() # C pour rafraîchir l'écran

# ⬇️ ça permet que le code commence ici 
if __name__ == "__main__":
    creation_bdd(entetes_colonne_bdd)
    game = Game()
    game.run()
