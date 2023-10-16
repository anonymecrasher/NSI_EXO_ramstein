# imprtation des module
import tkinter

# declaration des fonction

     

    
    

# declaration des class

class Soleil:
    def __init__(self, Canvas):
        Canvas.create_oval(50,50,150,150,fill = 'yellow', outline = 'yellow')
        
class Sol:
    def __init__(self, Canvas):
        Canvas.create_line(0,553,803,553,fill ='#A9A9A9',width = '100')
        
class Road:
    def __init__(self, Canvas):
        Canvas.create_line(50,553,150,553,fill ='white',width = '20')
        Canvas.create_line(250,553,350,553,fill ='white',width = '20')
        Canvas.create_line(450,553,550,553,fill ='white',width = '20')
        Canvas.create_line(650,553,750,553,fill ='white',width = '20')
        
class Oiseau:
    def __init__(self, Canvas, x, y):
        self.x = x
        self.y = y 
        self.Canvas = Canvas
        
        
    def draw(self):
        self.Canvas.create_line(50+x,453,70+x,433,fill ='black',width = '5')
        self.Canvas.create_line(50+x,453,30+x,433,fill ='black',width = '5')
        
class Main:
    def __init__(self):
        self.fenetre = tkinter.Tk()
        self.fenetre.title('Animation')
        self.zone_graphique = tkinter.Canvas(self.fenetre, width = 800, height = 600, bg = 'cyan')
        self.soleil = Soleil(self.zone_graphique)
        self.sol = Sol(self.zone_graphique)
        self.road = Road(self.zone_graphique)
        self.oiseau = Oiseau(self.zone_graphique,0)
        self.zone_graphique.pack()
        self.fenetre.mainloop()
        
        
    def animation():
        running = True
        while running == True:
             self.zone_graphique.delete('all')
             self.zone_graphique.update()
             time.sleep(0.1)
             x+=1
    
    
# fonction principal
def main():
    Maine = Main()
    Maine.animation()

# Programme principal
    
if __name__ == '__main__':
    main()