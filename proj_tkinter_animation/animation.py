# imprtation des module
import tkinter
import time

# declaration des fonction
def animation(zone_graphique,oiseau,sol,soleil,road,voiture):
        running = True
        while running == True:
            zone_graphique.delete('all')
            oiseau.update_pos()
            oiseau.draw()
            sol.draw()
            road.draw()
            soleil.draw()
            voiture.draw()
            zone_graphique.update()
            time.sleep(0.01)

# declaration des class

class Soleil:
    def __init__(self, Canvas):
        self.Canvas = Canvas
        
    def draw(self):
        self.Canvas.create_oval(50,50,150,150,fill = 'yellow', outline = 'yellow')
    
        
class Sol:
    def __init__(self, Canvas):
        self.Canvas = Canvas
        
    def draw(self):
        self.Canvas.create_line(0,553,803,553,fill ='#A9A9A9',width = '100')
        
class Road:
    def __init__(self, Canvas):
        self.Canvas = Canvas
        
    def draw(self):
        self.Canvas.create_line(50,553,150,553,fill ='white',width = '20')
        self.Canvas.create_line(250,553,350,553,fill ='white',width = '20')
        self.Canvas.create_line(450,553,550,553,fill ='white',width = '20')
        self.Canvas.create_line(650,553,750,553,fill ='white',width = '20')
        
class Oiseau:
    def __init__(self, Canvas, x, y):
        self.x = x
        self.y = y 
        self.Canvas = Canvas
        self.up = True
        self.gofor = True
        
        
    def draw(self):
        self.Canvas.create_line(50+self.x,453,70+self.x,453-self.y,fill ='black',width = '5')
        self.Canvas.create_line(50+self.x,453,30+self.x,453-self.y,fill ='black',width = '5')
        
    def update_pos(self):
        
        if self.x + 70 < 800 and self.gofor == True:
            self.x += 5
        elif self.x + 50 > 50 and self.gofor == False:
            self.x -= 5
        if self.x == 0:
            self.gofor = True
        elif self.x == 800 - 70:
            self.gofor = False
            
            
        if self.y < 20 and self.up == True:
            self.y += 2
            
        elif self.y > 0 and self.up == False:
            self.y -= 2
        if self.y == 0:
            self.up = True
        elif self.y == 20:
            self.up = False
class Voiture:
    def __init__(self, x, y ,Canvas):
        self.x = x
        self.y = y
        self.Canvas = Canvas
    def draw(self):
        self.Canvas.create_rectangle(self.x,self.y,self.x+150,self.y+40,fill= 'red', outline = 'red')
        self.Canvas.create_rectangle(self.x+30,self.y,self.x+120,self.y-30,fill= 'red', outline = 'red')
        self.Canvas.create_oval(self.x+15,self.y+20,self.x+55,self.y+60,fill = 'yellow', outline = 'yellow')
        self.Canvas.create_oval(self.x+95,self.y+20,self.x+145,self.y+60,fill = 'yellow', outline = 'yellow')
    def touche(self, event):
        touche = event.keycode
        if touche == 39:
            self.x += 10
        elif touche == 37:
            self.x -= 10
        elif touche == 38:
            keypressed = 'up'
        elif touche == 40:
            keypressed = 'down'
        
        
        

        
        
    
    
    
# fonction principal
def main():
    fenetre = tkinter.Tk()
    fenetre.title('Animation')
    zone_graphique = tkinter.Canvas(fenetre, width = 800, height = 600, bg = 'cyan')
    zone_graphique.pack()
    soleil = Soleil(zone_graphique)
    sol = Sol(zone_graphique)
    road = Road(zone_graphique)
    oiseau = Oiseau(zone_graphique,0,0)
    voiture = Voiture(50,500,zone_graphique)
    zone_graphique.focus_set()
    zone_graphique.bind('<Key>', voiture.touche)
    
    animation(zone_graphique,oiseau,sol,soleil,road,voiture)
    fenetre.mainloop()

# Programme principal
    
if __name__ == '__main__':
    main()
