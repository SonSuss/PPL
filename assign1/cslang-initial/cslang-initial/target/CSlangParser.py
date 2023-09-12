# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\f\4\2\t\2\3\2\6\2\6\n\2\r\2\16\2\7\3\2\3\2\3\2\2\2\3")
        buf.write("\2\2\2\2\13\2\5\3\2\2\2\4\6\7.\2\2\5\4\3\2\2\2\6\7\3\2")
        buf.write("\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\t\3\2\2\2\t\n\7\2\2\3\n")
        buf.write("\3\3\2\2\2\3\7")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'true'", "'false'", "'int'", "'float'", "'bool'", 
                     "'string'", "'return'", "'null'", "'class'", "'constructor'", 
                     "'var'", "'self'", "'new'", "'void'", "'const'", "'constant'", 
                     "'func'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", "'\\'", 
                     "'%'", "'/'", "'^'", "'.'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                      "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
                      "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                      "NEW", "VOID", "CONST", "CONSTANT", "FUNC", "NOT", 
                      "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
                      "LESS_EQUAL", "GREATER_EQUAL", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", "STRING_CONCAT", 
                      "DOT", "WS", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOL_LITERAL", 
                      "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSE=4
    FOR=5
    TRUE=6
    FALSE=7
    INT=8
    FLOAT=9
    BOOL=10
    STRING=11
    RETURN=12
    NULL=13
    CLASS=14
    CONSTRUCTOR=15
    VAR=16
    SELF=17
    NEW=18
    VOID=19
    CONST=20
    CONSTANT=21
    FUNC=22
    NOT=23
    AND=24
    OR=25
    EQUAL=26
    NOT_EQUAL=27
    LESS=28
    GREATER=29
    LESS_EQUAL=30
    GREATER_EQUAL=31
    PLUS=32
    MINUS=33
    MULTIPLY=34
    DIVIDE_I=35
    DIVIDE_I_L=36
    DIVIDE_F=37
    STRING_CONCAT=38
    DOT=39
    WS=40
    INTEGER_LITERAL=41
    FLOAT_LITERAL=42
    BOOL_LITERAL=43
    ID=44
    ERROR_CHAR=45
    UNCLOSE_STRING=46
    ILLEGAL_ESCAPE=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                self.match(CSlangParser.ID)
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.ID):
                    break

            self.state = 7
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





