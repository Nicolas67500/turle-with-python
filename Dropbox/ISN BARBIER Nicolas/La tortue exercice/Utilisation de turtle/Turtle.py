from turtle import*

# Pour gagner deux lignes
def departxy(x_depart,y_depart):
    up()
    goto(x_depart,y_depart)
    down()


def carre(c,x_depart,y_depart):

    def cote(c):
        forward(c)
        left(90)

    departxy(x_depart,y_depart)

    for k in range(4):
        cote(c)
    up()

    exitonclick()

def polygone_regulier(c,longueur,x_depart,y_depart):

    def nbcote(c,longueur):
        forward(longueur)
        left(360/c)

    departxy(x_depart,y_depart)

    for k in range(c):
        nbcote(c,longueur)



# Un escargot avec n'importe quel polygone :)
def escargot(c,x_depart,y_depart):

    speed(40)

    color("magenta","purple")
    begin_fill()

    for i in range(40,120):
        polygone_regulier(c,i,x_depart,y_depart)
        right(10)

    end_fill()

    exitonclick()


def etoile(b,longueur,x_depart,y_depart):
    color("black","yellow")
    begin_fill()

    def branche(longueur):
        forward(longueur)
        right(144)

    departxy(x_depart,y_depart)

    for k in range(b):
        branche(longueur)

    end_fill()

    exitonclick()


def etoile_geante(b,longueur,x_depart,y_depart):
    color("green","yellow")
    begin_fill()

    def branche(longueur):
        forward(longueur)
        right(144)

    departxy(x_depart,y_depart)

    for k in range(b):
        branche(longueur)
        longueur += 20
    end_fill()

    exitonclick()


def polygone_geant(b,c,longueur,x_depart,y_depart):
    color("blue","red")
    begin_fill()
    speed(5)
    for i in range(b):
        polygone_regulier(c, longueur, x_depart, y_depart)
        longueur += 10
    end_fill()
    exitonclick()



def pissenlitrainbow(r,nbcercle,x_depart,y_depart):
    speed(20)

    couleurs = ["grey", "blue", "red", "green", "magenta", "cyan", "yellow", "white"]

    # Sous-fonction
    def cercle(r,nbcercle):
        circle(r)
        left(360 / nbcercle)

    departxy(x_depart,y_depart)

    for couleur in couleurs:
        color(couleur)
        for k in range(nbcercle):
             cercle(r,nbcercle)

    exitonclick()

pissenlitrainbow(100,2,0,0)
def hexagone_multicolore():
    couleurs = [ "blue", "red", "green", "magenta", "cyan", "yellow"]
    bgcolor("black")

    speed(50)

    for k in range(200):
        color(couleurs[k%6]) # Division euclidienne pour avoir une "boucle" dans la liste.
        forward(k)
        left(60)

    exitonclick()

def donutmulticolore(b,x_depart,y_depart):
    # cyan  / rouge sang / vert pomme / magenta / bleu / jaune
    couleurs = ["#10EEE7", "#CB0303", "#77D711", "#863499", "#0EB3CF", "#EFF008"] # code couleur hexadécimale
    bgcolor("black")

    def cercle_multicolore():
        circle(600, 30)
        left(127)


    departxy(x_depart,y_depart)

    for k in range(b):
        color(couleurs[k%6])
        cercle_multicolore()

    exitonclick()

