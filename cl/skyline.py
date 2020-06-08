import matplotlib.pyplot as plt
import random as rand


def takeFirst(elem):
    return elem[0]


def takeSecond(elem):
    return elem[1]


def edificiDins(edi1, edi2):
    # vol dir que edi1 és contingut d'edi2:
    if edi1[0] >= edi2[0] and edi1[1] <= edi2[1] and edi1[2] <= edi2[2]:
        return 1
    # edi2 contingut a edi1:
    elif edi1[0] <= edi2[0] and edi1[1] >= edi2[1] and edi1[2] >= edi2[2]:
        return 2
    else:
        return 3  # no estan continguts


def esSolapen(edi1, edi2):
    op1 = (edi1[0] <= edi2[0] and edi1[2] >= edi2[0])
    op2 = (edi2[0] <= edi1[0] and edi2[2] >= edi1[0])
    if op1 or op2:
        return True
    else:
        return False


class Skyline:
    nom = "1"
    plots = []
    area = 0
    alcada = 0

    def __init__(self, plot):
        self.plots = plot
        # self.calculaAreaSkyline()

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

    def calculaAlçadaMax(self):
        self.alcada = max(self.plots, key=takeSecond)[1]

    def reordena(self, elem, index):
        insertat = False
        length = len(self.plots)
        while not insertat:
            if index == length:
                insertat = True
                self.plots.insert(index, elem)
            elif self.plots[index][0] >= elem[0]:
                insertat = True
                self.plots.insert(index, elem)
            index = index + 1

