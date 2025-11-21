from ressources import *
from database import *

class Game:
    def __init__(self):
        self.screen_size = ((1050, 600))
        self.screen = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE)
        pygame.display.set_caption("Biotope")
        # C'est pour l'icône de l'app j'en ai fais une relativement simple mais au moins on a tt les droits d'auteur !
        icone_Biotop = pygame.image.load("Asset/Logo_Biotop.png")
        pygame.display.set_icon(icone_Biotop)

    # Cette fonction tourne en permanence pour que dès qu'on referme la fenetre soit "detruit" proprement l'app
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # ça permet que quand on fait un "control" "w" ça ferme la fenetre
                    if event.key == pygame.K_w and event.mod & pygame.KMOD_CTRL:
                        running = False

# ⬇️ ça permet que le code commence ici 
if __name__ == "__main__":
    creation_bdd(entetes_colonne_bdd)
    game = Game()
    game.run()
