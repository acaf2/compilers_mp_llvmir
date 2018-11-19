import sys
from antlr4 import *
from CymbolLexer import CymbolLexer
from CymbolParser import CymbolParser
from MyVisitor import MyVisitor

def main(argv):
    input = FileStream("code.c")
    lexer = CymbolLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CymbolParser(stream)
    
    tree = parser.fileF()

    visitor = MyVisitor()
    visitor.visit(tree)
 
if __name__ == '__main__':
    main(sys.argv)
