# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\6\n:\n\n\r\n\16\n;\3\13\6\13?\n\13\r\13\16")
        buf.write("\13@\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\3\2\4\3\2c|\5\2\13\f\17\17\"\"\2K\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2")
        buf.write("\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13+\3\2\2\2\r-\3\2")
        buf.write("\2\2\17/\3\2\2\2\21\63\3\2\2\2\239\3\2\2\2\25>\3\2\2\2")
        buf.write("\27D\3\2\2\2\31F\3\2\2\2\33H\3\2\2\2\35\36\7e\2\2\36\37")
        buf.write("\7n\2\2\37 \7c\2\2 !\7u\2\2!\"\7u\2\2\"\4\3\2\2\2#$\7")
        buf.write("}\2\2$\6\3\2\2\2%&\7\177\2\2&\b\3\2\2\2\'(\7x\2\2()\7")
        buf.write("c\2\2)*\7t\2\2*\n\3\2\2\2+,\7<\2\2,\f\3\2\2\2-.\7=\2\2")
        buf.write(".\16\3\2\2\2/\60\7k\2\2\60\61\7p\2\2\61\62\7v\2\2\62\20")
        buf.write("\3\2\2\2\63\64\7x\2\2\64\65\7q\2\2\65\66\7k\2\2\66\67")
        buf.write("\7f\2\2\67\22\3\2\2\28:\t\2\2\298\3\2\2\2:;\3\2\2\2;9")
        buf.write("\3\2\2\2;<\3\2\2\2<\24\3\2\2\2=?\t\3\2\2>=\3\2\2\2?@\3")
        buf.write("\2\2\2@>\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\b\13\2\2C\26\3")
        buf.write("\2\2\2DE\13\2\2\2E\30\3\2\2\2FG\13\2\2\2G\32\3\2\2\2H")
        buf.write("I\13\2\2\2I\34\3\2\2\2\5\2;@\3\b\2\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    INTTYPE = 7
    VOIDTYPE = 8
    ID = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'{'", "'}'", "'var'", "':'", "';'", "'int'", "'void'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "INTTYPE", 
                  "VOIDTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


