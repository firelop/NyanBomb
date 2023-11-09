def definedTrajectoryMovement(objectToMove, movement):
    '''
    Déplace un objet donné à partir de la position attendue sur une fenêtre donnée. 
    :arg objectToMove, type:object, l'objet à déplacer
    :arg movement, type:list, liste composée des mouvements x et y que l'objet effectue à l'issu de la fonction 
    :returns list, retourne la modification des valeurs x et y de l'objet indiqué
    '''
    objectToMove.x += movement[0]
    objectToMove.y += movement[1]