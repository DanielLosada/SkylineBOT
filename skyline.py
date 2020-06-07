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

def esSolapen(edi1,edi2):
    if (edi1[0] <= edi2[0] and edi1[2] >= edi2[0]) or (edi2[0] <= edi1[0] and edi2[2] >= edi1[0]):
        return True
    else:
        return False
    



class Skyline:
    nom = "1"
    plots = []
    area = 0

    def __init__(self,plot):
        self.plots = plot
        self.calculaAreaSkyline()


    def eliminaPlotsSenseVolum(self):
        length = len(self.plots)
        x = 0
        while x < length:
            if self.plots[x][0] == self.plots[x][2] or self.plots[x][1] == 0:
                self.plots.remove(self.plots[x])
                length = length - 1
                x = x-1
            x = x+1

    def calculaAreaSkyline(self):
        ret = 0
        for x in self.plots:
            amplada = x[2] - x[0]
            area = amplada * x[1]
            ret = ret + area
        self.area = ret


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
                    
                if x < length-1 and self.plots[x][1] == self.plots[x+1][1] and self.plots[x][2] == self.plots[x+1][0]:#en cas de que dos edifici tinguin la mateixa alçada despres de dessolaparlos es fusionen
                    edificiFusionat = (self.plots[x][0],self.plots[x][1],self.plots[x+1][2])
                    self.plots.remove(self.plots[x+1])
                    self.plots.remove(self.plots[x])
                    self.plots.insert(x,edificiFusionat)
                    length = length-1
                    x = x-1
            x = x + 1
                        

    def interseccio(self,sky2): #es pasa com a parametre la llista d'edificis
        x = 0
        y = 0
        length1 = len(self.plots)
        length2 = len(sky2)
        res = []
        while x < length1 and y < length2:
            if self.plots[x][0] < sky2[y][0]:#si l'edifici de més a l'esquerra és del primer skyline
                primer = self.plots[x]
                if sky2[y][0] >= primer[0] and sky2[y][0] < primer[2]: #estan solapats
                    edificiAfegir = (sky2[y][0],min(sky2[y][1],primer[1]),min(sky2[y][2],primer[2]))
                    res = res + [edificiAfegir]
                    auxx = x
                    if y+1 >= length2 or (not esSolapen(primer, sky2[y+1])):#si no es solapa amb el seguent 
                        x = x+1
                    if auxx+1 >= length1 or (not esSolapen(self.plots[auxx+1],sky2[y])):
                        y = y+1
                else:
                    x = x+1
            else:
                primer = sky2[y]
                if self.plots[x][0] >= primer[0] and self.plots[x][0] < primer[2]: #estan solapats
                    edificiAfegir = (self.plots[x][0],min(self.plots[x][1],primer[1]),min(self.plots[x][2],primer[2]))
                    res = res + [edificiAfegir]
                    auxy = y
                    if x+1 >= length1 or (not esSolapen(primer, self.plots[x+1])):#si no es solapa amb el seguent 
                        y = y+1
                    if auxy+1 >= length2 or  (not esSolapen(sky2[auxy+1],self.plots[x])):
                        x = x+1
                else:
                    y = y+1
        self.plots = res
            

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
        self.plotsNoSolapats()

    


    def generarFigura(self):
        
        height = [x[1] for x in self.plots]
        width = [x[2]-x[0] for x in self.plots]
        pos = [((x[2]-x[0])/2)+x[0] for x in self.plots]
        plt.clf()
        plt.bar(pos,height,width=width) 
        plt.savefig("Skyline_" + self.nom)
        #plt.show()

    def unio(self, a):
        self.plots = self.plots + a
        self.ordenaPlots()
        self.plotsNoSolapats()
        '''
        height = [x[1] for x in self.plots] + [x[1] for x in a]
        width = [x[2]-x[0] for x in self.plots] + [x[2]-x[0] for x in a]
        pos = [((x[2]-x[0])/2)+x[0] for x in self.plots] + [((x[2]-x[0])/2)+x[0] for x in a]
        plt.bar(pos,height,width=width)
        plt.show()
        '''
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


#sky = Skyline([(1,2,3),(4,5,6)])
#sky.calculaAreaSkyline()
#sky.creacioEdificiAleatori({"n": 10, "h": 20, "w": 3, "xmin": 1, "xmax": 10})

#sky = Skyline([(3, 3, 5), (5, 18, 6), (7, 8, 8), (10, 8, 11), (12, 4, 13), (14, 4, 15), (15, 19, 18), (18, 10, 20), (20, 1, 21), (21, 11, 24), (24, 19, 25), (25, 17, 28), (34, 15, 37), (38, 10, 39), (43, 12, 45), (45, 16, 47), (47, 14, 48), (51, 2, 52), (52, 15, 55), (55, 13, 56), (56, 8, 57), (62, 14, 63), (65, 17, 68), (68, 10, 69), (69, 11, 72), (72, 18, 74), (74, 3, 75), (77, 15, 79), (80, 17, 83), (89, 14, 91), (91, 20, 94), (94, 5, 96), (96, 6, 99)])
#sky.interseccio([(2, 7, 3), (3, 13, 5), (7, 18, 9), (10, 14, 13), (13, 7, 14), (21, 11, 22), (22, 17, 23), (28, 17, 30), (34, 18, 36), (37, 15, 39), (39, 16, 41), (47, 5, 48), (48, 10, 51), (58, 16, 59), (59, 18, 60), (62, 14, 65), (75, 10, 76), (76, 18, 78), (78, 20, 80), (80, 5, 81), (81, 14, 84), (85, 18, 88), (88, 14, 90), (92, 11, 93), (95, 7, 96), (98, 13, 100)])

#sky.eliminaPlotsSenseVolum()
#sky.plotsNoSolapats()