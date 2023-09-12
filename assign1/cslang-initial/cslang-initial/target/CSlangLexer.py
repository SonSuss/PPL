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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u015b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\6)\u0117\n)\r)\16)\u0118\3)\3)\3*\6*\u011e")
        buf.write("\n*\r*\16*\u011f\3+\6+\u0123\n+\r+\16+\u0124\3+\3+\3+")
        buf.write("\3+\3+\5+\u012c\n+\3,\3,\5,\u0130\n,\3-\3-\5-\u0134\n")
        buf.write("-\3-\3-\3-\6-\u0139\n-\r-\16-\u013a\3.\3.\5.\u013f\n.")
        buf.write("\3/\3/\7/\u0143\n/\f/\16/\u0146\13/\3\60\3\60\3\60\6\60")
        buf.write("\u014b\n\60\r\60\16\60\u014c\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\2\2\67\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[\2]\2_\2a\2c\2e\2g/i\60k\61\3\2\6\5\2\13\f\17\17")
        buf.write("\"\"\4\2GGgg\3\2\62;\4\2C\\c|\2\u0161\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\3m\3\2\2\2\5s\3\2\2\2\7|\3\2\2\2\t\177\3\2\2\2\13\u0084")
        buf.write("\3\2\2\2\r\u0088\3\2\2\2\17\u008d\3\2\2\2\21\u0093\3\2")
        buf.write("\2\2\23\u0097\3\2\2\2\25\u009d\3\2\2\2\27\u00a2\3\2\2")
        buf.write("\2\31\u00a9\3\2\2\2\33\u00b0\3\2\2\2\35\u00b5\3\2\2\2")
        buf.write("\37\u00bb\3\2\2\2!\u00c7\3\2\2\2#\u00cb\3\2\2\2%\u00d0")
        buf.write("\3\2\2\2\'\u00d4\3\2\2\2)\u00d9\3\2\2\2+\u00df\3\2\2\2")
        buf.write("-\u00e8\3\2\2\2/\u00ed\3\2\2\2\61\u00ef\3\2\2\2\63\u00f2")
        buf.write("\3\2\2\2\65\u00f5\3\2\2\2\67\u00f8\3\2\2\29\u00fb\3\2")
        buf.write("\2\2;\u00fd\3\2\2\2=\u00ff\3\2\2\2?\u0102\3\2\2\2A\u0105")
        buf.write("\3\2\2\2C\u0107\3\2\2\2E\u0109\3\2\2\2G\u010b\3\2\2\2")
        buf.write("I\u010d\3\2\2\2K\u010f\3\2\2\2M\u0111\3\2\2\2O\u0113\3")
        buf.write("\2\2\2Q\u0116\3\2\2\2S\u011d\3\2\2\2U\u0122\3\2\2\2W\u012f")
        buf.write("\3\2\2\2Y\u0133\3\2\2\2[\u013e\3\2\2\2]\u0140\3\2\2\2")
        buf.write("_\u0147\3\2\2\2a\u014e\3\2\2\2c\u0150\3\2\2\2e\u0152\3")
        buf.write("\2\2\2g\u0154\3\2\2\2i\u0157\3\2\2\2k\u0159\3\2\2\2mn")
        buf.write("\7d\2\2no\7t\2\2op\7g\2\2pq\7c\2\2qr\7m\2\2r\4\3\2\2\2")
        buf.write("st\7e\2\2tu\7q\2\2uv\7p\2\2vw\7v\2\2wx\7k\2\2xy\7p\2\2")
        buf.write("yz\7w\2\2z{\7g\2\2{\6\3\2\2\2|}\7k\2\2}~\7h\2\2~\b\3\2")
        buf.write("\2\2\177\u0080\7g\2\2\u0080\u0081\7n\2\2\u0081\u0082\7")
        buf.write("u\2\2\u0082\u0083\7g\2\2\u0083\n\3\2\2\2\u0084\u0085\7")
        buf.write("h\2\2\u0085\u0086\7q\2\2\u0086\u0087\7t\2\2\u0087\f\3")
        buf.write("\2\2\2\u0088\u0089\7v\2\2\u0089\u008a\7t\2\2\u008a\u008b")
        buf.write("\7w\2\2\u008b\u008c\7g\2\2\u008c\16\3\2\2\2\u008d\u008e")
        buf.write("\7h\2\2\u008e\u008f\7c\2\2\u008f\u0090\7n\2\2\u0090\u0091")
        buf.write("\7u\2\2\u0091\u0092\7g\2\2\u0092\20\3\2\2\2\u0093\u0094")
        buf.write("\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096\7v\2\2\u0096\22")
        buf.write("\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099\7n\2\2\u0099\u009a")
        buf.write("\7q\2\2\u009a\u009b\7c\2\2\u009b\u009c\7v\2\2\u009c\24")
        buf.write("\3\2\2\2\u009d\u009e\7d\2\2\u009e\u009f\7q\2\2\u009f\u00a0")
        buf.write("\7q\2\2\u00a0\u00a1\7n\2\2\u00a1\26\3\2\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6")
        buf.write("\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7i\2\2\u00a8\30")
        buf.write("\3\2\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\32\3\2\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7n\2\2\u00b4\34")
        buf.write("\3\2\2\2\u00b5\u00b6\7e\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7c\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7u\2\2\u00ba\36")
        buf.write("\3\2\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7t\2\2\u00c6 \3")
        buf.write("\2\2\2\u00c7\u00c8\7x\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\"\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf\7h\2\2\u00cf$\3")
        buf.write("\2\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3")
        buf.write("\7y\2\2\u00d3&\3\2\2\2\u00d4\u00d5\7x\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7f\2\2\u00d8(\3")
        buf.write("\2\2\2\u00d9\u00da\7e\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7v\2\2\u00de*\3")
        buf.write("\2\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7u\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5")
        buf.write("\7c\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7v\2\2\u00e7,\3")
        buf.write("\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7e\2\2\u00ec.\3\2\2\2\u00ed\u00ee")
        buf.write("\7#\2\2\u00ee\60\3\2\2\2\u00ef\u00f0\7(\2\2\u00f0\u00f1")
        buf.write("\7(\2\2\u00f1\62\3\2\2\2\u00f2\u00f3\7~\2\2\u00f3\u00f4")
        buf.write("\7~\2\2\u00f4\64\3\2\2\2\u00f5\u00f6\7?\2\2\u00f6\u00f7")
        buf.write("\7?\2\2\u00f7\66\3\2\2\2\u00f8\u00f9\7#\2\2\u00f9\u00fa")
        buf.write("\7?\2\2\u00fa8\3\2\2\2\u00fb\u00fc\7>\2\2\u00fc:\3\2\2")
        buf.write("\2\u00fd\u00fe\7@\2\2\u00fe<\3\2\2\2\u00ff\u0100\7>\2")
        buf.write("\2\u0100\u0101\7?\2\2\u0101>\3\2\2\2\u0102\u0103\7@\2")
        buf.write("\2\u0103\u0104\7?\2\2\u0104@\3\2\2\2\u0105\u0106\7-\2")
        buf.write("\2\u0106B\3\2\2\2\u0107\u0108\7/\2\2\u0108D\3\2\2\2\u0109")
        buf.write("\u010a\7,\2\2\u010aF\3\2\2\2\u010b\u010c\7^\2\2\u010c")
        buf.write("H\3\2\2\2\u010d\u010e\7\'\2\2\u010eJ\3\2\2\2\u010f\u0110")
        buf.write("\7\61\2\2\u0110L\3\2\2\2\u0111\u0112\7`\2\2\u0112N\3\2")
        buf.write("\2\2\u0113\u0114\7\60\2\2\u0114P\3\2\2\2\u0115\u0117\t")
        buf.write("\2\2\2\u0116\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\b)\2\2\u011bR\3\2\2\2\u011c\u011e\5c\62\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120T\3\2\2\2\u0121\u0123\5c\62")
        buf.write("\2\u0122\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0122")
        buf.write("\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u012b\3\2\2\2\u0126")
        buf.write("\u012c\5]/\2\u0127\u012c\5_\60\2\u0128\u0129\5]/\2\u0129")
        buf.write("\u012a\5_\60\2\u012a\u012c\3\2\2\2\u012b\u0126\3\2\2\2")
        buf.write("\u012b\u0127\3\2\2\2\u012b\u0128\3\2\2\2\u012cV\3\2\2")
        buf.write("\2\u012d\u0130\5\r\7\2\u012e\u0130\5\17\b\2\u012f\u012d")
        buf.write("\3\2\2\2\u012f\u012e\3\2\2\2\u0130X\3\2\2\2\u0131\u0134")
        buf.write("\5e\63\2\u0132\u0134\5a\61\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0138\3\2\2\2\u0135\u0139\5e\63\2")
        buf.write("\u0136\u0139\5c\62\2\u0137\u0139\5a\61\2\u0138\u0135\3")
        buf.write("\2\2\2\u0138\u0136\3\2\2\2\u0138\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("Z\3\2\2\2\u013c\u013f\5A!\2\u013d\u013f\5C\"\2\u013e\u013c")
        buf.write("\3\2\2\2\u013e\u013d\3\2\2\2\u013f\\\3\2\2\2\u0140\u0144")
        buf.write("\5O(\2\u0141\u0143\5c\62\2\u0142\u0141\3\2\2\2\u0143\u0146")
        buf.write("\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145")
        buf.write("^\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\t\3\2\2\u0148")
        buf.write("\u014a\5[.\2\u0149\u014b\5c\62\2\u014a\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2")
        buf.write("\u014d`\3\2\2\2\u014e\u014f\7a\2\2\u014fb\3\2\2\2\u0150")
        buf.write("\u0151\t\4\2\2\u0151d\3\2\2\2\u0152\u0153\t\5\2\2\u0153")
        buf.write("f\3\2\2\2\u0154\u0155\13\2\2\2\u0155\u0156\b\64\3\2\u0156")
        buf.write("h\3\2\2\2\u0157\u0158\13\2\2\2\u0158j\3\2\2\2\u0159\u015a")
        buf.write("\13\2\2\2\u015al\3\2\2\2\16\2\u0118\u011f\u0124\u012b")
        buf.write("\u012f\u0133\u0138\u013a\u013e\u0144\u014c\4\b\2\2\3\64")
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
    NOT = 23
    AND = 24
    OR = 25
    EQUAL = 26
    NOT_EQUAL = 27
    LESS = 28
    GREATER = 29
    LESS_EQUAL = 30
    GREATER_EQUAL = 31
    PLUS = 32
    MINUS = 33
    MULTIPLY = 34
    DIVIDE_I = 35
    DIVIDE_I_L = 36
    DIVIDE_F = 37
    STRING_CONCAT = 38
    DOT = 39
    WS = 40
    INTEGER_LITERAL = 41
    FLOAT_LITERAL = 42
    BOOL_LITERAL = 43
    ID = 44
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'constant'", "'func'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", 
            "'-'", "'*'", "'\\'", "'%'", "'/'", "'^'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "CONSTANT", "FUNC", "NOT", 
            "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", 
            "GREATER_EQUAL", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", 
            "DIVIDE_F", "STRING_CONCAT", "DOT", "WS", "INTEGER_LITERAL", 
            "FLOAT_LITERAL", "BOOL_LITERAL", "ID", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "CONSTANT", "FUNC", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "PLUS", 
                  "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", 
                  "STRING_CONCAT", "DOT", "WS", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                  "BOOL_LITERAL", "ID", "SIGN", "DECIMAL", "EXPONENT", "UNDERSCORE", 
                  "DIGIT", "LETTER", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[50] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


