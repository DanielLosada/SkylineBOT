import matplotlib.pyplot as plt

class Skyline:
    nom = "1"
    a = [(1,2,3), (3,4,6)]

    def generarFigura(self):
        
        height = [x[1] for x in self.a]
        width = [x[2]-x[0] for x in self.a]
        pos = [((x[2]-x[0])/2)+x[0] for x in self.a]
        plt.bar(pos,height,width=width) 
        plt.savefig("Skyline_" + self.nom)
        #plt.show()

    def introduce_self(self):
        print("My name is " + self.nom)