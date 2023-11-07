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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u0241\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7")
        buf.write("\n\u00f8\n\n\f\n\16\n\u00fb\13\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\7\13\u0106\n\13\f\13\16\13\u0109\13")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\7?\u01ce\n?\f?\16?")
        buf.write("\u01d1\13?\3?\3?\3?\3@\3@\7@\u01d8\n@\f@\16@\u01db\13")
        buf.write("@\3A\6A\u01de\nA\rA\16A\u01df\3A\3A\3A\3A\3A\5A\u01e7")
        buf.write("\nA\3B\3B\7B\u01eb\nB\fB\16B\u01ee\13B\3C\6C\u01f1\nC")
        buf.write("\rC\16C\u01f2\3D\3D\5D\u01f7\nD\3E\3E\7E\u01fb\nE\fE\16")
        buf.write("E\u01fe\13E\3F\3F\5F\u0202\nF\3F\6F\u0205\nF\rF\16F\u0206")
        buf.write("\3G\3G\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u0219")
        buf.write("\nH\3I\3I\3I\5I\u021e\nI\3J\6J\u0221\nJ\rJ\16J\u0222\3")
        buf.write("J\3J\3K\3K\3K\3L\3L\3L\7L\u022d\nL\fL\16L\u0230\13L\3")
        buf.write("L\5L\u0233\nL\3L\3L\3M\3M\3M\7M\u023a\nM\fM\16M\u023d")
        buf.write("\13M\3M\3M\3M\3\u00f9\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C")
        buf.write("\u0085D\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093E\u0095F\u0097G\u0099H\3\2\r\7\2\f\f\17\17GHQ")
        buf.write("Q~~\4\2\f\f\17\17\6\2\n\f\16\17$$^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\4\2GGgg\7\2ddhhppttvv\5\2\13")
        buf.write("\f\17\17\"\"\5\3\n\f\16\17\"\"\2\u0254\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u00a4\3\2\2")
        buf.write("\2\7\u00ae\3\2\2\2\t\u00b9\3\2\2\2\13\u00c5\3\2\2\2\r")
        buf.write("\u00cf\3\2\2\2\17\u00da\3\2\2\2\21\u00e6\3\2\2\2\23\u00f3")
        buf.write("\3\2\2\2\25\u0101\3\2\2\2\27\u010e\3\2\2\2\31\u0114\3")
        buf.write("\2\2\2\33\u011d\3\2\2\2\35\u0120\3\2\2\2\37\u0125\3\2")
        buf.write("\2\2!\u0129\3\2\2\2#\u012e\3\2\2\2%\u0134\3\2\2\2\'\u0138")
        buf.write("\3\2\2\2)\u013e\3\2\2\2+\u0143\3\2\2\2-\u014a\3\2\2\2")
        buf.write("/\u0151\3\2\2\2\61\u0156\3\2\2\2\63\u015c\3\2\2\2\65\u0168")
        buf.write("\3\2\2\2\67\u016c\3\2\2\29\u0171\3\2\2\2;\u0175\3\2\2")
        buf.write("\2=\u017a\3\2\2\2?\u0180\3\2\2\2A\u0185\3\2\2\2C\u0187")
        buf.write("\3\2\2\2E\u018a\3\2\2\2G\u018d\3\2\2\2I\u0190\3\2\2\2")
        buf.write("K\u0193\3\2\2\2M\u0195\3\2\2\2O\u0197\3\2\2\2Q\u019a\3")
        buf.write("\2\2\2S\u019d\3\2\2\2U\u019f\3\2\2\2W\u01a2\3\2\2\2Y\u01a4")
        buf.write("\3\2\2\2[\u01a6\3\2\2\2]\u01a8\3\2\2\2_\u01aa\3\2\2\2")
        buf.write("a\u01ac\3\2\2\2c\u01ae\3\2\2\2e\u01b1\3\2\2\2g\u01b3\3")
        buf.write("\2\2\2i\u01b5\3\2\2\2k\u01b7\3\2\2\2m\u01b9\3\2\2\2o\u01bb")
        buf.write("\3\2\2\2q\u01bd\3\2\2\2s\u01bf\3\2\2\2u\u01c1\3\2\2\2")
        buf.write("w\u01c3\3\2\2\2y\u01c5\3\2\2\2{\u01c7\3\2\2\2}\u01ca\3")
        buf.write("\2\2\2\177\u01d5\3\2\2\2\u0081\u01dd\3\2\2\2\u0083\u01e8")
        buf.write("\3\2\2\2\u0085\u01f0\3\2\2\2\u0087\u01f6\3\2\2\2\u0089")
        buf.write("\u01f8\3\2\2\2\u008b\u01ff\3\2\2\2\u008d\u0208\3\2\2\2")
        buf.write("\u008f\u0218\3\2\2\2\u0091\u021d\3\2\2\2\u0093\u0220\3")
        buf.write("\2\2\2\u0095\u0226\3\2\2\2\u0097\u0229\3\2\2\2\u0099\u0236")
        buf.write("\3\2\2\2\u009b\u009c\7B\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7f\2\2\u00a0\u00a1")
        buf.write("\7K\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\4")
        buf.write("\3\2\2\2\u00a4\u00a5\7B\2\2\u00a5\u00a6\7y\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\u00ab\7K\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\6\3\2\2\2\u00ae\u00af\7B\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7f\2\2\u00b3\u00b4\7H\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\b")
        buf.write("\3\2\2\2\u00b9\u00ba\7B\2\2\u00ba\u00bb\7y\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7H\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\n")
        buf.write("\3\2\2\2\u00c5\u00c6\7B\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7f\2\2\u00ca\u00cb")
        buf.write("\7D\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\f\3\2\2\2\u00cf\u00d0\7B\2\2\u00d0\u00d1")
        buf.write("\7y\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7D\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7n\2\2\u00d9\16")
        buf.write("\3\2\2\2\u00da\u00db\7B\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7f\2\2\u00df\u00e0")
        buf.write("\7U\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7i\2\2\u00e5\20")
        buf.write("\3\2\2\2\u00e6\u00e7\7B\2\2\u00e7\u00e8\7y\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7U\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2")
        buf.write("\7i\2\2\u00f2\22\3\2\2\2\u00f3\u00f4\7\61\2\2\u00f4\u00f5")
        buf.write("\7,\2\2\u00f5\u00f9\3\2\2\2\u00f6\u00f8\13\2\2\2\u00f7")
        buf.write("\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00fa\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3")
        buf.write("\2\2\2\u00fc\u00fd\7,\2\2\u00fd\u00fe\7\61\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0100\b\n\2\2\u0100\24\3\2\2\2\u0101\u0102")
        buf.write("\7\61\2\2\u0102\u0103\7\61\2\2\u0103\u0107\3\2\2\2\u0104")
        buf.write("\u0106\n\2\2\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3")
        buf.write("\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b\t\3\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010d\b\13\2\2\u010d\26\3\2\2\2\u010e\u010f")
        buf.write("\7d\2\2\u010f\u0110\7t\2\2\u0110\u0111\7g\2\2\u0111\u0112")
        buf.write("\7c\2\2\u0112\u0113\7m\2\2\u0113\30\3\2\2\2\u0114\u0115")
        buf.write("\7e\2\2\u0115\u0116\7q\2\2\u0116\u0117\7p\2\2\u0117\u0118")
        buf.write("\7v\2\2\u0118\u0119\7k\2\2\u0119\u011a\7p\2\2\u011a\u011b")
        buf.write("\7w\2\2\u011b\u011c\7g\2\2\u011c\32\3\2\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7h\2\2\u011f\34\3\2\2\2\u0120\u0121")
        buf.write("\7g\2\2\u0121\u0122\7n\2\2\u0122\u0123\7u\2\2\u0123\u0124")
        buf.write("\7g\2\2\u0124\36\3\2\2\2\u0125\u0126\7h\2\2\u0126\u0127")
        buf.write("\7q\2\2\u0127\u0128\7t\2\2\u0128 \3\2\2\2\u0129\u012a")
        buf.write("\7v\2\2\u012a\u012b\7t\2\2\u012b\u012c\7w\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d\"\3\2\2\2\u012e\u012f\7h\2\2\u012f\u0130")
        buf.write("\7c\2\2\u0130\u0131\7n\2\2\u0131\u0132\7u\2\2\u0132\u0133")
        buf.write("\7g\2\2\u0133$\3\2\2\2\u0134\u0135\7k\2\2\u0135\u0136")
        buf.write("\7p\2\2\u0136\u0137\7v\2\2\u0137&\3\2\2\2\u0138\u0139")
        buf.write("\7h\2\2\u0139\u013a\7n\2\2\u013a\u013b\7q\2\2\u013b\u013c")
        buf.write("\7c\2\2\u013c\u013d\7v\2\2\u013d(\3\2\2\2\u013e\u013f")
        buf.write("\7d\2\2\u013f\u0140\7q\2\2\u0140\u0141\7q\2\2\u0141\u0142")
        buf.write("\7n\2\2\u0142*\3\2\2\2\u0143\u0144\7u\2\2\u0144\u0145")
        buf.write("\7v\2\2\u0145\u0146\7t\2\2\u0146\u0147\7k\2\2\u0147\u0148")
        buf.write("\7p\2\2\u0148\u0149\7i\2\2\u0149,\3\2\2\2\u014a\u014b")
        buf.write("\7t\2\2\u014b\u014c\7g\2\2\u014c\u014d\7v\2\2\u014d\u014e")
        buf.write("\7w\2\2\u014e\u014f\7t\2\2\u014f\u0150\7p\2\2\u0150.\3")
        buf.write("\2\2\2\u0151\u0152\7p\2\2\u0152\u0153\7w\2\2\u0153\u0154")
        buf.write("\7n\2\2\u0154\u0155\7n\2\2\u0155\60\3\2\2\2\u0156\u0157")
        buf.write("\7e\2\2\u0157\u0158\7n\2\2\u0158\u0159\7c\2\2\u0159\u015a")
        buf.write("\7u\2\2\u015a\u015b\7u\2\2\u015b\62\3\2\2\2\u015c\u015d")
        buf.write("\7e\2\2\u015d\u015e\7q\2\2\u015e\u015f\7p\2\2\u015f\u0160")
        buf.write("\7u\2\2\u0160\u0161\7v\2\2\u0161\u0162\7t\2\2\u0162\u0163")
        buf.write("\7w\2\2\u0163\u0164\7e\2\2\u0164\u0165\7v\2\2\u0165\u0166")
        buf.write("\7q\2\2\u0166\u0167\7t\2\2\u0167\64\3\2\2\2\u0168\u0169")
        buf.write("\7x\2\2\u0169\u016a\7c\2\2\u016a\u016b\7t\2\2\u016b\66")
        buf.write("\3\2\2\2\u016c\u016d\7u\2\2\u016d\u016e\7g\2\2\u016e\u016f")
        buf.write("\7n\2\2\u016f\u0170\7h\2\2\u01708\3\2\2\2\u0171\u0172")
        buf.write("\7p\2\2\u0172\u0173\7g\2\2\u0173\u0174\7y\2\2\u0174:\3")
        buf.write("\2\2\2\u0175\u0176\7x\2\2\u0176\u0177\7q\2\2\u0177\u0178")
        buf.write("\7k\2\2\u0178\u0179\7f\2\2\u0179<\3\2\2\2\u017a\u017b")
        buf.write("\7e\2\2\u017b\u017c\7q\2\2\u017c\u017d\7p\2\2\u017d\u017e")
        buf.write("\7u\2\2\u017e\u017f\7v\2\2\u017f>\3\2\2\2\u0180\u0181")
        buf.write("\7h\2\2\u0181\u0182\7w\2\2\u0182\u0183\7p\2\2\u0183\u0184")
        buf.write("\7e\2\2\u0184@\3\2\2\2\u0185\u0186\7#\2\2\u0186B\3\2\2")
        buf.write("\2\u0187\u0188\7(\2\2\u0188\u0189\7(\2\2\u0189D\3\2\2")
        buf.write("\2\u018a\u018b\7~\2\2\u018b\u018c\7~\2\2\u018cF\3\2\2")
        buf.write("\2\u018d\u018e\7?\2\2\u018e\u018f\7?\2\2\u018fH\3\2\2")
        buf.write("\2\u0190\u0191\7#\2\2\u0191\u0192\7?\2\2\u0192J\3\2\2")
        buf.write("\2\u0193\u0194\7>\2\2\u0194L\3\2\2\2\u0195\u0196\7@\2")
        buf.write("\2\u0196N\3\2\2\2\u0197\u0198\7>\2\2\u0198\u0199\7?\2")
        buf.write("\2\u0199P\3\2\2\2\u019a\u019b\7@\2\2\u019b\u019c\7?\2")
        buf.write("\2\u019cR\3\2\2\2\u019d\u019e\7?\2\2\u019eT\3\2\2\2\u019f")
        buf.write("\u01a0\7<\2\2\u01a0\u01a1\7?\2\2\u01a1V\3\2\2\2\u01a2")
        buf.write("\u01a3\7-\2\2\u01a3X\3\2\2\2\u01a4\u01a5\7/\2\2\u01a5")
        buf.write("Z\3\2\2\2\u01a6\u01a7\7,\2\2\u01a7\\\3\2\2\2\u01a8\u01a9")
        buf.write("\7^\2\2\u01a9^\3\2\2\2\u01aa\u01ab\7\'\2\2\u01ab`\3\2")
        buf.write("\2\2\u01ac\u01ad\7\61\2\2\u01adb\3\2\2\2\u01ae\u01af\7")
        buf.write(">\2\2\u01af\u01b0\7/\2\2\u01b0d\3\2\2\2\u01b1\u01b2\7")
        buf.write("`\2\2\u01b2f\3\2\2\2\u01b3\u01b4\7\60\2\2\u01b4h\3\2\2")
        buf.write("\2\u01b5\u01b6\7.\2\2\u01b6j\3\2\2\2\u01b7\u01b8\7=\2")
        buf.write("\2\u01b8l\3\2\2\2\u01b9\u01ba\7<\2\2\u01ban\3\2\2\2\u01bb")
        buf.write("\u01bc\7+\2\2\u01bcp\3\2\2\2\u01bd\u01be\7*\2\2\u01be")
        buf.write("r\3\2\2\2\u01bf\u01c0\7]\2\2\u01c0t\3\2\2\2\u01c1\u01c2")
        buf.write("\7_\2\2\u01c2v\3\2\2\2\u01c3\u01c4\7}\2\2\u01c4x\3\2\2")
        buf.write("\2\u01c5\u01c6\7\177\2\2\u01c6z\3\2\2\2\u01c7\u01c8\7")
        buf.write("B\2\2\u01c8\u01c9\5\177@\2\u01c9|\3\2\2\2\u01ca\u01cf")
        buf.write("\7$\2\2\u01cb\u01ce\5\u008fH\2\u01cc\u01ce\n\4\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2")
        buf.write("\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\3")
        buf.write("\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\7$\2\2\u01d3\u01d4")
        buf.write("\b?\3\2\u01d4~\3\2\2\2\u01d5\u01d9\t\5\2\2\u01d6\u01d8")
        buf.write("\t\6\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u0080\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01dc\u01de\5\u008dG\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01dd\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e6\3\2\2\2\u01e1\u01e7\5\u0089")
        buf.write("E\2\u01e2\u01e7\5\u008bF\2\u01e3\u01e4\5\u0089E\2\u01e4")
        buf.write("\u01e5\5\u008bF\2\u01e5\u01e7\3\2\2\2\u01e6\u01e1\3\2")
        buf.write("\2\2\u01e6\u01e2\3\2\2\2\u01e6\u01e3\3\2\2\2\u01e7\u0082")
        buf.write("\3\2\2\2\u01e8\u01ec\t\7\2\2\u01e9\u01eb\t\b\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed\u0084\3\2\2\2\u01ee\u01ec\3")
        buf.write("\2\2\2\u01ef\u01f1\5\u008dG\2\u01f0\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3\u0086\3\2\2\2\u01f4\u01f7\5W,\2\u01f5\u01f7\5Y")
        buf.write("-\2\u01f6\u01f4\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7\u0088")
        buf.write("\3\2\2\2\u01f8\u01fc\5g\64\2\u01f9\u01fb\5\u008dG\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u008a\3\2\2\2\u01fe\u01fc\3")
        buf.write("\2\2\2\u01ff\u0201\t\t\2\2\u0200\u0202\5\u0087D\2\u0201")
        buf.write("\u0200\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0204\3\2\2\2")
        buf.write("\u0203\u0205\5\u008dG\2\u0204\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u008c\3\2\2\2\u0208\u0209\t\b\2\2\u0209\u008e\3\2\2\2")
        buf.write("\u020a\u020b\7^\2\2\u020b\u0219\7^\2\2\u020c\u020d\7^")
        buf.write("\2\2\u020d\u0219\7d\2\2\u020e\u020f\7^\2\2\u020f\u0219")
        buf.write("\7h\2\2\u0210\u0211\7^\2\2\u0211\u0219\7t\2\2\u0212\u0213")
        buf.write("\7^\2\2\u0213\u0219\7p\2\2\u0214\u0215\7^\2\2\u0215\u0219")
        buf.write("\7v\2\2\u0216\u0217\7^\2\2\u0217\u0219\7$\2\2\u0218\u020a")
        buf.write("\3\2\2\2\u0218\u020c\3\2\2\2\u0218\u020e\3\2\2\2\u0218")
        buf.write("\u0210\3\2\2\2\u0218\u0212\3\2\2\2\u0218\u0214\3\2\2\2")
        buf.write("\u0218\u0216\3\2\2\2\u0219\u0090\3\2\2\2\u021a\u021b\7")
        buf.write("^\2\2\u021b\u021e\n\n\2\2\u021c\u021e\7^\2\2\u021d\u021a")
        buf.write("\3\2\2\2\u021d\u021c\3\2\2\2\u021e\u0092\3\2\2\2\u021f")
        buf.write("\u0221\t\13\2\2\u0220\u021f\3\2\2\2\u0221\u0222\3\2\2")
        buf.write("\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224")
        buf.write("\3\2\2\2\u0224\u0225\bJ\2\2\u0225\u0094\3\2\2\2\u0226")
        buf.write("\u0227\13\2\2\2\u0227\u0228\bK\4\2\u0228\u0096\3\2\2\2")
        buf.write("\u0229\u022e\7$\2\2\u022a\u022d\5\u008fH\2\u022b\u022d")
        buf.write("\n\4\2\2\u022c\u022a\3\2\2\2\u022c\u022b\3\2\2\2\u022d")
        buf.write("\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2")
        buf.write("\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0233\t")
        buf.write("\f\2\2\u0232\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235")
        buf.write("\bL\5\2\u0235\u0098\3\2\2\2\u0236\u023b\7$\2\2\u0237\u023a")
        buf.write("\5\u008fH\2\u0238\u023a\n\4\2\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u0238\3\2\2\2\u023a\u023d\3\2\2\2\u023b\u0239\3\2\2\2")
        buf.write("\u023b\u023c\3\2\2\2\u023c\u023e\3\2\2\2\u023d\u023b\3")
        buf.write("\2\2\2\u023e\u023f\5\u0091I\2\u023f\u0240\bM\6\2\u0240")
        buf.write("\u009a\3\2\2\2\30\2\u00f9\u0107\u01cd\u01cf\u01d9\u01df")
        buf.write("\u01e6\u01ec\u01f2\u01f6\u01fc\u0201\u0206\u0218\u021d")
        buf.write("\u0222\u022c\u022e\u0232\u0239\u023b\7\b\2\2\3?\2\3K\3")
        buf.write("\3L\4\3M\5")
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
    FUNC = 31
    NOT = 32
    AND = 33
    OR = 34
    EQUAL = 35
    NOT_EQUAL = 36
    LESS = 37
    GREATER = 38
    LESS_EQUAL = 39
    GREATER_EQUAL = 40
    INITIAL = 41
    ASSIGN = 42
    PLUS = 43
    MINUS = 44
    MULTIPLY = 45
    DIVIDE_I = 46
    DIVIDE_I_L = 47
    DIVIDE_F = 48
    SUPER_CLASS = 49
    STRING_CONCAT = 50
    DOT = 51
    COMMA = 52
    SEMICOLON = 53
    COLON = 54
    RPAREN = 55
    LPAREN = 56
    LBRACK = 57
    RBRACK = 58
    LBRASE = 59
    RBRASE = 60
    AT_ID = 61
    STRING_LITERAL = 62
    ID = 63
    FLOAT_LITERAL = 64
    NON_ZERO_INT = 65
    INT_LITERAL = 66
    WS = 67
    ERROR_CHAR = 68
    UNCLOSE_STRING = 69
    ILLEGAL_ESCAPE = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'@readInt'", "'@writeInt'", "'@readFloat'", "'@writeFloat'", 
            "'@readBool'", "'@writeBool'", "'@readString'", "'@writeString'", 
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'func'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'='", "':='", "'+'", 
            "'-'", "'*'", "'\\'", "'%'", "'/'", "'<-'", "'^'", "'.'", "','", 
            "';'", "':'", "')'", "'('", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
            "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
            "VOID", "CONST", "FUNC", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
            "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "INITIAL", 
            "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", 
            "DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", 
            "SEMICOLON", "COLON", "RPAREN", "LPAREN", "LBRACK", "RBRACK", 
            "LBRASE", "RBRASE", "AT_ID", "STRING_LITERAL", "ID", "FLOAT_LITERAL", 
            "NON_ZERO_INT", "INT_LITERAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                  "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                  "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "NOT", 
                  "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
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
            actions[61] = self.STRING_LITERAL_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
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

     


