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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("\u00a3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2~\n\2\3\3\3\3\5\3\u0082\n\3\3\3\3\3\3")
        buf.write("\3\7\3\u0087\n\3\f\3\16\3\u008a\13\3\3\4\6\4\u008d\n\4")
        buf.write("\r\4\16\4\u008e\3\5\6\5\u0092\n\5\r\5\16\5\u0093\3\6\6")
        buf.write("\6\u0097\n\6\r\6\16\6\u0098\3\6\3\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3")
        buf.write("\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2\u00be\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3}\3\2\2\2\5")
        buf.write("\u0081\3\2\2\2\7\u008c\3\2\2\2\t\u0091\3\2\2\2\13\u0096")
        buf.write("\3\2\2\2\r\u009c\3\2\2\2\17\u009f\3\2\2\2\21\u00a1\3\2")
        buf.write("\2\2\23\24\7d\2\2\24\25\7t\2\2\25\26\7g\2\2\26\27\7c\2")
        buf.write("\2\27~\7m\2\2\30\31\7e\2\2\31\32\7q\2\2\32\33\7p\2\2\33")
        buf.write("\34\7v\2\2\34\35\7k\2\2\35\36\7p\2\2\36\37\7w\2\2\37~")
        buf.write("\7g\2\2 !\7k\2\2!~\7h\2\2\"#\7g\2\2#$\7n\2\2$%\7u\2\2")
        buf.write("%~\7g\2\2&\'\7h\2\2\'(\7q\2\2(~\7t\2\2)*\7v\2\2*+\7t\2")
        buf.write("\2+,\7w\2\2,~\7g\2\2-.\7h\2\2./\7c\2\2/\60\7n\2\2\60\61")
        buf.write("\7u\2\2\61~\7g\2\2\62\63\7k\2\2\63\64\7p\2\2\64~\7v\2")
        buf.write("\2\65\66\7h\2\2\66\67\7n\2\2\678\7q\2\289\7c\2\29~\7v")
        buf.write("\2\2:;\7d\2\2;<\7q\2\2<=\7q\2\2=~\7n\2\2>?\7u\2\2?@\7")
        buf.write("v\2\2@A\7t\2\2AB\7k\2\2BC\7p\2\2C~\7i\2\2DE\7t\2\2EF\7")
        buf.write("g\2\2FG\7v\2\2GH\7w\2\2HI\7t\2\2I~\7p\2\2JK\7p\2\2KL\7")
        buf.write("w\2\2LM\7n\2\2M~\7n\2\2NO\7e\2\2OP\7n\2\2PQ\7c\2\2QR\7")
        buf.write("u\2\2R~\7u\2\2ST\7e\2\2TU\7q\2\2UV\7p\2\2VW\7u\2\2WX\7")
        buf.write("v\2\2XY\7t\2\2YZ\7w\2\2Z[\7e\2\2[\\\7v\2\2\\]\7q\2\2]")
        buf.write("~\7t\2\2^_\7x\2\2_`\7c\2\2`~\7t\2\2ab\7u\2\2bc\7g\2\2")
        buf.write("cd\7n\2\2d~\7h\2\2ef\7p\2\2fg\7g\2\2g~\7y\2\2hi\7x\2\2")
        buf.write("ij\7q\2\2jk\7k\2\2k~\7f\2\2lm\7e\2\2mn\7q\2\2no\7p\2\2")
        buf.write("op\7u\2\2p~\7v\2\2qr\7e\2\2rs\7q\2\2st\7p\2\2tu\7u\2\2")
        buf.write("uv\7v\2\2vw\7c\2\2wx\7p\2\2x~\7v\2\2yz\7h\2\2z{\7w\2\2")
        buf.write("{|\7p\2\2|~\7e\2\2}\23\3\2\2\2}\30\3\2\2\2} \3\2\2\2}")
        buf.write("\"\3\2\2\2}&\3\2\2\2})\3\2\2\2}-\3\2\2\2}\62\3\2\2\2}")
        buf.write("\65\3\2\2\2}:\3\2\2\2}>\3\2\2\2}D\3\2\2\2}J\3\2\2\2}N")
        buf.write("\3\2\2\2}S\3\2\2\2}^\3\2\2\2}a\3\2\2\2}e\3\2\2\2}h\3\2")
        buf.write("\2\2}l\3\2\2\2}q\3\2\2\2}y\3\2\2\2~\4\3\2\2\2\177\u0082")
        buf.write("\5\t\5\2\u0080\u0082\7a\2\2\u0081\177\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\u0088\3\2\2\2\u0083\u0087\5\t\5\2\u0084")
        buf.write("\u0087\5\7\4\2\u0085\u0087\7a\2\2\u0086\u0083\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3")
        buf.write("\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\6")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008d\t\2\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\b\3\2\2\2\u0090\u0092\t\3\2")
        buf.write("\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\n\3\2\2\2\u0095\u0097")
        buf.write("\t\4\2\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\b\6\2\2\u009b\f\3\2\2\2\u009c\u009d\13\2")
        buf.write("\2\2\u009d\u009e\b\7\3\2\u009e\16\3\2\2\2\u009f\u00a0")
        buf.write("\13\2\2\2\u00a0\20\3\2\2\2\u00a1\u00a2\13\2\2\2\u00a2")
        buf.write("\22\3\2\2\2\n\2}\u0081\u0086\u0088\u008e\u0093\u0098\4")
        buf.write("\b\2\2\3\7\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    KEYWORDS = 1
    ID = 2
    DIGITS = 3
    LETTERS = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "KEYWORDS", "ID", "DIGITS", "LETTERS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "KEYWORDS", "ID", "DIGITS", "LETTERS", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


