import matplotlib.pyplot as plt

class Skyline:
    nom = "1"
    a = [(1,2,2), (2,4,6)]

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
        
    def calculPosReflex(self,min,max,pos):
        llargada = max-min
        puntMitg = min + (llargada/2)
        distPMitgMax = puntMitg - min
        if pos < puntMitg: 
            distPMitg = puntMitg - pos
            ret = pos + distPMitg*2
            return ret
        elif pos > puntMitg:
            distPMitg = pos - puntMitg
            ret = pos - distPMitg*2
            return ret
        else:
            return pos

    


    def reflectit(self):
        min, max = [self.a[0][0], self.a[-1][-1]]
        ret = []
        for x in self.a:
            print("x[0]: ", x[0])
            print("x[1]: ", x[1])
            print("x[2]: ", x[2])
            aux = (self.calculPosReflex(min,max,x[2]),x[1],self.calculPosReflex(min,max,x[0]))
            ret = ret + [aux]            
        print("ret: ", ret)
        self.a = ret

    def introduce_self(self):
        print("My name is " + self.nom)