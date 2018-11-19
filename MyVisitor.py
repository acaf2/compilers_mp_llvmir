import sys
from antlr4 import *
from CymbolLexer import CymbolLexer
from CymbolParser import CymbolParser
from CymbolVisitor import CymbolVisitor

##############################################################
##Desenvolvido por:
##      >Adrion Cavalcanti - acaf2
##      >Thyago Monteiro   - tmp2
##
##ERROS IDENTIFICADOS:
##1. EXPRESSOES CONSTANTES:
##      llvm ir:     calcula expressoes e salva o valor cte
##      cymbol ir:   utiliza expr aritmetica pra calulcar os 
##                   valores e assim salvá-los.

class MyVisitor(CymbolVisitor):

    varDic = {}                         #Variable Dictionary
    varEnd = {}                         #Variable Adress
    acm = 0                             #Accumulator
    virgula = 0                         #bad pratice
    def visitFuncDecl(self, ctx):
        self.varDic.clear()
        self.varEnd.clear()
        self.acm = 0
        print("define i32 @" + ctx.ID().getText() + "(",end='')
        
        if ctx.paramTypeList() != None :
            ctx.paramTypeList().accept(self)
            self.virgula = 0
            self.acm += 1
        else:
            self.acm = 1 
        
        print(") #0 {")
        if ctx.ID().getText() == "main":
            print ("     %1 = alloca i32, align 4")
            print ("     store i32 0, i32* %1, align 4")
            self.acm += 1
        
        acmAux = self.acm
        for x in self.varDic:
            self.varEnd[x] = self.acm
            print("     %"+str(self.acm)+" = alloca i32, align 4")
            self.acm += 1

        for x in self.varDic:
            y = self.varDic.get(x)
            self.varDic.update({x:acmAux})
            print("     store i32 %"+str(y)+", i32* %"+str(acmAux)+", align 4")
            acmAux += 1
            
        result = ctx.block().accept(self)

        print("}")
        return result

    def visitVarDecl(self, ctx):
        idName = ctx.ID().getText()
        self.varEnd[idName] = self.acm
        self.varDic[idName] = self.acm
        print("     %"+ str(self.acm) + " = alloca i32, align 4")
        self.acm = self.acm + 1
        result = 0
        if ctx.expr() != None:
            result = ctx.expr().accept(self)
            print("     store i32 "+str(result)+", i32* %"+ str(self.varEnd.get(idName))+", align 4")
        return result

    def visitParamType(self, ctx):
        idName = str(ctx.ID().getText())
        self.varDic[idName] = self.acm
        self.acm += 1
        if self.virgula == 0:
            print("i32", end='')
            self.virgula = 1
        else :
            print(", i32", end='')
        return self.visitChildren(ctx)
    
    def visitIntExpr(self, ctx):
        val = ctx.INT().getText()
        return val
    
    def visitVarIdExpr(self,ctx):
        id =  ctx.ID().getText()
        val = self.varDic.get(id)
        print("     %"+str(self.acm)+" = load i32, i32* %"+str(self.varEnd.get(id))+", align 4") 
        self.varDic.update({id:self.acm})
        self.acm += 1
        return "%"+str(self.acm-1)

    def visitAddSubExpr(self,ctx):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        if '+' in ctx.getText():
            print("     %"+ str(self.acm) +" = add nsw i32 "+str(left)+", "+str(right))
            self.acm += 1
        else:
            print("     %"+ str(self.acm) +" = sub nsw i32 "+str(left)+", "+str(right))
            self.acm += 1
        return "%"+str(self.acm-1)

    def visitMulDivExpr(self,ctx):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        if '*' in ctx.getText():
            print("     %"+ str(self.acm) +" = mul nsw i32 "+str(left)+", "+str(right))
            self.acm += 1
        else:
            print("     %"+ str(self.acm) +" = div nsw i32 "+str(left)+", "+str(right))
            self.acm += 1
        return "%"+str(self.acm-1)

    def visitFunctionCallExpr(self,ctx):
        val = 0
        if ctx.exprList() != None:
            val = ctx.exprList().accept(self)
            print ("     %"+str(self.acm)+" = call i32 @"+ctx.ID().getText()+"("+val+")")
            self.acm += 1
        else:
            print ("     %"+str(self.acm)+" = call i32 @"+ctx.ID().getText()+"()")
            self.acm += 1
        return "%"+str(self.acm-1)

    def visitExprList(self,ctx):
        result = ""
        for i in range(len(ctx.expr())):
            result2 = str(ctx.expr(i).accept(self))
            if i == 0:
                result = result + "i32 "+result2
            else: 
                result = result + ", i32 "+result2

        return result

    def visitAssignStat(self, ctx):
        idName = str(ctx.ID())
        temp = self.varDic.get(idName)
        result = ctx.expr().accept(self)
        print("     store i32 "+str(result)+", i32* %"+ str(self.varEnd.get(idName))+", align 4")
        return result
    
    def visitReturnStat(self,ctx):
        result = ctx.expr().accept(self)
        print ("     ret i32 "+result)
        return result

    def visitParenExpr(self,ctx):
        result = ctx.expr().accept(self)
        return result

    def visitSignedExpr(self, ctx):
        result = ctx.expr().accept(self)
        signal = ctx.getText()[0]
        if(signal == '-'):
            print("     %"+ str(self.acm) +" = sub nsw i32 0, i32 "+str(result))
            self.acm += 1
            result = "%"+str(self.acm-1)    
            
        return result