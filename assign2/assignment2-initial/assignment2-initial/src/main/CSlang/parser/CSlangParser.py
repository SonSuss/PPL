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
        buf.write("\u0231\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\3\2\3\3\3\3\3\3\5\3~\n\3\3\3\3\3")
        buf.write("\3\3\7\3\u0083\n\3\f\3\16\3\u0086\13\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\5\4\u008d\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u0097\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\7\7\u00a5\n\7\f\7\16\7\u00a8\13\7\3\7\5\7\u00ab\n")
        buf.write("\7\3\b\3\b\5\b\u00af\n\b\3\b\3\b\3\b\5\b\u00b4\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00be\n\t\3\n\3\n\5\n")
        buf.write("\u00c2\n\n\3\n\3\n\3\13\3\13\3\13\5\13\u00c9\n\13\3\f")
        buf.write("\3\f\3\f\5\f\u00ce\n\f\3\r\3\r\3\r\3\r\5\r\u00d4\n\r\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00da\n\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00e5\n\16\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u00f0\n\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00f6\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\5\24\u0105")
        buf.write("\n\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u010f")
        buf.write("\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u0118\n")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\5\30\u0122")
        buf.write("\n\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\7\32\u012f\n\32\f\32\16\32\u0132\13\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u0156\n\33\3\34\3\34\3\34\5\34\u015b\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u0167\n\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u016e\n\36\3\36\5\36\u0171")
        buf.write("\n\36\3\37\3\37\3\37\7\37\u0176\n\37\f\37\16\37\u0179")
        buf.write("\13\37\3 \3 \3!\3!\3!\7!\u0180\n!\f!\16!\u0183\13!\3!")
        buf.write("\5!\u0186\n!\3\"\3\"\3\"\3\"\3\"\5\"\u018d\n\"\3#\3#\3")
        buf.write("#\3#\3#\5#\u0194\n#\3$\3$\3$\3$\3$\3$\3$\7$\u019d\n$\f")
        buf.write("$\16$\u01a0\13$\3%\3%\3%\3%\3%\3%\3%\7%\u01a9\n%\f%\16")
        buf.write("%\u01ac\13%\3&\3&\3&\3&\3&\3&\3&\7&\u01b5\n&\f&\16&\u01b8")
        buf.write("\13&\3\'\3\'\3\'\3\'\5\'\u01be\n\'\3(\3(\3(\5(\u01c3\n")
        buf.write("(\3)\3)\3)\3)\3)\3)\5)\u01cb\n)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\5*\u01d5\n*\3*\3*\3*\3*\3*\3*\5*\u01dd\n*\7*\u01df\n")
        buf.write("*\f*\16*\u01e2\13*\3+\3+\5+\u01e6\n+\3+\3+\3+\3+\3+\5")
        buf.write("+\u01ed\n+\3+\5+\u01f0\n+\3,\3,\3,\3,\3,\3,\3,\5,\u01f9")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0203\n-\3.\3.\5.\u0207")
        buf.write("\n.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\5\67\u0222\n\67\38\38\39\39\39\39\79\u022a")
        buf.write("\n9\f9\169\u022d\139\39\39\39\2\6FHJR:\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnp\2\n\4\2@@BB\3\2&\'\3\2(+\3\2\60")
        buf.write("\63\3\2./\3\2$%\4\2\24\27BB\3\2\22\23\2\u0240\2u\3\2\2")
        buf.write("\2\4z\3\2\2\2\6\u008c\3\2\2\2\b\u008e\3\2\2\2\n\u009a")
        buf.write("\3\2\2\2\f\u00aa\3\2\2\2\16\u00ae\3\2\2\2\20\u00bd\3\2")
        buf.write("\2\2\22\u00c1\3\2\2\2\24\u00c5\3\2\2\2\26\u00ca\3\2\2")
        buf.write("\2\30\u00cf\3\2\2\2\32\u00e4\3\2\2\2\34\u00e6\3\2\2\2")
        buf.write("\36\u00e9\3\2\2\2 \u00ed\3\2\2\2\"\u00f7\3\2\2\2$\u00ff")
        buf.write("\3\2\2\2&\u0102\3\2\2\2(\u0108\3\2\2\2*\u010e\3\2\2\2")
        buf.write(",\u0112\3\2\2\2.\u0121\3\2\2\2\60\u0128\3\2\2\2\62\u012c")
        buf.write("\3\2\2\2\64\u0155\3\2\2\2\66\u015a\3\2\2\28\u015c\3\2")
        buf.write("\2\2:\u0170\3\2\2\2<\u0172\3\2\2\2>\u017a\3\2\2\2@\u0185")
        buf.write("\3\2\2\2B\u018c\3\2\2\2D\u0193\3\2\2\2F\u0195\3\2\2\2")
        buf.write("H\u01a1\3\2\2\2J\u01ad\3\2\2\2L\u01bd\3\2\2\2N\u01c2\3")
        buf.write("\2\2\2P\u01ca\3\2\2\2R\u01cc\3\2\2\2T\u01ef\3\2\2\2V\u01f8")
        buf.write("\3\2\2\2X\u0202\3\2\2\2Z\u0206\3\2\2\2\\\u0208\3\2\2\2")
        buf.write("^\u020a\3\2\2\2`\u020c\3\2\2\2b\u020e\3\2\2\2d\u0210\3")
        buf.write("\2\2\2f\u0212\3\2\2\2h\u0214\3\2\2\2j\u0216\3\2\2\2l\u0221")
        buf.write("\3\2\2\2n\u0223\3\2\2\2p\u0225\3\2\2\2rt\5\4\3\2sr\3\2")
        buf.write("\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2")
        buf.write("xy\7\2\2\3y\3\3\2\2\2z}\7\32\2\2{|\7B\2\2|~\7\64\2\2}")
        buf.write("{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080\7B\2\2\u0080")
        buf.write("\u0084\7>\2\2\u0081\u0083\5\6\4\2\u0082\u0081\3\2\2\2")
        buf.write("\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3")
        buf.write("\2\2\2\u0085\u0087\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088")
        buf.write("\7?\2\2\u0088\5\3\2\2\2\u0089\u008d\5\b\5\2\u008a\u008d")
        buf.write("\5\n\6\2\u008b\u008d\5\22\n\2\u008c\u0089\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\7\3\2\2\2\u008e")
        buf.write("\u008f\7\"\2\2\u008f\u0090\t\2\2\2\u0090\u0091\7;\2\2")
        buf.write("\u0091\u0092\5\f\7\2\u0092\u0093\7:\2\2\u0093\u0096\7")
        buf.write("9\2\2\u0094\u0097\5h\65\2\u0095\u0097\7\37\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0099\5\62\32\2\u0099\t\3\2\2\2\u009a\u009b\7\"\2\2\u009b")
        buf.write("\u009c\7\33\2\2\u009c\u009d\7;\2\2\u009d\u009e\5\f\7\2")
        buf.write("\u009e\u009f\7:\2\2\u009f\u00a0\5\62\32\2\u00a0\13\3\2")
        buf.write("\2\2\u00a1\u00a6\5\16\b\2\u00a2\u00a3\7\67\2\2\u00a3\u00a5")
        buf.write("\5\16\b\2\u00a4\u00a2\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00ab\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a1\3")
        buf.write("\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\r\3\2\2\2\u00ac\u00af")
        buf.write("\5> \2\u00ad\u00af\5<\37\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b3\79\2\2\u00b1")
        buf.write("\u00b4\5h\65\2\u00b2\u00b4\5j\66\2\u00b3\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b2\3\2\2\2\u00b4\17\3\2\2\2\u00b5\u00be\5\22")
        buf.write("\n\2\u00b6\u00be\5\34\17\2\u00b7\u00be\5 \21\2\u00b8\u00be")
        buf.write("\5\"\22\2\u00b9\u00be\5(\25\2\u00ba\u00be\5$\23\2\u00bb")
        buf.write("\u00be\5&\24\2\u00bc\u00be\5*\26\2\u00bd\u00b5\3\2\2\2")
        buf.write("\u00bd\u00b6\3\2\2\2\u00bd\u00b7\3\2\2\2\u00bd\u00b8\3")
        buf.write("\2\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00ba\3\2\2\2\u00bd\u00bb")
        buf.write("\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\21\3\2\2\2\u00bf\u00c2")
        buf.write("\5\24\13\2\u00c0\u00c2\5\26\f\2\u00c1\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\78\2\2")
        buf.write("\u00c4\23\3\2\2\2\u00c5\u00c8\7 \2\2\u00c6\u00c9\5\30")
        buf.write("\r\2\u00c7\u00c9\5\32\16\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c9\25\3\2\2\2\u00ca\u00cd\7\34\2\2\u00cb\u00ce")
        buf.write("\5\30\r\2\u00cc\u00ce\5\32\16\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\27\3\2\2\2\u00cf\u00d0\5<\37\2\u00d0")
        buf.write("\u00d3\79\2\2\u00d1\u00d4\5h\65\2\u00d2\u00d4\5j\66\2")
        buf.write("\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\31\3\2")
        buf.write("\2\2\u00d5\u00d6\5> \2\u00d6\u00d9\79\2\2\u00d7\u00da")
        buf.write("\5h\65\2\u00d8\u00da\5j\66\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\7,\2\2")
        buf.write("\u00dc\u00dd\5B\"\2\u00dd\u00e5\3\2\2\2\u00de\u00df\5")
        buf.write("> \2\u00df\u00e0\7\67\2\2\u00e0\u00e1\5\32\16\2\u00e1")
        buf.write("\u00e2\7\67\2\2\u00e2\u00e3\5B\"\2\u00e3\u00e5\3\2\2\2")
        buf.write("\u00e4\u00d5\3\2\2\2\u00e4\u00de\3\2\2\2\u00e5\33\3\2")
        buf.write("\2\2\u00e6\u00e7\5\36\20\2\u00e7\u00e8\78\2\2\u00e8\35")
        buf.write("\3\2\2\2\u00e9\u00ea\5\66\34\2\u00ea\u00eb\7-\2\2\u00eb")
        buf.write("\u00ec\5B\"\2\u00ec\37\3\2\2\2\u00ed\u00ef\7\17\2\2\u00ee")
        buf.write("\u00f0\5\62\32\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2")
        buf.write("\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\5B\"\2\u00f2\u00f5")
        buf.write("\5\62\32\2\u00f3\u00f4\7\20\2\2\u00f4\u00f6\5\62\32\2")
        buf.write("\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6!\3\2\2")
        buf.write("\2\u00f7\u00f8\7\21\2\2\u00f8\u00f9\5\36\20\2\u00f9\u00fa")
        buf.write("\78\2\2\u00fa\u00fb\5B\"\2\u00fb\u00fc\78\2\2\u00fc\u00fd")
        buf.write("\5\36\20\2\u00fd\u00fe\5\62\32\2\u00fe#\3\2\2\2\u00ff")
        buf.write("\u0100\7\16\2\2\u0100\u0101\78\2\2\u0101%\3\2\2\2\u0102")
        buf.write("\u0104\7\30\2\2\u0103\u0105\5B\"\2\u0104\u0103\3\2\2\2")
        buf.write("\u0104\u0105\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\7")
        buf.write("8\2\2\u0107\'\3\2\2\2\u0108\u0109\7\r\2\2\u0109\u010a")
        buf.write("\78\2\2\u010a)\3\2\2\2\u010b\u010f\5,\27\2\u010c\u010f")
        buf.write("\5.\30\2\u010d\u010f\5\60\31\2\u010e\u010b\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0111\78\2\2\u0111+\3\2\2\2\u0112\u0117\5R*\2\u0113")
        buf.write("\u0114\7<\2\2\u0114\u0115\5B\"\2\u0115\u0116\7=\2\2\u0116")
        buf.write("\u0118\3\2\2\2\u0117\u0113\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\u011a\7\66\2\2\u011a\u011b")
        buf.write("\7B\2\2\u011b\u011c\7;\2\2\u011c\u011d\5@!\2\u011d\u011e")
        buf.write("\7:\2\2\u011e-\3\2\2\2\u011f\u0120\7B\2\2\u0120\u0122")
        buf.write("\7\66\2\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\u0124\7@\2\2\u0124\u0125\7;\2\2\u0125")
        buf.write("\u0126\5@!\2\u0126\u0127\7:\2\2\u0127/\3\2\2\2\u0128\u0129")
        buf.write("\5B\"\2\u0129\u012a\7\66\2\2\u012a\u012b\5\64\33\2\u012b")
        buf.write("\61\3\2\2\2\u012c\u0130\7>\2\2\u012d\u012f\5\20\t\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0130\3")
        buf.write("\2\2\2\u0133\u0134\7?\2\2\u0134\63\3\2\2\2\u0135\u0136")
        buf.write("\7\3\2\2\u0136\u0137\7;\2\2\u0137\u0156\7:\2\2\u0138\u0139")
        buf.write("\7\4\2\2\u0139\u013a\7;\2\2\u013a\u013b\5B\"\2\u013b\u013c")
        buf.write("\7:\2\2\u013c\u0156\3\2\2\2\u013d\u013e\7\5\2\2\u013e")
        buf.write("\u013f\7;\2\2\u013f\u0156\7:\2\2\u0140\u0141\7\6\2\2\u0141")
        buf.write("\u0142\7;\2\2\u0142\u0143\5B\"\2\u0143\u0144\7:\2\2\u0144")
        buf.write("\u0156\3\2\2\2\u0145\u0146\7\7\2\2\u0146\u0147\7;\2\2")
        buf.write("\u0147\u0156\7:\2\2\u0148\u0149\7\b\2\2\u0149\u014a\7")
        buf.write(";\2\2\u014a\u014b\5B\"\2\u014b\u014c\7:\2\2\u014c\u0156")
        buf.write("\3\2\2\2\u014d\u014e\7\t\2\2\u014e\u014f\7;\2\2\u014f")
        buf.write("\u0156\7:\2\2\u0150\u0151\7\n\2\2\u0151\u0152\7;\2\2\u0152")
        buf.write("\u0153\5B\"\2\u0153\u0154\7:\2\2\u0154\u0156\3\2\2\2\u0155")
        buf.write("\u0135\3\2\2\2\u0155\u0138\3\2\2\2\u0155\u013d\3\2\2\2")
        buf.write("\u0155\u0140\3\2\2\2\u0155\u0145\3\2\2\2\u0155\u0148\3")
        buf.write("\2\2\2\u0155\u014d\3\2\2\2\u0155\u0150\3\2\2\2\u0156\65")
        buf.write("\3\2\2\2\u0157\u015b\5> \2\u0158\u015b\58\35\2\u0159\u015b")
        buf.write("\5:\36\2\u015a\u0157\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u0159\3\2\2\2\u015b\67\3\2\2\2\u015c\u015d\5R*\2\u015d")
        buf.write("\u015e\7<\2\2\u015e\u015f\5B\"\2\u015f\u0160\7=\2\2\u0160")
        buf.write("9\3\2\2\2\u0161\u0166\5R*\2\u0162\u0163\7<\2\2\u0163\u0164")
        buf.write("\5B\"\2\u0164\u0165\7=\2\2\u0165\u0167\3\2\2\2\u0166\u0162")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0169\7\66\2\2\u0169\u016a\7B\2\2\u016a\u0171\3\2\2\2")
        buf.write("\u016b\u016c\7B\2\2\u016c\u016e\7\66\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171")
        buf.write("\7@\2\2\u0170\u0161\3\2\2\2\u0170\u016d\3\2\2\2\u0171")
        buf.write(";\3\2\2\2\u0172\u0177\5> \2\u0173\u0174\7\67\2\2\u0174")
        buf.write("\u0176\5> \2\u0175\u0173\3\2\2\2\u0176\u0179\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178=\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017b\t\2\2\2\u017b?\3\2\2\2\u017c")
        buf.write("\u0181\5B\"\2\u017d\u017e\7\67\2\2\u017e\u0180\5B\"\2")
        buf.write("\u017f\u017d\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3")
        buf.write("\2\2\2\u0181\u0182\3\2\2\2\u0182\u0186\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u017c\3\2\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186A\3\2\2\2\u0187\u0188\5D#\2\u0188")
        buf.write("\u0189\7\65\2\2\u0189\u018a\5D#\2\u018a\u018d\3\2\2\2")
        buf.write("\u018b\u018d\5D#\2\u018c\u0187\3\2\2\2\u018c\u018b\3\2")
        buf.write("\2\2\u018dC\3\2\2\2\u018e\u018f\5F$\2\u018f\u0190\5Z.")
        buf.write("\2\u0190\u0191\5F$\2\u0191\u0194\3\2\2\2\u0192\u0194\5")
        buf.write("F$\2\u0193\u018e\3\2\2\2\u0193\u0192\3\2\2\2\u0194E\3")
        buf.write("\2\2\2\u0195\u0196\b$\1\2\u0196\u0197\5H%\2\u0197\u019e")
        buf.write("\3\2\2\2\u0198\u0199\f\4\2\2\u0199\u019a\5d\63\2\u019a")
        buf.write("\u019b\5H%\2\u019b\u019d\3\2\2\2\u019c\u0198\3\2\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019fG\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\b%\1\2")
        buf.write("\u01a2\u01a3\5J&\2\u01a3\u01aa\3\2\2\2\u01a4\u01a5\f\4")
        buf.write("\2\2\u01a5\u01a6\5b\62\2\u01a6\u01a7\5J&\2\u01a7\u01a9")
        buf.write("\3\2\2\2\u01a8\u01a4\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01abI\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ad\u01ae\b&\1\2\u01ae\u01af\5L\'\2\u01af")
        buf.write("\u01b6\3\2\2\2\u01b0\u01b1\f\4\2\2\u01b1\u01b2\5`\61\2")
        buf.write("\u01b2\u01b3\5L\'\2\u01b3\u01b5\3\2\2\2\u01b4\u01b0\3")
        buf.write("\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7K\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba")
        buf.write("\5f\64\2\u01ba\u01bb\5L\'\2\u01bb\u01be\3\2\2\2\u01bc")
        buf.write("\u01be\5N(\2\u01bd\u01b9\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("M\3\2\2\2\u01bf\u01c0\7/\2\2\u01c0\u01c3\5N(\2\u01c1\u01c3")
        buf.write("\5P)\2\u01c2\u01bf\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3O")
        buf.write("\3\2\2\2\u01c4\u01c5\5R*\2\u01c5\u01c6\7<\2\2\u01c6\u01c7")
        buf.write("\5B\"\2\u01c7\u01c8\7=\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01cb")
        buf.write("\5R*\2\u01ca\u01c4\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cbQ")
        buf.write("\3\2\2\2\u01cc\u01cd\b*\1\2\u01cd\u01ce\5T+\2\u01ce\u01e0")
        buf.write("\3\2\2\2\u01cf\u01d4\f\4\2\2\u01d0\u01d1\7<\2\2\u01d1")
        buf.write("\u01d2\5B\"\2\u01d2\u01d3\7=\2\2\u01d3\u01d5\3\2\2\2\u01d4")
        buf.write("\u01d0\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d7\7\66\2\2\u01d7\u01dc\7B\2\2\u01d8\u01d9\7")
        buf.write(";\2\2\u01d9\u01da\5@!\2\u01da\u01db\7:\2\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01d8\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("\u01df\3\2\2\2\u01de\u01cf\3\2\2\2\u01df\u01e2\3\2\2\2")
        buf.write("\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1S\3\2\2")
        buf.write("\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7B\2\2\u01e4\u01e6")
        buf.write("\7\66\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u01ec\7@\2\2\u01e8\u01e9\7;\2\2\u01e9")
        buf.write("\u01ea\5@!\2\u01ea\u01eb\7:\2\2\u01eb\u01ed\3\2\2\2\u01ec")
        buf.write("\u01e8\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01f0\3\2\2\2")
        buf.write("\u01ee\u01f0\5V,\2\u01ef\u01e5\3\2\2\2\u01ef\u01ee\3\2")
        buf.write("\2\2\u01f0U\3\2\2\2\u01f1\u01f2\7\36\2\2\u01f2\u01f3\7")
        buf.write("B\2\2\u01f3\u01f4\7;\2\2\u01f4\u01f5\5@!\2\u01f5\u01f6")
        buf.write("\7:\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f9\5X-\2\u01f8\u01f1")
        buf.write("\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9W\3\2\2\2\u01fa\u01fb")
        buf.write("\7;\2\2\u01fb\u01fc\5B\"\2\u01fc\u01fd\7:\2\2\u01fd\u0203")
        buf.write("\3\2\2\2\u01fe\u0203\5l\67\2\u01ff\u0203\7B\2\2\u0200")
        buf.write("\u0203\7\31\2\2\u0201\u0203\7\35\2\2\u0202\u01fa\3\2\2")
        buf.write("\2\u0202\u01fe\3\2\2\2\u0202\u01ff\3\2\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0202\u0201\3\2\2\2\u0203Y\3\2\2\2\u0204\u0207")
        buf.write("\5\\/\2\u0205\u0207\5^\60\2\u0206\u0204\3\2\2\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207[\3\2\2\2\u0208\u0209\t\3\2\2\u0209")
        buf.write("]\3\2\2\2\u020a\u020b\t\4\2\2\u020b_\3\2\2\2\u020c\u020d")
        buf.write("\t\5\2\2\u020da\3\2\2\2\u020e\u020f\t\6\2\2\u020fc\3\2")
        buf.write("\2\2\u0210\u0211\t\7\2\2\u0211e\3\2\2\2\u0212\u0213\7")
        buf.write("#\2\2\u0213g\3\2\2\2\u0214\u0215\t\b\2\2\u0215i\3\2\2")
        buf.write("\2\u0216\u0217\7<\2\2\u0217\u0218\7D\2\2\u0218\u0219\7")
        buf.write("=\2\2\u0219\u021a\5h\65\2\u021ak\3\2\2\2\u021b\u0222\7")
        buf.write("E\2\2\u021c\u0222\7C\2\2\u021d\u0222\5n8\2\u021e\u0222")
        buf.write("\7A\2\2\u021f\u0222\5p9\2\u0220\u0222\7D\2\2\u0221\u021b")
        buf.write("\3\2\2\2\u0221\u021c\3\2\2\2\u0221\u021d\3\2\2\2\u0221")
        buf.write("\u021e\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0220\3\2\2\2")
        buf.write("\u0222m\3\2\2\2\u0223\u0224\t\t\2\2\u0224o\3\2\2\2\u0225")
        buf.write("\u0226\7<\2\2\u0226\u022b\5l\67\2\u0227\u0228\7\67\2\2")
        buf.write("\u0228\u022a\5l\67\2\u0229\u0227\3\2\2\2\u022a\u022d\3")
        buf.write("\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022e")
        buf.write("\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u022f\7=\2\2\u022f")
        buf.write("q\3\2\2\2\64u}\u0084\u008c\u0096\u00a6\u00aa\u00ae\u00b3")
        buf.write("\u00bd\u00c1\u00c8\u00cd\u00d3\u00d9\u00e4\u00ef\u00f5")
        buf.write("\u0104\u010e\u0117\u0121\u0130\u0155\u015a\u0166\u016d")
        buf.write("\u0170\u0177\u0181\u0185\u018c\u0193\u019e\u01aa\u01b6")
        buf.write("\u01bd\u01c2\u01ca\u01d4\u01dc\u01e0\u01e5\u01ec\u01ef")
        buf.write("\u01f8\u0202\u0206\u0221\u022b")
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
    RULE_method_dcl = 3
    RULE_constructor_decl = 4
    RULE_param_lst = 5
    RULE_param = 6
    RULE_statements = 7
    RULE_storedecl = 8
    RULE_constdecl = 9
    RULE_vardecl = 10
    RULE_non_inital_decl = 11
    RULE_inital_decl = 12
    RULE_assigndecl = 13
    RULE_assign = 14
    RULE_ifstmt = 15
    RULE_forstmt = 16
    RULE_continue_state = 17
    RULE_return_state = 18
    RULE_break_state = 19
    RULE_callstmt = 20
    RULE_instance_method_invo_access = 21
    RULE_static_method_invo_access = 22
    RULE_io_st = 23
    RULE_block = 24
    RULE_io_mt = 25
    RULE_lhs = 26
    RULE_arraycell = 27
    RULE_fieldaccess = 28
    RULE_idlst = 29
    RULE_iden = 30
    RULE_expr_lst = 31
    RULE_expr = 32
    RULE_expr1 = 33
    RULE_expr2 = 34
    RULE_expr3 = 35
    RULE_expr4 = 36
    RULE_expr5 = 37
    RULE_expr6 = 38
    RULE_expr7 = 39
    RULE_expr8 = 40
    RULE_expr9 = 41
    RULE_expr10 = 42
    RULE_expr11 = 43
    RULE_relational = 44
    RULE_relat_bool = 45
    RULE_relat_int_float = 46
    RULE_multiplying = 47
    RULE_adding = 48
    RULE_logical_bin = 49
    RULE_logical_not = 50
    RULE_typ = 51
    RULE_array_type = 52
    RULE_literal = 53
    RULE_bool_literal = 54
    RULE_array = 55

    ruleNames =  [ "program", "class_dcl", "class_body", "method_dcl", "constructor_decl", 
                   "param_lst", "param", "statements", "storedecl", "constdecl", 
                   "vardecl", "non_inital_decl", "inital_decl", "assigndecl", 
                   "assign", "ifstmt", "forstmt", "continue_state", "return_state", 
                   "break_state", "callstmt", "instance_method_invo_access", 
                   "static_method_invo_access", "io_st", "block", "io_mt", 
                   "lhs", "arraycell", "fieldaccess", "idlst", "iden", "expr_lst", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "relational", "relat_bool", "relat_int_float", "multiplying", 
                   "adding", "logical_bin", "logical_not", "typ", "array_type", 
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
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CLASS:
                self.state = 112
                self.class_dcl()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
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
            self.state = 120
            self.match(CSlangParser.CLASS)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(CSlangParser.ID)
                self.state = 122
                self.match(CSlangParser.SUPER_CLASS)


            self.state = 125
            self.match(CSlangParser.ID)
            self.state = 126
            self.match(CSlangParser.LBRASE)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 127
                self.class_body()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
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

        def method_dcl(self):
            return self.getTypedRuleContext(CSlangParser.Method_dclContext,0)


        def constructor_decl(self):
            return self.getTypedRuleContext(CSlangParser.Constructor_declContext,0)


        def storedecl(self):
            return self.getTypedRuleContext(CSlangParser.StoredeclContext,0)


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
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 135
                self.method_dcl()
                pass

            elif la_ == 2:
                self.state = 136
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.state = 137
                self.storedecl()
                pass


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

        def block(self):
            return self.getTypedRuleContext(CSlangParser.BlockContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dcl" ):
                return visitor.visitMethod_dcl(self)
            else:
                return visitor.visitChildren(self)




    def method_dcl(self):

        localctx = CSlangParser.Method_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CSlangParser.FUNC)
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==CSlangParser.AT_ID or _la==CSlangParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 142
            self.match(CSlangParser.LPAREN)
            self.state = 143
            self.param_lst()
            self.state = 144
            self.match(CSlangParser.RPAREN)
            self.state = 145
            self.match(CSlangParser.COLON)
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 146
                self.typ()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 147
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 150
            self.block()
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

        def block(self):
            return self.getTypedRuleContext(CSlangParser.BlockContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(CSlangParser.FUNC)
            self.state = 153
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 154
            self.match(CSlangParser.LPAREN)
            self.state = 155
            self.param_lst()
            self.state = 156
            self.match(CSlangParser.RPAREN)
            self.state = 157
            self.block()
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
        self.enterRule(localctx, 10, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.AT_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.param()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 160
                    self.match(CSlangParser.COMMA)
                    self.state = 161
                    self.param()
                    self.state = 166
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

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def idlst(self):
            return self.getTypedRuleContext(CSlangParser.IdlstContext,0)


        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 170
                self.iden()
                pass

            elif la_ == 2:
                self.state = 171
                self.idlst()
                pass


            self.state = 174
            self.match(CSlangParser.COLON)
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 175
                self.typ()
                pass
            elif token in [CSlangParser.LBRACK]:
                self.state = 176
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


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def storedecl(self):
            return self.getTypedRuleContext(CSlangParser.StoredeclContext,0)


        def assigndecl(self):
            return self.getTypedRuleContext(CSlangParser.AssigndeclContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(CSlangParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(CSlangParser.ForstmtContext,0)


        def break_state(self):
            return self.getTypedRuleContext(CSlangParser.Break_stateContext,0)


        def continue_state(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stateContext,0)


        def return_state(self):
            return self.getTypedRuleContext(CSlangParser.Return_stateContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(CSlangParser.CallstmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statements)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.storedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.assigndecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 183
                self.break_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 184
                self.continue_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 185
                self.return_state()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 186
                self.callstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoredeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def constdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(CSlangParser.VardeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_storedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStoredecl" ):
                return visitor.visitStoredecl(self)
            else:
                return visitor.visitChildren(self)




    def storedecl(self):

        localctx = CSlangParser.StoredeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_storedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CONST]:
                self.state = 189
                self.constdecl()
                pass
            elif token in [CSlangParser.VAR]:
                self.state = 190
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 193
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def non_inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Non_inital_declContext,0)


        def inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Inital_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = CSlangParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(CSlangParser.CONST)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 196
                self.non_inital_decl()
                pass

            elif la_ == 2:
                self.state = 197
                self.inital_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
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
            return CSlangParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = CSlangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(CSlangParser.VAR)
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 201
                self.non_inital_decl()
                pass

            elif la_ == 2:
                self.state = 202
                self.inital_decl()
                pass


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

        def idlst(self):
            return self.getTypedRuleContext(CSlangParser.IdlstContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


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
        self.enterRule(localctx, 22, self.RULE_non_inital_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.idlst()
            self.state = 206
            self.match(CSlangParser.COLON)
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 207
                self.typ()
                pass
            elif token in [CSlangParser.LBRACK]:
                self.state = 208
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

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INITIAL(self):
            return self.getToken(CSlangParser.INITIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


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
        self.enterRule(localctx, 24, self.RULE_inital_decl)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.iden()
                self.state = 212
                self.match(CSlangParser.COLON)
                self.state = 215
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                    self.state = 213
                    self.typ()
                    pass
                elif token in [CSlangParser.LBRACK]:
                    self.state = 214
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 217
                self.match(CSlangParser.INITIAL)
                self.state = 218
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.iden()
                self.state = 221
                self.match(CSlangParser.COMMA)
                self.state = 222
                self.inital_decl()
                self.state = 223
                self.match(CSlangParser.COMMA)
                self.state = 224
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigndeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(CSlangParser.AssignContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assigndecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigndecl" ):
                return visitor.visitAssigndecl(self)
            else:
                return visitor.visitChildren(self)




    def assigndecl(self):

        localctx = CSlangParser.AssigndeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assigndecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.assign()
            self.state = 229
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
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
            return CSlangParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = CSlangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.lhs()
            self.state = 232
            self.match(CSlangParser.ASSIGN)
            self.state = 233
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BlockContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = CSlangParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(CSlangParser.IF)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBRASE:
                self.state = 236
                self.block()


            self.state = 239
            self.expr()
            self.state = 240
            self.block()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 241
                self.match(CSlangParser.ELSE)
                self.state = 242
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.AssignContext)
            else:
                return self.getTypedRuleContext(CSlangParser.AssignContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMICOLON)
            else:
                return self.getToken(CSlangParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(CSlangParser.BlockContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = CSlangParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(CSlangParser.FOR)
            self.state = 246
            self.assign()
            self.state = 247
            self.match(CSlangParser.SEMICOLON)
            self.state = 248
            self.expr()
            self.state = 249
            self.match(CSlangParser.SEMICOLON)
            self.state = 250
            self.assign()
            self.state = 251
            self.block()
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
        self.enterRule(localctx, 34, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(CSlangParser.CONTINUE)
            self.state = 254
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

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_state" ):
                return visitor.visitReturn_state(self)
            else:
                return visitor.visitChildren(self)




    def return_state(self):

        localctx = CSlangParser.Return_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(CSlangParser.RETURN)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (CSlangParser.TRUE - 16)) | (1 << (CSlangParser.FALSE - 16)) | (1 << (CSlangParser.NULL - 16)) | (1 << (CSlangParser.SELF - 16)) | (1 << (CSlangParser.NEW - 16)) | (1 << (CSlangParser.NOT - 16)) | (1 << (CSlangParser.MINUS - 16)) | (1 << (CSlangParser.LPAREN - 16)) | (1 << (CSlangParser.LBRACK - 16)) | (1 << (CSlangParser.AT_ID - 16)) | (1 << (CSlangParser.STRING_LITERAL - 16)) | (1 << (CSlangParser.ID - 16)) | (1 << (CSlangParser.FLOAT_LITERAL - 16)) | (1 << (CSlangParser.NON_ZERO_INT - 16)) | (1 << (CSlangParser.INT_LITERAL - 16)))) != 0):
                self.state = 257
                self.expr()


            self.state = 260
            self.match(CSlangParser.SEMICOLON)
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
        self.enterRule(localctx, 38, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(CSlangParser.BREAK)
            self.state = 263
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def instance_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Instance_method_invo_accessContext,0)


        def static_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_invo_accessContext,0)


        def io_st(self):
            return self.getTypedRuleContext(CSlangParser.Io_stContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = CSlangParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 265
                self.instance_method_invo_access()
                pass

            elif la_ == 2:
                self.state = 266
                self.static_method_invo_access()
                pass

            elif la_ == 3:
                self.state = 267
                self.io_st()
                pass


            self.state = 270
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

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instance_method_invo_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invo_access" ):
                return visitor.visitInstance_method_invo_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invo_access(self):

        localctx = CSlangParser.Instance_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_instance_method_invo_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.expr8(0)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBRACK:
                self.state = 273
                self.match(CSlangParser.LBRACK)
                self.state = 274
                self.expr()
                self.state = 275
                self.match(CSlangParser.RBRACK)


            self.state = 279
            self.match(CSlangParser.DOT)
            self.state = 280
            self.match(CSlangParser.ID)

            self.state = 281
            self.match(CSlangParser.LPAREN)
            self.state = 282
            self.expr_lst()
            self.state = 283
            self.match(CSlangParser.RPAREN)
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
        self.enterRule(localctx, 44, self.RULE_static_method_invo_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 285
                self.match(CSlangParser.ID)
                self.state = 286
                self.match(CSlangParser.DOT)


            self.state = 289
            self.match(CSlangParser.AT_ID)

            self.state = 290
            self.match(CSlangParser.LPAREN)
            self.state = 291
            self.expr_lst()
            self.state = 292
            self.match(CSlangParser.RPAREN)
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def io_mt(self):
            return self.getTypedRuleContext(CSlangParser.Io_mtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_io_st

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_st" ):
                return visitor.visitIo_st(self)
            else:
                return visitor.visitChildren(self)




    def io_st(self):

        localctx = CSlangParser.Io_stContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_io_st)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.expr()
            self.state = 295
            self.match(CSlangParser.DOT)
            self.state = 296
            self.io_mt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
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
            return CSlangParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CSlangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(CSlangParser.LBRASE)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (CSlangParser.BREAK - 11)) | (1 << (CSlangParser.CONTINUE - 11)) | (1 << (CSlangParser.IF - 11)) | (1 << (CSlangParser.FOR - 11)) | (1 << (CSlangParser.TRUE - 11)) | (1 << (CSlangParser.FALSE - 11)) | (1 << (CSlangParser.RETURN - 11)) | (1 << (CSlangParser.NULL - 11)) | (1 << (CSlangParser.VAR - 11)) | (1 << (CSlangParser.SELF - 11)) | (1 << (CSlangParser.NEW - 11)) | (1 << (CSlangParser.CONST - 11)) | (1 << (CSlangParser.NOT - 11)) | (1 << (CSlangParser.MINUS - 11)) | (1 << (CSlangParser.LPAREN - 11)) | (1 << (CSlangParser.LBRACK - 11)) | (1 << (CSlangParser.AT_ID - 11)) | (1 << (CSlangParser.STRING_LITERAL - 11)) | (1 << (CSlangParser.ID - 11)) | (1 << (CSlangParser.FLOAT_LITERAL - 11)) | (1 << (CSlangParser.NON_ZERO_INT - 11)) | (1 << (CSlangParser.INT_LITERAL - 11)))) != 0):
                self.state = 299
                self.statements()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 305
            self.match(CSlangParser.RBRASE)
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

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_io_mt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_mt" ):
                return visitor.visitIo_mt(self)
            else:
                return visitor.visitChildren(self)




    def io_mt(self):

        localctx = CSlangParser.Io_mtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_io_mt)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(CSlangParser.T__0)
                self.state = 308
                self.match(CSlangParser.LPAREN)
                self.state = 309
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(CSlangParser.T__1)
                self.state = 311
                self.match(CSlangParser.LPAREN)
                self.state = 312
                self.expr()
                self.state = 313
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.match(CSlangParser.T__2)
                self.state = 316
                self.match(CSlangParser.LPAREN)
                self.state = 317
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                self.match(CSlangParser.T__3)
                self.state = 319
                self.match(CSlangParser.LPAREN)
                self.state = 320
                self.expr()
                self.state = 321
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
                self.match(CSlangParser.T__4)
                self.state = 324
                self.match(CSlangParser.LPAREN)
                self.state = 325
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 326
                self.match(CSlangParser.T__5)
                self.state = 327
                self.match(CSlangParser.LPAREN)
                self.state = 328
                self.expr()
                self.state = 329
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 331
                self.match(CSlangParser.T__6)
                self.state = 332
                self.match(CSlangParser.LPAREN)
                self.state = 333
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 334
                self.match(CSlangParser.T__7)
                self.state = 335
                self.match(CSlangParser.LPAREN)
                self.state = 336
                self.expr()
                self.state = 337
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


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def arraycell(self):
            return self.getTypedRuleContext(CSlangParser.ArraycellContext,0)


        def fieldaccess(self):
            return self.getTypedRuleContext(CSlangParser.FieldaccessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.iden()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.arraycell()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.fieldaccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraycellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraycell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraycell" ):
                return visitor.visitArraycell(self)
            else:
                return visitor.visitChildren(self)




    def arraycell(self):

        localctx = CSlangParser.ArraycellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arraycell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expr8(0)
            self.state = 347
            self.match(CSlangParser.LBRACK)
            self.state = 348
            self.expr()
            self.state = 349
            self.match(CSlangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_fieldaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldaccess" ):
                return visitor.visitFieldaccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldaccess(self):

        localctx = CSlangParser.FieldaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_fieldaccess)
        self._la = 0 # Token type
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.expr8(0)
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.LBRACK:
                    self.state = 352
                    self.match(CSlangParser.LBRACK)
                    self.state = 353
                    self.expr()
                    self.state = 354
                    self.match(CSlangParser.RBRACK)


                self.state = 358
                self.match(CSlangParser.DOT)
                self.state = 359
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 361
                    self.match(CSlangParser.ID)
                    self.state = 362
                    self.match(CSlangParser.DOT)


                self.state = 365
                self.match(CSlangParser.AT_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.IdenContext)
            else:
                return self.getTypedRuleContext(CSlangParser.IdenContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_idlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlst" ):
                return visitor.visitIdlst(self)
            else:
                return visitor.visitChildren(self)




    def idlst(self):

        localctx = CSlangParser.IdlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_idlst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.iden()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 369
                self.match(CSlangParser.COMMA)
                self.state = 370
                self.iden()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_iden

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIden" ):
                return visitor.visitIden(self)
            else:
                return visitor.visitChildren(self)




    def iden(self):

        localctx = CSlangParser.IdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_iden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
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


    class Expr_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lst" ):
                return visitor.visitExpr_lst(self)
            else:
                return visitor.visitChildren(self)




    def expr_lst(self):

        localctx = CSlangParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr_lst)
        self._la = 0 # Token type
        try:
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.NOT, CSlangParser.MINUS, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.AT_ID, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.expr()
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 379
                    self.match(CSlangParser.COMMA)
                    self.state = 380
                    self.expr()
                    self.state = 385
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def STRING_CONCAT(self):
            return self.getToken(CSlangParser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.expr1()
                self.state = 390
                self.match(CSlangParser.STRING_CONCAT)
                self.state = 391
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr2Context,i)


        def relational(self):
            return self.getTypedRuleContext(CSlangParser.RelationalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = CSlangParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr1)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.expr2(0)
                self.state = 397
                self.relational()
                self.state = 398
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    self.logical_bin()
                    self.state = 408
                    self.expr3(0) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 418
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 419
                    self.adding()
                    self.state = 420
                    self.expr4(0) 
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 430
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 431
                    self.multiplying()
                    self.state = 432
                    self.expr5() 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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


        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


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
        self.enterRule(localctx, 74, self.RULE_expr5)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.logical_not()
                self.state = 440
                self.expr5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.AT_ID, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
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
        self.enterRule(localctx, 76, self.RULE_expr6)
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.match(CSlangParser.MINUS)
                self.state = 446
                self.expr6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.AT_ID, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.expr7()
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


        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = CSlangParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr7)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.expr8(0)
                self.state = 451
                self.match(CSlangParser.LBRACK)
                self.state = 452
                self.expr()
                self.state = 453
                self.match(CSlangParser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 478
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 461
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 466
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSlangParser.LBRACK:
                        self.state = 462
                        self.match(CSlangParser.LBRACK)
                        self.state = 463
                        self.expr()
                        self.state = 464
                        self.match(CSlangParser.RBRACK)


                    self.state = 468
                    self.match(CSlangParser.DOT)
                    self.state = 469
                    self.match(CSlangParser.ID)
                    self.state = 474
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        self.state = 470
                        self.match(CSlangParser.LPAREN)
                        self.state = 471
                        self.expr_lst()
                        self.state = 472
                        self.match(CSlangParser.RPAREN)

             
                self.state = 480
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 481
                    self.match(CSlangParser.ID)
                    self.state = 482
                    self.match(CSlangParser.DOT)


                self.state = 485
                self.match(CSlangParser.AT_ID)
                self.state = 490
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 486
                    self.match(CSlangParser.LPAREN)
                    self.state = 487
                    self.expr_lst()
                    self.state = 488
                    self.match(CSlangParser.RPAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
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
        self.enterRule(localctx, 84, self.RULE_expr10)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(CSlangParser.NEW)
                self.state = 496
                self.match(CSlangParser.ID)
                self.state = 497
                self.match(CSlangParser.LPAREN)
                self.state = 498
                self.expr_lst()
                self.state = 499
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
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


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr11)
        try:
            self.state = 512
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.match(CSlangParser.LPAREN)
                self.state = 505
                self.expr()
                self.state = 506
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.FLOAT_LITERAL, CSlangParser.NON_ZERO_INT, CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.literal()
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 510
                self.match(CSlangParser.NULL)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 511
                self.match(CSlangParser.SELF)
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
        self.enterRule(localctx, 88, self.RULE_relational)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.EQUAL, CSlangParser.NOT_EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.relat_bool()
                pass
            elif token in [CSlangParser.LESS, CSlangParser.GREATER, CSlangParser.LESS_EQUAL, CSlangParser.GREATER_EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
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
        self.enterRule(localctx, 90, self.RULE_relat_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
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
        self.enterRule(localctx, 92, self.RULE_relat_int_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
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
        self.enterRule(localctx, 94, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
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
        self.enterRule(localctx, 96, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
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
        self.enterRule(localctx, 98, self.RULE_logical_bin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
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
        self.enterRule(localctx, 100, self.RULE_logical_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(CSlangParser.NOT)
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
        self.enterRule(localctx, 102, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
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

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(CSlangParser.LBRACK)
            self.state = 533
            self.match(CSlangParser.NON_ZERO_INT)
            self.state = 534
            self.match(CSlangParser.RBRACK)
            self.state = 535
            self.typ()
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
        self.enterRule(localctx, 106, self.RULE_literal)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(CSlangParser.INT_LITERAL)
                pass
            elif token in [CSlangParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.match(CSlangParser.FLOAT_LITERAL)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 539
                self.bool_literal()
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 540
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 541
                self.array()
                pass
            elif token in [CSlangParser.NON_ZERO_INT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 542
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
        self.enterRule(localctx, 108, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
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
        self.enterRule(localctx, 110, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(CSlangParser.LBRACK)
            self.state = 548
            self.literal()
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 549
                self.match(CSlangParser.COMMA)
                self.state = 550
                self.literal()
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 556
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
        self._predicates[34] = self.expr2_sempred
        self._predicates[35] = self.expr3_sempred
        self._predicates[36] = self.expr4_sempred
        self._predicates[40] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




