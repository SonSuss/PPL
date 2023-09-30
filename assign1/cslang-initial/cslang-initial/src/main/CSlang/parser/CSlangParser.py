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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u0216\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\7")
        buf.write("\2v\n\2\f\2\16\2y\13\2\3\2\3\2\3\3\6\3~\n\3\r\3\16\3\177")
        buf.write("\3\4\3\4\3\4\5\4\u0085\n\4\3\4\3\4\3\4\7\4\u008a\n\4\f")
        buf.write("\4\16\4\u008d\13\4\3\4\3\4\3\5\3\5\3\5\5\5\u0094\n\5\3")
        buf.write("\6\6\6\u0097\n\6\r\6\16\6\u0098\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\7\t\u00ae\n\t\f\t\16\t\u00b1\13\t\3\t\5\t\u00b4\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\5\17\u00c4\n\17\3\20\3\20\3\21\3\21\3\22\3\22\3")
        buf.write("\22\5\22\u00cd\n\22\3\22\3\22\3\22\3\22\5\22\u00d3\n\22")
        buf.write("\3\23\3\23\3\23\7\23\u00d8\n\23\f\23\16\23\u00db\13\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00e3\n\24\f\24\16")
        buf.write("\24\u00e6\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u00ef\n\25\f\25\16\25\u00f2\13\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u00fb\n\26\f\26\16\26\u00fe\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0107\n\27\f")
        buf.write("\27\16\27\u010a\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\7\30\u0113\n\30\f\30\16\30\u0116\13\30\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u011c\n\31\3\32\3\32\3\32\5\32\u0121\n\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u012b\n")
        buf.write("\33\f\33\16\33\u012e\13\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u013b\n\34\3\34\7\34")
        buf.write("\u013e\n\34\f\34\16\34\u0141\13\34\3\35\3\35\5\35\u0145")
        buf.write("\n\35\3\35\3\35\3\35\5\35\u014a\n\35\3\35\3\35\3\35\5")
        buf.write("\35\u014f\n\35\3\35\3\35\5\35\u0153\n\35\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u0159\n\36\3\36\3\36\5\36\u015d\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0167\n\37\3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0173\n \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\5#\u017f\n#\3#\3#\3$\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\5$\u018c\n$\3$\3$\3$\3$\5$\u0192\n$\3%\3%\3")
        buf.write("%\5%\u0197\n%\3%\3%\3&\3&\3&\3&\3\'\3\'\5\'\u01a1\n\'")
        buf.write("\3\'\3\'\3\'\3\'\5\'\u01a7\n\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\7.\u01c3\n.\f.\16.\u01c6\13.\3.\3.\3/\3/\5/\u01cc\n")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\7\61\u01d6\n")
        buf.write("\61\f\61\16\61\u01d9\13\61\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u01f9\n\64\3\65\3\65\3\66\3\66\3")
        buf.write("\67\3\67\38\38\38\38\38\38\58\u0207\n8\39\39\3:\3:\3:")
        buf.write("\3:\7:\u020f\n:\f:\16:\u0212\13:\3:\3:\3:\2\t&(*,.\64")
        buf.write("\66;\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\f\4\2BBDD\3")
        buf.write("\2\62\65\3\2\60\61\3\2&\'\3\2()\3\2*-\4\2\35\35!!\6\2")
        buf.write("\25\30  $$DD\5\2\25\30$$DD\3\2\23\24\2\u021f\2w\3\2\2")
        buf.write("\2\4}\3\2\2\2\6\u0081\3\2\2\2\b\u0093\3\2\2\2\n\u0096")
        buf.write("\3\2\2\2\f\u009a\3\2\2\2\16\u00a3\3\2\2\2\20\u00b3\3\2")
        buf.write("\2\2\22\u00b5\3\2\2\2\24\u00b9\3\2\2\2\26\u00bb\3\2\2")
        buf.write("\2\30\u00bd\3\2\2\2\32\u00bf\3\2\2\2\34\u00c3\3\2\2\2")
        buf.write("\36\u00c5\3\2\2\2 \u00c7\3\2\2\2\"\u00d2\3\2\2\2$\u00d4")
        buf.write("\3\2\2\2&\u00dc\3\2\2\2(\u00e7\3\2\2\2*\u00f3\3\2\2\2")
        buf.write(",\u00ff\3\2\2\2.\u010b\3\2\2\2\60\u011b\3\2\2\2\62\u0120")
        buf.write("\3\2\2\2\64\u0122\3\2\2\2\66\u012f\3\2\2\28\u0152\3\2")
        buf.write("\2\2:\u015c\3\2\2\2<\u0166\3\2\2\2>\u0172\3\2\2\2@\u0174")
        buf.write("\3\2\2\2B\u0177\3\2\2\2D\u017b\3\2\2\2F\u0191\3\2\2\2")
        buf.write("H\u0193\3\2\2\2J\u019a\3\2\2\2L\u019e\3\2\2\2N\u01a8\3")
        buf.write("\2\2\2P\u01b0\3\2\2\2R\u01b3\3\2\2\2T\u01b6\3\2\2\2V\u01ba")
        buf.write("\3\2\2\2X\u01bd\3\2\2\2Z\u01c0\3\2\2\2\\\u01cb\3\2\2\2")
        buf.write("^\u01cd\3\2\2\2`\u01d2\3\2\2\2b\u01da\3\2\2\2d\u01dc\3")
        buf.write("\2\2\2f\u01f8\3\2\2\2h\u01fa\3\2\2\2j\u01fc\3\2\2\2l\u01fe")
        buf.write("\3\2\2\2n\u0206\3\2\2\2p\u0208\3\2\2\2r\u020a\3\2\2\2")
        buf.write("tv\5\4\3\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2xz\3")
        buf.write("\2\2\2yw\3\2\2\2z{\7\2\2\3{\3\3\2\2\2|~\5\6\4\2}|\3\2")
        buf.write("\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\5\3\2\2\2\u0081\u0084\7\33\2\2\u0082\u0083\7D\2\2\u0083")
        buf.write("\u0085\7\66\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2")
        buf.write("\2\u0085\u0086\3\2\2\2\u0086\u0087\7D\2\2\u0087\u008b")
        buf.write("\7@\2\2\u0088\u008a\5\b\5\2\u0089\u0088\3\2\2\2\u008a")
        buf.write("\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\7")
        buf.write("A\2\2\u008f\7\3\2\2\2\u0090\u0094\5\n\6\2\u0091\u0094")
        buf.write("\5D#\2\u0092\u0094\5\16\b\2\u0093\u0090\3\2\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\t\3\2\2\2\u0095")
        buf.write("\u0097\5\f\7\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\13\3\2")
        buf.write("\2\2\u009a\u009b\7#\2\2\u009b\u009c\t\2\2\2\u009c\u009d")
        buf.write("\7=\2\2\u009d\u009e\5\20\t\2\u009e\u009f\7<\2\2\u009f")
        buf.write("\u00a0\7;\2\2\u00a0\u00a1\5j\66\2\u00a1\u00a2\5Z.\2\u00a2")
        buf.write("\r\3\2\2\2\u00a3\u00a4\7#\2\2\u00a4\u00a5\7\34\2\2\u00a5")
        buf.write("\u00a6\7=\2\2\u00a6\u00a7\5\20\t\2\u00a7\u00a8\7<\2\2")
        buf.write("\u00a8\u00a9\5Z.\2\u00a9\17\3\2\2\2\u00aa\u00af\5\22\n")
        buf.write("\2\u00ab\u00ac\79\2\2\u00ac\u00ae\5\22\n\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b4\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00b4\3\2\2\2\u00b3\u00aa\3\2\2\2\u00b3\u00b2\3")
        buf.write("\2\2\2\u00b4\21\3\2\2\2\u00b5\u00b6\5`\61\2\u00b6\u00b7")
        buf.write("\7;\2\2\u00b7\u00b8\5j\66\2\u00b8\23\3\2\2\2\u00b9\u00ba")
        buf.write("\t\3\2\2\u00ba\25\3\2\2\2\u00bb\u00bc\t\4\2\2\u00bc\27")
        buf.write("\3\2\2\2\u00bd\u00be\t\5\2\2\u00be\31\3\2\2\2\u00bf\u00c0")
        buf.write("\7%\2\2\u00c0\33\3\2\2\2\u00c1\u00c4\5\36\20\2\u00c2\u00c4")
        buf.write("\5 \21\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\35\3\2\2\2\u00c5\u00c6\t\6\2\2\u00c6\37\3\2\2\2\u00c7")
        buf.write("\u00c8\t\7\2\2\u00c8!\3\2\2\2\u00c9\u00cc\5&\24\2\u00ca")
        buf.write("\u00cd\5\34\17\2\u00cb\u00cd\5\30\r\2\u00cc\u00ca\3\2")
        buf.write("\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf")
        buf.write("\5&\24\2\u00cf\u00d3\3\2\2\2\u00d0\u00d3\5p9\2\u00d1\u00d3")
        buf.write("\7D\2\2\u00d2\u00c9\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d3#\3\2\2\2\u00d4\u00d9\5&\24\2\u00d5")
        buf.write("\u00d6\79\2\2\u00d6\u00d8\5$\23\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da%\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd")
        buf.write("\b\24\1\2\u00dd\u00de\5(\25\2\u00de\u00e4\3\2\2\2\u00df")
        buf.write("\u00e0\f\4\2\2\u00e0\u00e1\7\67\2\2\u00e1\u00e3\5&\24")
        buf.write("\5\u00e2\u00df\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\'\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e7\u00e8\b\25\1\2\u00e8\u00e9\5*\26\2\u00e9")
        buf.write("\u00f0\3\2\2\2\u00ea\u00eb\f\4\2\2\u00eb\u00ec\5\34\17")
        buf.write("\2\u00ec\u00ed\5(\25\5\u00ed\u00ef\3\2\2\2\u00ee\u00ea")
        buf.write("\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1)\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3")
        buf.write("\u00f4\b\26\1\2\u00f4\u00f5\5,\27\2\u00f5\u00fc\3\2\2")
        buf.write("\2\u00f6\u00f7\f\4\2\2\u00f7\u00f8\5\30\r\2\u00f8\u00f9")
        buf.write("\5,\27\2\u00f9\u00fb\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fb")
        buf.write("\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd+\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\b\27\1")
        buf.write("\2\u0100\u0101\5.\30\2\u0101\u0108\3\2\2\2\u0102\u0103")
        buf.write("\f\4\2\2\u0103\u0104\5\26\f\2\u0104\u0105\5.\30\2\u0105")
        buf.write("\u0107\3\2\2\2\u0106\u0102\3\2\2\2\u0107\u010a\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109-\3\2\2")
        buf.write("\2\u010a\u0108\3\2\2\2\u010b\u010c\b\30\1\2\u010c\u010d")
        buf.write("\5\60\31\2\u010d\u0114\3\2\2\2\u010e\u010f\f\4\2\2\u010f")
        buf.write("\u0110\5\24\13\2\u0110\u0111\5\60\31\2\u0111\u0113\3\2")
        buf.write("\2\2\u0112\u010e\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115/\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0117\u0118\5\32\16\2\u0118\u0119\5\62\32\2\u0119")
        buf.write("\u011c\3\2\2\2\u011a\u011c\5\62\32\2\u011b\u0117\3\2\2")
        buf.write("\2\u011b\u011a\3\2\2\2\u011c\61\3\2\2\2\u011d\u011e\7")
        buf.write("\61\2\2\u011e\u0121\5\62\32\2\u011f\u0121\5\64\33\2\u0120")
        buf.write("\u011d\3\2\2\2\u0120\u011f\3\2\2\2\u0121\63\3\2\2\2\u0122")
        buf.write("\u0123\b\33\1\2\u0123\u0124\5\66\34\2\u0124\u012c\3\2")
        buf.write("\2\2\u0125\u0126\f\4\2\2\u0126\u0127\7>\2\2\u0127\u0128")
        buf.write("\5\64\33\2\u0128\u0129\7?\2\2\u0129\u012b\3\2\2\2\u012a")
        buf.write("\u0125\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\65\3\2\2\2\u012e\u012c\3\2")
        buf.write("\2\2\u012f\u0130\b\34\1\2\u0130\u0131\58\35\2\u0131\u013f")
        buf.write("\3\2\2\2\u0132\u0133\f\5\2\2\u0133\u0134\78\2\2\u0134")
        buf.write("\u013e\7D\2\2\u0135\u0136\f\4\2\2\u0136\u0137\78\2\2\u0137")
        buf.write("\u0138\7D\2\2\u0138\u013a\7=\2\2\u0139\u013b\5$\23\2\u013a")
        buf.write("\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\u013e\7<\2\2\u013d\u0132\3\2\2\2\u013d\u0135\3")
        buf.write("\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\67\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143")
        buf.write("\7D\2\2\u0143\u0145\78\2\2\u0144\u0142\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0153\7B\2\2\u0147")
        buf.write("\u0148\7D\2\2\u0148\u014a\78\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\7B\2\2")
        buf.write("\u014c\u014e\7=\2\2\u014d\u014f\5$\23\2\u014e\u014d\3")
        buf.write("\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0153")
        buf.write("\7<\2\2\u0151\u0153\5:\36\2\u0152\u0144\3\2\2\2\u0152")
        buf.write("\u0149\3\2\2\2\u0152\u0151\3\2\2\2\u01539\3\2\2\2\u0154")
        buf.write("\u0155\7\37\2\2\u0155\u0156\7D\2\2\u0156\u0158\7=\2\2")
        buf.write("\u0157\u0159\5$\23\2\u0158\u0157\3\2\2\2\u0158\u0159\3")
        buf.write("\2\2\2\u0159\u015a\3\2\2\2\u015a\u015d\7<\2\2\u015b\u015d")
        buf.write("\5<\37\2\u015c\u0154\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write(";\3\2\2\2\u015e\u015f\7=\2\2\u015f\u0160\5&\24\2\u0160")
        buf.write("\u0161\7<\2\2\u0161\u0167\3\2\2\2\u0162\u0167\5n8\2\u0163")
        buf.write("\u0167\7\36\2\2\u0164\u0167\7D\2\2\u0165\u0167\7\32\2")
        buf.write("\2\u0166\u015e\3\2\2\2\u0166\u0162\3\2\2\2\u0166\u0163")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0165\3\2\2\2\u0167")
        buf.write("=\3\2\2\2\u0168\u0173\5D#\2\u0169\u0173\5@!\2\u016a\u0173")
        buf.write("\5L\'\2\u016b\u0173\5N(\2\u016c\u0173\5P)\2\u016d\u0173")
        buf.write("\5R*\2\u016e\u0173\5T+\2\u016f\u0173\5V,\2\u0170\u0173")
        buf.write("\5X-\2\u0171\u0173\5d\63\2\u0172\u0168\3\2\2\2\u0172\u0169")
        buf.write("\3\2\2\2\u0172\u016a\3\2\2\2\u0172\u016b\3\2\2\2\u0172")
        buf.write("\u016c\3\2\2\2\u0172\u016d\3\2\2\2\u0172\u016e\3\2\2\2")
        buf.write("\u0172\u016f\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0171\3")
        buf.write("\2\2\2\u0173?\3\2\2\2\u0174\u0175\5B\"\2\u0175\u0176\7")
        buf.write(":\2\2\u0176A\3\2\2\2\u0177\u0178\5\\/\2\u0178\u0179\7")
        buf.write("/\2\2\u0179\u017a\5&\24\2\u017aC\3\2\2\2\u017b\u017e\5")
        buf.write("h\65\2\u017c\u017f\5F$\2\u017d\u017f\5H%\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\7:\2\2\u0181E\3\2\2\2\u0182\u0183\5b\62\2\u0183")
        buf.write("\u0184\79\2\2\u0184\u0185\5F$\2\u0185\u0186\79\2\2\u0186")
        buf.write("\u0187\5&\24\2\u0187\u0192\3\2\2\2\u0188\u0189\5b\62\2")
        buf.write("\u0189\u018b\7;\2\2\u018a\u018c\5J&\2\u018b\u018a\3\2")
        buf.write("\2\2\u018b\u018c\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e")
        buf.write("\5l\67\2\u018e\u018f\7.\2\2\u018f\u0190\5&\24\2\u0190")
        buf.write("\u0192\3\2\2\2\u0191\u0182\3\2\2\2\u0191\u0188\3\2\2\2")
        buf.write("\u0192G\3\2\2\2\u0193\u0194\5`\61\2\u0194\u0196\7;\2\2")
        buf.write("\u0195\u0197\5J&\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2")
        buf.write("\2\2\u0197\u0198\3\2\2\2\u0198\u0199\5l\67\2\u0199I\3")
        buf.write("\2\2\2\u019a\u019b\7>\2\2\u019b\u019c\7F\2\2\u019c\u019d")
        buf.write("\7?\2\2\u019dK\3\2\2\2\u019e\u01a0\7\20\2\2\u019f\u01a1")
        buf.write("\5Z.\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a3\5\"\22\2\u01a3\u01a6\5Z.\2\u01a4")
        buf.write("\u01a5\7\21\2\2\u01a5\u01a7\5Z.\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7M\3\2\2\2\u01a8\u01a9\7\22\2")
        buf.write("\2\u01a9\u01aa\5B\"\2\u01aa\u01ab\7:\2\2\u01ab\u01ac\5")
        buf.write("\"\22\2\u01ac\u01ad\7:\2\2\u01ad\u01ae\5B\"\2\u01ae\u01af")
        buf.write("\5Z.\2\u01afO\3\2\2\2\u01b0\u01b1\7\16\2\2\u01b1\u01b2")
        buf.write("\7:\2\2\u01b2Q\3\2\2\2\u01b3\u01b4\7\17\2\2\u01b4\u01b5")
        buf.write("\7:\2\2\u01b5S\3\2\2\2\u01b6\u01b7\7\31\2\2\u01b7\u01b8")
        buf.write("\5&\24\2\u01b8\u01b9\7:\2\2\u01b9U\3\2\2\2\u01ba\u01bb")
        buf.write("\5\66\34\2\u01bb\u01bc\7:\2\2\u01bcW\3\2\2\2\u01bd\u01be")
        buf.write("\58\35\2\u01be\u01bf\7:\2\2\u01bfY\3\2\2\2\u01c0\u01c4")
        buf.write("\7@\2\2\u01c1\u01c3\5> \2\u01c2\u01c1\3\2\2\2\u01c3\u01c6")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\7A\2\2")
        buf.write("\u01c8[\3\2\2\2\u01c9\u01cc\5^\60\2\u01ca\u01cc\5b\62")
        buf.write("\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc]\3\2")
        buf.write("\2\2\u01cd\u01ce\5&\24\2\u01ce\u01cf\7>\2\2\u01cf\u01d0")
        buf.write("\5&\24\2\u01d0\u01d1\7?\2\2\u01d1_\3\2\2\2\u01d2\u01d7")
        buf.write("\5b\62\2\u01d3\u01d4\79\2\2\u01d4\u01d6\5b\62\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8a\3\2\2\2\u01d9\u01d7\3\2\2")
        buf.write("\2\u01da\u01db\t\2\2\2\u01dbc\3\2\2\2\u01dc\u01dd\7\3")
        buf.write("\2\2\u01dd\u01de\5f\64\2\u01de\u01df\7:\2\2\u01dfe\3\2")
        buf.write("\2\2\u01e0\u01f9\7\4\2\2\u01e1\u01e2\7\5\2\2\u01e2\u01e3")
        buf.write("\7=\2\2\u01e3\u01e4\5&\24\2\u01e4\u01e5\7<\2\2\u01e5\u01f9")
        buf.write("\3\2\2\2\u01e6\u01f9\7\6\2\2\u01e7\u01e8\7\7\2\2\u01e8")
        buf.write("\u01e9\7=\2\2\u01e9\u01ea\5&\24\2\u01ea\u01eb\7<\2\2\u01eb")
        buf.write("\u01f9\3\2\2\2\u01ec\u01f9\7\b\2\2\u01ed\u01ee\7\t\2\2")
        buf.write("\u01ee\u01ef\7=\2\2\u01ef\u01f0\5&\24\2\u01f0\u01f1\7")
        buf.write("<\2\2\u01f1\u01f9\3\2\2\2\u01f2\u01f9\7\n\2\2\u01f3\u01f4")
        buf.write("\7\13\2\2\u01f4\u01f5\7=\2\2\u01f5\u01f6\5&\24\2\u01f6")
        buf.write("\u01f7\7<\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01e0\3\2\2\2")
        buf.write("\u01f8\u01e1\3\2\2\2\u01f8\u01e6\3\2\2\2\u01f8\u01e7\3")
        buf.write("\2\2\2\u01f8\u01ec\3\2\2\2\u01f8\u01ed\3\2\2\2\u01f8\u01f2")
        buf.write("\3\2\2\2\u01f8\u01f3\3\2\2\2\u01f9g\3\2\2\2\u01fa\u01fb")
        buf.write("\t\b\2\2\u01fbi\3\2\2\2\u01fc\u01fd\t\t\2\2\u01fdk\3\2")
        buf.write("\2\2\u01fe\u01ff\t\n\2\2\u01ffm\3\2\2\2\u0200\u0207\7")
        buf.write("G\2\2\u0201\u0207\7E\2\2\u0202\u0207\5p9\2\u0203\u0207")
        buf.write("\7C\2\2\u0204\u0207\5r:\2\u0205\u0207\7F\2\2\u0206\u0200")
        buf.write("\3\2\2\2\u0206\u0201\3\2\2\2\u0206\u0202\3\2\2\2\u0206")
        buf.write("\u0203\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0205\3\2\2\2")
        buf.write("\u0207o\3\2\2\2\u0208\u0209\t\13\2\2\u0209q\3\2\2\2\u020a")
        buf.write("\u020b\7>\2\2\u020b\u0210\5n8\2\u020c\u020d\79\2\2\u020d")
        buf.write("\u020f\5n8\2\u020e\u020c\3\2\2\2\u020f\u0212\3\2\2\2\u0210")
        buf.write("\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0213\3\2\2\2")
        buf.write("\u0212\u0210\3\2\2\2\u0213\u0214\7?\2\2\u0214s\3\2\2\2")
        buf.write("-w\177\u0084\u008b\u0093\u0098\u00af\u00b3\u00c3\u00cc")
        buf.write("\u00d2\u00d9\u00e4\u00f0\u00fc\u0108\u0114\u011b\u0120")
        buf.write("\u012c\u013a\u013d\u013f\u0144\u0149\u014e\u0152\u0158")
        buf.write("\u015c\u0166\u0172\u017e\u018b\u0191\u0196\u01a0\u01a6")
        buf.write("\u01c4\u01cb\u01d7\u01f8\u0206\u0210")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'io.'", "'@readInt()'", "'@writeInt'", 
                     "'@readFloat()'", "'@writeFloat'", "'@readBool()'", 
                     "'@writeBool'", "'@readString()'", "'@writeString'", 
                     "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'if'", "'else'", "'for'", "'true'", "'false'", "'int'", 
                     "'float'", "'bool'", "'string'", "'return'", "'null'", 
                     "'class'", "'constructor'", "'var'", "'self'", "'new'", 
                     "'void'", "'const'", "'constant'", "'func'", "'array'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'='", "':='", "'+'", "'-'", "'*'", 
                     "'\\'", "'%'", "'/'", "'<-'", "'^'", "'.'", "','", 
                     "';'", "':'", "')'", "'('", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                      "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", 
                      "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
                      "VOID", "CONST", "CONSTANT", "FUNC", "ARRAY", "NOT", 
                      "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
                      "LESS_EQUAL", "GREATER_EQUAL", "INITIAL", "ASSIGN", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", 
                      "DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", "DOT", 
                      "COMMA", "SEMICOLON", "COLON", "RPAREN", "LPAREN", 
                      "LBRACK", "RBRACK", "LBRASE", "RBRASE", "AT_ID", "STRING_LITERAL", 
                      "ID", "FLOAT_LITERAL", "NON_ZERO_INT", "INT_LITERAL", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_lst = 1
    RULE_class_dcl = 2
    RULE_class_body = 3
    RULE_method_lst = 4
    RULE_method_dcl = 5
    RULE_constructor_decl = 6
    RULE_param_lst = 7
    RULE_param = 8
    RULE_multiplying = 9
    RULE_adding = 10
    RULE_logical_bin = 11
    RULE_logical_not = 12
    RULE_relational = 13
    RULE_relat_bool = 14
    RULE_relat_int_float = 15
    RULE_relational_expr = 16
    RULE_expr_lst = 17
    RULE_expr = 18
    RULE_expr1 = 19
    RULE_expr2 = 20
    RULE_expr3 = 21
    RULE_expr4 = 22
    RULE_expr5 = 23
    RULE_expr6 = 24
    RULE_expr7 = 25
    RULE_expr8 = 26
    RULE_expr9 = 27
    RULE_expr10 = 28
    RULE_expr11 = 29
    RULE_statements = 30
    RULE_assign_decl = 31
    RULE_attribute_assign = 32
    RULE_attribute_decl = 33
    RULE_attribute_init_nom = 34
    RULE_attribute_init_typ = 35
    RULE_array_element_typ = 36
    RULE_if_state = 37
    RULE_for_state = 38
    RULE_break_state = 39
    RULE_continue_state = 40
    RULE_return_state = 41
    RULE_instance_method_invo_access = 42
    RULE_static_method_invo_access = 43
    RULE_block_state = 44
    RULE_lhs = 45
    RULE_index_op = 46
    RULE_id_lst = 47
    RULE_id_access = 48
    RULE_io_st = 49
    RULE_io = 50
    RULE_fm = 51
    RULE_typ = 52
    RULE_attri_type = 53
    RULE_literal = 54
    RULE_bool_literal = 55
    RULE_array = 56

    ruleNames =  [ "program", "class_lst", "class_dcl", "class_body", "method_lst", 
                   "method_dcl", "constructor_decl", "param_lst", "param", 
                   "multiplying", "adding", "logical_bin", "logical_not", 
                   "relational", "relat_bool", "relat_int_float", "relational_expr", 
                   "expr_lst", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "statements", "assign_decl", "attribute_assign", 
                   "attribute_decl", "attribute_init_nom", "attribute_init_typ", 
                   "array_element_typ", "if_state", "for_state", "break_state", 
                   "continue_state", "return_state", "instance_method_invo_access", 
                   "static_method_invo_access", "block_state", "lhs", "index_op", 
                   "id_lst", "id_access", "io_st", "io", "fm", "typ", "attri_type", 
                   "literal", "bool_literal", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    BLOCK_COMMENT=10
    LINE_COMMENT=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSE=15
    FOR=16
    TRUE=17
    FALSE=18
    INT=19
    FLOAT=20
    BOOL=21
    STRING=22
    RETURN=23
    NULL=24
    CLASS=25
    CONSTRUCTOR=26
    VAR=27
    SELF=28
    NEW=29
    VOID=30
    CONST=31
    CONSTANT=32
    FUNC=33
    ARRAY=34
    NOT=35
    AND=36
    OR=37
    EQUAL=38
    NOT_EQUAL=39
    LESS=40
    GREATER=41
    LESS_EQUAL=42
    GREATER_EQUAL=43
    INITIAL=44
    ASSIGN=45
    PLUS=46
    MINUS=47
    MULTIPLY=48
    DIVIDE_I=49
    DIVIDE_I_L=50
    DIVIDE_F=51
    SUPER_CLASS=52
    STRING_CONCAT=53
    DOT=54
    COMMA=55
    SEMICOLON=56
    COLON=57
    RPAREN=58
    LPAREN=59
    LBRACK=60
    RBRACK=61
    LBRASE=62
    RBRASE=63
    AT_ID=64
    STRING_LITERAL=65
    ID=66
    FLOAT_LITERAL=67
    NON_ZERO_INT=68
    INT_LITERAL=69
    WS=70
    ERROR_CHAR=71
    UNCLOSE_STRING=72
    ILLEGAL_ESCAPE=73

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

        def class_lst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_lstContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_lstContext,i)


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
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CLASS:
                self.state = 114
                self.class_lst()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_dclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_lst" ):
                return visitor.visitClass_lst(self)
            else:
                return visitor.visitChildren(self)




    def class_lst(self):

        localctx = CSlangParser.Class_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 122
                    self.class_dcl()

                else:
                    raise NoViableAltException(self)
                self.state = 125 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def LBRASE(self):
            return self.getToken(CSlangParser.LBRASE, 0)

        def RBRASE(self):
            return self.getToken(CSlangParser.RBRASE, 0)

        def SUPER_CLASS(self):
            return self.getToken(CSlangParser.SUPER_CLASS, 0)

        def class_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_bodyContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_bodyContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dcl" ):
                return visitor.visitClass_dcl(self)
            else:
                return visitor.visitChildren(self)




    def class_dcl(self):

        localctx = CSlangParser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(CSlangParser.CLASS)
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 128
                self.match(CSlangParser.ID)
                self.state = 129
                self.match(CSlangParser.SUPER_CLASS)


            self.state = 132
            self.match(CSlangParser.ID)
            self.state = 133
            self.match(CSlangParser.LBRASE)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 134
                self.class_body()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(CSlangParser.RBRASE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_lst(self):
            return self.getTypedRuleContext(CSlangParser.Method_lstContext,0)


        def attribute_decl(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_declContext,0)


        def constructor_decl(self):
            return self.getTypedRuleContext(CSlangParser.Constructor_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = CSlangParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 142
                self.method_lst()
                pass

            elif la_ == 2:
                self.state = 143
                self.attribute_decl()
                pass

            elif la_ == 3:
                self.state = 144
                self.constructor_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Method_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Method_dclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_lst" ):
                return visitor.visitMethod_lst(self)
            else:
                return visitor.visitChildren(self)




    def method_lst(self):

        localctx = CSlangParser.Method_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 147
                    self.method_dcl()

                else:
                    raise NoViableAltException(self)
                self.state = 150 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def param_lst(self):
            return self.getTypedRuleContext(CSlangParser.Param_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def block_state(self):
            return self.getTypedRuleContext(CSlangParser.Block_stateContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dcl" ):
                return visitor.visitMethod_dcl(self)
            else:
                return visitor.visitChildren(self)




    def method_dcl(self):

        localctx = CSlangParser.Method_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(CSlangParser.FUNC)
            self.state = 153
            _la = self._input.LA(1)
            if not(_la==CSlangParser.AT_ID or _la==CSlangParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 154
            self.match(CSlangParser.LPAREN)
            self.state = 155
            self.param_lst()
            self.state = 156
            self.match(CSlangParser.RPAREN)
            self.state = 157
            self.match(CSlangParser.COLON)
            self.state = 158
            self.typ()
            self.state = 159
            self.block_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def param_lst(self):
            return self.getTypedRuleContext(CSlangParser.Param_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def block_state(self):
            return self.getTypedRuleContext(CSlangParser.Block_stateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(CSlangParser.FUNC)
            self.state = 162
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 163
            self.match(CSlangParser.LPAREN)
            self.state = 164
            self.param_lst()
            self.state = 165
            self.match(CSlangParser.RPAREN)
            self.state = 166
            self.block_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ParamContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_param_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lst" ):
                return visitor.visitParam_lst(self)
            else:
                return visitor.visitChildren(self)




    def param_lst(self):

        localctx = CSlangParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.AT_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.param()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 169
                    self.match(CSlangParser.COMMA)
                    self.state = 170
                    self.param()
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [CSlangParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_lst(self):
            return self.getTypedRuleContext(CSlangParser.Id_lstContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.id_lst()
            self.state = 180
            self.match(CSlangParser.COLON)
            self.state = 181
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(CSlangParser.MULTIPLY, 0)

        def DIVIDE_F(self):
            return self.getToken(CSlangParser.DIVIDE_F, 0)

        def DIVIDE_I(self):
            return self.getToken(CSlangParser.DIVIDE_I, 0)

        def DIVIDE_I_L(self):
            return self.getToken(CSlangParser.DIVIDE_I_L, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)




    def multiplying(self):

        localctx = CSlangParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MULTIPLY) | (1 << CSlangParser.DIVIDE_I) | (1 << CSlangParser.DIVIDE_I_L) | (1 << CSlangParser.DIVIDE_F))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(CSlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)




    def adding(self):

        localctx = CSlangParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==CSlangParser.PLUS or _la==CSlangParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_binContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_logical_bin

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_bin" ):
                return visitor.visitLogical_bin(self)
            else:
                return visitor.visitChildren(self)




    def logical_bin(self):

        localctx = CSlangParser.Logical_binContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logical_bin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_logical_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_not" ):
                return visitor.visitLogical_not(self)
            else:
                return visitor.visitChildren(self)




    def logical_not(self):

        localctx = CSlangParser.Logical_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logical_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(CSlangParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relat_bool(self):
            return self.getTypedRuleContext(CSlangParser.Relat_boolContext,0)


        def relat_int_float(self):
            return self.getTypedRuleContext(CSlangParser.Relat_int_floatContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = CSlangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relational)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.EQUAL, CSlangParser.NOT_EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.relat_bool()
                pass
            elif token in [CSlangParser.LESS, CSlangParser.GREATER, CSlangParser.LESS_EQUAL, CSlangParser.GREATER_EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.relat_int_float()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relat_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(CSlangParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_relat_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelat_bool" ):
                return visitor.visitRelat_bool(self)
            else:
                return visitor.visitChildren(self)




    def relat_bool(self):

        localctx = CSlangParser.Relat_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relat_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==CSlangParser.EQUAL or _la==CSlangParser.NOT_EQUAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relat_int_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(CSlangParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(CSlangParser.GREATER_EQUAL, 0)

        def GREATER(self):
            return self.getToken(CSlangParser.GREATER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_relat_int_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelat_int_float" ):
                return visitor.visitRelat_int_float(self)
            else:
                return visitor.visitChildren(self)




    def relat_int_float(self):

        localctx = CSlangParser.Relat_int_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relat_int_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.LESS) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.LESS_EQUAL) | (1 << CSlangParser.GREATER_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def relational(self):
            return self.getTypedRuleContext(CSlangParser.RelationalContext,0)


        def logical_bin(self):
            return self.getTypedRuleContext(CSlangParser.Logical_binContext,0)


        def bool_literal(self):
            return self.getTypedRuleContext(CSlangParser.Bool_literalContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = CSlangParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_relational_expr)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.expr(0)
                self.state = 202
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.EQUAL, CSlangParser.NOT_EQUAL, CSlangParser.LESS, CSlangParser.GREATER, CSlangParser.LESS_EQUAL, CSlangParser.GREATER_EQUAL]:
                    self.state = 200
                    self.relational()
                    pass
                elif token in [CSlangParser.AND, CSlangParser.OR]:
                    self.state = 201
                    self.logical_bin()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 204
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.bool_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(CSlangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def expr_lst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr_lstContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr_lstContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lst" ):
                return visitor.visitExpr_lst(self)
            else:
                return visitor.visitChildren(self)




    def expr_lst(self):

        localctx = CSlangParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.expr(0)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 211
                    self.match(CSlangParser.COMMA)
                    self.state = 212
                    self.expr_lst() 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(CSlangParser.Expr1Context,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def STRING_CONCAT(self):
            return self.getToken(CSlangParser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    self.match(CSlangParser.STRING_CONCAT)
                    self.state = 223
                    self.expr(3) 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def relational(self):
            return self.getTypedRuleContext(CSlangParser.RelationalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 233
                    self.relational()
                    self.state = 234
                    self.expr1(3) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def logical_bin(self):
            return self.getTypedRuleContext(CSlangParser.Logical_binContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    self.logical_bin()
                    self.state = 246
                    self.expr3(0) 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def adding(self):
            return self.getTypedRuleContext(CSlangParser.AddingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    self.adding()
                    self.state = 258
                    self.expr4(0) 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def multiplying(self):
            return self.getTypedRuleContext(CSlangParser.MultiplyingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 269
                    self.multiplying()
                    self.state = 270
                    self.expr5() 
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_not(self):
            return self.getTypedRuleContext(CSlangParser.Logical_notContext,0)


        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr5)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.logical_not()
                self.state = 278
                self.expr6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.AT_ID, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr6)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(CSlangParser.MINUS)
                self.state = 284
                self.expr6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.AT_ID, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def expr7(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr7Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr7Context,i)


        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 291
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 292
                    self.match(CSlangParser.LBRACK)
                    self.state = 293
                    self.expr7(0)
                    self.state = 294
                    self.match(CSlangParser.RBRACK) 
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 315
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 304
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 305
                        self.match(CSlangParser.DOT)
                        self.state = 306
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 307
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 308
                        self.match(CSlangParser.DOT)
                        self.state = 309
                        self.match(CSlangParser.ID)

                        self.state = 310
                        self.match(CSlangParser.LPAREN)
                        self.state = 312
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & ((1 << (CSlangParser.TRUE - 17)) | (1 << (CSlangParser.FALSE - 17)) | (1 << (CSlangParser.NULL - 17)) | (1 << (CSlangParser.SELF - 17)) | (1 << (CSlangParser.NEW - 17)) | (1 << (CSlangParser.NOT - 17)) | (1 << (CSlangParser.MINUS - 17)) | (1 << (CSlangParser.LPAREN - 17)) | (1 << (CSlangParser.LBRACK - 17)) | (1 << (CSlangParser.AT_ID - 17)) | (1 << (CSlangParser.STRING_LITERAL - 17)) | (1 << (CSlangParser.ID - 17)) | (1 << (CSlangParser.FLOAT_LITERAL - 17)) | (1 << (CSlangParser.NON_ZERO_INT - 17)) | (1 << (CSlangParser.INT_LITERAL - 17)))) != 0):
                            self.state = 311
                            self.expr_lst()


                        self.state = 314
                        self.match(CSlangParser.RPAREN)
                        pass

             
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 320
                    self.match(CSlangParser.ID)
                    self.state = 321
                    self.match(CSlangParser.DOT)


                self.state = 324
                self.match(CSlangParser.AT_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 325
                    self.match(CSlangParser.ID)
                    self.state = 326
                    self.match(CSlangParser.DOT)


                self.state = 329
                self.match(CSlangParser.AT_ID)

                self.state = 330
                self.match(CSlangParser.LPAREN)
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & ((1 << (CSlangParser.TRUE - 17)) | (1 << (CSlangParser.FALSE - 17)) | (1 << (CSlangParser.NULL - 17)) | (1 << (CSlangParser.SELF - 17)) | (1 << (CSlangParser.NEW - 17)) | (1 << (CSlangParser.NOT - 17)) | (1 << (CSlangParser.MINUS - 17)) | (1 << (CSlangParser.LPAREN - 17)) | (1 << (CSlangParser.LBRACK - 17)) | (1 << (CSlangParser.AT_ID - 17)) | (1 << (CSlangParser.STRING_LITERAL - 17)) | (1 << (CSlangParser.ID - 17)) | (1 << (CSlangParser.FLOAT_LITERAL - 17)) | (1 << (CSlangParser.NON_ZERO_INT - 17)) | (1 << (CSlangParser.INT_LITERAL - 17)))) != 0):
                    self.state = 331
                    self.expr_lst()


                self.state = 334
                self.match(CSlangParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def expr11(self):
            return self.getTypedRuleContext(CSlangParser.Expr11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(CSlangParser.NEW)
                self.state = 339
                self.match(CSlangParser.ID)

                self.state = 340
                self.match(CSlangParser.LPAREN)
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & ((1 << (CSlangParser.TRUE - 17)) | (1 << (CSlangParser.FALSE - 17)) | (1 << (CSlangParser.NULL - 17)) | (1 << (CSlangParser.SELF - 17)) | (1 << (CSlangParser.NEW - 17)) | (1 << (CSlangParser.NOT - 17)) | (1 << (CSlangParser.MINUS - 17)) | (1 << (CSlangParser.LPAREN - 17)) | (1 << (CSlangParser.LBRACK - 17)) | (1 << (CSlangParser.AT_ID - 17)) | (1 << (CSlangParser.STRING_LITERAL - 17)) | (1 << (CSlangParser.ID - 17)) | (1 << (CSlangParser.FLOAT_LITERAL - 17)) | (1 << (CSlangParser.NON_ZERO_INT - 17)) | (1 << (CSlangParser.INT_LITERAL - 17)))) != 0):
                    self.state = 341
                    self.expr_lst()


                self.state = 344
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr11)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(CSlangParser.LPAREN)
                self.state = 349
                self.expr(0)
                self.state = 350
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.match(CSlangParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_declContext,0)


        def assign_decl(self):
            return self.getTypedRuleContext(CSlangParser.Assign_declContext,0)


        def if_state(self):
            return self.getTypedRuleContext(CSlangParser.If_stateContext,0)


        def for_state(self):
            return self.getTypedRuleContext(CSlangParser.For_stateContext,0)


        def break_state(self):
            return self.getTypedRuleContext(CSlangParser.Break_stateContext,0)


        def continue_state(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stateContext,0)


        def return_state(self):
            return self.getTypedRuleContext(CSlangParser.Return_stateContext,0)


        def instance_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Instance_method_invo_accessContext,0)


        def static_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_invo_accessContext,0)


        def io_st(self):
            return self.getTypedRuleContext(CSlangParser.Io_stContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statements)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.assign_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.if_state()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.for_state()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 362
                self.break_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 363
                self.continue_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 364
                self.return_state()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 365
                self.instance_method_invo_access()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 366
                self.static_method_invo_access()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 367
                self.io_st()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_assign(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_assignContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assign_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_decl" ):
                return visitor.visitAssign_decl(self)
            else:
                return visitor.visitChildren(self)




    def assign_decl(self):

        localctx = CSlangParser.Assign_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assign_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.attribute_assign()
            self.state = 371
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_assign" ):
                return visitor.visitAttribute_assign(self)
            else:
                return visitor.visitChildren(self)




    def attribute_assign(self):

        localctx = CSlangParser.Attribute_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_attribute_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.lhs()
            self.state = 374
            self.match(CSlangParser.ASSIGN)
            self.state = 375
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fm(self):
            return self.getTypedRuleContext(CSlangParser.FmContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def attribute_init_nom(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_init_nomContext,0)


        def attribute_init_typ(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_init_typContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = CSlangParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.fm()
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 378
                self.attribute_init_nom()
                pass

            elif la_ == 2:
                self.state = 379
                self.attribute_init_typ()
                pass


            self.state = 382
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_init_nomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_access(self):
            return self.getTypedRuleContext(CSlangParser.Id_accessContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def attribute_init_nom(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_init_nomContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def attri_type(self):
            return self.getTypedRuleContext(CSlangParser.Attri_typeContext,0)


        def INITIAL(self):
            return self.getToken(CSlangParser.INITIAL, 0)

        def array_element_typ(self):
            return self.getTypedRuleContext(CSlangParser.Array_element_typContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_init_nom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_init_nom" ):
                return visitor.visitAttribute_init_nom(self)
            else:
                return visitor.visitChildren(self)




    def attribute_init_nom(self):

        localctx = CSlangParser.Attribute_init_nomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_attribute_init_nom)
        self._la = 0 # Token type
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.id_access()
                self.state = 385
                self.match(CSlangParser.COMMA)
                self.state = 386
                self.attribute_init_nom()
                self.state = 387
                self.match(CSlangParser.COMMA)
                self.state = 388
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.id_access()
                self.state = 391
                self.match(CSlangParser.COLON)
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.LBRACK:
                    self.state = 392
                    self.array_element_typ()


                self.state = 395
                self.attri_type()
                self.state = 396
                self.match(CSlangParser.INITIAL)
                self.state = 397
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_init_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_lst(self):
            return self.getTypedRuleContext(CSlangParser.Id_lstContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def attri_type(self):
            return self.getTypedRuleContext(CSlangParser.Attri_typeContext,0)


        def array_element_typ(self):
            return self.getTypedRuleContext(CSlangParser.Array_element_typContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_init_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_init_typ" ):
                return visitor.visitAttribute_init_typ(self)
            else:
                return visitor.visitChildren(self)




    def attribute_init_typ(self):

        localctx = CSlangParser.Attribute_init_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_attribute_init_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.id_lst()
            self.state = 402
            self.match(CSlangParser.COLON)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBRACK:
                self.state = 403
                self.array_element_typ()


            self.state = 406
            self.attri_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def NON_ZERO_INT(self):
            return self.getToken(CSlangParser.NON_ZERO_INT, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_element_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_typ" ):
                return visitor.visitArray_element_typ(self)
            else:
                return visitor.visitChildren(self)




    def array_element_typ(self):

        localctx = CSlangParser.Array_element_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_element_typ)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(CSlangParser.LBRACK)
            self.state = 409
            self.match(CSlangParser.NON_ZERO_INT)
            self.state = 410
            self.match(CSlangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def relational_expr(self):
            return self.getTypedRuleContext(CSlangParser.Relational_exprContext,0)


        def block_state(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_stateContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_stateContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_state" ):
                return visitor.visitIf_state(self)
            else:
                return visitor.visitChildren(self)




    def if_state(self):

        localctx = CSlangParser.If_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_if_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(CSlangParser.IF)
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBRASE:
                self.state = 413
                self.block_state()


            self.state = 416
            self.relational_expr()
            self.state = 417
            self.block_state()
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 418
                self.match(CSlangParser.ELSE)
                self.state = 419
                self.block_state()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def attribute_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Attribute_assignContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Attribute_assignContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMICOLON)
            else:
                return self.getToken(CSlangParser.SEMICOLON, i)

        def relational_expr(self):
            return self.getTypedRuleContext(CSlangParser.Relational_exprContext,0)


        def block_state(self):
            return self.getTypedRuleContext(CSlangParser.Block_stateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_state" ):
                return visitor.visitFor_state(self)
            else:
                return visitor.visitChildren(self)




    def for_state(self):

        localctx = CSlangParser.For_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(CSlangParser.FOR)
            self.state = 423
            self.attribute_assign()
            self.state = 424
            self.match(CSlangParser.SEMICOLON)
            self.state = 425
            self.relational_expr()
            self.state = 426
            self.match(CSlangParser.SEMICOLON)
            self.state = 427
            self.attribute_assign()
            self.state = 428
            self.block_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_state" ):
                return visitor.visitBreak_state(self)
            else:
                return visitor.visitChildren(self)




    def break_state(self):

        localctx = CSlangParser.Break_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(CSlangParser.BREAK)
            self.state = 431
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_state" ):
                return visitor.visitContinue_state(self)
            else:
                return visitor.visitChildren(self)




    def continue_state(self):

        localctx = CSlangParser.Continue_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(CSlangParser.CONTINUE)
            self.state = 434
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_return_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_state" ):
                return visitor.visitReturn_state(self)
            else:
                return visitor.visitChildren(self)




    def return_state(self):

        localctx = CSlangParser.Return_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(CSlangParser.RETURN)
            self.state = 437
            self.expr(0)
            self.state = 438
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invo_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instance_method_invo_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invo_access" ):
                return visitor.visitInstance_method_invo_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invo_access(self):

        localctx = CSlangParser.Instance_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_instance_method_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.expr8(0)
            self.state = 441
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invo_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_static_method_invo_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invo_access" ):
                return visitor.visitStatic_method_invo_access(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invo_access(self):

        localctx = CSlangParser.Static_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_static_method_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.expr9()
            self.state = 444
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRASE(self):
            return self.getToken(CSlangParser.LBRASE, 0)

        def RBRASE(self):
            return self.getToken(CSlangParser.RBRASE, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StatementsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StatementsContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_block_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_state" ):
                return visitor.visitBlock_state(self)
            else:
                return visitor.visitChildren(self)




    def block_state(self):

        localctx = CSlangParser.Block_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(CSlangParser.LBRASE)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.NULL) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.NOT) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.LPAREN) | (1 << CSlangParser.LBRACK))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSlangParser.AT_ID - 64)) | (1 << (CSlangParser.STRING_LITERAL - 64)) | (1 << (CSlangParser.ID - 64)) | (1 << (CSlangParser.FLOAT_LITERAL - 64)) | (1 << (CSlangParser.NON_ZERO_INT - 64)) | (1 << (CSlangParser.INT_LITERAL - 64)))) != 0):
                self.state = 447
                self.statements()
                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 453
            self.match(CSlangParser.RBRASE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_op(self):
            return self.getTypedRuleContext(CSlangParser.Index_opContext,0)


        def id_access(self):
            return self.getTypedRuleContext(CSlangParser.Id_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lhs)
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.id_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = CSlangParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.expr(0)
            self.state = 460
            self.match(CSlangParser.LBRACK)
            self.state = 461
            self.expr(0)
            self.state = 462
            self.match(CSlangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Id_accessContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Id_accessContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_id_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_lst" ):
                return visitor.visitId_lst(self)
            else:
                return visitor.visitChildren(self)




    def id_lst(self):

        localctx = CSlangParser.Id_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_id_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.id_access()
            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 465
                self.match(CSlangParser.COMMA)
                self.state = 466
                self.id_access()
                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_id_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_access" ):
                return visitor.visitId_access(self)
            else:
                return visitor.visitChildren(self)




    def id_access(self):

        localctx = CSlangParser.Id_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_id_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not(_la==CSlangParser.AT_ID or _la==CSlangParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_stContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def io(self):
            return self.getTypedRuleContext(CSlangParser.IoContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_io_st

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_st" ):
                return visitor.visitIo_st(self)
            else:
                return visitor.visitChildren(self)




    def io_st(self):

        localctx = CSlangParser.Io_stContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_io_st)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(CSlangParser.T__0)
            self.state = 475
            self.io()
            self.state = 476
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_io

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo" ):
                return visitor.visitIo(self)
            else:
                return visitor.visitChildren(self)




    def io(self):

        localctx = CSlangParser.IoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_io)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(CSlangParser.T__1)
                pass
            elif token in [CSlangParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(CSlangParser.T__2)
                self.state = 480
                self.match(CSlangParser.LPAREN)
                self.state = 481
                self.expr(0)
                self.state = 482
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.match(CSlangParser.T__3)
                pass
            elif token in [CSlangParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
                self.match(CSlangParser.T__4)
                self.state = 486
                self.match(CSlangParser.LPAREN)
                self.state = 487
                self.expr(0)
                self.state = 488
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 490
                self.match(CSlangParser.T__5)
                pass
            elif token in [CSlangParser.T__6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 491
                self.match(CSlangParser.T__6)
                self.state = 492
                self.match(CSlangParser.LPAREN)
                self.state = 493
                self.expr(0)
                self.state = 494
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 496
                self.match(CSlangParser.T__7)
                pass
            elif token in [CSlangParser.T__8]:
                self.enterOuterAlt(localctx, 8)
                self.state = 497
                self.match(CSlangParser.T__8)
                self.state = 498
                self.match(CSlangParser.LPAREN)
                self.state = 499
                self.expr(0)
                self.state = 500
                self.match(CSlangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_fm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFm" ):
                return visitor.visitFm(self)
            else:
                return visitor.visitChildren(self)




    def fm(self):

        localctx = CSlangParser.FmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ARRAY(self):
            return self.getToken(CSlangParser.ARRAY, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            _la = self._input.LA(1)
            if not(((((_la - 19)) & ~0x3f) == 0 and ((1 << (_la - 19)) & ((1 << (CSlangParser.INT - 19)) | (1 << (CSlangParser.FLOAT - 19)) | (1 << (CSlangParser.BOOL - 19)) | (1 << (CSlangParser.STRING - 19)) | (1 << (CSlangParser.VOID - 19)) | (1 << (CSlangParser.ARRAY - 19)) | (1 << (CSlangParser.ID - 19)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attri_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ARRAY(self):
            return self.getToken(CSlangParser.ARRAY, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attri_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttri_type" ):
                return visitor.visitAttri_type(self)
            else:
                return visitor.visitChildren(self)




    def attri_type(self):

        localctx = CSlangParser.Attri_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_attri_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            _la = self._input.LA(1)
            if not(((((_la - 19)) & ~0x3f) == 0 and ((1 << (_la - 19)) & ((1 << (CSlangParser.INT - 19)) | (1 << (CSlangParser.FLOAT - 19)) | (1 << (CSlangParser.BOOL - 19)) | (1 << (CSlangParser.STRING - 19)) | (1 << (CSlangParser.ARRAY - 19)) | (1 << (CSlangParser.ID - 19)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(CSlangParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(CSlangParser.FLOAT_LITERAL, 0)

        def bool_literal(self):
            return self.getTypedRuleContext(CSlangParser.Bool_literalContext,0)


        def STRING_LITERAL(self):
            return self.getToken(CSlangParser.STRING_LITERAL, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def NON_ZERO_INT(self):
            return self.getToken(CSlangParser.NON_ZERO_INT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literal)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.match(CSlangParser.INT_LITERAL)
                pass
            elif token in [CSlangParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                self.match(CSlangParser.FLOAT_LITERAL)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 512
                self.bool_literal()
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 513
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 514
                self.array()
                pass
            elif token in [CSlangParser.NON_ZERO_INT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 515
                self.match(CSlangParser.NON_ZERO_INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_bool_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_literal" ):
                return visitor.visitBool_literal(self)
            else:
                return visitor.visitChildren(self)




    def bool_literal(self):

        localctx = CSlangParser.Bool_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            _la = self._input.LA(1)
            if not(_la==CSlangParser.TRUE or _la==CSlangParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.LiteralContext)
            else:
                return self.getTypedRuleContext(CSlangParser.LiteralContext,i)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = CSlangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(CSlangParser.LBRACK)
            self.state = 521
            self.literal()
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 522
                self.match(CSlangParser.COMMA)
                self.state = 523
                self.literal()
                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 529
            self.match(CSlangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_sempred
        self._predicates[19] = self.expr1_sempred
        self._predicates[20] = self.expr2_sempred
        self._predicates[21] = self.expr3_sempred
        self._predicates[22] = self.expr4_sempred
        self._predicates[25] = self.expr7_sempred
        self._predicates[26] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




