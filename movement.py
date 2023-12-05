def definedTrajectoryMovement(objectToMove, newPositions):
    '''
    Déplace un objet donné à partir de la position attendue sur une fenêtre donnée. 
    :arg objectToMove, type:object, l'objet à déplacer
    :arg newPositions, type:list, liste composée des nouvelles valeurs x et y de l'objet 
    :returns list, retourne la modification des valeurs x et y de l'objet indiqué
    '''
    objectToMove.previousX = objectToMove.x
    objectToMove.previousY = objectToMove.y
    objectToMove.x = newPositions[0]
    objectToMove.y = newPositions[1]
    
def movementEquation(objectToMove, frameRate, wind):
    '''
    Calcule le mouvement à effectuer en fonction de sa position initiale, de sa vitesse initiale, et du temps qui se déroule entre deux frames du jeu. 
    :arg objectToMove, type:object, l'objet à déplacer
    :arg frameRate, type:int or float, entier définissant le nombre de secondes se déroulant entre deux frames du jeu
    :returns list, retourne la modification des valeurs x et y de l'objet indiqué à effectuer
    '''
    
    newPositionX = (objectToMove.accelerationX/2)*(frameRate**2)+objectToMove.speedX+objectToMove.x+wind
    newPositionY = (objectToMove.accelerationY/2)*(frameRate**2)+objectToMove.speedY+objectToMove.y
    objectToMove.speedX += objectToMove.accelerationX*frameRate
    objectToMove.speedY += objectToMove.accelerationY*frameRate
    return newPositionX, newPositionY