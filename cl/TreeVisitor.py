#from skyline import Skyline
from antlr4 import *
import sys
sys.path.insert(1, '../')
import skyline
#import skyline
#import skyline.py


if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor


class TreeVisitor(SkylineVisitor):

    def __init__(self):
        self.nivell = 0

    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = next(ctx.getChildren())
        a = self.visit(n)
        print(a.plots)
        return a
    
    def visitExpr(self, ctx: SkylineParser.ExprContext):
        n = next(ctx.getChildren())
        return self.visit(n)
    
    def visitExprovar(self, ctx: SkylineParser.ExprovarContext):
        l = [n for n in ctx.getChildren()] 
        a = self.visit(l[2])
        return a 
        
    def visitCreaoskyline(self, ctx: SkylineParser.CreaoskylineContext):
        n = next(ctx.getChildren())
        return self.visit(n)

    def visitCrea(self, ctx: SkylineParser.CreaContext):
        n = next(ctx.getChildren())
        return self.visit(n)
    
    def visitSimple(self, ctx: SkylineParser.SimpleContext):
        #simple: '(' NUM ',' NUM ',' NUM ')'; (xmin,alçada,xmax)
        xmin = int(ctx.NUM(0).getText())
        xmax = int(ctx.NUM(2).getText())
        alcada = int(ctx.NUM(1).getText())
        sky = skyline.Skyline([])
        sky.creacioEdificiSimple((xmin,alcada,xmax))
        return sky

    def visitCompost(self, ctx: SkylineParser.CompostContext):
        #[(xmin,alçada,xmax),(xmin,alçada,xmax),...]
        l = [self.visit(n).plots for n in ctx.simple()]
        res = []
        for i in l:
            res = res + [i[0]]
        sky = skyline.Skyline([])
        sky.creacioEdificiCompostos(res)
        return sky

    def visitAleatori(self, ctx: SkylineParser.AleatoriContext):
        #{n,h,w,xmin,xmax}
        n = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        w = int(ctx.NUM(2).getText())
        xmin = int(ctx.NUM(3).getText())
        xmax = int(ctx.NUM(4).getText())
        ale = {'n': n, 'h': h, 'w': w,'xmin': xmin, 'xmax':xmax}
        sky = skyline.Skyline([])
        sky.creacioEdificiAleatori(ale)
        return sky

    def visitSkyline(self, ctx: SkylineParser.SkylineContext):
        n = next(ctx.getChildren())
        return self.visit(n)

    def visitSkylineope(self, ctx: SkylineParser.SkylineopeContext):
        l = [n for n in ctx.getChildren()] 
        if len(l) == 1: # |skyline
            return self.visit(l[0])
        elif len(l) == 2: # | '-' skyline
            sky = self.visit(l[1]) #agafo l'skyline
            sky.reflectit()
            return sky
        elif len(l) == 3:

            if str(next(ctx.getChildren())) == '(':
                return self.visit(l[1])
            else:
                if ctx.skylineope() and not ctx.NUM():
                    sky1 = self.visit(l[0])
                    sky2 = self.visit(l[2])
                    if str(l[1]) == '*': #interseccio d'skylines
                        sky1.interseccio(sky2.plots)
                    elif str(l[1]) == '+': #unio skylines
                        sky1.unio(sky2.plots)
                    return sky1
                else:
                    sky = self.visit(l[0])
                    num = int(l[2].getText())
                    if str(l[1]) == '*': #replicació
                        sky.multiplicaSkyline(num)
                    elif str(l[1]) == '+': #desplaçament dreta
                        sky.desplacamentEdificisDreta(num)
                    else:
                        sky.desplacamentEdificisEsquerra(num)
                    return sky

            '''
        elif len(l) == 3:
            print("hi ha 3")
            if str(next(ctx.getChildren())) == '(':
                print('operacio entre parentesis')
            else:
                if ctx.skyline(): #en cas que hi hagi algun skyline
                    if ctx.skylineope():
                        sky1 = self.visit(l[0])
                        sky2 = self.visit(ctx.skylineope(0))
                        print(sky2.plots)
                        print('skyline op skylineope')
                        if str(l[1]) == '*': #interseccio d'skylines
                            sky1.interseccio(sky2.plots)
                        elif str(l[1]) == '+':
                            sky1.unio(sky2.plots)
                        return sky1
                    elif ctx.NUM():
                        print('skyline op NUM')
                        sky1 = self.visit(l[0])

                    else:
                        print('skyline op skyline')
                    #l2 = [n for n in ctx.skyline()]
                    #if(len(l2) == 2): #vol dir que hi ha skyliskylinene op skyline
                    #    print('skyline op skyline')

'''




         





    
    

