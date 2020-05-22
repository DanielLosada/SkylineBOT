import matplotlib.pyplot as plt
import random as rand

def takeFirst(elem):
    return elem[0]

def edificiDins(edi1, edi2):
    if edi1[0] >= edi2[0] and edi1[1] <= edi2[1] and edi1[2] <= edi2[2]:#vol dir que edi1 és contingut d'edi2
        return 1 
    elif edi1[0] <= edi2[0] and edi1[1] >= edi2[1] and edi1[2] >= edi2[2]:#edi2 contingut a edi1
        return 2
    else:
        return 3 # no estan continguts




class Skyline:
    nom = "1"
    plots = []

    def __init__(self,plot):
        self.plots = plot


    def eliminaPlotsSenseVolum(self):
        length = len(self.plots)
        x = 0
        while x < length:
            if self.plots[x][0] == self.plots[x][2] or self.plots[x][1] == 0:
                self.plots.remove(self.plots[x])
                length = length - 1
                x = x-1
            x = x+1

    def reordena(self,elem,index):
        insertat = False
        length = len(self.plots)
        while not insertat:
            if index == length:
                insertat = True
                self.plots.insert(index,elem)
            elif self.plots[index][0]>=elem[0]:
                insertat = True
                self.plots.insert(index,elem)
            index = index +1

#per a que funcioni els edificis han d'estar ordenats en ordre creixent de posicio inicial
    def plotsNoSolapats(self):
        self.eliminaPlotsSenseVolum()
        length = len(self.plots)
        x = 0
        while x < length-1:
            if(self.plots[x][0]>=self.plots[x][2]):
                self.plots.remove(self.plots[x])
                length = length-1
                x = x-2
                if x < -1:
                    x = -1
            else:
                aux=edificiDins(self.plots[x],self.plots[x+1])
                if aux == 1 or aux == 2:
                    if aux == 1:
                        self.plots.remove(self.plots[x])
                        x = x - 2
                        if x < -1:
                            x = -1
                    else:
                        self.plots.remove(self.plots[x+1])
                        x = x-1
                    length = length -1
                    
                elif self.plots[x][2] > self.plots[x+1][0]:#edificis solapats
                    if self.plots[x][1] <= self.plots[x+1][1]:#puede provocar min>max asi que hay que eliminarlo
                        self.plots[x] = list(self.plots[x])
                        self.plots[x][2] = self.plots[x+1][0]
                        self.plots[x] = tuple(self.plots[x])
                        if(self.plots[x][0]>=self.plots[x][2]):
                            self.plots.remove(self.plots[x])
                            length = length-1
                            x = x-2
                            if x < -1:
                                x = -1
                    else:#como mueve la posucion inicial puede provocar que dejen de estar ordenados
                        self.plots[x+1]= list(self.plots[x+1])
                        self.plots[x+1][0] = self.plots[x][2]
                        self.plots[x+1] = tuple(self.plots[x+1])
                        if self.plots[x][0] > self.plots[x+1][0]:
                            aux = self.plots[x]
                            self.plots.remove(aux)
                            self.reordena(aux, x)
                    
                if x < length-1 and self.plots[x][1] == self.plots[x+1][1]:#en cas de que dos edifici tinguin la mateixa alçada despres de dessolaparlos es fusionen
                    edificiFusionat = (self.plots[x][0],self.plots[x][1],self.plots[x+1][2])
                    self.plots.remove(self.plots[x+1])
                    self.plots.remove(self.plots[x])
                    self.plots.insert(x,edificiFusionat)
                    length = length-1
                    x = x-1
            x = x + 1
                        

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
        for _ in range(n):
            min = rand.randint(xmin,xmax)
            max = xmax
            if(min + w <= xmax):
                max = rand.randint(min+1, min + w)
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


#sky = Skyline([])
#sky.creacioEdificiAleatori({"n": 10, "h": 20, "w": 3, "xmin": 1, "xmax": 10})

#sky = Skyline([(1,13,2),(1,6,4),(1,8,3)])


#sky.eliminaPlotsSenseVolum()
#sky.plotsNoSolapats()