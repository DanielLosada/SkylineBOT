# Generated from Skyline.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#variable.
    def visitVariable(self, ctx:SkylineParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#exprovar.
    def visitExprovar(self, ctx:SkylineParser.ExprovarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#creaoskyline.
    def visitCreaoskyline(self, ctx:SkylineParser.CreaoskylineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#crea.
    def visitCrea(self, ctx:SkylineParser.CreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skylineope.
    def visitSkylineope(self, ctx:SkylineParser.SkylineopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyline.
    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#simple.
    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#compost.
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#aleatori.
    def visitAleatori(self, ctx:SkylineParser.AleatoriContext):
        return self.visitChildren(ctx)



del SkylineParser