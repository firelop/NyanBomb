def definedTrajectoryMovement(objectToMove, futurePosition):
    '''
    Déplace un objet donné à partir de la position attendue sur une fenêtre donnée. 
    :arg objectToMove, type:object, l'objet à déplacer
    :arg futurePosition, type:list, liste composée des valeurs x et y de la position attendue de l'objet à l'issu de la fonction 
    :returns list, retourne la modification des valeurs x et y de l'objet indiqué
    '''
    objectToMove.x = futurePosition[0]
    objectToMove.y = futurePosition[1]