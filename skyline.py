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

    def unio(self, a):
        height = [x[1] for x in self.a] + [x[1] for x in a]
        width = [x[2]-x[0] for x in self.a] + [x[2]-x[0] for x in a]
        pos = [((x[2]-x[0])/2)+x[0] for x in self.a] + [((x[2]-x[0])/2)+x[0] for x in a]
        plt.bar(pos,height,width=width)
        plt.show()
        
        '''
        height1 = [x[1] for x in self.a]
        height2 = [x[1] for x in a]
        height = height1 + height2
        width1 = [x[2]-x[0] for x in self.a]
        width2 = [x[2]-x[0] for x in a]
        width = width1 + width2
        pos1 = [((x[2]-x[0])/2)+x[0] for x in self.a]
        pos2 = [((x[2]-x[0])/2)+x[0] for x in a]
        pos = pos1 + pos2
        plt.bar(pos,height,width=width)
        plt.show()
        '''

    def introduce_self(self):
        print("My name is " + self.nom)