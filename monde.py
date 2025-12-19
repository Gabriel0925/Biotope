from ressources import *

# Ce fichier servira à créer la map et la gérer

class Terrain:
    def __init__(self, map_filenames, size_spriteX=64, size_spriteY=64, nb_spritesX=18, nb_spritesY=12):
        """
        Constructeur de la classe Terrain.
        :param map_filenames: Liste des noms de fichiers des maps à charger.
        :param size_spriteX: Largeur d'une tuile (en pixels).
        :param size_spriteY: Hauteur d'une tuile (en pixels).
        :param nb_spritesX: Nombre de tuiles en largeur.
        :param nb_spritesY: Nombre de tuiles en hauteur.
        """

        pg.init()
        self.screen = pg.display.set_mode((nb_spritesX * size_spriteX, nb_spritesY * size_spriteY))
        pg.display.set_caption("Terrain Pygame")

        # Chemins et tailles
        self.path_media = 'Asset/map/'
        self.size_spriteX = size_spriteX
        self.size_spriteY = size_spriteY
        self.nb_spritesX = nb_spritesX
        self.nb_spritesY = nb_spritesY
        self.nb_pixelsX = nb_spritesX * size_spriteX
        self.nb_pixelsY = nb_spritesY * size_spriteY

        # Dictionnaire des tuiles (codes -> noms de fichiers)
        self.sprites = {
            '  ': None,
            '00': 'Grece.png',  # Exemple de tuile
            '01': 'USA.png',
            '02': 'allemagne.png'
            # Ajoutez ici d'autres tuiles selon vos besoins
        }

        # Dictionnaire des tuiles (codes -> images PIL)
        self.sprites_pil = {
            key: Image.open(self.path_media + self.sprites[key]).convert('RGBA')
            for key in self.sprites.keys()
            if key != '  '
        }
        self.sprites_pil['  '] = None

        # Construction du background
        matrix_map_pil = self.lire_map(self.path_media+map_filenames[0])

        # Fusion des maps supplémentaires
        for map_filename in map_filenames[1:]:
            matrix_map_add_pil = self.lire_map(map_filename)
            for y in range(self.nb_spritesY):
                for x in range(self.nb_spritesX):
                    if matrix_map_add_pil[y][x] is not None:
                        matrix_map_pil[y][x] = Image.alpha_composite(
                            matrix_map_pil[y][x],
                            matrix_map_add_pil[y][x]
                        )

        # Création de l'image finale
        background_pil = Image.new('RGBA', (self.nb_pixelsX, self.nb_pixelsY), 0)
        for y in range(self.nb_spritesY):
            for x in range(self.nb_spritesX):
                background_pil.paste(
                    matrix_map_pil[y][x],
                    (x * self.size_spriteX, y * self.size_spriteY)
                )

        # Conversion pour Pygame
        self.background_img = pg.image.fromstring(
            background_pil.tobytes(),
            background_pil.size,
            'RGBA'
        )

    def lire_map(self, map_file_name):
        """
        Lit un fichier de map et retourne une matrice d'images PIL.
        :param map_file_name: Nom du fichier de map à lire.
        :return: Matrice d'images PIL.
        """
        matrix_map = []
        with open(map_file_name, 'r') as f:
            for line in f:
                if line[0] == 'M':
                    codes = line.split('|')
                    matrix_map.append(
                        [c for c in codes if c != '\n' and c[0] != 'M']
                    )

        # Conversion des codes en images PIL
        matrix_map_pil = [
            [
                self.sprites_pil[matrix_map[y][x]]
                for x in range(self.nb_spritesX)
            ]
            for y in range(self.nb_spritesY)
        ]

        return matrix_map_pil

    def dessine(self):
        """
        Dessine le background sur l'écran.
        """
        self.screen.blit(self.background_img, (0, 0))
