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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u0282\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u010a\n\13\f\13\16\13\u010d\13\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0118\n")
        buf.write("\f\f\f\16\f\u011b\13\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3@\3@\5@\u01e7\n@\3A\5A\u01ea\nA\3A\3A\7A\u01ee")
        buf.write("\nA\fA\16A\u01f1\13A\3B\6B\u01f4\nB\rB\16B\u01f5\3B\3")
        buf.write("B\3B\3B\3B\5B\u01fd\nB\3C\6C\u0200\nC\rC\16C\u0201\3D")
        buf.write("\3D\5D\u0206\nD\3E\3E\3E\7E\u020b\nE\fE\16E\u020e\13E")
        buf.write("\3E\3E\3E\3F\3F\7F\u0215\nF\fF\16F\u0218\13F\3F\3F\7F")
        buf.write("\u021c\nF\fF\16F\u021f\13F\3F\3F\7F\u0223\nF\fF\16F\u0226")
        buf.write("\13F\3F\3F\7F\u022a\nF\fF\16F\u022d\13F\7F\u022f\nF\f")
        buf.write("F\16F\u0232\13F\3F\3F\3G\3G\5G\u0238\nG\3H\3H\7H\u023c")
        buf.write("\nH\fH\16H\u023f\13H\3I\3I\5I\u0243\nI\3I\6I\u0246\nI")
        buf.write("\rI\16I\u0247\3J\3J\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3")
        buf.write("K\3K\3K\5K\u025a\nK\3L\3L\3L\5L\u025f\nL\3M\6M\u0262\n")
        buf.write("M\rM\16M\u0263\3M\3M\3N\3N\3N\3O\3O\3O\7O\u026e\nO\fO")
        buf.write("\16O\u0271\13O\3O\5O\u0274\nO\3O\3O\3P\3P\3P\7P\u027b")
        buf.write("\nP\fP\16P\u027e\13P\3P\3P\3P\3\u010b\2Q\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097\2\u0099H\u009bI\u009dJ\u009f")
        buf.write("K\3\2\r\7\2\f\f\17\17GHQQ~~\4\2\f\f\17\17\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\f\f\17\17$$\4\2GGgg\3\2\62;\7\2ddhh")
        buf.write("ppttvv\5\2\13\f\17\17\"\"\6\2\n\f\16\17$$^^\5\3\n\f\16")
        buf.write("\17\"\"\2\u029e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1")
        buf.write("\3\2\2\2\5\u00a5\3\2\2\2\7\u00b0\3\2\2\2\t\u00ba\3\2\2")
        buf.write("\2\13\u00c7\3\2\2\2\r\u00d3\3\2\2\2\17\u00df\3\2\2\2\21")
        buf.write("\u00ea\3\2\2\2\23\u00f8\3\2\2\2\25\u0105\3\2\2\2\27\u0113")
        buf.write("\3\2\2\2\31\u0120\3\2\2\2\33\u0126\3\2\2\2\35\u012f\3")
        buf.write("\2\2\2\37\u0132\3\2\2\2!\u0137\3\2\2\2#\u013b\3\2\2\2")
        buf.write("%\u0140\3\2\2\2\'\u0146\3\2\2\2)\u014a\3\2\2\2+\u0150")
        buf.write("\3\2\2\2-\u0155\3\2\2\2/\u015c\3\2\2\2\61\u0163\3\2\2")
        buf.write("\2\63\u0168\3\2\2\2\65\u016e\3\2\2\2\67\u017a\3\2\2\2")
        buf.write("9\u017e\3\2\2\2;\u0183\3\2\2\2=\u0187\3\2\2\2?\u018c\3")
        buf.write("\2\2\2A\u0192\3\2\2\2C\u019b\3\2\2\2E\u01a0\3\2\2\2G\u01a2")
        buf.write("\3\2\2\2I\u01a5\3\2\2\2K\u01a8\3\2\2\2M\u01ab\3\2\2\2")
        buf.write("O\u01ae\3\2\2\2Q\u01b0\3\2\2\2S\u01b2\3\2\2\2U\u01b5\3")
        buf.write("\2\2\2W\u01b8\3\2\2\2Y\u01ba\3\2\2\2[\u01bd\3\2\2\2]\u01bf")
        buf.write("\3\2\2\2_\u01c1\3\2\2\2a\u01c3\3\2\2\2c\u01c5\3\2\2\2")
        buf.write("e\u01c7\3\2\2\2g\u01c9\3\2\2\2i\u01cc\3\2\2\2k\u01ce\3")
        buf.write("\2\2\2m\u01d0\3\2\2\2o\u01d2\3\2\2\2q\u01d4\3\2\2\2s\u01d6")
        buf.write("\3\2\2\2u\u01d8\3\2\2\2w\u01da\3\2\2\2y\u01dc\3\2\2\2")
        buf.write("{\u01de\3\2\2\2}\u01e0\3\2\2\2\177\u01e6\3\2\2\2\u0081")
        buf.write("\u01e9\3\2\2\2\u0083\u01f3\3\2\2\2\u0085\u01ff\3\2\2\2")
        buf.write("\u0087\u0205\3\2\2\2\u0089\u0207\3\2\2\2\u008b\u0212\3")
        buf.write("\2\2\2\u008d\u0237\3\2\2\2\u008f\u0239\3\2\2\2\u0091\u0240")
        buf.write("\3\2\2\2\u0093\u0249\3\2\2\2\u0095\u0259\3\2\2\2\u0097")
        buf.write("\u025e\3\2\2\2\u0099\u0261\3\2\2\2\u009b\u0267\3\2\2\2")
        buf.write("\u009d\u026a\3\2\2\2\u009f\u0277\3\2\2\2\u00a1\u00a2\7")
        buf.write("k\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7\60\2\2\u00a4\4")
        buf.write("\3\2\2\2\u00a5\u00a6\7B\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7f\2\2\u00aa\u00ab")
        buf.write("\7K\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae")
        buf.write("\7*\2\2\u00ae\u00af\7+\2\2\u00af\6\3\2\2\2\u00b0\u00b1")
        buf.write("\7B\2\2\u00b1\u00b2\7y\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7K\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\b")
        buf.write("\3\2\2\2\u00ba\u00bb\7B\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7f\2\2\u00bf\u00c0")
        buf.write("\7H\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7*\2\2\u00c5\u00c6")
        buf.write("\7+\2\2\u00c6\n\3\2\2\2\u00c7\u00c8\7B\2\2\u00c8\u00c9")
        buf.write("\7y\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7H\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\f\3\2\2\2\u00d3\u00d4\7B\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7D\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7*\2\2\u00dd\u00de")
        buf.write("\7+\2\2\u00de\16\3\2\2\2\u00df\u00e0\7B\2\2\u00e0\u00e1")
        buf.write("\7y\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7D\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7n\2\2\u00e9\20")
        buf.write("\3\2\2\2\u00ea\u00eb\7B\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7f\2\2\u00ef\u00f0")
        buf.write("\7U\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6")
        buf.write("\7*\2\2\u00f6\u00f7\7+\2\2\u00f7\22\3\2\2\2\u00f8\u00f9")
        buf.write("\7B\2\2\u00f9\u00fa\7y\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7U\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104\7i\2\2\u0104\24")
        buf.write("\3\2\2\2\u0105\u0106\7\61\2\2\u0106\u0107\7,\2\2\u0107")
        buf.write("\u010b\3\2\2\2\u0108\u010a\13\2\2\2\u0109\u0108\3\2\2")
        buf.write("\2\u010a\u010d\3\2\2\2\u010b\u010c\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e")
        buf.write("\u010f\7,\2\2\u010f\u0110\7\61\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\b\13\2\2\u0112\26\3\2\2\2\u0113\u0114\7\61")
        buf.write("\2\2\u0114\u0115\7\61\2\2\u0115\u0119\3\2\2\2\u0116\u0118")
        buf.write("\n\2\2\2\u0117\u0116\3\2\2\2\u0118\u011b\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c\3\2\2\2")
        buf.write("\u011b\u0119\3\2\2\2\u011c\u011d\t\3\2\2\u011d\u011e\3")
        buf.write("\2\2\2\u011e\u011f\b\f\2\2\u011f\30\3\2\2\2\u0120\u0121")
        buf.write("\7d\2\2\u0121\u0122\7t\2\2\u0122\u0123\7g\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7m\2\2\u0125\32\3\2\2\2\u0126\u0127")
        buf.write("\7e\2\2\u0127\u0128\7q\2\2\u0128\u0129\7p\2\2\u0129\u012a")
        buf.write("\7v\2\2\u012a\u012b\7k\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7g\2\2\u012e\34\3\2\2\2\u012f\u0130")
        buf.write("\7k\2\2\u0130\u0131\7h\2\2\u0131\36\3\2\2\2\u0132\u0133")
        buf.write("\7g\2\2\u0133\u0134\7n\2\2\u0134\u0135\7u\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136 \3\2\2\2\u0137\u0138\7h\2\2\u0138\u0139")
        buf.write("\7q\2\2\u0139\u013a\7t\2\2\u013a\"\3\2\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\u013d\7t\2\2\u013d\u013e\7w\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f$\3\2\2\2\u0140\u0141\7h\2\2\u0141\u0142")
        buf.write("\7c\2\2\u0142\u0143\7n\2\2\u0143\u0144\7u\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145&\3\2\2\2\u0146\u0147\7k\2\2\u0147\u0148")
        buf.write("\7p\2\2\u0148\u0149\7v\2\2\u0149(\3\2\2\2\u014a\u014b")
        buf.write("\7h\2\2\u014b\u014c\7n\2\2\u014c\u014d\7q\2\2\u014d\u014e")
        buf.write("\7c\2\2\u014e\u014f\7v\2\2\u014f*\3\2\2\2\u0150\u0151")
        buf.write("\7d\2\2\u0151\u0152\7q\2\2\u0152\u0153\7q\2\2\u0153\u0154")
        buf.write("\7n\2\2\u0154,\3\2\2\2\u0155\u0156\7u\2\2\u0156\u0157")
        buf.write("\7v\2\2\u0157\u0158\7t\2\2\u0158\u0159\7k\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015a\u015b\7i\2\2\u015b.\3\2\2\2\u015c\u015d")
        buf.write("\7t\2\2\u015d\u015e\7g\2\2\u015e\u015f\7v\2\2\u015f\u0160")
        buf.write("\7w\2\2\u0160\u0161\7t\2\2\u0161\u0162\7p\2\2\u0162\60")
        buf.write("\3\2\2\2\u0163\u0164\7p\2\2\u0164\u0165\7w\2\2\u0165\u0166")
        buf.write("\7n\2\2\u0166\u0167\7n\2\2\u0167\62\3\2\2\2\u0168\u0169")
        buf.write("\7e\2\2\u0169\u016a\7n\2\2\u016a\u016b\7c\2\2\u016b\u016c")
        buf.write("\7u\2\2\u016c\u016d\7u\2\2\u016d\64\3\2\2\2\u016e\u016f")
        buf.write("\7e\2\2\u016f\u0170\7q\2\2\u0170\u0171\7p\2\2\u0171\u0172")
        buf.write("\7u\2\2\u0172\u0173\7v\2\2\u0173\u0174\7t\2\2\u0174\u0175")
        buf.write("\7w\2\2\u0175\u0176\7e\2\2\u0176\u0177\7v\2\2\u0177\u0178")
        buf.write("\7q\2\2\u0178\u0179\7t\2\2\u0179\66\3\2\2\2\u017a\u017b")
        buf.write("\7x\2\2\u017b\u017c\7c\2\2\u017c\u017d\7t\2\2\u017d8\3")
        buf.write("\2\2\2\u017e\u017f\7u\2\2\u017f\u0180\7g\2\2\u0180\u0181")
        buf.write("\7n\2\2\u0181\u0182\7h\2\2\u0182:\3\2\2\2\u0183\u0184")
        buf.write("\7p\2\2\u0184\u0185\7g\2\2\u0185\u0186\7y\2\2\u0186<\3")
        buf.write("\2\2\2\u0187\u0188\7x\2\2\u0188\u0189\7q\2\2\u0189\u018a")
        buf.write("\7k\2\2\u018a\u018b\7f\2\2\u018b>\3\2\2\2\u018c\u018d")
        buf.write("\7e\2\2\u018d\u018e\7q\2\2\u018e\u018f\7p\2\2\u018f\u0190")
        buf.write("\7u\2\2\u0190\u0191\7v\2\2\u0191@\3\2\2\2\u0192\u0193")
        buf.write("\7e\2\2\u0193\u0194\7q\2\2\u0194\u0195\7p\2\2\u0195\u0196")
        buf.write("\7u\2\2\u0196\u0197\7v\2\2\u0197\u0198\7c\2\2\u0198\u0199")
        buf.write("\7p\2\2\u0199\u019a\7v\2\2\u019aB\3\2\2\2\u019b\u019c")
        buf.write("\7h\2\2\u019c\u019d\7w\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7e\2\2\u019fD\3\2\2\2\u01a0\u01a1\7#\2\2\u01a1F\3\2\2")
        buf.write("\2\u01a2\u01a3\7(\2\2\u01a3\u01a4\7(\2\2\u01a4H\3\2\2")
        buf.write("\2\u01a5\u01a6\7~\2\2\u01a6\u01a7\7~\2\2\u01a7J\3\2\2")
        buf.write("\2\u01a8\u01a9\7?\2\2\u01a9\u01aa\7?\2\2\u01aaL\3\2\2")
        buf.write("\2\u01ab\u01ac\7#\2\2\u01ac\u01ad\7?\2\2\u01adN\3\2\2")
        buf.write("\2\u01ae\u01af\7>\2\2\u01afP\3\2\2\2\u01b0\u01b1\7@\2")
        buf.write("\2\u01b1R\3\2\2\2\u01b2\u01b3\7>\2\2\u01b3\u01b4\7?\2")
        buf.write("\2\u01b4T\3\2\2\2\u01b5\u01b6\7@\2\2\u01b6\u01b7\7?\2")
        buf.write("\2\u01b7V\3\2\2\2\u01b8\u01b9\7?\2\2\u01b9X\3\2\2\2\u01ba")
        buf.write("\u01bb\7<\2\2\u01bb\u01bc\7?\2\2\u01bcZ\3\2\2\2\u01bd")
        buf.write("\u01be\7-\2\2\u01be\\\3\2\2\2\u01bf\u01c0\7/\2\2\u01c0")
        buf.write("^\3\2\2\2\u01c1\u01c2\7,\2\2\u01c2`\3\2\2\2\u01c3\u01c4")
        buf.write("\7^\2\2\u01c4b\3\2\2\2\u01c5\u01c6\7\'\2\2\u01c6d\3\2")
        buf.write("\2\2\u01c7\u01c8\7\61\2\2\u01c8f\3\2\2\2\u01c9\u01ca\7")
        buf.write(">\2\2\u01ca\u01cb\7/\2\2\u01cbh\3\2\2\2\u01cc\u01cd\7")
        buf.write("`\2\2\u01cdj\3\2\2\2\u01ce\u01cf\7\60\2\2\u01cfl\3\2\2")
        buf.write("\2\u01d0\u01d1\7.\2\2\u01d1n\3\2\2\2\u01d2\u01d3\7=\2")
        buf.write("\2\u01d3p\3\2\2\2\u01d4\u01d5\7<\2\2\u01d5r\3\2\2\2\u01d6")
        buf.write("\u01d7\7+\2\2\u01d7t\3\2\2\2\u01d8\u01d9\7*\2\2\u01d9")
        buf.write("v\3\2\2\2\u01da\u01db\7]\2\2\u01dbx\3\2\2\2\u01dc\u01dd")
        buf.write("\7_\2\2\u01ddz\3\2\2\2\u01de\u01df\7}\2\2\u01df|\3\2\2")
        buf.write("\2\u01e0\u01e1\7\177\2\2\u01e1~\3\2\2\2\u01e2\u01e7\5")
        buf.write("\u0085C\2\u01e3\u01e7\5\u0083B\2\u01e4\u01e7\5\u0087D")
        buf.write("\2\u01e5\u01e7\5\u0089E\2\u01e6\u01e2\3\2\2\2\u01e6\u01e3")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7")
        buf.write("\u0080\3\2\2\2\u01e8\u01ea\7B\2\2\u01e9\u01e8\3\2\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ef\t")
        buf.write("\4\2\2\u01ec\u01ee\t\5\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1")
        buf.write("\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u0082\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f4\5\u0093")
        buf.write("J\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01fc\3\2\2\2\u01f7")
        buf.write("\u01fd\5\u008fH\2\u01f8\u01fd\5\u0091I\2\u01f9\u01fa\5")
        buf.write("\u008fH\2\u01fa\u01fb\5\u0091I\2\u01fb\u01fd\3\2\2\2\u01fc")
        buf.write("\u01f7\3\2\2\2\u01fc\u01f8\3\2\2\2\u01fc\u01f9\3\2\2\2")
        buf.write("\u01fd\u0084\3\2\2\2\u01fe\u0200\5\u0093J\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0086\3\2\2\2\u0203\u0206\5#\22\2")
        buf.write("\u0204\u0206\5%\23\2\u0205\u0203\3\2\2\2\u0205\u0204\3")
        buf.write("\2\2\2\u0206\u0088\3\2\2\2\u0207\u020c\7$\2\2\u0208\u020b")
        buf.write("\5\u0095K\2\u0209\u020b\n\6\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020c\u020d\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c\3")
        buf.write("\2\2\2\u020f\u0210\7$\2\2\u0210\u0211\bE\3\2\u0211\u008a")
        buf.write("\3\2\2\2\u0212\u0216\5w<\2\u0213\u0215\7\"\2\2\u0214\u0213")
        buf.write("\3\2\2\2\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216")
        buf.write("\u0217\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0216\3\2\2\2")
        buf.write("\u0219\u021d\5\177@\2\u021a\u021c\7\"\2\2\u021b\u021a")
        buf.write("\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u0230\3\2\2\2\u021f\u021d\3\2\2\2")
        buf.write("\u0220\u0224\5m\67\2\u0221\u0223\7\"\2\2\u0222\u0221\3")
        buf.write("\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225")
        buf.write("\3\2\2\2\u0225\u0227\3\2\2\2\u0226\u0224\3\2\2\2\u0227")
        buf.write("\u022b\5\177@\2\u0228\u022a\7\"\2\2\u0229\u0228\3\2\2")
        buf.write("\2\u022a\u022d\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c")
        buf.write("\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022e")
        buf.write("\u0220\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u0233\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0233\u0234\5y=\2\u0234\u008c\3\2\2\2\u0235\u0238")
        buf.write("\5[.\2\u0236\u0238\5]/\2\u0237\u0235\3\2\2\2\u0237\u0236")
        buf.write("\3\2\2\2\u0238\u008e\3\2\2\2\u0239\u023d\5k\66\2\u023a")
        buf.write("\u023c\5\u0093J\2\u023b\u023a\3\2\2\2\u023c\u023f\3\2")
        buf.write("\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0090")
        buf.write("\3\2\2\2\u023f\u023d\3\2\2\2\u0240\u0242\t\7\2\2\u0241")
        buf.write("\u0243\5\u008dG\2\u0242\u0241\3\2\2\2\u0242\u0243\3\2")
        buf.write("\2\2\u0243\u0245\3\2\2\2\u0244\u0246\5\u0093J\2\u0245")
        buf.write("\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0245\3\2\2\2")
        buf.write("\u0247\u0248\3\2\2\2\u0248\u0092\3\2\2\2\u0249\u024a\t")
        buf.write("\b\2\2\u024a\u0094\3\2\2\2\u024b\u024c\7^\2\2\u024c\u025a")
        buf.write("\7^\2\2\u024d\u024e\7^\2\2\u024e\u025a\7d\2\2\u024f\u0250")
        buf.write("\7^\2\2\u0250\u025a\7h\2\2\u0251\u0252\7^\2\2\u0252\u025a")
        buf.write("\7t\2\2\u0253\u0254\7^\2\2\u0254\u025a\7p\2\2\u0255\u0256")
        buf.write("\7^\2\2\u0256\u025a\7v\2\2\u0257\u0258\7^\2\2\u0258\u025a")
        buf.write("\7$\2\2\u0259\u024b\3\2\2\2\u0259\u024d\3\2\2\2\u0259")
        buf.write("\u024f\3\2\2\2\u0259\u0251\3\2\2\2\u0259\u0253\3\2\2\2")
        buf.write("\u0259\u0255\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u0096\3")
        buf.write("\2\2\2\u025b\u025c\7^\2\2\u025c\u025f\n\t\2\2\u025d\u025f")
        buf.write("\7^\2\2\u025e\u025b\3\2\2\2\u025e\u025d\3\2\2\2\u025f")
        buf.write("\u0098\3\2\2\2\u0260\u0262\t\n\2\2\u0261\u0260\3\2\2\2")
        buf.write("\u0262\u0263\3\2\2\2\u0263\u0261\3\2\2\2\u0263\u0264\3")
        buf.write("\2\2\2\u0264\u0265\3\2\2\2\u0265\u0266\bM\2\2\u0266\u009a")
        buf.write("\3\2\2\2\u0267\u0268\13\2\2\2\u0268\u0269\bN\4\2\u0269")
        buf.write("\u009c\3\2\2\2\u026a\u026f\7$\2\2\u026b\u026e\5\u0095")
        buf.write("K\2\u026c\u026e\n\13\2\2\u026d\u026b\3\2\2\2\u026d\u026c")
        buf.write("\3\2\2\2\u026e\u0271\3\2\2\2\u026f\u026d\3\2\2\2\u026f")
        buf.write("\u0270\3\2\2\2\u0270\u0273\3\2\2\2\u0271\u026f\3\2\2\2")
        buf.write("\u0272\u0274\t\f\2\2\u0273\u0272\3\2\2\2\u0274\u0275\3")
        buf.write("\2\2\2\u0275\u0276\bO\5\2\u0276\u009e\3\2\2\2\u0277\u027c")
        buf.write("\7$\2\2\u0278\u027b\5\u0095K\2\u0279\u027b\n\13\2\2\u027a")
        buf.write("\u0278\3\2\2\2\u027a\u0279\3\2\2\2\u027b\u027e\3\2\2\2")
        buf.write("\u027c\u027a\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u027f\3")
        buf.write("\2\2\2\u027e\u027c\3\2\2\2\u027f\u0280\5\u0097L\2\u0280")
        buf.write("\u0281\bP\6\2\u0281\u00a0\3\2\2\2\37\2\u010b\u0119\u01e6")
        buf.write("\u01e9\u01ef\u01f5\u01fc\u0201\u0205\u020a\u020c\u0216")
        buf.write("\u021d\u0224\u022b\u0230\u0237\u023d\u0242\u0247\u0259")
        buf.write("\u025e\u0263\u026d\u026f\u0273\u027a\u027c\7\b\2\2\3E")
        buf.write("\2\3N\3\3O\4\3P\5")
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
    NOT = 34
    AND = 35
    OR = 36
    EQUAL = 37
    NOT_EQUAL = 38
    LESS = 39
    GREATER = 40
    LESS_EQUAL = 41
    GREATER_EQUAL = 42
    INITIAL = 43
    ASSIGN = 44
    PLUS = 45
    MINUS = 46
    MULTIPLY = 47
    DIVIDE_I = 48
    DIVIDE_I_L = 49
    DIVIDE_F = 50
    SUPER_CLASS = 51
    STRING_CONCAT = 52
    DOT = 53
    COMMA = 54
    SEMICOLON = 55
    COLON = 56
    RPAREN = 57
    LPAREN = 58
    LBRACK = 59
    RBRACK = 60
    LBRASE = 61
    RBRASE = 62
    LITERAL = 63
    ID = 64
    FLOAT_LITERAL = 65
    INT_LITERAL = 66
    BOOL_LITERAL = 67
    STRING_LITERAL = 68
    ARRAY = 69
    WS = 70
    ERROR_CHAR = 71
    UNCLOSE_STRING = 72
    ILLEGAL_ESCAPE = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'io.'", "'@readInt()'", "'@writeInt'", "'@readFloat()'", "'@writeFloat'", 
            "'@readBool()'", "'@writeBool'", "'@readString()'", "'@writeString'", 
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
            "RBRACK", "LBRASE", "RBRASE", "LITERAL", "ID", "FLOAT_LITERAL", 
            "INT_LITERAL", "BOOL_LITERAL", "STRING_LITERAL", "ARRAY", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
                  "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "CONSTANT", "FUNC", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "INITIAL", 
                  "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", 
                  "DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", 
                  "SEMICOLON", "COLON", "RPAREN", "LPAREN", "LBRACK", "RBRACK", 
                  "LBRASE", "RBRASE", "LITERAL", "ID", "FLOAT_LITERAL", 
                  "INT_LITERAL", "BOOL_LITERAL", "STRING_LITERAL", "ARRAY", 
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
            actions[67] = self.STRING_LITERAL_action 
            actions[76] = self.ERROR_CHAR_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text[1:-1]
     

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

     


