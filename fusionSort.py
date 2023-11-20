
def getDistance(particles, turret):
    towerX = turret.x
    towerY = turret.y
    particleX = [particle.x for particle in particles]
    particleY = [particle.y for particle in particles]
    distances = None
    return distances

def triFusion(particles, turret):
    distances = getDistance(particles, turret)
    


def fusion(tableau, left, right):
    pass

'''
Exemple : 
tri_fusion (tableau) :
    Si la longueur est > 1:
      # séparer
      milieu = longueur // 2
      gauche = tableau [0 ... milieu - 1]
      droite = tableau [milieu ... fin]

      # diviser
      tri_fusion(gauche)
      tri_fusion(droite)

      # combiner
      fusion(tableau, gauche, droi


fusion (tableau, gauche, droite)
    i, j, k = 0
    tant que i < longueur de gauche et j < longueur de droite
        Si gauche[i] < droite[j] alors
            tableau[k] = gauche[i] et i = i + 1
        Sinon
            tableau[k] = droite[j] et j = j + 1
        k = k + 1

    Pour les éléments restant, les ajouter à fin de tableau    
'''
