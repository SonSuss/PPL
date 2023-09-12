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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2#")
        buf.write("\u011d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\6\33\u00d9\n\33\r")
        buf.write("\33\16\33\u00da\3\33\3\33\3\34\6\34\u00e0\n\34\r\34\16")
        buf.write("\34\u00e1\3\35\6\35\u00e5\n\35\r\35\16\35\u00e6\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u00ee\n\35\3\36\3\36\5\36\u00f2")
        buf.write("\n\36\3\37\3\37\5\37\u00f6\n\37\3\37\3\37\3\37\6\37\u00fb")
        buf.write("\n\37\r\37\16\37\u00fc\3 \3 \5 \u0101\n \3!\3!\7!\u0105")
        buf.write("\n!\f!\16!\u0108\13!\3\"\3\"\3\"\6\"\u010d\n\"\r\"\16")
        buf.write("\"\u010e\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\2\2")
        buf.write(")\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?\2A\2C\2E\2G\2I\2K")
        buf.write("!M\"O#\3\2\6\5\2\13\f\17\17\"\"\4\2GGgg\3\2\62;\4\2C\\")
        buf.write("c|\2\u0123\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\3Q\3\2\2\2\5W\3\2\2")
        buf.write("\2\7`\3\2\2\2\tc\3\2\2\2\13h\3\2\2\2\rl\3\2\2\2\17q\3")
        buf.write("\2\2\2\21w\3\2\2\2\23{\3\2\2\2\25\u0081\3\2\2\2\27\u0086")
        buf.write("\3\2\2\2\31\u008d\3\2\2\2\33\u0094\3\2\2\2\35\u0099\3")
        buf.write("\2\2\2\37\u009f\3\2\2\2!\u00ab\3\2\2\2#\u00af\3\2\2\2")
        buf.write("%\u00b4\3\2\2\2\'\u00b8\3\2\2\2)\u00bd\3\2\2\2+\u00c3")
        buf.write("\3\2\2\2-\u00cc\3\2\2\2/\u00d1\3\2\2\2\61\u00d3\3\2\2")
        buf.write("\2\63\u00d5\3\2\2\2\65\u00d8\3\2\2\2\67\u00df\3\2\2\2")
        buf.write("9\u00e4\3\2\2\2;\u00f1\3\2\2\2=\u00f5\3\2\2\2?\u0100\3")
        buf.write("\2\2\2A\u0102\3\2\2\2C\u0109\3\2\2\2E\u0110\3\2\2\2G\u0112")
        buf.write("\3\2\2\2I\u0114\3\2\2\2K\u0116\3\2\2\2M\u0119\3\2\2\2")
        buf.write("O\u011b\3\2\2\2QR\7d\2\2RS\7t\2\2ST\7g\2\2TU\7c\2\2UV")
        buf.write("\7m\2\2V\4\3\2\2\2WX\7e\2\2XY\7q\2\2YZ\7p\2\2Z[\7v\2\2")
        buf.write("[\\\7k\2\2\\]\7p\2\2]^\7w\2\2^_\7g\2\2_\6\3\2\2\2`a\7")
        buf.write("k\2\2ab\7h\2\2b\b\3\2\2\2cd\7g\2\2de\7n\2\2ef\7u\2\2f")
        buf.write("g\7g\2\2g\n\3\2\2\2hi\7h\2\2ij\7q\2\2jk\7t\2\2k\f\3\2")
        buf.write("\2\2lm\7v\2\2mn\7t\2\2no\7w\2\2op\7g\2\2p\16\3\2\2\2q")
        buf.write("r\7h\2\2rs\7c\2\2st\7n\2\2tu\7u\2\2uv\7g\2\2v\20\3\2\2")
        buf.write("\2wx\7k\2\2xy\7p\2\2yz\7v\2\2z\22\3\2\2\2{|\7h\2\2|}\7")
        buf.write("n\2\2}~\7q\2\2~\177\7c\2\2\177\u0080\7v\2\2\u0080\24\3")
        buf.write("\2\2\2\u0081\u0082\7d\2\2\u0082\u0083\7q\2\2\u0083\u0084")
        buf.write("\7q\2\2\u0084\u0085\7n\2\2\u0085\26\3\2\2\2\u0086\u0087")
        buf.write("\7u\2\2\u0087\u0088\7v\2\2\u0088\u0089\7t\2\2\u0089\u008a")
        buf.write("\7k\2\2\u008a\u008b\7p\2\2\u008b\u008c\7i\2\2\u008c\30")
        buf.write("\3\2\2\2\u008d\u008e\7t\2\2\u008e\u008f\7g\2\2\u008f\u0090")
        buf.write("\7v\2\2\u0090\u0091\7w\2\2\u0091\u0092\7t\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\32\3\2\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7w\2\2\u0096\u0097\7n\2\2\u0097\u0098\7n\2\2\u0098\34")
        buf.write("\3\2\2\2\u0099\u009a\7e\2\2\u009a\u009b\7n\2\2\u009b\u009c")
        buf.write("\7c\2\2\u009c\u009d\7u\2\2\u009d\u009e\7u\2\2\u009e\36")
        buf.write("\3\2\2\2\u009f\u00a0\7e\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7e\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7t\2\2\u00aa \3")
        buf.write("\2\2\2\u00ab\u00ac\7x\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\"\3\2\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3\7h\2\2\u00b3$\3")
        buf.write("\2\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7y\2\2\u00b7&\3\2\2\2\u00b8\u00b9\7x\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7f\2\2\u00bc(\3")
        buf.write("\2\2\2\u00bd\u00be\7e\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7v\2\2\u00c2*\3")
        buf.write("\2\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7v\2\2\u00cb,\3")
        buf.write("\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7e\2\2\u00d0.\3\2\2\2\u00d1\u00d2")
        buf.write("\7-\2\2\u00d2\60\3\2\2\2\u00d3\u00d4\7/\2\2\u00d4\62\3")
        buf.write("\2\2\2\u00d5\u00d6\7\60\2\2\u00d6\64\3\2\2\2\u00d7\u00d9")
        buf.write("\t\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2")
        buf.write("\u00dc\u00dd\b\33\2\2\u00dd\66\3\2\2\2\u00de\u00e0\5G")
        buf.write("$\2\u00df\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e28\3\2\2\2\u00e3\u00e5")
        buf.write("\5G$\2\u00e4\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ed\3\2\2\2\u00e8")
        buf.write("\u00ee\5A!\2\u00e9\u00ee\5C\"\2\u00ea\u00eb\5A!\2\u00eb")
        buf.write("\u00ec\5C\"\2\u00ec\u00ee\3\2\2\2\u00ed\u00e8\3\2\2\2")
        buf.write("\u00ed\u00e9\3\2\2\2\u00ed\u00ea\3\2\2\2\u00ee:\3\2\2")
        buf.write("\2\u00ef\u00f2\5\r\7\2\u00f0\u00f2\5\17\b\2\u00f1\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2<\3\2\2\2\u00f3\u00f6")
        buf.write("\5I%\2\u00f4\u00f6\5E#\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6\u00fa\3\2\2\2\u00f7\u00fb\5I%\2\u00f8\u00fb")
        buf.write("\5G$\2\u00f9\u00fb\5E#\2\u00fa\u00f7\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd>\3\2\2\2\u00fe")
        buf.write("\u0101\5/\30\2\u00ff\u0101\5\61\31\2\u0100\u00fe\3\2\2")
        buf.write("\2\u0100\u00ff\3\2\2\2\u0101@\3\2\2\2\u0102\u0106\5\63")
        buf.write("\32\2\u0103\u0105\5G$\2\u0104\u0103\3\2\2\2\u0105\u0108")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write("B\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010a\t\3\2\2\u010a")
        buf.write("\u010c\5? \2\u010b\u010d\5G$\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010fD\3\2\2\2\u0110\u0111\7a\2\2\u0111F\3\2\2\2\u0112")
        buf.write("\u0113\t\4\2\2\u0113H\3\2\2\2\u0114\u0115\t\5\2\2\u0115")
        buf.write("J\3\2\2\2\u0116\u0117\13\2\2\2\u0117\u0118\b&\3\2\u0118")
        buf.write("L\3\2\2\2\u0119\u011a\13\2\2\2\u011aN\3\2\2\2\u011b\u011c")
        buf.write("\13\2\2\2\u011cP\3\2\2\2\16\2\u00da\u00e1\u00e6\u00ed")
        buf.write("\u00f1\u00f5\u00fa\u00fc\u0100\u0106\u010e\4\b\2\2\3&")
        buf.write("\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSE = 4
    FOR = 5
    TRUE = 6
    FALSE = 7
    INT = 8
    FLOAT = 9
    BOOL = 10
    STRING = 11
    RETURN = 12
    NULL = 13
    CLASS = 14
    CONSTRUCTOR = 15
    VAR = 16
    SELF = 17
    NEW = 18
    VOID = 19
    CONST = 20
    CONSTANT = 21
    FUNC = 22
    PLUS = 23
    MINUS = 24
    DOT = 25
    WS = 26
    INTEGER_LITERAL = 27
    FLOAT_LITERAL = 28
    BOOL_LITERAL = 29
    ID = 30
    ERROR_CHAR = 31
    UNCLOSE_STRING = 32
    ILLEGAL_ESCAPE = 33

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'constant'", "'func'", "'+'", "'-'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "CONSTANT", "FUNC", "PLUS", 
            "MINUS", "DOT", "WS", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOL_LITERAL", 
            "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "CONSTANT", "FUNC", "PLUS", "MINUS", "DOT", "WS", "INTEGER_LITERAL", 
                  "FLOAT_LITERAL", "BOOL_LITERAL", "ID", "SIGN", "DECIMAL", 
                  "EXPONENT", "UNDERSCORE", "DIGIT", "LETTER", "ERROR_CHAR", 
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
            actions[36] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


