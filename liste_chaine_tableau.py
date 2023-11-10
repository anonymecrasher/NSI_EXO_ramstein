t1 = [3,None]
t2 = [6,[7,None]]
t2[1][0] = 1
t1[1] = t2

print(t1)
print(id(t2))
print(id(t1))

t2[1][1] = [5, None]
t2[1][1][1] = [11, None]
print(t2)
print(id(t1[1][1][1][1]))
print(t1)

t3 = [1,[2,[3,[4, None]]]]

class Maillon():
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant
        
m1 = Maillon(5)
m2 = Maillon(7)
print(id(m2))
print(hex(id(m2)))
print(bin(id(m2)))

print(id(m1))
print(hex(id(m1)))
print(bin(id(m1)))

m2.valeur = 9
print(m2.valeur)
m3 = Maillon(2)
m4 = Maillon(11)

l1 = m1
l1.suivant = m2
print(l1.valeur,l1.suivant.valeur)
l1.suivant.suivant = m3
l1.suivant.suivant.suivant = m4
l2 = Maillon(1,Maillon(2,Maillon(3,Maillon(4))))
print(l2.valeur,l2.suivant.valeur)
print(l2.suivant.suivant.suivant.valeur)
print(l2)
