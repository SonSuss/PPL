# Generated from e:/hocbaidcm/PPL/assignment/assign3/assignment3/initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,13,72,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,4,8,56,8,8,11,8,12,8,
        57,1,9,4,9,61,8,9,11,9,12,9,62,1,9,1,9,1,10,1,10,1,11,1,11,1,12,
        1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        23,12,25,13,1,0,2,1,0,97,122,3,0,9,10,13,13,32,32,73,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,33,1,0,0,0,5,35,1,0,0,0,7,37,
        1,0,0,0,9,41,1,0,0,0,11,43,1,0,0,0,13,45,1,0,0,0,15,49,1,0,0,0,17,
        55,1,0,0,0,19,60,1,0,0,0,21,66,1,0,0,0,23,68,1,0,0,0,25,70,1,0,0,
        0,27,28,5,99,0,0,28,29,5,108,0,0,29,30,5,97,0,0,30,31,5,115,0,0,
        31,32,5,115,0,0,32,2,1,0,0,0,33,34,5,123,0,0,34,4,1,0,0,0,35,36,
        5,125,0,0,36,6,1,0,0,0,37,38,5,118,0,0,38,39,5,97,0,0,39,40,5,114,
        0,0,40,8,1,0,0,0,41,42,5,58,0,0,42,10,1,0,0,0,43,44,5,59,0,0,44,
        12,1,0,0,0,45,46,5,105,0,0,46,47,5,110,0,0,47,48,5,116,0,0,48,14,
        1,0,0,0,49,50,5,118,0,0,50,51,5,111,0,0,51,52,5,105,0,0,52,53,5,
        100,0,0,53,16,1,0,0,0,54,56,7,0,0,0,55,54,1,0,0,0,56,57,1,0,0,0,
        57,55,1,0,0,0,57,58,1,0,0,0,58,18,1,0,0,0,59,61,7,1,0,0,60,59,1,
        0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,
        65,6,9,0,0,65,20,1,0,0,0,66,67,9,0,0,0,67,22,1,0,0,0,68,69,9,0,0,
        0,69,24,1,0,0,0,70,71,9,0,0,0,71,26,1,0,0,0,3,0,57,62,1,6,0,0
    ]

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
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