# per a que funcioni els edificis han d'estar ordenats
# en ordre creixent de posicio inicial
    def plotsNoSolapats(self):
        self.eliminaPlotsSenseVolum()
        length = len(self.plots)
        x = 0
        while x < length-1:
            if(self.plots[x][0] >= self.plots[x][2]):
                self.plots.remove(self.plots[x])
                length = length-1
                x = x-2
                if x < -1:
                    x = -1
            else:
                aux = edificiDins(self.plots[x], self.plots[x+1])
                if aux == 1 or aux == 2:
                    if aux == 1:
                        self.plots.remove(self.plots[x])
                        x = x - 2
                        if x < -1:
                            x = -1
                    else:
                        self.plots.remove(self.plots[x+1])
                        x = x-1
                    length = length - 1

                # edificis solapats
                elif self.plots[x][2] > self.plots[x+1][0]:
                    # puede provocar min>max asi que hay que eliminarlo:
                    if self.plots[x][1] <= self.plots[x+1][1]:
                        self.plots[x] = list(self.plots[x])
                        self.plots[x][2] = self.plots[x+1][0]
                        self.plots[x] = tuple(self.plots[x])
                        if(self.plots[x][0] >= self.plots[x][2]):
                            self.plots.remove(self.plots[x])
                            length = length - 1
                            x = x - 2
                            if x < - 1:
                                x = - 1
                    # como mueve la posucion inicial puede
                    # provocar que dejen de estar ordenados
                    else:
                        self.plots[x+1] = list(self.plots[x+1])
                        self.plots[x+1][0] = self.plots[x][2]
                        self.plots[x+1] = tuple(self.plots[x+1])
                        if self.plots[x][0] > self.plots[x+1][0]:
                            aux = self.plots[x]
                            self.plots.remove(aux)
                            self.reordena(aux, x)

                # en cas de que dos edifici tinguin la mateixa
                # alçada despres de dessolaparlos es fusionen
                op1 = self.plots[x][1] == self.plots[x+1][1]
                op2 = self.plots[x][2] == self.plots[x+1][0]
                if x < length - 1 and op1 and op2:
                    edificiFusionat = (self.plots[x][0],
                                       self.plots[x][1], self.plots[x+1][2])
                    self.plots.remove(self.plots[x+1])
                    self.plots.remove(self.plots[x])
                    self.plots.insert(x, edificiFusionat)
                    length = length - 1
                    x = x-1
            x = x + 1

    # es pasa com a parametre la llista d'edificis
    def interseccio(self, sky2):
        x = 0
        y = 0
        length1 = len(self.plots)
        length2 = len(sky2)
        res = []
        while x < length1 and y < length2:
            # si l'edifici de més a l'esquerra és del primer skyline:
            if self.plots[x][0] < sky2[y][0]:
                primer = self.plots[x]
                # estan solapats:
                if sky2[y][0] >= primer[0] and sky2[y][0] < primer[2]:
                    edificiAfegir = (sky2[y][0], min(sky2[y][1], primer[1]),
                                     min(sky2[y][2], primer[2]))
                    res = res + [edificiAfegir]
                    auxx = x
                    # si no es solapa amb el seguent:
                    if y+1 >= length2 or (not esSolapen(primer, sky2[y+1])):
                        x = x+1
                    if auxx+1 >= length1 or (not esSolapen(self.plots[auxx+1],
                                             sky2[y])):
                        y = y+1
                else:
                    x = x+1
            else:
                primer = sky2[y]
                # estan solapats:
                op1 = self.plots[x][0] >= primer[0]
                op2 = self.plots[x][0] < primer[2]
                if op1 and op2:
                    edificiAfegir = (self.plots[x][0], min(self.plots[x][1],
                                     primer[1]),
                                     min(self.plots[x][2], primer[2]))
                    res = res + [edificiAfegir]
                    auxy = y

                    # si no es solapa amb el seguent:
                    if x+1 >= length1 or (not esSolapen(primer,
                                                        self.plots[x+1])):
                        y = y+1
                    if auxy+1 >= length2 or (not esSolapen(sky2[auxy+1],
                                             self.plots[x])):
                        x = x+1
                else:
                    y = y+1
        self.plots = res

    def ordenaPlots(self):
        self.plots.sort(key=takeFirst)

    # plot -> (xmin,alçada,xmax):
    def creacioEdificiSimple(self, plot):
        self.plots = [plot]

    # plots -> [(xmin,alçada,xmax),(xmin,alçada,xmax),...]
    def creacioEdificiCompostos(self, plots):
        self.plots = plots
        self.ordenaPlots()

    # plot -> {n,h,w,xmin,xmax} n = nombre edificis,
    # h = alçada aleatoria entre 0 i h,
    # w = amblada aleatoria entre 1 i w,
    # xmin i xmax -> posicions inici entre xmin i xmax
    def creacioEdificiAleatori(self, plot):
        n = plot['n']
        h = plot['h']
        w = plot['w']
        xmin = plot['xmin']
        xmax = plot['xmax']
        res = []
        for _ in range(n):
            mini = rand.randint(xmin, xmax-1)
            maxi = xmax
            if(mini + w <= xmax):
                maxi = rand.randint(mini+1, mini + w)
            else:
                maxi = rand.randint(mini+1, xmax)
            res = res + [(mini, rand.randint(0, h), maxi)]
        self.plots = res
        self.ordenaPlots()
        self.plotsNoSolapats()
        print(self.plots)

    def generarFigura(self):
        height = [x[1] for x in self.plots]
        width = [x[2]-x[0] for x in self.plots]
        pos = [((x[2]-x[0])/2)+x[0] for x in self.plots]
        plt.clf()
        plt.bar(pos, height, width=width)
        plt.savefig("Skyline")

    def unio(self, a):
        self.plots = self.plots + a
        self.ordenaPlots()
        self.plotsNoSolapats()

    def calculPosReflex(self, min, max, pos):
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
            ret = ret + [(self.calculPosReflex(min, max, x[2]), x[1],
                         self.calculPosReflex(min, max, x[0]))]
        self.plots = ret
        self.ordenaPlots()

    def multiplicaSkyline(self, num):
        amplada = self.plots[-1][-1] - self.plots[0][0]
        ret = []
        for x in range(1, num):
            for y in self.plots:
                ret = ret + [(y[0] + (amplada*x), y[1], y[2] + (amplada*x))]
        self.plots = self.plots + ret

    def desplacamentEdificisDreta(self, n):
        self.plots = list(map(lambda e: (e[0]+n, e[1], e[2]+n), self.plots))

    def desplacamentEdificisEsquerra(self, n):
        self.plots = list(map(lambda e: (e[0]-n, e[1], e[2]-n), self.plots))
