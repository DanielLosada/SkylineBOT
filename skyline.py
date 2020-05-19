import matplotlib.pyplot as plt
import random as rand

def takeFirst(elem):
    return elem[0]


class Skyline:
    nom = "1"
    plots = [(1,2,3), (3,4,6)]

   

    def ordenaPlots(self):
        self.plots.sort(key=takeFirst)
        
    def creacioEdificiSimple(self,plot): #plot -> (xmin,alçada,xmax)
        self.plots = [plot]
    
    def creacioEdificiCompostos(self, plots): #plots -> [(xmin,alçada,xmax),(xmin,alçada,xmax),...]
        self.plots = plots
        self.ordenaPlots()
        
    def creacioEdificiAleatori(self,plot): #plot -> {n,h,w,xmin,xmax} n = nombre edificis, h = alçada aleatoria entre 0 i h, w = amblada aleatoria entre 1 i w, xmin i xmax -> posicions inici entre xmin i xmax
        n = plot['n']
        h = plot['h']
        w = plot['w']
        xmin = plot['xmin']
        xmax = plot['xmax']
        res = []
        for x in range(0,n):
            min = rand.randint(xmin,xmax)
            max = xmax
            if(min + w <= xmax):
                max = rand.randint(min, min + w)
            res = res + [(min,rand.randint(0,h),max)]
        self.plots = res
        self.ordenaPlots()



    def generarFigura(self):
        
        height = [x[1] for x in self.plots]
        width = [x[2]-x[0] for x in self.plots]
        pos = [((x[2]-x[0])/2)+x[0] for x in self.plots]
        plt.clf()
        plt.bar(pos,height,width=width) 
        plt.savefig("Skyline_" + self.nom)
        #plt.show()

    def unio(self, a):
        height = [x[1] for x in self.plots] + [x[1] for x in a]
        width = [x[2]-x[0] for x in self.plots] + [x[2]-x[0] for x in a]
        pos = [((x[2]-x[0])/2)+x[0] for x in self.plots] + [((x[2]-x[0])/2)+x[0] for x in a]
        plt.bar(pos,height,width=width)
        plt.show()
        
        '''
        height1 = [x[1] for x in self.plots]
        height2 = [x[1] for x in a]
        height = height1 + height2
        width1 = [x[2]-x[0] for x in self.plots]
        width2 = [x[2]-x[0] for x in a]
        width = width1 + width2
        pos1 = [((x[2]-x[0])/2)+x[0] for x in self.plots]
        pos2 = [((x[2]-x[0])/2)+x[0] for x in a]
        pos = pos1 + pos2
        plt.bar(pos,height,width=width)
        plt.show()
        '''
        
    def calculPosReflex(self,min,max,pos):
        llargada = max-min
        puntMitg = min + (llargada/2)
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
        min, max = [self.plots[0][0], self.plots[-1][-1]]
        ret = []
        for x in self.plots:
            ret = ret + [(self.calculPosReflex(min,max,x[2]),x[1],self.calculPosReflex(min,max,x[0]))]            
        self.plots = ret
        self.ordenaPlots()

    def multiplicaSkyline(self, num):
        amplada = self.plots[-1][-1] - self.plots[0][0]
        ret = []
        for x in range(1,num):
            for y in self.plots:
                ret = ret + [(y[0]+(amplada*x), y[1],y[2]+(amplada*x))]
        self.plots = self.plots + ret
        
    
    def desplacamentEdificisDreta(self, num):
        self.plots = list(map(lambda elem: (elem[0]+num,elem[1], elem[2]+num), self.plots))

    def desplacamentEdificisEsquerra(self, num):
        self.plots = list(map(lambda elem: (elem[0]-num,elem[1], elem[2]-num), self.plots))