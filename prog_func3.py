## Importation des modules
import turtle


## Définition des fonctions
def forme(position, n):
    '''
    Dessine une forme géométrique en fonction du paramètre n
    @param entrée position : (int, int), position de la forme sous la forme (absisse, ordonnée)
    @param entrée n : int, numéro de la forme, nombre de côtés si n>=3
    '''
    turtle.penup()
    turtle.goto(position[0], position[1])
    turtle.pendown()

    if n == 1:
        turtle.circle(50)
    elif n == 2:
        for i in range(5):
            turtle.forward(50)
            turtle.left(180 - 180 / 5)
    elif n >= 3:
        for i in range(n):
            turtle.forward(50)
            turtle.left(360 / n)


## Programme principal

# configuration de la tortue
turtle.speed(0)
turtle.pensize(2)

# exécution du dessin
forme((0, 0), 7)

# fin du dessin
turtle.done()
