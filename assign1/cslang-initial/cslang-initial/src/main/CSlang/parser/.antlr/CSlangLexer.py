# Generated from e:\hocbaidcm\PPL\assignment\assign1\cslang-initial\cslang-initial\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u025d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\7\13\u0108\n\13\f\13\16\13\u010b\13\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0116\n\f\f\f\16")
        buf.write("\f\u0119\13\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\3A\3A\7A\u01ea\nA\fA\16A\u01ed\13A\3A\3")
        buf.write("A\3A\3B\5B\u01f3\nB\3B\3B\7B\u01f7\nB\fB\16B\u01fa\13")
        buf.write("B\3C\6C\u01fd\nC\rC\16C\u01fe\3C\3C\3C\3C\3C\5C\u0206")
        buf.write("\nC\3D\6D\u0209\nD\rD\16D\u020a\3E\3E\5E\u020f\nE\3F\3")
        buf.write("F\5F\u0213\nF\3G\3G\7G\u0217\nG\fG\16G\u021a\13G\3H\3")
        buf.write("H\5H\u021e\nH\3H\6H\u0221\nH\rH\16H\u0222\3I\3I\3J\3J")
        buf.write("\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u0235\nJ\3K\3")
        buf.write("K\3K\5K\u023a\nK\3L\6L\u023d\nL\rL\16L\u023e\3L\3L\3M")
        buf.write("\3M\3M\3N\3N\3N\7N\u0249\nN\fN\16N\u024c\13N\3N\5N\u024f")
        buf.write("\nN\3N\3N\3O\3O\3O\7O\u0256\nO\fO\16O\u0259\13O\3O\3O")
        buf.write("\3O\3\u0109\2P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097G\u0099H\u009bI\u009dJ\3\2\r\7\2\f\f\17\17GHQ")
        buf.write("Q~~\4\2\f\f\17\17\5\2\f\f\17\17$$\5\2C\\aac|\6\2\62;C")
        buf.write("\\aac|\4\2GGgg\3\2\62;\7\2ddhhppttvv\5\2\13\f\17\17\"")
        buf.write("\"\6\2\n\f\16\17$$^^\5\3\n\f\16\17\"\"\2\u0271\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\3\u009f\3\2\2\2\5\u00a3\3\2\2\2\7\u00ae\3\2\2")
        buf.write("\2\t\u00b8\3\2\2\2\13\u00c5\3\2\2\2\r\u00d1\3\2\2\2\17")
        buf.write("\u00dd\3\2\2\2\21\u00e8\3\2\2\2\23\u00f6\3\2\2\2\25\u0103")
        buf.write("\3\2\2\2\27\u0111\3\2\2\2\31\u011e\3\2\2\2\33\u0124\3")
        buf.write("\2\2\2\35\u012d\3\2\2\2\37\u0130\3\2\2\2!\u0135\3\2\2")
        buf.write("\2#\u0139\3\2\2\2%\u013e\3\2\2\2\'\u0144\3\2\2\2)\u0148")
        buf.write("\3\2\2\2+\u014e\3\2\2\2-\u0153\3\2\2\2/\u015a\3\2\2\2")
        buf.write("\61\u0161\3\2\2\2\63\u0166\3\2\2\2\65\u016c\3\2\2\2\67")
        buf.write("\u0178\3\2\2\29\u017c\3\2\2\2;\u0181\3\2\2\2=\u0185\3")
        buf.write("\2\2\2?\u018a\3\2\2\2A\u0190\3\2\2\2C\u0199\3\2\2\2E\u019e")
        buf.write("\3\2\2\2G\u01a4\3\2\2\2I\u01a6\3\2\2\2K\u01a9\3\2\2\2")
        buf.write("M\u01ac\3\2\2\2O\u01af\3\2\2\2Q\u01b2\3\2\2\2S\u01b4\3")
        buf.write("\2\2\2U\u01b6\3\2\2\2W\u01b9\3\2\2\2Y\u01bc\3\2\2\2[\u01be")
        buf.write("\3\2\2\2]\u01c1\3\2\2\2_\u01c3\3\2\2\2a\u01c5\3\2\2\2")
        buf.write("c\u01c7\3\2\2\2e\u01c9\3\2\2\2g\u01cb\3\2\2\2i\u01cd\3")
        buf.write("\2\2\2k\u01d0\3\2\2\2m\u01d2\3\2\2\2o\u01d4\3\2\2\2q\u01d6")
        buf.write("\3\2\2\2s\u01d8\3\2\2\2u\u01da\3\2\2\2w\u01dc\3\2\2\2")
        buf.write("y\u01de\3\2\2\2{\u01e0\3\2\2\2}\u01e2\3\2\2\2\177\u01e4")
        buf.write("\3\2\2\2\u0081\u01e6\3\2\2\2\u0083\u01f2\3\2\2\2\u0085")
        buf.write("\u01fc\3\2\2\2\u0087\u0208\3\2\2\2\u0089\u020e\3\2\2\2")
        buf.write("\u008b\u0212\3\2\2\2\u008d\u0214\3\2\2\2\u008f\u021b\3")
        buf.write("\2\2\2\u0091\u0224\3\2\2\2\u0093\u0234\3\2\2\2\u0095\u0239")
        buf.write("\3\2\2\2\u0097\u023c\3\2\2\2\u0099\u0242\3\2\2\2\u009b")
        buf.write("\u0245\3\2\2\2\u009d\u0252\3\2\2\2\u009f\u00a0\7k\2\2")
        buf.write("\u00a0\u00a1\7q\2\2\u00a1\u00a2\7\60\2\2\u00a2\4\3\2\2")
        buf.write("\2\u00a3\u00a4\7B\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7")
        buf.write("g\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7f\2\2\u00a8\u00a9")
        buf.write("\7K\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac")
        buf.write("\7*\2\2\u00ac\u00ad\7+\2\2\u00ad\6\3\2\2\2\u00ae\u00af")
        buf.write("\7B\2\2\u00af\u00b0\7y\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\7k\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7K\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7\7v\2\2\u00b7\b")
        buf.write("\3\2\2\2\u00b8\u00b9\7B\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7f\2\2\u00bd\u00be")
        buf.write("\7H\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7*\2\2\u00c3\u00c4")
        buf.write("\7+\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\7B\2\2\u00c6\u00c7")
        buf.write("\7y\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7H\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\f\3\2\2\2\u00d1\u00d2\7B\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7f\2\2\u00d6\u00d7\7D\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7*\2\2\u00db\u00dc")
        buf.write("\7+\2\2\u00dc\16\3\2\2\2\u00dd\u00de\7B\2\2\u00de\u00df")
        buf.write("\7y\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7D\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7n\2\2\u00e7\20")
        buf.write("\3\2\2\2\u00e8\u00e9\7B\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7f\2\2\u00ed\u00ee")
        buf.write("\7U\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7i\2\2\u00f3\u00f4")
        buf.write("\7*\2\2\u00f4\u00f5\7+\2\2\u00f5\22\3\2\2\2\u00f6\u00f7")
        buf.write("\7B\2\2\u00f7\u00f8\7y\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7U\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7i\2\2\u0102\24")
        buf.write("\3\2\2\2\u0103\u0104\7\61\2\2\u0104\u0105\7,\2\2\u0105")
        buf.write("\u0109\3\2\2\2\u0106\u0108\13\2\2\2\u0107\u0106\3\2\2")
        buf.write("\2\u0108\u010b\3\2\2\2\u0109\u010a\3\2\2\2\u0109\u0107")
        buf.write("\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u0109\3\2\2\2\u010c")
        buf.write("\u010d\7,\2\2\u010d\u010e\7\61\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\b\13\2\2\u0110\26\3\2\2\2\u0111\u0112\7\61")
        buf.write("\2\2\u0112\u0113\7\61\2\2\u0113\u0117\3\2\2\2\u0114\u0116")
        buf.write("\n\2\2\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a\3\2\2\2")
        buf.write("\u0119\u0117\3\2\2\2\u011a\u011b\t\3\2\2\u011b\u011c\3")
        buf.write("\2\2\2\u011c\u011d\b\f\2\2\u011d\30\3\2\2\2\u011e\u011f")
        buf.write("\7d\2\2\u011f\u0120\7t\2\2\u0120\u0121\7g\2\2\u0121\u0122")
        buf.write("\7c\2\2\u0122\u0123\7m\2\2\u0123\32\3\2\2\2\u0124\u0125")
        buf.write("\7e\2\2\u0125\u0126\7q\2\2\u0126\u0127\7p\2\2\u0127\u0128")
        buf.write("\7v\2\2\u0128\u0129\7k\2\2\u0129\u012a\7p\2\2\u012a\u012b")
        buf.write("\7w\2\2\u012b\u012c\7g\2\2\u012c\34\3\2\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7h\2\2\u012f\36\3\2\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\u0132\7n\2\2\u0132\u0133\7u\2\2\u0133\u0134")
        buf.write("\7g\2\2\u0134 \3\2\2\2\u0135\u0136\7h\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7t\2\2\u0138\"\3\2\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013a\u013b\7t\2\2\u013b\u013c\7w\2\2\u013c\u013d")
        buf.write("\7g\2\2\u013d$\3\2\2\2\u013e\u013f\7h\2\2\u013f\u0140")
        buf.write("\7c\2\2\u0140\u0141\7n\2\2\u0141\u0142\7u\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143&\3\2\2\2\u0144\u0145\7k\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146\u0147\7v\2\2\u0147(\3\2\2\2\u0148\u0149")
        buf.write("\7h\2\2\u0149\u014a\7n\2\2\u014a\u014b\7q\2\2\u014b\u014c")
        buf.write("\7c\2\2\u014c\u014d\7v\2\2\u014d*\3\2\2\2\u014e\u014f")
        buf.write("\7d\2\2\u014f\u0150\7q\2\2\u0150\u0151\7q\2\2\u0151\u0152")
        buf.write("\7n\2\2\u0152,\3\2\2\2\u0153\u0154\7u\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155\u0156\7t\2\2\u0156\u0157\7k\2\2\u0157\u0158")
        buf.write("\7p\2\2\u0158\u0159\7i\2\2\u0159.\3\2\2\2\u015a\u015b")
        buf.write("\7t\2\2\u015b\u015c\7g\2\2\u015c\u015d\7v\2\2\u015d\u015e")
        buf.write("\7w\2\2\u015e\u015f\7t\2\2\u015f\u0160\7p\2\2\u0160\60")
        buf.write("\3\2\2\2\u0161\u0162\7p\2\2\u0162\u0163\7w\2\2\u0163\u0164")
        buf.write("\7n\2\2\u0164\u0165\7n\2\2\u0165\62\3\2\2\2\u0166\u0167")
        buf.write("\7e\2\2\u0167\u0168\7n\2\2\u0168\u0169\7c\2\2\u0169\u016a")
        buf.write("\7u\2\2\u016a\u016b\7u\2\2\u016b\64\3\2\2\2\u016c\u016d")
        buf.write("\7e\2\2\u016d\u016e\7q\2\2\u016e\u016f\7p\2\2\u016f\u0170")
        buf.write("\7u\2\2\u0170\u0171\7v\2\2\u0171\u0172\7t\2\2\u0172\u0173")
        buf.write("\7w\2\2\u0173\u0174\7e\2\2\u0174\u0175\7v\2\2\u0175\u0176")
        buf.write("\7q\2\2\u0176\u0177\7t\2\2\u0177\66\3\2\2\2\u0178\u0179")
        buf.write("\7x\2\2\u0179\u017a\7c\2\2\u017a\u017b\7t\2\2\u017b8\3")
        buf.write("\2\2\2\u017c\u017d\7u\2\2\u017d\u017e\7g\2\2\u017e\u017f")
        buf.write("\7n\2\2\u017f\u0180\7h\2\2\u0180:\3\2\2\2\u0181\u0182")
        buf.write("\7p\2\2\u0182\u0183\7g\2\2\u0183\u0184\7y\2\2\u0184<\3")
        buf.write("\2\2\2\u0185\u0186\7x\2\2\u0186\u0187\7q\2\2\u0187\u0188")
        buf.write("\7k\2\2\u0188\u0189\7f\2\2\u0189>\3\2\2\2\u018a\u018b")
        buf.write("\7e\2\2\u018b\u018c\7q\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7u\2\2\u018e\u018f\7v\2\2\u018f@\3\2\2\2\u0190\u0191")
        buf.write("\7e\2\2\u0191\u0192\7q\2\2\u0192\u0193\7p\2\2\u0193\u0194")
        buf.write("\7u\2\2\u0194\u0195\7v\2\2\u0195\u0196\7c\2\2\u0196\u0197")
        buf.write("\7p\2\2\u0197\u0198\7v\2\2\u0198B\3\2\2\2\u0199\u019a")
        buf.write("\7h\2\2\u019a\u019b\7w\2\2\u019b\u019c\7p\2\2\u019c\u019d")
        buf.write("\7e\2\2\u019dD\3\2\2\2\u019e\u019f\7c\2\2\u019f\u01a0")
        buf.write("\7t\2\2\u01a0\u01a1\7t\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3")
        buf.write("\7{\2\2\u01a3F\3\2\2\2\u01a4\u01a5\7#\2\2\u01a5H\3\2\2")
        buf.write("\2\u01a6\u01a7\7(\2\2\u01a7\u01a8\7(\2\2\u01a8J\3\2\2")
        buf.write("\2\u01a9\u01aa\7~\2\2\u01aa\u01ab\7~\2\2\u01abL\3\2\2")
        buf.write("\2\u01ac\u01ad\7?\2\2\u01ad\u01ae\7?\2\2\u01aeN\3\2\2")
        buf.write("\2\u01af\u01b0\7#\2\2\u01b0\u01b1\7?\2\2\u01b1P\3\2\2")
        buf.write("\2\u01b2\u01b3\7>\2\2\u01b3R\3\2\2\2\u01b4\u01b5\7@\2")
        buf.write("\2\u01b5T\3\2\2\2\u01b6\u01b7\7>\2\2\u01b7\u01b8\7?\2")
        buf.write("\2\u01b8V\3\2\2\2\u01b9\u01ba\7@\2\2\u01ba\u01bb\7?\2")
        buf.write("\2\u01bbX\3\2\2\2\u01bc\u01bd\7?\2\2\u01bdZ\3\2\2\2\u01be")
        buf.write("\u01bf\7<\2\2\u01bf\u01c0\7?\2\2\u01c0\\\3\2\2\2\u01c1")
        buf.write("\u01c2\7-\2\2\u01c2^\3\2\2\2\u01c3\u01c4\7/\2\2\u01c4")
        buf.write("`\3\2\2\2\u01c5\u01c6\7,\2\2\u01c6b\3\2\2\2\u01c7\u01c8")
        buf.write("\7^\2\2\u01c8d\3\2\2\2\u01c9\u01ca\7\'\2\2\u01caf\3\2")
        buf.write("\2\2\u01cb\u01cc\7\61\2\2\u01cch\3\2\2\2\u01cd\u01ce\7")
        buf.write(">\2\2\u01ce\u01cf\7/\2\2\u01cfj\3\2\2\2\u01d0\u01d1\7")
        buf.write("`\2\2\u01d1l\3\2\2\2\u01d2\u01d3\7\60\2\2\u01d3n\3\2\2")
        buf.write("\2\u01d4\u01d5\7.\2\2\u01d5p\3\2\2\2\u01d6\u01d7\7=\2")
        buf.write("\2\u01d7r\3\2\2\2\u01d8\u01d9\7<\2\2\u01d9t\3\2\2\2\u01da")
        buf.write("\u01db\7+\2\2\u01dbv\3\2\2\2\u01dc\u01dd\7*\2\2\u01dd")
        buf.write("x\3\2\2\2\u01de\u01df\7]\2\2\u01dfz\3\2\2\2\u01e0\u01e1")
        buf.write("\7_\2\2\u01e1|\3\2\2\2\u01e2\u01e3\7}\2\2\u01e3~\3\2\2")
        buf.write("\2\u01e4\u01e5\7\177\2\2\u01e5\u0080\3\2\2\2\u01e6\u01eb")
        buf.write("\7$\2\2\u01e7\u01ea\5\u0093J\2\u01e8\u01ea\n\4\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea\u01ed\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ee\3")
        buf.write("\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef\7$\2\2\u01ef\u01f0")
        buf.write("\bA\3\2\u01f0\u0082\3\2\2\2\u01f1\u01f3\7B\2\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f8\t\5\2\2\u01f5\u01f7\t\6\2\2\u01f6\u01f5\3\2\2\2")
        buf.write("\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3")
        buf.write("\2\2\2\u01f9\u0084\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fd")
        buf.write("\5\u0091I\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0205\3\2\2\2")
        buf.write("\u0200\u0206\5\u008dG\2\u0201\u0206\5\u008fH\2\u0202\u0203")
        buf.write("\5\u008dG\2\u0203\u0204\5\u008fH\2\u0204\u0206\3\2\2\2")
        buf.write("\u0205\u0200\3\2\2\2\u0205\u0201\3\2\2\2\u0205\u0202\3")
        buf.write("\2\2\2\u0206\u0086\3\2\2\2\u0207\u0209\5\u0091I\2\u0208")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u0088\3\2\2\2\u020c\u020f\5")
        buf.write("#\22\2\u020d\u020f\5%\23\2\u020e\u020c\3\2\2\2\u020e\u020d")
        buf.write("\3\2\2\2\u020f\u008a\3\2\2\2\u0210\u0213\5]/\2\u0211\u0213")
        buf.write("\5_\60\2\u0212\u0210\3\2\2\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u008c\3\2\2\2\u0214\u0218\5m\67\2\u0215\u0217\5\u0091")
        buf.write("I\2\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u008e\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021b\u021d\t\7\2\2\u021c\u021e\5\u008b")
        buf.write("F\2\u021d\u021c\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0220")
        buf.write("\3\2\2\2\u021f\u0221\5\u0091I\2\u0220\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2")
        buf.write("\u0223\u0090\3\2\2\2\u0224\u0225\t\b\2\2\u0225\u0092\3")
        buf.write("\2\2\2\u0226\u0227\7^\2\2\u0227\u0235\7^\2\2\u0228\u0229")
        buf.write("\7^\2\2\u0229\u0235\7d\2\2\u022a\u022b\7^\2\2\u022b\u0235")
        buf.write("\7h\2\2\u022c\u022d\7^\2\2\u022d\u0235\7t\2\2\u022e\u022f")
        buf.write("\7^\2\2\u022f\u0235\7p\2\2\u0230\u0231\7^\2\2\u0231\u0235")
        buf.write("\7v\2\2\u0232\u0233\7^\2\2\u0233\u0235\7$\2\2\u0234\u0226")
        buf.write("\3\2\2\2\u0234\u0228\3\2\2\2\u0234\u022a\3\2\2\2\u0234")
        buf.write("\u022c\3\2\2\2\u0234\u022e\3\2\2\2\u0234\u0230\3\2\2\2")
        buf.write("\u0234\u0232\3\2\2\2\u0235\u0094\3\2\2\2\u0236\u0237\7")
        buf.write("^\2\2\u0237\u023a\n\t\2\2\u0238\u023a\7^\2\2\u0239\u0236")
        buf.write("\3\2\2\2\u0239\u0238\3\2\2\2\u023a\u0096\3\2\2\2\u023b")
        buf.write("\u023d\t\n\2\2\u023c\u023b\3\2\2\2\u023d\u023e\3\2\2\2")
        buf.write("\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0240\3")
        buf.write("\2\2\2\u0240\u0241\bL\2\2\u0241\u0098\3\2\2\2\u0242\u0243")
        buf.write("\13\2\2\2\u0243\u0244\bM\4\2\u0244\u009a\3\2\2\2\u0245")
        buf.write("\u024a\7$\2\2\u0246\u0249\5\u0093J\2\u0247\u0249\n\13")
        buf.write("\2\2\u0248\u0246\3\2\2\2\u0248\u0247\3\2\2\2\u0249\u024c")
        buf.write("\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b")
        buf.write("\u024e\3\2\2\2\u024c\u024a\3\2\2\2\u024d\u024f\t\f\2\2")
        buf.write("\u024e\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0251\b")
        buf.write("N\5\2\u0251\u009c\3\2\2\2\u0252\u0257\7$\2\2\u0253\u0256")
        buf.write("\5\u0093J\2\u0254\u0256\n\13\2\2\u0255\u0253\3\2\2\2\u0255")
        buf.write("\u0254\3\2\2\2\u0256\u0259\3\2\2\2\u0257\u0255\3\2\2\2")
        buf.write("\u0257\u0258\3\2\2\2\u0258\u025a\3\2\2\2\u0259\u0257\3")
        buf.write("\2\2\2\u025a\u025b\5\u0095K\2\u025b\u025c\bO\6\2\u025c")
        buf.write("\u009e\3\2\2\2\31\2\u0109\u0117\u01e9\u01eb\u01f2\u01f8")
        buf.write("\u01fe\u0205\u020a\u020e\u0212\u0218\u021d\u0222\u0234")
        buf.write("\u0239\u023e\u0248\u024a\u024e\u0255\u0257\7\b\2\2\3A")
        buf.write("\2\3M\3\3N\4\3O\5")
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
    T__8 = 9
    BLOCK_COMMENT = 10
    LINE_COMMENT = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSE = 15
    FOR = 16
    TRUE = 17
    FALSE = 18
    INT = 19
    FLOAT = 20
    BOOL = 21
    STRING = 22
    RETURN = 23
    NULL = 24
    CLASS = 25
    CONSTRUCTOR = 26
    VAR = 27
    SELF = 28
    NEW = 29
    VOID = 30
    CONST = 31
    CONSTANT = 32
    FUNC = 33
    ARRAY = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL = 38
    NOT_EQUAL = 39
    LESS = 40
    GREATER = 41
    LESS_EQUAL = 42
    GREATER_EQUAL = 43
    INITIAL = 44
    ASSIGN = 45
    PLUS = 46
    MINUS = 47
    MULTIPLY = 48
    DIVIDE_I = 49
    DIVIDE_I_L = 50
    DIVIDE_F = 51
    SUPER_CLASS = 52
    STRING_CONCAT = 53
    DOT = 54
    COMMA = 55
    SEMICOLON = 56
    COLON = 57
    RPAREN = 58
    LPAREN = 59
    LBRACK = 60
    RBRACK = 61
    LBRASE = 62
    RBRASE = 63
    STRING_LITERAL = 64
    ID = 65
    FLOAT_LITERAL = 66
    INT_LITERAL = 67
    BOOL_LITERAL = 68
    WS = 69
    ERROR_CHAR = 70
    UNCLOSE_STRING = 71
    ILLEGAL_ESCAPE = 72

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'io.'", "'@readInt()'", "'@writeInt'", "'@readFloat()'", "'@writeFloat'", 
            "'@readBool()'", "'@writeBool'", "'@readString()'", "'@writeString'", 
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'constant'", "'func'", "'array'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'='", "':='", "'+'", "'-'", "'*'", "'\\'", "'%'", "'/'", "'<-'", 
            "'^'", "'.'", "','", "';'", "':'", "')'", "'('", "'['", "']'", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
            "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
            "VOID", "CONST", "CONSTANT", "FUNC", "ARRAY", "NOT", "AND", 
            "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", 
            "GREATER_EQUAL", "INITIAL", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", 
            "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", 
            "DOT", "COMMA", "SEMICOLON", "COLON", "RPAREN", "LPAREN", "LBRACK", 
            "RBRACK", "LBRASE", "RBRASE", "STRING_LITERAL", "ID", "FLOAT_LITERAL", 
            "INT_LITERAL", "BOOL_LITERAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
                  "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "CONSTANT", "FUNC", "ARRAY", "NOT", "AND", "OR", "EQUAL", 
                  "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                  "INITIAL", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", 
                  "DIVIDE_I_L", "DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", 
                  "DOT", "COMMA", "SEMICOLON", "COLON", "RPAREN", "LPAREN", 
                  "LBRACK", "RBRACK", "LBRASE", "RBRASE", "STRING_LITERAL", 
                  "ID", "FLOAT_LITERAL", "INT_LITERAL", "BOOL_LITERAL", 
                  "SIGN", "DECIMAL", "EXPONENT", "DIGIT", "ESC_SEQ", "ILL_ESQ", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[63] = self.STRING_LITERAL_action 
            actions[75] = self.ERROR_CHAR_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
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

     


