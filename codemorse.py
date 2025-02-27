dico =  {'A': '.-', 'B': '-...', 'C': '-.-.',
 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I': '..',
 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---',
 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..',
 '0': '-----', '1': '.----', '2': '..---',
 '3': '...--', '4': '....-', '5': '.....',
 '6': '-....', '7': '--...', '8': '---..',
 '9': '----.'
 }


class Noeud:
    def __init__(self, etiquette, gauche = None, droit = None):
        """Construit un noeud ayant deux enfants : gauche et droit."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

    def estFeuille(self):
        return self.gauche == None and self.droit == None


def encode(mot, dico):
    """Encode un/des mots en code morse"""
    morse = ''
    for lettre in mot:
        if lettre == ' ':
            morse += '   '
        else:
            for car, code in dico.items():
                if car == lettre.upper():
                    morse += code + ' '
    print(morse)

def construire_arbre_binaire(dico):
    """Construit un arbre binaire à partir du dictionnaire du code morse"""
    racine = Noeud(None)
    for car, code in dico.items():
        courant = racine
        for symbole in code:
            if symbole == '.':
                if courant.gauche == None:
                    courant.gauche = Noeud(None)
                courant = courant.gauche
            else:
                if courant.droit == None:
                    courant.droit = Noeud(None)
                courant = courant.droit        
        courant.etiquette = car
    return racine
 
def decode(mot, dico):
    """Décode le/les mots écrits en code morse"""
    mot_decode = ''
    racine = construire_arbre_binaire(dico)
    courant = racine
    compteur = 0
    n = len(mot)
    for i in mot:
        compteur += 1
        if i == '.':
            courant = courant.gauche
        elif i == '-':
            courant = courant.droit
        elif i == ' ' and courant.etiquette == None:
            mot_decode += ' '
        elif i == ' ':
            mot_decode += courant.etiquette
            courant = racine

        if compteur == n:
            mot_decode += courant.etiquette
        
    print(mot_decode)


encode("Hello world", dico)
decode('.... . .-.. .-.. ---   .-- --- .-. .-.. -..', dico)
