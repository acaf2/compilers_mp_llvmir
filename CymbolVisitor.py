# Generated from Cymbol.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CymbolParser import CymbolParser
else:
    from CymbolParser import CymbolParser

# This class defines a complete generic visitor for a parse tree produced by CymbolParser.

class CymbolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CymbolParser#fileF.
    def visitFileF(self, ctx:CymbolParser.FileFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#varDecl.
    def visitVarDecl(self, ctx:CymbolParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#FormTypeInt.
    def visitFormTypeInt(self, ctx:CymbolParser.FormTypeIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#funcDecl.
    def visitFuncDecl(self, ctx:CymbolParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#paramTypeList.
    def visitParamTypeList(self, ctx:CymbolParser.ParamTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#paramType.
    def visitParamType(self, ctx:CymbolParser.ParamTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#block.
    def visitBlock(self, ctx:CymbolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#assignStat.
    def visitAssignStat(self, ctx:CymbolParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#returnStat.
    def visitReturnStat(self, ctx:CymbolParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#exprStat.
    def visitExprStat(self, ctx:CymbolParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#exprList.
    def visitExprList(self, ctx:CymbolParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#stat.
    def visitStat(self, ctx:CymbolParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#SignedExpr.
    def visitSignedExpr(self, ctx:CymbolParser.SignedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:CymbolParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:CymbolParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#IntExpr.
    def visitIntExpr(self, ctx:CymbolParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#ParenExpr.
    def visitParenExpr(self, ctx:CymbolParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:CymbolParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#VarIdExpr.
    def visitVarIdExpr(self, ctx:CymbolParser.VarIdExprContext):
        return self.visitChildren(ctx)



del CymbolParser
