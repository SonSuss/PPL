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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u0221\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\5\3\u0084\n\3\3\3\3\3\3\3\7\3\u0089\n\3\f\3\16\3\u008c")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\4\5\4\u0093\n\4\3\5\6\5\u0096")
        buf.write("\n\5\r\5\16\5\u0097\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u00ad\n")
        buf.write("\b\f\b\16\b\u00b0\13\b\3\b\5\b\u00b3\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\5\16\u00c3")
        buf.write("\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00d0\n\21\f\21\16\21\u00d3\13\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00db\n\22\3\23\3\23\3\23\7")
        buf.write("\23\u00e0\n\23\f\23\16\23\u00e3\13\23\5\23\u00e5\n\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00ed\n\24\f\24\16")
        buf.write("\24\u00f0\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u00f9\n\25\f\25\16\25\u00fc\13\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u0105\n\26\f\26\16\26\u0108\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0111\n\27\f")
        buf.write("\27\16\27\u0114\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\7\30\u011d\n\30\f\30\16\30\u0120\13\30\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u0126\n\31\3\32\3\32\3\32\5\32\u012b\n\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0135\n")
        buf.write("\33\f\33\16\33\u0138\13\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0147\n\34")
        buf.write("\f\34\16\34\u014a\13\34\3\35\3\35\5\35\u014e\n\35\3\35")
        buf.write("\3\35\3\35\5\35\u0153\n\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u015b\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u0164\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u016e\n\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u0178\n")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\5#\u0183\n#\3#\3#\3$")
        buf.write("\3$\3$\5$\u018a\n$\3%\3%\3%\3&\3&\3&\3&\5&\u0193\n&\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u0199\n\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\5\'\u01a4\n\'\3(\3(\3(\3(\3(\3)\3)\5)\u01ad")
        buf.write("\n)\3)\3)\3)\3)\5)\u01b3\n)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\5.\u01ca\n.\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\5\60\u01d7\n\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\7\61\u01e2\n")
        buf.write("\61\f\61\16\61\u01e5\13\61\3\61\3\61\3\62\3\62\5\62\u01eb")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\7\64\u01f5")
        buf.write("\n\64\f\64\16\64\u01f8\13\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\5\66\u0201\n\66\3\66\3\66\3\66\3\67\3\67\3")
        buf.write("8\38\39\39\3:\3:\3:\3:\3:\3:\5:\u0212\n:\3;\3;\3<\3<\3")
        buf.write("<\3<\7<\u021a\n<\f<\16<\u021d\13<\3<\3<\3<\2\n &(*,.\64")
        buf.write("\66=\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\f\4\2@@B")
        buf.write("B\3\2\60\63\3\2./\3\2$%\3\2&\'\3\2(+\3\2\3\n\5\2\24\27")
        buf.write("\37\37BB\4\2\24\27BB\3\2\22\23\2\u0221\2{\3\2\2\2\4\u0080")
        buf.write("\3\2\2\2\6\u0092\3\2\2\2\b\u0095\3\2\2\2\n\u0099\3\2\2")
        buf.write("\2\f\u00a2\3\2\2\2\16\u00b2\3\2\2\2\20\u00b4\3\2\2\2\22")
        buf.write("\u00b8\3\2\2\2\24\u00ba\3\2\2\2\26\u00bc\3\2\2\2\30\u00be")
        buf.write("\3\2\2\2\32\u00c2\3\2\2\2\34\u00c4\3\2\2\2\36\u00c6\3")
        buf.write("\2\2\2 \u00c8\3\2\2\2\"\u00da\3\2\2\2$\u00e4\3\2\2\2&")
        buf.write("\u00e6\3\2\2\2(\u00f1\3\2\2\2*\u00fd\3\2\2\2,\u0109\3")
        buf.write("\2\2\2.\u0115\3\2\2\2\60\u0125\3\2\2\2\62\u012a\3\2\2")
        buf.write("\2\64\u012c\3\2\2\2\66\u0139\3\2\2\28\u015a\3\2\2\2:\u0163")
        buf.write("\3\2\2\2<\u016d\3\2\2\2>\u0177\3\2\2\2@\u0179\3\2\2\2")
        buf.write("B\u017c\3\2\2\2D\u0182\3\2\2\2F\u0186\3\2\2\2H\u018b\3")
        buf.write("\2\2\2J\u018e\3\2\2\2L\u01a3\3\2\2\2N\u01a5\3\2\2\2P\u01aa")
        buf.write("\3\2\2\2R\u01b4\3\2\2\2T\u01bc\3\2\2\2V\u01bf\3\2\2\2")
        buf.write("X\u01c2\3\2\2\2Z\u01c9\3\2\2\2\\\u01cb\3\2\2\2^\u01d6")
        buf.write("\3\2\2\2`\u01df\3\2\2\2b\u01ea\3\2\2\2d\u01ec\3\2\2\2")
        buf.write("f\u01f1\3\2\2\2h\u01f9\3\2\2\2j\u01fb\3\2\2\2l\u0205\3")
        buf.write("\2\2\2n\u0207\3\2\2\2p\u0209\3\2\2\2r\u0211\3\2\2\2t\u0213")
        buf.write("\3\2\2\2v\u0215\3\2\2\2xz\5\4\3\2yx\3\2\2\2z}\3\2\2\2")
        buf.write("{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\2\2\3")
        buf.write("\177\3\3\2\2\2\u0080\u0083\7\32\2\2\u0081\u0082\7B\2\2")
        buf.write("\u0082\u0084\7\64\2\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\7B\2\2\u0086")
        buf.write("\u008a\7>\2\2\u0087\u0089\5\6\4\2\u0088\u0087\3\2\2\2")
        buf.write("\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3")
        buf.write("\2\2\2\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e")
        buf.write("\7?\2\2\u008e\5\3\2\2\2\u008f\u0093\5\b\5\2\u0090\u0093")
        buf.write("\5D#\2\u0091\u0093\5\f\7\2\u0092\u008f\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\7\3\2\2\2\u0094\u0096")
        buf.write("\5\n\6\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\t\3\2\2\2\u0099")
        buf.write("\u009a\7\"\2\2\u009a\u009b\t\2\2\2\u009b\u009c\7;\2\2")
        buf.write("\u009c\u009d\5\16\b\2\u009d\u009e\7:\2\2\u009e\u009f\7")
        buf.write("9\2\2\u009f\u00a0\5n8\2\u00a0\u00a1\5`\61\2\u00a1\13\3")
        buf.write("\2\2\2\u00a2\u00a3\7\"\2\2\u00a3\u00a4\7\33\2\2\u00a4")
        buf.write("\u00a5\7;\2\2\u00a5\u00a6\5\16\b\2\u00a6\u00a7\7:\2\2")
        buf.write("\u00a7\u00a8\5`\61\2\u00a8\r\3\2\2\2\u00a9\u00ae\5\20")
        buf.write("\t\2\u00aa\u00ab\7\67\2\2\u00ab\u00ad\5\20\t\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\u00b3\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b1\u00b3\3\2\2\2\u00b2\u00a9\3\2\2\2\u00b2\u00b1\3")
        buf.write("\2\2\2\u00b3\17\3\2\2\2\u00b4\u00b5\5f\64\2\u00b5\u00b6")
        buf.write("\79\2\2\u00b6\u00b7\5n8\2\u00b7\21\3\2\2\2\u00b8\u00b9")
        buf.write("\t\3\2\2\u00b9\23\3\2\2\2\u00ba\u00bb\t\4\2\2\u00bb\25")
        buf.write("\3\2\2\2\u00bc\u00bd\t\5\2\2\u00bd\27\3\2\2\2\u00be\u00bf")
        buf.write("\7#\2\2\u00bf\31\3\2\2\2\u00c0\u00c3\5\34\17\2\u00c1\u00c3")
        buf.write("\5\36\20\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3")
        buf.write("\33\3\2\2\2\u00c4\u00c5\t\6\2\2\u00c5\35\3\2\2\2\u00c6")
        buf.write("\u00c7\t\7\2\2\u00c7\37\3\2\2\2\u00c8\u00c9\b\21\1\2\u00c9")
        buf.write("\u00ca\5\"\22\2\u00ca\u00d1\3\2\2\2\u00cb\u00cc\f\4\2")
        buf.write("\2\u00cc\u00cd\5\26\f\2\u00cd\u00ce\5\"\22\2\u00ce\u00d0")
        buf.write("\3\2\2\2\u00cf\u00cb\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2!\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d4\u00d5\5&\24\2\u00d5\u00d6\5\32\16")
        buf.write("\2\u00d6\u00d7\5&\24\2\u00d7\u00db\3\2\2\2\u00d8\u00db")
        buf.write("\5t;\2\u00d9\u00db\7B\2\2\u00da\u00d4\3\2\2\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00d9\3\2\2\2\u00db#\3\2\2\2\u00dc\u00e1")
        buf.write("\5&\24\2\u00dd\u00de\7\67\2\2\u00de\u00e0\5$\23\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2")
        buf.write("\u00e1\u00e2\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3")
        buf.write("\2\2\2\u00e4\u00dc\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5%")
        buf.write("\3\2\2\2\u00e6\u00e7\b\24\1\2\u00e7\u00e8\5(\25\2\u00e8")
        buf.write("\u00ee\3\2\2\2\u00e9\u00ea\f\4\2\2\u00ea\u00eb\7\65\2")
        buf.write("\2\u00eb\u00ed\5&\24\5\u00ec\u00e9\3\2\2\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\'\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\b\25\1\2\u00f2")
        buf.write("\u00f3\5*\26\2\u00f3\u00fa\3\2\2\2\u00f4\u00f5\f\4\2\2")
        buf.write("\u00f5\u00f6\5\32\16\2\u00f6\u00f7\5(\25\5\u00f7\u00f9")
        buf.write("\3\2\2\2\u00f8\u00f4\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb)\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00fe\b\26\1\2\u00fe\u00ff\5,\27")
        buf.write("\2\u00ff\u0106\3\2\2\2\u0100\u0101\f\4\2\2\u0101\u0102")
        buf.write("\5\26\f\2\u0102\u0103\5,\27\2\u0103\u0105\3\2\2\2\u0104")
        buf.write("\u0100\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107+\3\2\2\2\u0108\u0106\3\2\2")
        buf.write("\2\u0109\u010a\b\27\1\2\u010a\u010b\5.\30\2\u010b\u0112")
        buf.write("\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e\5\24\13\2\u010e")
        buf.write("\u010f\5.\30\2\u010f\u0111\3\2\2\2\u0110\u010c\3\2\2\2")
        buf.write("\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3")
        buf.write("\2\2\2\u0113-\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116")
        buf.write("\b\30\1\2\u0116\u0117\5\60\31\2\u0117\u011e\3\2\2\2\u0118")
        buf.write("\u0119\f\4\2\2\u0119\u011a\5\22\n\2\u011a\u011b\5\60\31")
        buf.write("\2\u011b\u011d\3\2\2\2\u011c\u0118\3\2\2\2\u011d\u0120")
        buf.write("\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f")
        buf.write("/\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\5\30\r\2\u0122")
        buf.write("\u0123\5\62\32\2\u0123\u0126\3\2\2\2\u0124\u0126\5\62")
        buf.write("\32\2\u0125\u0121\3\2\2\2\u0125\u0124\3\2\2\2\u0126\61")
        buf.write("\3\2\2\2\u0127\u0128\7/\2\2\u0128\u012b\5\62\32\2\u0129")
        buf.write("\u012b\5\64\33\2\u012a\u0127\3\2\2\2\u012a\u0129\3\2\2")
        buf.write("\2\u012b\63\3\2\2\2\u012c\u012d\b\33\1\2\u012d\u012e\5")
        buf.write("\66\34\2\u012e\u0136\3\2\2\2\u012f\u0130\f\4\2\2\u0130")
        buf.write("\u0131\7<\2\2\u0131\u0132\5\64\33\2\u0132\u0133\7=\2\2")
        buf.write("\u0133\u0135\3\2\2\2\u0134\u012f\3\2\2\2\u0135\u0138\3")
        buf.write("\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\65")
        buf.write("\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a\b\34\1\2\u013a")
        buf.write("\u013b\58\35\2\u013b\u0148\3\2\2\2\u013c\u013d\f\5\2\2")
        buf.write("\u013d\u013e\7\66\2\2\u013e\u0147\7B\2\2\u013f\u0140\f")
        buf.write("\4\2\2\u0140\u0141\7\66\2\2\u0141\u0142\7B\2\2\u0142\u0143")
        buf.write("\7;\2\2\u0143\u0144\5$\23\2\u0144\u0145\7:\2\2\u0145\u0147")
        buf.write("\3\2\2\2\u0146\u013c\3\2\2\2\u0146\u013f\3\2\2\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\67\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\7B\2")
        buf.write("\2\u014c\u014e\7\66\2\2\u014d\u014b\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u015b\7@\2\2\u0150")
        buf.write("\u0151\7B\2\2\u0151\u0153\7\66\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\7")
        buf.write("@\2\2\u0155\u0156\7;\2\2\u0156\u0157\5$\23\2\u0157\u0158")
        buf.write("\7:\2\2\u0158\u015b\3\2\2\2\u0159\u015b\5:\36\2\u015a")
        buf.write("\u014d\3\2\2\2\u015a\u0152\3\2\2\2\u015a\u0159\3\2\2\2")
        buf.write("\u015b9\3\2\2\2\u015c\u015d\7\36\2\2\u015d\u015e\7B\2")
        buf.write("\2\u015e\u015f\7;\2\2\u015f\u0160\5$\23\2\u0160\u0161")
        buf.write("\7:\2\2\u0161\u0164\3\2\2\2\u0162\u0164\5<\37\2\u0163")
        buf.write("\u015c\3\2\2\2\u0163\u0162\3\2\2\2\u0164;\3\2\2\2\u0165")
        buf.write("\u0166\7;\2\2\u0166\u0167\5&\24\2\u0167\u0168\7:\2\2\u0168")
        buf.write("\u016e\3\2\2\2\u0169\u016e\5r:\2\u016a\u016e\7\35\2\2")
        buf.write("\u016b\u016e\7B\2\2\u016c\u016e\7\31\2\2\u016d\u0165\3")
        buf.write("\2\2\2\u016d\u0169\3\2\2\2\u016d\u016a\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016c\3\2\2\2\u016e=\3\2\2\2\u016f\u0178")
        buf.write("\5D#\2\u0170\u0178\5@!\2\u0171\u0178\5P)\2\u0172\u0178")
        buf.write("\5R*\2\u0173\u0178\5T+\2\u0174\u0178\5V,\2\u0175\u0178")
        buf.write("\5X-\2\u0176\u0178\5Z.\2\u0177\u016f\3\2\2\2\u0177\u0170")
        buf.write("\3\2\2\2\u0177\u0171\3\2\2\2\u0177\u0172\3\2\2\2\u0177")
        buf.write("\u0173\3\2\2\2\u0177\u0174\3\2\2\2\u0177\u0175\3\2\2\2")
        buf.write("\u0177\u0176\3\2\2\2\u0178?\3\2\2\2\u0179\u017a\5B\"\2")
        buf.write("\u017a\u017b\78\2\2\u017bA\3\2\2\2\u017c\u017d\5b\62\2")
        buf.write("\u017d\u017e\7-\2\2\u017e\u017f\5&\24\2\u017fC\3\2\2\2")
        buf.write("\u0180\u0183\5F$\2\u0181\u0183\5H%\2\u0182\u0180\3\2\2")
        buf.write("\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185")
        buf.write("\78\2\2\u0185E\3\2\2\2\u0186\u0189\7\34\2\2\u0187\u018a")
        buf.write("\5J&\2\u0188\u018a\5L\'\2\u0189\u0187\3\2\2\2\u0189\u0188")
        buf.write("\3\2\2\2\u018aG\3\2\2\2\u018b\u018c\7 \2\2\u018c\u018d")
        buf.write("\5L\'\2\u018dI\3\2\2\2\u018e\u018f\5f\64\2\u018f\u0192")
        buf.write("\79\2\2\u0190\u0193\5p9\2\u0191\u0193\5N(\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193K\3\2\2\2\u0194\u0195")
        buf.write("\5h\65\2\u0195\u0198\79\2\2\u0196\u0199\5p9\2\u0197\u0199")
        buf.write("\5N(\2\u0198\u0196\3\2\2\2\u0198\u0197\3\2\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019a\u019b\7,\2\2\u019b\u019c\5&\24\2\u019c")
        buf.write("\u01a4\3\2\2\2\u019d\u019e\5h\65\2\u019e\u019f\7\67\2")
        buf.write("\2\u019f\u01a0\5L\'\2\u01a0\u01a1\7\67\2\2\u01a1\u01a2")
        buf.write("\5&\24\2\u01a2\u01a4\3\2\2\2\u01a3\u0194\3\2\2\2\u01a3")
        buf.write("\u019d\3\2\2\2\u01a4M\3\2\2\2\u01a5\u01a6\7<\2\2\u01a6")
        buf.write("\u01a7\7D\2\2\u01a7\u01a8\7=\2\2\u01a8\u01a9\5p9\2\u01a9")
        buf.write("O\3\2\2\2\u01aa\u01ac\7\17\2\2\u01ab\u01ad\5`\61\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01af\5&\24\2\u01af\u01b2\5`\61\2\u01b0\u01b1\7")
        buf.write("\20\2\2\u01b1\u01b3\5`\61\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3Q\3\2\2\2\u01b4\u01b5\7\21\2\2\u01b5")
        buf.write("\u01b6\5B\"\2\u01b6\u01b7\78\2\2\u01b7\u01b8\5 \21\2\u01b8")
        buf.write("\u01b9\78\2\2\u01b9\u01ba\5B\"\2\u01ba\u01bb\5`\61\2\u01bb")
        buf.write("S\3\2\2\2\u01bc\u01bd\7\r\2\2\u01bd\u01be\78\2\2\u01be")
        buf.write("U\3\2\2\2\u01bf\u01c0\7\16\2\2\u01c0\u01c1\78\2\2\u01c1")
        buf.write("W\3\2\2\2\u01c2\u01c3\7\30\2\2\u01c3\u01c4\5&\24\2\u01c4")
        buf.write("\u01c5\78\2\2\u01c5Y\3\2\2\2\u01c6\u01ca\5\\/\2\u01c7")
        buf.write("\u01ca\5^\60\2\u01c8\u01ca\5j\66\2\u01c9\u01c6\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca[\3\2\2")
        buf.write("\2\u01cb\u01cc\5&\24\2\u01cc\u01cd\7\66\2\2\u01cd\u01ce")
        buf.write("\7B\2\2\u01ce\u01cf\7;\2\2\u01cf\u01d0\5$\23\2\u01d0\u01d1")
        buf.write("\7:\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\78\2\2\u01d3]")
        buf.write("\3\2\2\2\u01d4\u01d5\7B\2\2\u01d5\u01d7\7\66\2\2\u01d6")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u01d9\7@\2\2\u01d9\u01da\7;\2\2\u01da\u01db\5$")
        buf.write("\23\2\u01db\u01dc\7:\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de")
        buf.write("\78\2\2\u01de_\3\2\2\2\u01df\u01e3\7>\2\2\u01e0\u01e2")
        buf.write("\5> \2\u01e1\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e7\7?\2\2\u01e7a\3\2\2\2\u01e8")
        buf.write("\u01eb\5d\63\2\u01e9\u01eb\5h\65\2\u01ea\u01e8\3\2\2\2")
        buf.write("\u01ea\u01e9\3\2\2\2\u01ebc\3\2\2\2\u01ec\u01ed\5&\24")
        buf.write("\2\u01ed\u01ee\7<\2\2\u01ee\u01ef\5&\24\2\u01ef\u01f0")
        buf.write("\7=\2\2\u01f0e\3\2\2\2\u01f1\u01f6\5h\65\2\u01f2\u01f3")
        buf.write("\7\67\2\2\u01f3\u01f5\5h\65\2\u01f4\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2")
        buf.write("\u01f7g\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fa\t\2\2")
        buf.write("\2\u01fai\3\2\2\2\u01fb\u01fc\5&\24\2\u01fc\u01fd\7\66")
        buf.write("\2\2\u01fd\u01fe\5l\67\2\u01fe\u0200\7;\2\2\u01ff\u0201")
        buf.write("\5&\24\2\u0200\u01ff\3\2\2\2\u0200\u0201\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0203\7:\2\2\u0203\u0204\78\2\2\u0204")
        buf.write("k\3\2\2\2\u0205\u0206\t\b\2\2\u0206m\3\2\2\2\u0207\u0208")
        buf.write("\t\t\2\2\u0208o\3\2\2\2\u0209\u020a\t\n\2\2\u020aq\3\2")
        buf.write("\2\2\u020b\u0212\7E\2\2\u020c\u0212\7C\2\2\u020d\u0212")
        buf.write("\5t;\2\u020e\u0212\7A\2\2\u020f\u0212\5v<\2\u0210\u0212")
        buf.write("\7D\2\2\u0211\u020b\3\2\2\2\u0211\u020c\3\2\2\2\u0211")
        buf.write("\u020d\3\2\2\2\u0211\u020e\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0210\3\2\2\2\u0212s\3\2\2\2\u0213\u0214\t\13\2")
        buf.write("\2\u0214u\3\2\2\2\u0215\u0216\7<\2\2\u0216\u021b\5r:\2")
        buf.write("\u0217\u0218\7\67\2\2\u0218\u021a\5r:\2\u0219\u0217\3")
        buf.write("\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c")
        buf.write("\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b\3\2\2\2\u021e")
        buf.write("\u021f\7=\2\2\u021fw\3\2\2\2-{\u0083\u008a\u0092\u0097")
        buf.write("\u00ae\u00b2\u00c2\u00d1\u00da\u00e1\u00e4\u00ee\u00fa")
        buf.write("\u0106\u0112\u011e\u0125\u012a\u0136\u0146\u0148\u014d")
        buf.write("\u0152\u015a\u0163\u016d\u0177\u0182\u0189\u0192\u0198")
        buf.write("\u01a3\u01ac\u01b2\u01c9\u01d6\u01e3\u01ea\u01f6\u0200")
        buf.write("\u0211\u021b")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@readInt'", "'@writeInt'", "'@readFloat'", 
                     "'@writeFloat'", "'@readBool'", "'@writeBool'", "'@readString'", 
                     "'@writeString'", "<INVALID>", "<INVALID>", "'break'", 
                     "'continue'", "'if'", "'else'", "'for'", "'true'", 
                     "'false'", "'int'", "'float'", "'bool'", "'string'", 
                     "'return'", "'null'", "'class'", "'constructor'", "'var'", 
                     "'self'", "'new'", "'void'", "'const'", "'constant'", 
                     "'func'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'='", "':='", "'+'", "'-'", 
                     "'*'", "'\\'", "'%'", "'/'", "'<-'", "'^'", "'.'", 
                     "','", "';'", "':'", "')'", "'('", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                      "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                      "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                      "CONST", "CONSTANT", "FUNC", "NOT", "AND", "OR", "EQUAL", 
                      "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "INITIAL", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", "SUPER_CLASS", 
                      "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", "COLON", 
                      "RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", 
                      "RBRASE", "AT_ID", "STRING_LITERAL", "ID", "FLOAT_LITERAL", 
                      "NON_ZERO_INT", "INT_LITERAL", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_body = 2
    RULE_method_lst = 3
    RULE_method_dcl = 4
    RULE_constructor_decl = 5
    RULE_param_lst = 6
    RULE_param = 7
    RULE_multiplying = 8
    RULE_adding = 9
    RULE_logical_bin = 10
    RULE_logical_not = 11
    RULE_relational = 12
    RULE_relat_bool = 13
    RULE_relat_int_float = 14
    RULE_relational_expr0 = 15
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
    RULE_variable_decl = 34
    RULE_constraint_decl = 35
    RULE_non_inital_decl = 36
    RULE_inital_decl = 37
    RULE_array_type = 38
    RULE_if_state = 39
    RULE_for_state = 40
    RULE_break_state = 41
    RULE_continue_state = 42
    RULE_return_state = 43
    RULE_call_state = 44
    RULE_instance_method_invo_access = 45
    RULE_static_method_invo_access = 46
    RULE_block_state = 47
    RULE_lhs = 48
    RULE_index_op = 49
    RULE_id_lst = 50
    RULE_id_access = 51
    RULE_io_st = 52
    RULE_io_mt = 53
    RULE_typ = 54
    RULE_attri_type = 55
    RULE_literal = 56
    RULE_bool_literal = 57
    RULE_array = 58

    ruleNames =  [ "program", "class_dcl", "class_body", "method_lst", "method_dcl", 
                   "constructor_decl", "param_lst", "param", "multiplying", 
                   "adding", "logical_bin", "logical_not", "relational", 
                   "relat_bool", "relat_int_float", "relational_expr0", 
                   "relational_expr", "expr_lst", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "expr9", "expr10", "expr11", "statements", "assign_decl", 
                   "attribute_assign", "attribute_decl", "variable_decl", 
                   "constraint_decl", "non_inital_decl", "inital_decl", 
                   "array_type", "if_state", "for_state", "break_state", 
                   "continue_state", "return_state", "call_state", "instance_method_invo_access", 
                   "static_method_invo_access", "block_state", "lhs", "index_op", 
                   "id_lst", "id_access", "io_st", "io_mt", "typ", "attri_type", 
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
    BLOCK_COMMENT=9
    LINE_COMMENT=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELSE=14
    FOR=15
    TRUE=16
    FALSE=17
    INT=18
    FLOAT=19
    BOOL=20
    STRING=21
    RETURN=22
    NULL=23
    CLASS=24
    CONSTRUCTOR=25
    VAR=26
    SELF=27
    NEW=28
    VOID=29
    CONST=30
    CONSTANT=31
    FUNC=32
    NOT=33
    AND=34
    OR=35
    EQUAL=36
    NOT_EQUAL=37
    LESS=38
    GREATER=39
    LESS_EQUAL=40
    GREATER_EQUAL=41
    INITIAL=42
    ASSIGN=43
    PLUS=44
    MINUS=45
    MULTIPLY=46
    DIVIDE_I=47
    DIVIDE_I_L=48
    DIVIDE_F=49
    SUPER_CLASS=50
    STRING_CONCAT=51
    DOT=52
    COMMA=53
    SEMICOLON=54
    COLON=55
    RPAREN=56
    LPAREN=57
    LBRACK=58
    RBRACK=59
    LBRASE=60
    RBRASE=61
    AT_ID=62
    STRING_LITERAL=63
    ID=64
    FLOAT_LITERAL=65
    NON_ZERO_INT=66
    INT_LITERAL=67
    WS=68
    ERROR_CHAR=69
    UNCLOSE_STRING=70
    ILLEGAL_ESCAPE=71

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

        def class_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_dclContext,i)


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
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CLASS:
                self.state = 118
                self.class_dcl()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(CSlangParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_class_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(CSlangParser.CLASS)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 127
                self.match(CSlangParser.ID)
                self.state = 128
                self.match(CSlangParser.SUPER_CLASS)


            self.state = 131
            self.match(CSlangParser.ID)
            self.state = 132
            self.match(CSlangParser.LBRASE)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 133
                self.class_body()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
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
        self.enterRule(localctx, 4, self.RULE_class_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 141
                self.method_lst()
                pass

            elif la_ == 2:
                self.state = 142
                self.attribute_decl()
                pass

            elif la_ == 3:
                self.state = 143
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
        self.enterRule(localctx, 6, self.RULE_method_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 146
                    self.method_dcl()

                else:
                    raise NoViableAltException(self)
                self.state = 149 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(CSlangParser.FUNC)
            self.state = 152
            _la = self._input.LA(1)
            if not(_la==CSlangParser.AT_ID or _la==CSlangParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 153
            self.match(CSlangParser.LPAREN)
            self.state = 154
            self.param_lst()
            self.state = 155
            self.match(CSlangParser.RPAREN)
            self.state = 156
            self.match(CSlangParser.COLON)
            self.state = 157
            self.typ()
            self.state = 158
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
        self.enterRule(localctx, 10, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(CSlangParser.FUNC)
            self.state = 161
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 162
            self.match(CSlangParser.LPAREN)
            self.state = 163
            self.param_lst()
            self.state = 164
            self.match(CSlangParser.RPAREN)
            self.state = 165
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
        self.enterRule(localctx, 12, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.AT_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.param()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 168
                    self.match(CSlangParser.COMMA)
                    self.state = 169
                    self.param()
                    self.state = 174
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
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.id_lst()
            self.state = 179
            self.match(CSlangParser.COLON)
            self.state = 180
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
        self.enterRule(localctx, 16, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
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
        self.enterRule(localctx, 18, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
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
        self.enterRule(localctx, 20, self.RULE_logical_bin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
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
        self.enterRule(localctx, 22, self.RULE_logical_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
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
        self.enterRule(localctx, 24, self.RULE_relational)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.EQUAL, CSlangParser.NOT_EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.relat_bool()
                pass
            elif token in [CSlangParser.LESS, CSlangParser.GREATER, CSlangParser.LESS_EQUAL, CSlangParser.GREATER_EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
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
        self.enterRule(localctx, 26, self.RULE_relat_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 28, self.RULE_relat_int_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
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


    class Relational_expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self):
            return self.getTypedRuleContext(CSlangParser.Relational_exprContext,0)


        def relational_expr0(self):
            return self.getTypedRuleContext(CSlangParser.Relational_expr0Context,0)


        def logical_bin(self):
            return self.getTypedRuleContext(CSlangParser.Logical_binContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_relational_expr0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr0" ):
                return visitor.visitRelational_expr0(self)
            else:
                return visitor.visitChildren(self)



    def relational_expr0(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Relational_expr0Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_relational_expr0, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.relational_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Relational_expr0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr0)
                    self.state = 201
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 202
                    self.logical_bin()
                    self.state = 203
                    self.relational_expr() 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.expr(0)
                self.state = 211
                self.relational()
                self.state = 212
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.bool_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (CSlangParser.TRUE - 16)) | (1 << (CSlangParser.FALSE - 16)) | (1 << (CSlangParser.NULL - 16)) | (1 << (CSlangParser.SELF - 16)) | (1 << (CSlangParser.NEW - 16)) | (1 << (CSlangParser.NOT - 16)) | (1 << (CSlangParser.MINUS - 16)) | (1 << (CSlangParser.LPAREN - 16)) | (1 << (CSlangParser.LBRACK - 16)) | (1 << (CSlangParser.AT_ID - 16)) | (1 << (CSlangParser.STRING_LITERAL - 16)) | (1 << (CSlangParser.ID - 16)) | (1 << (CSlangParser.FLOAT_LITERAL - 16)) | (1 << (CSlangParser.NON_ZERO_INT - 16)) | (1 << (CSlangParser.INT_LITERAL - 16)))) != 0):
                self.state = 218
                self.expr(0)
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 219
                        self.match(CSlangParser.COMMA)
                        self.state = 220
                        self.expr_lst() 
                    self.state = 225
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)



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
            self.state = 229
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    self.match(CSlangParser.STRING_CONCAT)
                    self.state = 233
                    self.expr(3) 
                self.state = 238
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
            self.state = 240
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    self.relational()
                    self.state = 244
                    self.expr1(3) 
                self.state = 250
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
            self.state = 252
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    self.logical_bin()
                    self.state = 256
                    self.expr3(0) 
                self.state = 262
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
            self.state = 264
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    self.adding()
                    self.state = 268
                    self.expr4(0) 
                self.state = 274
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
            self.state = 276
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    self.multiplying()
                    self.state = 280
                    self.expr5() 
                self.state = 286
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
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.logical_not()
                self.state = 288
                self.expr6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.AT_ID, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
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
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(CSlangParser.MINUS)
                self.state = 294
                self.expr6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.AT_ID, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
            self.state = 299
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 301
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302
                    self.match(CSlangParser.LBRACK)
                    self.state = 303
                    self.expr7(0)
                    self.state = 304
                    self.match(CSlangParser.RBRACK) 
                self.state = 310
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

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 324
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 314
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 315
                        self.match(CSlangParser.DOT)
                        self.state = 316
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 317
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 318
                        self.match(CSlangParser.DOT)
                        self.state = 319
                        self.match(CSlangParser.ID)

                        self.state = 320
                        self.match(CSlangParser.LPAREN)
                        self.state = 321
                        self.expr_lst()
                        self.state = 322
                        self.match(CSlangParser.RPAREN)
                        pass

             
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

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
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 329
                    self.match(CSlangParser.ID)
                    self.state = 330
                    self.match(CSlangParser.DOT)


                self.state = 333
                self.match(CSlangParser.AT_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 334
                    self.match(CSlangParser.ID)
                    self.state = 335
                    self.match(CSlangParser.DOT)


                self.state = 338
                self.match(CSlangParser.AT_ID)

                self.state = 339
                self.match(CSlangParser.LPAREN)
                self.state = 340
                self.expr_lst()
                self.state = 341
                self.match(CSlangParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
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

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

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
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(CSlangParser.NEW)
                self.state = 347
                self.match(CSlangParser.ID)
                self.state = 348
                self.match(CSlangParser.LPAREN)
                self.state = 349
                self.expr_lst()
                self.state = 350
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(CSlangParser.LPAREN)
                self.state = 356
                self.expr(0)
                self.state = 357
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 362
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


        def call_state(self):
            return self.getTypedRuleContext(CSlangParser.Call_stateContext,0)


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
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.assign_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.if_state()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 368
                self.for_state()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 369
                self.break_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 370
                self.continue_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 371
                self.return_state()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 372
                self.call_state()
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
            self.state = 375
            self.attribute_assign()
            self.state = 376
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
            self.state = 378
            self.lhs()
            self.state = 379
            self.match(CSlangParser.ASSIGN)
            self.state = 380
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

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def variable_decl(self):
            return self.getTypedRuleContext(CSlangParser.Variable_declContext,0)


        def constraint_decl(self):
            return self.getTypedRuleContext(CSlangParser.Constraint_declContext,0)


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
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.state = 382
                self.variable_decl()
                pass
            elif token in [CSlangParser.CONST]:
                self.state = 383
                self.constraint_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 386
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def non_inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Non_inital_declContext,0)


        def inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Inital_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = CSlangParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(CSlangParser.VAR)
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 389
                self.non_inital_decl()
                pass

            elif la_ == 2:
                self.state = 390
                self.inital_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constraint_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Inital_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constraint_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraint_decl" ):
                return visitor.visitConstraint_decl(self)
            else:
                return visitor.visitChildren(self)




    def constraint_decl(self):

        localctx = CSlangParser.Constraint_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_constraint_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(CSlangParser.CONST)
            self.state = 394
            self.inital_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_inital_declContext(ParserRuleContext):
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


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_non_inital_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_inital_decl" ):
                return visitor.visitNon_inital_decl(self)
            else:
                return visitor.visitChildren(self)




    def non_inital_decl(self):

        localctx = CSlangParser.Non_inital_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_non_inital_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.id_lst()
            self.state = 397
            self.match(CSlangParser.COLON)
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 398
                self.attri_type()
                pass
            elif token in [CSlangParser.LBRACK]:
                self.state = 399
                self.array_type()
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


    class Inital_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_access(self):
            return self.getTypedRuleContext(CSlangParser.Id_accessContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INITIAL(self):
            return self.getToken(CSlangParser.INITIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def attri_type(self):
            return self.getTypedRuleContext(CSlangParser.Attri_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Inital_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_inital_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInital_decl" ):
                return visitor.visitInital_decl(self)
            else:
                return visitor.visitChildren(self)




    def inital_decl(self):

        localctx = CSlangParser.Inital_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_inital_decl)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.id_access()
                self.state = 403
                self.match(CSlangParser.COLON)
                self.state = 406
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                    self.state = 404
                    self.attri_type()
                    pass
                elif token in [CSlangParser.LBRACK]:
                    self.state = 405
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 408
                self.match(CSlangParser.INITIAL)
                self.state = 409
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.id_access()
                self.state = 412
                self.match(CSlangParser.COMMA)
                self.state = 413
                self.inital_decl()
                self.state = 414
                self.match(CSlangParser.COMMA)
                self.state = 415
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
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

        def attri_type(self):
            return self.getTypedRuleContext(CSlangParser.Attri_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(CSlangParser.LBRACK)
            self.state = 420
            self.match(CSlangParser.NON_ZERO_INT)
            self.state = 421
            self.match(CSlangParser.RBRACK)
            self.state = 422
            self.attri_type()
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


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
        self.enterRule(localctx, 78, self.RULE_if_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(CSlangParser.IF)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBRASE:
                self.state = 425
                self.block_state()


            self.state = 428
            self.expr(0)
            self.state = 429
            self.block_state()
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 430
                self.match(CSlangParser.ELSE)
                self.state = 431
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

        def relational_expr0(self):
            return self.getTypedRuleContext(CSlangParser.Relational_expr0Context,0)


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
        self.enterRule(localctx, 80, self.RULE_for_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(CSlangParser.FOR)
            self.state = 435
            self.attribute_assign()
            self.state = 436
            self.match(CSlangParser.SEMICOLON)
            self.state = 437
            self.relational_expr0(0)
            self.state = 438
            self.match(CSlangParser.SEMICOLON)
            self.state = 439
            self.attribute_assign()
            self.state = 440
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
        self.enterRule(localctx, 82, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(CSlangParser.BREAK)
            self.state = 443
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
        self.enterRule(localctx, 84, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(CSlangParser.CONTINUE)
            self.state = 446
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
        self.enterRule(localctx, 86, self.RULE_return_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(CSlangParser.RETURN)
            self.state = 449
            self.expr(0)
            self.state = 450
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Instance_method_invo_accessContext,0)


        def static_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_invo_accessContext,0)


        def io_st(self):
            return self.getTypedRuleContext(CSlangParser.Io_stContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_call_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_state" ):
                return visitor.visitCall_state(self)
            else:
                return visitor.visitChildren(self)




    def call_state(self):

        localctx = CSlangParser.Call_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_call_state)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.instance_method_invo_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.static_method_invo_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.io_st()
                pass


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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instance_method_invo_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invo_access" ):
                return visitor.visitInstance_method_invo_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invo_access(self):

        localctx = CSlangParser.Instance_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_instance_method_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.expr(0)
            self.state = 458
            self.match(CSlangParser.DOT)
            self.state = 459
            self.match(CSlangParser.ID)

            self.state = 460
            self.match(CSlangParser.LPAREN)
            self.state = 461
            self.expr_lst()
            self.state = 462
            self.match(CSlangParser.RPAREN)
            self.state = 464
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

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_static_method_invo_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invo_access" ):
                return visitor.visitStatic_method_invo_access(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invo_access(self):

        localctx = CSlangParser.Static_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_static_method_invo_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 466
                self.match(CSlangParser.ID)
                self.state = 467
                self.match(CSlangParser.DOT)


            self.state = 470
            self.match(CSlangParser.AT_ID)

            self.state = 471
            self.match(CSlangParser.LPAREN)
            self.state = 472
            self.expr_lst()
            self.state = 473
            self.match(CSlangParser.RPAREN)
            self.state = 475
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
        self.enterRule(localctx, 94, self.RULE_block_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(CSlangParser.LBRASE)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (CSlangParser.BREAK - 11)) | (1 << (CSlangParser.CONTINUE - 11)) | (1 << (CSlangParser.IF - 11)) | (1 << (CSlangParser.FOR - 11)) | (1 << (CSlangParser.TRUE - 11)) | (1 << (CSlangParser.FALSE - 11)) | (1 << (CSlangParser.RETURN - 11)) | (1 << (CSlangParser.NULL - 11)) | (1 << (CSlangParser.VAR - 11)) | (1 << (CSlangParser.SELF - 11)) | (1 << (CSlangParser.NEW - 11)) | (1 << (CSlangParser.CONST - 11)) | (1 << (CSlangParser.NOT - 11)) | (1 << (CSlangParser.MINUS - 11)) | (1 << (CSlangParser.LPAREN - 11)) | (1 << (CSlangParser.LBRACK - 11)) | (1 << (CSlangParser.AT_ID - 11)) | (1 << (CSlangParser.STRING_LITERAL - 11)) | (1 << (CSlangParser.ID - 11)) | (1 << (CSlangParser.FLOAT_LITERAL - 11)) | (1 << (CSlangParser.NON_ZERO_INT - 11)) | (1 << (CSlangParser.INT_LITERAL - 11)))) != 0):
                self.state = 478
                self.statements()
                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 484
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
        self.enterRule(localctx, 96, self.RULE_lhs)
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
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
        self.enterRule(localctx, 98, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.expr(0)
            self.state = 491
            self.match(CSlangParser.LBRACK)
            self.state = 492
            self.expr(0)
            self.state = 493
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
        self.enterRule(localctx, 100, self.RULE_id_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.id_access()
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 496
                self.match(CSlangParser.COMMA)
                self.state = 497
                self.id_access()
                self.state = 502
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
        self.enterRule(localctx, 102, self.RULE_id_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def io_mt(self):
            return self.getTypedRuleContext(CSlangParser.Io_mtContext,0)


        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

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
        self.enterRule(localctx, 104, self.RULE_io_st)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.expr(0)
            self.state = 506
            self.match(CSlangParser.DOT)
            self.state = 507
            self.io_mt()
            self.state = 508
            self.match(CSlangParser.LPAREN)
            self.state = 510
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (CSlangParser.TRUE - 16)) | (1 << (CSlangParser.FALSE - 16)) | (1 << (CSlangParser.NULL - 16)) | (1 << (CSlangParser.SELF - 16)) | (1 << (CSlangParser.NEW - 16)) | (1 << (CSlangParser.NOT - 16)) | (1 << (CSlangParser.MINUS - 16)) | (1 << (CSlangParser.LPAREN - 16)) | (1 << (CSlangParser.LBRACK - 16)) | (1 << (CSlangParser.AT_ID - 16)) | (1 << (CSlangParser.STRING_LITERAL - 16)) | (1 << (CSlangParser.ID - 16)) | (1 << (CSlangParser.FLOAT_LITERAL - 16)) | (1 << (CSlangParser.NON_ZERO_INT - 16)) | (1 << (CSlangParser.INT_LITERAL - 16)))) != 0):
                self.state = 509
                self.expr(0)


            self.state = 512
            self.match(CSlangParser.RPAREN)
            self.state = 513
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_mtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSlangParser.RULE_io_mt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_mt" ):
                return visitor.visitIo_mt(self)
            else:
                return visitor.visitChildren(self)




    def io_mt(self):

        localctx = CSlangParser.Io_mtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_io_mt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.T__1) | (1 << CSlangParser.T__2) | (1 << CSlangParser.T__3) | (1 << CSlangParser.T__4) | (1 << CSlangParser.T__5) | (1 << CSlangParser.T__6) | (1 << CSlangParser.T__7))) != 0)):
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

        def getRuleIndex(self):
            return CSlangParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            _la = self._input.LA(1)
            if not(((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & ((1 << (CSlangParser.INT - 18)) | (1 << (CSlangParser.FLOAT - 18)) | (1 << (CSlangParser.BOOL - 18)) | (1 << (CSlangParser.STRING - 18)) | (1 << (CSlangParser.VOID - 18)) | (1 << (CSlangParser.ID - 18)))) != 0)):
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

        def getRuleIndex(self):
            return CSlangParser.RULE_attri_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttri_type" ):
                return visitor.visitAttri_type(self)
            else:
                return visitor.visitChildren(self)




    def attri_type(self):

        localctx = CSlangParser.Attri_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_attri_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            _la = self._input.LA(1)
            if not(((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & ((1 << (CSlangParser.INT - 18)) | (1 << (CSlangParser.FLOAT - 18)) | (1 << (CSlangParser.BOOL - 18)) | (1 << (CSlangParser.STRING - 18)) | (1 << (CSlangParser.ID - 18)))) != 0)):
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
        self.enterRule(localctx, 112, self.RULE_literal)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(CSlangParser.INT_LITERAL)
                pass
            elif token in [CSlangParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(CSlangParser.FLOAT_LITERAL)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.bool_literal()
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 525
                self.array()
                pass
            elif token in [CSlangParser.NON_ZERO_INT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 526
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
        self.enterRule(localctx, 114, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
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
        self.enterRule(localctx, 116, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(CSlangParser.LBRACK)
            self.state = 532
            self.literal()
            self.state = 537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 533
                self.match(CSlangParser.COMMA)
                self.state = 534
                self.literal()
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 540
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
        self._predicates[15] = self.relational_expr0_sempred
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

    def relational_expr0_sempred(self, localctx:Relational_expr0Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




