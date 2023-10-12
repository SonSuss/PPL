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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u024c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\7\n\u00fa\n\n\f\n\16\n\u00fd\13\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\7\13\u0108\n\13\f\13\16\13\u010b")
        buf.write("\13\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+")
        buf.write("\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3?\3@\3@\3@\7@\u01d9\n@\f@\16@\u01dc\13@\3@\3@\3@\3A")
        buf.write("\3A\7A\u01e3\nA\fA\16A\u01e6\13A\3B\6B\u01e9\nB\rB\16")
        buf.write("B\u01ea\3B\3B\3B\3B\3B\5B\u01f2\nB\3C\3C\7C\u01f6\nC\f")
        buf.write("C\16C\u01f9\13C\3D\6D\u01fc\nD\rD\16D\u01fd\3E\3E\5E\u0202")
        buf.write("\nE\3F\3F\7F\u0206\nF\fF\16F\u0209\13F\3G\3G\5G\u020d")
        buf.write("\nG\3G\6G\u0210\nG\rG\16G\u0211\3H\3H\3I\3I\3I\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0224\nI\3J\3J\3J\5J\u0229")
        buf.write("\nJ\3K\6K\u022c\nK\rK\16K\u022d\3K\3K\3L\3L\3L\3M\3M\3")
        buf.write("M\7M\u0238\nM\fM\16M\u023b\13M\3M\5M\u023e\nM\3M\3M\3")
        buf.write("N\3N\3N\7N\u0245\nN\fN\16N\u0248\13N\3N\3N\3N\3\u00fb")
        buf.write("\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089\2")
        buf.write("\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095F\u0097")
        buf.write("G\u0099H\u009bI\3\2\r\7\2\f\f\17\17GHQQ~~\4\2\f\f\17\17")
        buf.write("\6\2\n\f\16\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3")
        buf.write("\2\62;\4\2GGgg\7\2ddhhppttvv\5\2\13\f\17\17\"\"\5\3\n")
        buf.write("\f\16\17\"\"\2\u025f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\3\u009d\3\2\2\2\5\u00a6\3\2\2\2\7\u00b0")
        buf.write("\3\2\2\2\t\u00bb\3\2\2\2\13\u00c7\3\2\2\2\r\u00d1\3\2")
        buf.write("\2\2\17\u00dc\3\2\2\2\21\u00e8\3\2\2\2\23\u00f5\3\2\2")
        buf.write("\2\25\u0103\3\2\2\2\27\u0110\3\2\2\2\31\u0116\3\2\2\2")
        buf.write("\33\u011f\3\2\2\2\35\u0122\3\2\2\2\37\u0127\3\2\2\2!\u012b")
        buf.write("\3\2\2\2#\u0130\3\2\2\2%\u0136\3\2\2\2\'\u013a\3\2\2\2")
        buf.write(")\u0140\3\2\2\2+\u0145\3\2\2\2-\u014c\3\2\2\2/\u0153\3")
        buf.write("\2\2\2\61\u0158\3\2\2\2\63\u015e\3\2\2\2\65\u016a\3\2")
        buf.write("\2\2\67\u016e\3\2\2\29\u0173\3\2\2\2;\u0177\3\2\2\2=\u017c")
        buf.write("\3\2\2\2?\u0182\3\2\2\2A\u018b\3\2\2\2C\u0190\3\2\2\2")
        buf.write("E\u0192\3\2\2\2G\u0195\3\2\2\2I\u0198\3\2\2\2K\u019b\3")
        buf.write("\2\2\2M\u019e\3\2\2\2O\u01a0\3\2\2\2Q\u01a2\3\2\2\2S\u01a5")
        buf.write("\3\2\2\2U\u01a8\3\2\2\2W\u01aa\3\2\2\2Y\u01ad\3\2\2\2")
        buf.write("[\u01af\3\2\2\2]\u01b1\3\2\2\2_\u01b3\3\2\2\2a\u01b5\3")
        buf.write("\2\2\2c\u01b7\3\2\2\2e\u01b9\3\2\2\2g\u01bc\3\2\2\2i\u01be")
        buf.write("\3\2\2\2k\u01c0\3\2\2\2m\u01c2\3\2\2\2o\u01c4\3\2\2\2")
        buf.write("q\u01c6\3\2\2\2s\u01c8\3\2\2\2u\u01ca\3\2\2\2w\u01cc\3")
        buf.write("\2\2\2y\u01ce\3\2\2\2{\u01d0\3\2\2\2}\u01d2\3\2\2\2\177")
        buf.write("\u01d5\3\2\2\2\u0081\u01e0\3\2\2\2\u0083\u01e8\3\2\2\2")
        buf.write("\u0085\u01f3\3\2\2\2\u0087\u01fb\3\2\2\2\u0089\u0201\3")
        buf.write("\2\2\2\u008b\u0203\3\2\2\2\u008d\u020a\3\2\2\2\u008f\u0213")
        buf.write("\3\2\2\2\u0091\u0223\3\2\2\2\u0093\u0228\3\2\2\2\u0095")
        buf.write("\u022b\3\2\2\2\u0097\u0231\3\2\2\2\u0099\u0234\3\2\2\2")
        buf.write("\u009b\u0241\3\2\2\2\u009d\u009e\7B\2\2\u009e\u009f\7")
        buf.write("t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2")
        buf.write("\7f\2\2\u00a2\u00a3\7K\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\4\3\2\2\2\u00a6\u00a7\7B\2\2\u00a7\u00a8")
        buf.write("\7y\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7K\2\2\u00ad\u00ae")
        buf.write("\7p\2\2\u00ae\u00af\7v\2\2\u00af\6\3\2\2\2\u00b0\u00b1")
        buf.write("\7B\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4")
        buf.write("\7c\2\2\u00b4\u00b5\7f\2\2\u00b5\u00b6\7H\2\2\u00b6\u00b7")
        buf.write("\7n\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\b\3\2\2\2\u00bb\u00bc\7B\2\2\u00bc\u00bd")
        buf.write("\7y\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7H\2\2\u00c2\u00c3")
        buf.write("\7n\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\n\3\2\2\2\u00c7\u00c8\7B\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc")
        buf.write("\7f\2\2\u00cc\u00cd\7D\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7q\2\2\u00cf\u00d0\7n\2\2\u00d0\f\3\2\2\2\u00d1\u00d2")
        buf.write("\7B\2\2\u00d2\u00d3\7y\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7D\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\16\3\2\2\2\u00dc\u00dd\7B\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7f\2\2\u00e1\u00e2\7U\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7i\2\2\u00e7\20\3\2\2\2\u00e8\u00e9\7B\2\2\u00e9\u00ea")
        buf.write("\7y\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7U\2\2\u00ef\u00f0")
        buf.write("\7v\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\u00f4\7i\2\2\u00f4\22\3\2\2\2\u00f5\u00f6")
        buf.write("\7\61\2\2\u00f6\u00f7\7,\2\2\u00f7\u00fb\3\2\2\2\u00f8")
        buf.write("\u00fa\13\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd\3\2\2")
        buf.write("\2\u00fb\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fe")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff")
        buf.write("\u0100\7\61\2\2\u0100\u0101\3\2\2\2\u0101\u0102\b\n\2")
        buf.write("\2\u0102\24\3\2\2\2\u0103\u0104\7\61\2\2\u0104\u0105\7")
        buf.write("\61\2\2\u0105\u0109\3\2\2\2\u0106\u0108\n\2\2\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u0109\3")
        buf.write("\2\2\2\u010c\u010d\t\3\2\2\u010d\u010e\3\2\2\2\u010e\u010f")
        buf.write("\b\13\2\2\u010f\26\3\2\2\2\u0110\u0111\7d\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7g\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7m\2\2\u0115\30\3\2\2\2\u0116\u0117\7e\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\u0119\7p\2\2\u0119\u011a\7v\2\2\u011a\u011b")
        buf.write("\7k\2\2\u011b\u011c\7p\2\2\u011c\u011d\7w\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011e\32\3\2\2\2\u011f\u0120\7k\2\2\u0120\u0121")
        buf.write("\7h\2\2\u0121\34\3\2\2\2\u0122\u0123\7g\2\2\u0123\u0124")
        buf.write("\7n\2\2\u0124\u0125\7u\2\2\u0125\u0126\7g\2\2\u0126\36")
        buf.write("\3\2\2\2\u0127\u0128\7h\2\2\u0128\u0129\7q\2\2\u0129\u012a")
        buf.write("\7t\2\2\u012a \3\2\2\2\u012b\u012c\7v\2\2\u012c\u012d")
        buf.write("\7t\2\2\u012d\u012e\7w\2\2\u012e\u012f\7g\2\2\u012f\"")
        buf.write("\3\2\2\2\u0130\u0131\7h\2\2\u0131\u0132\7c\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\u0134\7u\2\2\u0134\u0135\7g\2\2\u0135$\3")
        buf.write("\2\2\2\u0136\u0137\7k\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7v\2\2\u0139&\3\2\2\2\u013a\u013b\7h\2\2\u013b\u013c")
        buf.write("\7n\2\2\u013c\u013d\7q\2\2\u013d\u013e\7c\2\2\u013e\u013f")
        buf.write("\7v\2\2\u013f(\3\2\2\2\u0140\u0141\7d\2\2\u0141\u0142")
        buf.write("\7q\2\2\u0142\u0143\7q\2\2\u0143\u0144\7n\2\2\u0144*\3")
        buf.write("\2\2\2\u0145\u0146\7u\2\2\u0146\u0147\7v\2\2\u0147\u0148")
        buf.write("\7t\2\2\u0148\u0149\7k\2\2\u0149\u014a\7p\2\2\u014a\u014b")
        buf.write("\7i\2\2\u014b,\3\2\2\2\u014c\u014d\7t\2\2\u014d\u014e")
        buf.write("\7g\2\2\u014e\u014f\7v\2\2\u014f\u0150\7w\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151\u0152\7p\2\2\u0152.\3\2\2\2\u0153\u0154")
        buf.write("\7p\2\2\u0154\u0155\7w\2\2\u0155\u0156\7n\2\2\u0156\u0157")
        buf.write("\7n\2\2\u0157\60\3\2\2\2\u0158\u0159\7e\2\2\u0159\u015a")
        buf.write("\7n\2\2\u015a\u015b\7c\2\2\u015b\u015c\7u\2\2\u015c\u015d")
        buf.write("\7u\2\2\u015d\62\3\2\2\2\u015e\u015f\7e\2\2\u015f\u0160")
        buf.write("\7q\2\2\u0160\u0161\7p\2\2\u0161\u0162\7u\2\2\u0162\u0163")
        buf.write("\7v\2\2\u0163\u0164\7t\2\2\u0164\u0165\7w\2\2\u0165\u0166")
        buf.write("\7e\2\2\u0166\u0167\7v\2\2\u0167\u0168\7q\2\2\u0168\u0169")
        buf.write("\7t\2\2\u0169\64\3\2\2\2\u016a\u016b\7x\2\2\u016b\u016c")
        buf.write("\7c\2\2\u016c\u016d\7t\2\2\u016d\66\3\2\2\2\u016e\u016f")
        buf.write("\7u\2\2\u016f\u0170\7g\2\2\u0170\u0171\7n\2\2\u0171\u0172")
        buf.write("\7h\2\2\u01728\3\2\2\2\u0173\u0174\7p\2\2\u0174\u0175")
        buf.write("\7g\2\2\u0175\u0176\7y\2\2\u0176:\3\2\2\2\u0177\u0178")
        buf.write("\7x\2\2\u0178\u0179\7q\2\2\u0179\u017a\7k\2\2\u017a\u017b")
        buf.write("\7f\2\2\u017b<\3\2\2\2\u017c\u017d\7e\2\2\u017d\u017e")
        buf.write("\7q\2\2\u017e\u017f\7p\2\2\u017f\u0180\7u\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181>\3\2\2\2\u0182\u0183\7e\2\2\u0183\u0184")
        buf.write("\7q\2\2\u0184\u0185\7p\2\2\u0185\u0186\7u\2\2\u0186\u0187")
        buf.write("\7v\2\2\u0187\u0188\7c\2\2\u0188\u0189\7p\2\2\u0189\u018a")
        buf.write("\7v\2\2\u018a@\3\2\2\2\u018b\u018c\7h\2\2\u018c\u018d")
        buf.write("\7w\2\2\u018d\u018e\7p\2\2\u018e\u018f\7e\2\2\u018fB\3")
        buf.write("\2\2\2\u0190\u0191\7#\2\2\u0191D\3\2\2\2\u0192\u0193\7")
        buf.write("(\2\2\u0193\u0194\7(\2\2\u0194F\3\2\2\2\u0195\u0196\7")
        buf.write("~\2\2\u0196\u0197\7~\2\2\u0197H\3\2\2\2\u0198\u0199\7")
        buf.write("?\2\2\u0199\u019a\7?\2\2\u019aJ\3\2\2\2\u019b\u019c\7")
        buf.write("#\2\2\u019c\u019d\7?\2\2\u019dL\3\2\2\2\u019e\u019f\7")
        buf.write(">\2\2\u019fN\3\2\2\2\u01a0\u01a1\7@\2\2\u01a1P\3\2\2\2")
        buf.write("\u01a2\u01a3\7>\2\2\u01a3\u01a4\7?\2\2\u01a4R\3\2\2\2")
        buf.write("\u01a5\u01a6\7@\2\2\u01a6\u01a7\7?\2\2\u01a7T\3\2\2\2")
        buf.write("\u01a8\u01a9\7?\2\2\u01a9V\3\2\2\2\u01aa\u01ab\7<\2\2")
        buf.write("\u01ab\u01ac\7?\2\2\u01acX\3\2\2\2\u01ad\u01ae\7-\2\2")
        buf.write("\u01aeZ\3\2\2\2\u01af\u01b0\7/\2\2\u01b0\\\3\2\2\2\u01b1")
        buf.write("\u01b2\7,\2\2\u01b2^\3\2\2\2\u01b3\u01b4\7^\2\2\u01b4")
        buf.write("`\3\2\2\2\u01b5\u01b6\7\'\2\2\u01b6b\3\2\2\2\u01b7\u01b8")
        buf.write("\7\61\2\2\u01b8d\3\2\2\2\u01b9\u01ba\7>\2\2\u01ba\u01bb")
        buf.write("\7/\2\2\u01bbf\3\2\2\2\u01bc\u01bd\7`\2\2\u01bdh\3\2\2")
        buf.write("\2\u01be\u01bf\7\60\2\2\u01bfj\3\2\2\2\u01c0\u01c1\7.")
        buf.write("\2\2\u01c1l\3\2\2\2\u01c2\u01c3\7=\2\2\u01c3n\3\2\2\2")
        buf.write("\u01c4\u01c5\7<\2\2\u01c5p\3\2\2\2\u01c6\u01c7\7+\2\2")
        buf.write("\u01c7r\3\2\2\2\u01c8\u01c9\7*\2\2\u01c9t\3\2\2\2\u01ca")
        buf.write("\u01cb\7]\2\2\u01cbv\3\2\2\2\u01cc\u01cd\7_\2\2\u01cd")
        buf.write("x\3\2\2\2\u01ce\u01cf\7}\2\2\u01cfz\3\2\2\2\u01d0\u01d1")
        buf.write("\7\177\2\2\u01d1|\3\2\2\2\u01d2\u01d3\7B\2\2\u01d3\u01d4")
        buf.write("\5\u0081A\2\u01d4~\3\2\2\2\u01d5\u01da\7$\2\2\u01d6\u01d9")
        buf.write("\5\u0091I\2\u01d7\u01d9\n\4\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dd\u01de\7$\2\2\u01de\u01df\b@\3\2\u01df\u0080")
        buf.write("\3\2\2\2\u01e0\u01e4\t\5\2\2\u01e1\u01e3\t\6\2\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e4\u01e5\3\2\2\2\u01e5\u0082\3\2\2\2\u01e6\u01e4\3")
        buf.write("\2\2\2\u01e7\u01e9\5\u008fH\2\u01e8\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u01f1\3\2\2\2\u01ec\u01f2\5\u008bF\2\u01ed\u01f2")
        buf.write("\5\u008dG\2\u01ee\u01ef\5\u008bF\2\u01ef\u01f0\5\u008d")
        buf.write("G\2\u01f0\u01f2\3\2\2\2\u01f1\u01ec\3\2\2\2\u01f1\u01ed")
        buf.write("\3\2\2\2\u01f1\u01ee\3\2\2\2\u01f2\u0084\3\2\2\2\u01f3")
        buf.write("\u01f7\t\7\2\2\u01f4\u01f6\t\b\2\2\u01f5\u01f4\3\2\2\2")
        buf.write("\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3")
        buf.write("\2\2\2\u01f8\u0086\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fc")
        buf.write("\5\u008fH\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0088\3\2\2\2")
        buf.write("\u01ff\u0202\5Y-\2\u0200\u0202\5[.\2\u0201\u01ff\3\2\2")
        buf.write("\2\u0201\u0200\3\2\2\2\u0202\u008a\3\2\2\2\u0203\u0207")
        buf.write("\5i\65\2\u0204\u0206\5\u008fH\2\u0205\u0204\3\2\2\2\u0206")
        buf.write("\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208\u008c\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u020c\t")
        buf.write("\t\2\2\u020b\u020d\5\u0089E\2\u020c\u020b\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u0210\5\u008f")
        buf.write("H\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u008e\3\2\2\2\u0213")
        buf.write("\u0214\t\b\2\2\u0214\u0090\3\2\2\2\u0215\u0216\7^\2\2")
        buf.write("\u0216\u0224\7^\2\2\u0217\u0218\7^\2\2\u0218\u0224\7d")
        buf.write("\2\2\u0219\u021a\7^\2\2\u021a\u0224\7h\2\2\u021b\u021c")
        buf.write("\7^\2\2\u021c\u0224\7t\2\2\u021d\u021e\7^\2\2\u021e\u0224")
        buf.write("\7p\2\2\u021f\u0220\7^\2\2\u0220\u0224\7v\2\2\u0221\u0222")
        buf.write("\7^\2\2\u0222\u0224\7$\2\2\u0223\u0215\3\2\2\2\u0223\u0217")
        buf.write("\3\2\2\2\u0223\u0219\3\2\2\2\u0223\u021b\3\2\2\2\u0223")
        buf.write("\u021d\3\2\2\2\u0223\u021f\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0224\u0092\3\2\2\2\u0225\u0226\7^\2\2\u0226\u0229\n")
        buf.write("\n\2\2\u0227\u0229\7^\2\2\u0228\u0225\3\2\2\2\u0228\u0227")
        buf.write("\3\2\2\2\u0229\u0094\3\2\2\2\u022a\u022c\t\13\2\2\u022b")
        buf.write("\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022b\3\2\2\2")
        buf.write("\u022d\u022e\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\b")
        buf.write("K\2\2\u0230\u0096\3\2\2\2\u0231\u0232\13\2\2\2\u0232\u0233")
        buf.write("\bL\4\2\u0233\u0098\3\2\2\2\u0234\u0239\7$\2\2\u0235\u0238")
        buf.write("\5\u0091I\2\u0236\u0238\n\4\2\2\u0237\u0235\3\2\2\2\u0237")
        buf.write("\u0236\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u0239\u023a\3\2\2\2\u023a\u023d\3\2\2\2\u023b\u0239\3")
        buf.write("\2\2\2\u023c\u023e\t\f\2\2\u023d\u023c\3\2\2\2\u023e\u023f")
        buf.write("\3\2\2\2\u023f\u0240\bM\5\2\u0240\u009a\3\2\2\2\u0241")
        buf.write("\u0246\7$\2\2\u0242\u0245\5\u0091I\2\u0243\u0245\n\4\2")
        buf.write("\2\u0244\u0242\3\2\2\2\u0244\u0243\3\2\2\2\u0245\u0248")
        buf.write("\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247")
        buf.write("\u0249\3\2\2\2\u0248\u0246\3\2\2\2\u0249\u024a\5\u0093")
        buf.write("J\2\u024a\u024b\bN\6\2\u024b\u009c\3\2\2\2\30\2\u00fb")
        buf.write("\u0109\u01d8\u01da\u01e4\u01ea\u01f1\u01f7\u01fd\u0201")
        buf.write("\u0207\u020c\u0211\u0223\u0228\u022d\u0237\u0239\u023d")
        buf.write("\u0244\u0246\7\b\2\2\3@\2\3L\3\3M\4\3N\5")
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
    T__6 = 7
    T__7 = 8
    BLOCK_COMMENT = 9
    LINE_COMMENT = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSE = 14
    FOR = 15
    TRUE = 16
    FALSE = 17
    INT = 18
    FLOAT = 19
    BOOL = 20
    STRING = 21
    RETURN = 22
    NULL = 23
    CLASS = 24
    CONSTRUCTOR = 25
    VAR = 26
    SELF = 27
    NEW = 28
    VOID = 29
    CONST = 30
    CONSTANT = 31
    FUNC = 32
    NOT = 33
    AND = 34
    OR = 35
    EQUAL = 36
    NOT_EQUAL = 37
    LESS = 38
    GREATER = 39
    LESS_EQUAL = 40
    GREATER_EQUAL = 41
    INITIAL = 42
    ASSIGN = 43
    PLUS = 44
    MINUS = 45
    MULTIPLY = 46
    DIVIDE_I = 47
    DIVIDE_I_L = 48
    DIVIDE_F = 49
    SUPER_CLASS = 50
    STRING_CONCAT = 51
    DOT = 52
    COMMA = 53
    SEMICOLON = 54
    COLON = 55
    RPAREN = 56
    LPAREN = 57
    LBRACK = 58
    RBRACK = 59
    LBRASE = 60
    RBRASE = 61
    AT_ID = 62
    STRING_LITERAL = 63
    ID = 64
    FLOAT_LITERAL = 65
    NON_ZERO_INT = 66
    INT_LITERAL = 67
    WS = 68
    ERROR_CHAR = 69
    UNCLOSE_STRING = 70
    ILLEGAL_ESCAPE = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'@readInt'", "'@writeInt'", "'@readFloat'", "'@writeFloat'", 
            "'@readBool'", "'@writeBool'", "'@readString'", "'@writeString'", 
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'constant'", "'func'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
            "':='", "'+'", "'-'", "'*'", "'\\'", "'%'", "'/'", "'<-'", "'^'", 
            "'.'", "','", "';'", "':'", "')'", "'('", "'['", "']'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
            "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
            "VOID", "CONST", "CONSTANT", "FUNC", "NOT", "AND", "OR", "EQUAL", 
            "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
            "INITIAL", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", 
            "DIVIDE_I_L", "DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", "DOT", 
            "COMMA", "SEMICOLON", "COLON", "RPAREN", "LPAREN", "LBRACK", 
            "RBRACK", "LBRASE", "RBRASE", "AT_ID", "STRING_LITERAL", "ID", 
            "FLOAT_LITERAL", "NON_ZERO_INT", "INT_LITERAL", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                  "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                  "VAR", "SELF", "NEW", "VOID", "CONST", "CONSTANT", "FUNC", 
                  "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
                  "LESS_EQUAL", "GREATER_EQUAL", "INITIAL", "ASSIGN", "PLUS", 
                  "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", 
                  "SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", 
                  "COLON", "RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", 
                  "RBRASE", "AT_ID", "STRING_LITERAL", "ID", "FLOAT_LITERAL", 
                  "NON_ZERO_INT", "INT_LITERAL", "SIGN", "DECIMAL", "EXPONENT", 
                  "DIGIT", "ESC_SEQ", "ILL_ESQ", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[62] = self.STRING_LITERAL_action 
            actions[74] = self.ERROR_CHAR_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            unclose_string= str(self.text);
            whatif =['\b', '\t', '\f', '\n', '\r', '\\']
            if unclose_string[-1] in whatif:
                raise UncloseString(unclose_string[1:-1])
            else:
                raise UncloseString(unclose_string[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            raise IllegalEscape(self.text[1:])

     


