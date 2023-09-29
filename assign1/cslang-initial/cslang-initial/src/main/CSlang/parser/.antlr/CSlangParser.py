# Generated from e:\hocbaidcm\PPL\assignment\assign1\cslang-initial\cslang-initial\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3J")
        buf.write("\u020f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\3\2\3\3\3\3\3\3\5\3~\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\6\5\u0085\n\5\r\5\16\5\u0086\3\6\3\6\3\6")
        buf.write("\5\6\u008c\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u0095\n")
        buf.write("\7\f\7\16\7\u0098\13\7\3\7\3\7\3\b\6\b\u009d\n\b\r\b\16")
        buf.write("\b\u009e\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00b4\n\13\f\13")
        buf.write("\16\13\u00b7\13\13\3\13\5\13\u00ba\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\5\21")
        buf.write("\u00ca\n\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\7\24\u00d3")
        buf.write("\n\24\f\24\16\24\u00d6\13\24\3\24\5\24\u00d9\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\7\25\u00e1\n\25\f\25\16\25\u00e4")
        buf.write("\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00ed\n")
        buf.write("\26\f\26\16\26\u00f0\13\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u00f9\n\27\f\27\16\27\u00fc\13\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u0105\n\30\f\30\16\30")
        buf.write("\u0108\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0111")
        buf.write("\n\31\f\31\16\31\u0114\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u011b\n\32\3\33\3\33\3\33\5\33\u0120\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u012a\n\34\f\34")
        buf.write("\16\34\u012d\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u013c\n\35\f\35\16")
        buf.write("\35\u013f\13\35\3\36\3\36\3\36\3\36\3\36\5\36\u0146\n")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u014e\n\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0157\n\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u0160\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\5!\u016c\n!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\5#\u017b\n#\3$\3$\3$\5$\u0180\n$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\5%\u0190\n%\3&\3&\3&\5&\u0195\n")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\5(\u019f\n(\3(\3(\3(\3(")
        buf.write("\5(\u01a5\n(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\7/\u01c1\n/\f/\16")
        buf.write("/\u01c4\13/\3/\3/\3\60\3\60\5\60\u01ca\n\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\7\62\u01d4\n\62\f\62\16")
        buf.write("\62\u01d7\13\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01f5")
        buf.write("\n\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\38\58")
        buf.write("\u0202\n8\39\39\39\39\79\u0208\n9\f9\169\u020b\139\39")
        buf.write("\39\39\2\t(*,.\60\668:\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnp\2\n\3\2\62\65\3\2\60\61\3\2&\'\3\2()\3\2*-\4\2\35")
        buf.write("\35!!\3\2%)\6\2\25\30  $$CC\2\u0213\2u\3\2\2\2\4}\3\2")
        buf.write("\2\2\6\177\3\2\2\2\b\u0084\3\2\2\2\n\u0088\3\2\2\2\f\u0090")
        buf.write("\3\2\2\2\16\u009c\3\2\2\2\20\u00a0\3\2\2\2\22\u00a9\3")
        buf.write("\2\2\2\24\u00b9\3\2\2\2\26\u00bb\3\2\2\2\30\u00bf\3\2")
        buf.write("\2\2\32\u00c1\3\2\2\2\34\u00c3\3\2\2\2\36\u00c5\3\2\2")
        buf.write("\2 \u00c9\3\2\2\2\"\u00cb\3\2\2\2$\u00cd\3\2\2\2&\u00d8")
        buf.write("\3\2\2\2(\u00da\3\2\2\2*\u00e5\3\2\2\2,\u00f1\3\2\2\2")
        buf.write(".\u00fd\3\2\2\2\60\u0109\3\2\2\2\62\u011a\3\2\2\2\64\u011f")
        buf.write("\3\2\2\2\66\u0121\3\2\2\28\u012e\3\2\2\2:\u014d\3\2\2")
        buf.write("\2<\u0156\3\2\2\2>\u015f\3\2\2\2@\u016b\3\2\2\2B\u016d")
        buf.write("\3\2\2\2D\u017a\3\2\2\2F\u017c\3\2\2\2H\u018f\3\2\2\2")
        buf.write("J\u0191\3\2\2\2L\u0198\3\2\2\2N\u019c\3\2\2\2P\u01a6\3")
        buf.write("\2\2\2R\u01ae\3\2\2\2T\u01b1\3\2\2\2V\u01b4\3\2\2\2X\u01b8")
        buf.write("\3\2\2\2Z\u01bb\3\2\2\2\\\u01be\3\2\2\2^\u01c9\3\2\2\2")
        buf.write("`\u01cb\3\2\2\2b\u01d0\3\2\2\2d\u01d8\3\2\2\2f\u01f4\3")
        buf.write("\2\2\2h\u01f6\3\2\2\2j\u01f8\3\2\2\2l\u01fa\3\2\2\2n\u0201")
        buf.write("\3\2\2\2p\u0203\3\2\2\2rt\5\4\3\2sr\3\2\2\2tw\3\2\2\2")
        buf.write("us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2xy\7\2\2\3y\3")
        buf.write("\3\2\2\2z~\5\b\5\2{~\5\16\b\2|~\5\6\4\2}z\3\2\2\2}{\3")
        buf.write("\2\2\2}|\3\2\2\2~\5\3\2\2\2\177\u0080\7!\2\2\u0080\u0081")
        buf.write("\5H%\2\u0081\u0082\7:\2\2\u0082\7\3\2\2\2\u0083\u0085")
        buf.write("\5\n\6\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\t\3\2\2\2\u0088")
        buf.write("\u008b\7\33\2\2\u0089\u008a\7C\2\2\u008a\u008c\7\66\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d")
        buf.write("\3\2\2\2\u008d\u008e\7C\2\2\u008e\u008f\5\f\7\2\u008f")
        buf.write("\13\3\2\2\2\u0090\u0096\7@\2\2\u0091\u0095\5\20\t\2\u0092")
        buf.write("\u0095\5@!\2\u0093\u0095\5\22\n\2\u0094\u0091\3\2\2\2")
        buf.write("\u0094\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095\u0098\3")
        buf.write("\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\7A\2\2\u009a")
        buf.write("\r\3\2\2\2\u009b\u009d\5\20\t\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\17\3\2\2\2\u00a0\u00a1\7#\2\2\u00a1\u00a2\7C\2")
        buf.write("\2\u00a2\u00a3\7=\2\2\u00a3\u00a4\5\24\13\2\u00a4\u00a5")
        buf.write("\7<\2\2\u00a5\u00a6\7;\2\2\u00a6\u00a7\5l\67\2\u00a7\u00a8")
        buf.write("\5\\/\2\u00a8\21\3\2\2\2\u00a9\u00aa\7#\2\2\u00aa\u00ab")
        buf.write("\7\34\2\2\u00ab\u00ac\7=\2\2\u00ac\u00ad\5\24\13\2\u00ad")
        buf.write("\u00ae\7<\2\2\u00ae\u00af\5\\/\2\u00af\23\3\2\2\2\u00b0")
        buf.write("\u00b5\5\26\f\2\u00b1\u00b2\79\2\2\u00b2\u00b4\5\26\f")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00ba\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b0\3\2\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00ba\25\3\2\2\2\u00bb\u00bc\5b\62")
        buf.write("\2\u00bc\u00bd\7;\2\2\u00bd\u00be\5l\67\2\u00be\27\3\2")
        buf.write("\2\2\u00bf\u00c0\t\2\2\2\u00c0\31\3\2\2\2\u00c1\u00c2")
        buf.write("\t\3\2\2\u00c2\33\3\2\2\2\u00c3\u00c4\t\4\2\2\u00c4\35")
        buf.write("\3\2\2\2\u00c5\u00c6\7%\2\2\u00c6\37\3\2\2\2\u00c7\u00ca")
        buf.write("\5\"\22\2\u00c8\u00ca\5$\23\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca!\3\2\2\2\u00cb\u00cc\t\5\2\2\u00cc")
        buf.write("#\3\2\2\2\u00cd\u00ce\t\6\2\2\u00ce%\3\2\2\2\u00cf\u00d4")
        buf.write("\5(\25\2\u00d0\u00d1\79\2\2\u00d1\u00d3\5&\24\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\u00d9\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00cf\3\2\2\2\u00d8\u00d7")
        buf.write("\3\2\2\2\u00d9\'\3\2\2\2\u00da\u00db\b\25\1\2\u00db\u00dc")
        buf.write("\5*\26\2\u00dc\u00e2\3\2\2\2\u00dd\u00de\f\4\2\2\u00de")
        buf.write("\u00df\7\67\2\2\u00df\u00e1\5(\25\5\u00e0\u00dd\3\2\2")
        buf.write("\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3)\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6")
        buf.write("\b\26\1\2\u00e6\u00e7\5,\27\2\u00e7\u00ee\3\2\2\2\u00e8")
        buf.write("\u00e9\f\4\2\2\u00e9\u00ea\5 \21\2\u00ea\u00eb\5*\26\5")
        buf.write("\u00eb\u00ed\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ed\u00f0\3")
        buf.write("\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef+")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\b\27\1\2\u00f2")
        buf.write("\u00f3\5.\30\2\u00f3\u00fa\3\2\2\2\u00f4\u00f5\f\4\2\2")
        buf.write("\u00f5\u00f6\5\34\17\2\u00f6\u00f7\5.\30\2\u00f7\u00f9")
        buf.write("\3\2\2\2\u00f8\u00f4\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb-\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00fe\b\30\1\2\u00fe\u00ff\5\60\31")
        buf.write("\2\u00ff\u0106\3\2\2\2\u0100\u0101\f\4\2\2\u0101\u0102")
        buf.write("\5\32\16\2\u0102\u0103\5\60\31\2\u0103\u0105\3\2\2\2\u0104")
        buf.write("\u0100\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107/\3\2\2\2\u0108\u0106\3\2\2")
        buf.write("\2\u0109\u010a\b\31\1\2\u010a\u010b\5\62\32\2\u010b\u0112")
        buf.write("\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e\5\30\r\2\u010e")
        buf.write("\u010f\5\62\32\2\u010f\u0111\3\2\2\2\u0110\u010c\3\2\2")
        buf.write("\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\61\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116")
        buf.write("\5\64\33\2\u0116\u0117\5\36\20\2\u0117\u0118\5\62\32\2")
        buf.write("\u0118\u011b\3\2\2\2\u0119\u011b\5\64\33\2\u011a\u0115")
        buf.write("\3\2\2\2\u011a\u0119\3\2\2\2\u011b\63\3\2\2\2\u011c\u011d")
        buf.write("\7\61\2\2\u011d\u0120\5\64\33\2\u011e\u0120\5\66\34\2")
        buf.write("\u011f\u011c\3\2\2\2\u011f\u011e\3\2\2\2\u0120\65\3\2")
        buf.write("\2\2\u0121\u0122\b\34\1\2\u0122\u0123\58\35\2\u0123\u012b")
        buf.write("\3\2\2\2\u0124\u0125\f\4\2\2\u0125\u0126\7>\2\2\u0126")
        buf.write("\u0127\5\66\34\2\u0127\u0128\7?\2\2\u0128\u012a\3\2\2")
        buf.write("\2\u0129\u0124\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\67\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012e\u012f\b\35\1\2\u012f\u0130\5:\36\2\u0130")
        buf.write("\u013d\3\2\2\2\u0131\u0132\f\5\2\2\u0132\u0133\78\2\2")
        buf.write("\u0133\u013c\5:\36\2\u0134\u0135\f\4\2\2\u0135\u0136\7")
        buf.write("9\2\2\u0136\u0137\5:\36\2\u0137\u0138\7=\2\2\u0138\u0139")
        buf.write("\5&\24\2\u0139\u013a\7<\2\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u0131\3\2\2\2\u013b\u0134\3\2\2\2\u013c\u013f\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e9\3\2\2")
        buf.write("\2\u013f\u013d\3\2\2\2\u0140\u0141\7C\2\2\u0141\u0142")
        buf.write("\78\2\2\u0142\u014e\7C\2\2\u0143\u0144\7C\2\2\u0144\u0146")
        buf.write("\78\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0148\7C\2\2\u0148\u0149\7=\2\2\u0149")
        buf.write("\u014a\5&\24\2\u014a\u014b\7<\2\2\u014b\u014e\3\2\2\2")
        buf.write("\u014c\u014e\5<\37\2\u014d\u0140\3\2\2\2\u014d\u0145\3")
        buf.write("\2\2\2\u014d\u014c\3\2\2\2\u014e;\3\2\2\2\u014f\u0150")
        buf.write("\7\37\2\2\u0150\u0151\7C\2\2\u0151\u0152\7=\2\2\u0152")
        buf.write("\u0153\5&\24\2\u0153\u0154\7<\2\2\u0154\u0157\3\2\2\2")
        buf.write("\u0155\u0157\5> \2\u0156\u014f\3\2\2\2\u0156\u0155\3\2")
        buf.write("\2\2\u0157=\3\2\2\2\u0158\u0159\7=\2\2\u0159\u015a\5(")
        buf.write("\25\2\u015a\u015b\7<\2\2\u015b\u0160\3\2\2\2\u015c\u0160")
        buf.write("\5n8\2\u015d\u0160\7\36\2\2\u015e\u0160\7C\2\2\u015f\u0158")
        buf.write("\3\2\2\2\u015f\u015c\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160?\3\2\2\2\u0161\u016c\5F$\2\u0162")
        buf.write("\u016c\5B\"\2\u0163\u016c\5N(\2\u0164\u016c\5P)\2\u0165")
        buf.write("\u016c\5R*\2\u0166\u016c\5T+\2\u0167\u016c\5V,\2\u0168")
        buf.write("\u016c\5X-\2\u0169\u016c\5Z.\2\u016a\u016c\5d\63\2\u016b")
        buf.write("\u0161\3\2\2\2\u016b\u0162\3\2\2\2\u016b\u0163\3\2\2\2")
        buf.write("\u016b\u0164\3\2\2\2\u016b\u0165\3\2\2\2\u016b\u0166\3")
        buf.write("\2\2\2\u016b\u0167\3\2\2\2\u016b\u0168\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016a\3\2\2\2\u016cA\3\2\2\2\u016d\u016e")
        buf.write("\5D#\2\u016e\u016f\7:\2\2\u016fC\3\2\2\2\u0170\u0171\5")
        buf.write("^\60\2\u0171\u0172\79\2\2\u0172\u0173\5D#\2\u0173\u0174")
        buf.write("\79\2\2\u0174\u0175\5(\25\2\u0175\u017b\3\2\2\2\u0176")
        buf.write("\u0177\5^\60\2\u0177\u0178\7/\2\2\u0178\u0179\5(\25\2")
        buf.write("\u0179\u017b\3\2\2\2\u017a\u0170\3\2\2\2\u017a\u0176\3")
        buf.write("\2\2\2\u017bE\3\2\2\2\u017c\u017f\5h\65\2\u017d\u0180")
        buf.write("\5H%\2\u017e\u0180\5J&\2\u017f\u017d\3\2\2\2\u017f\u017e")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\7:\2\2\u0182")
        buf.write("G\3\2\2\2\u0183\u0184\7C\2\2\u0184\u0185\79\2\2\u0185")
        buf.write("\u0186\5H%\2\u0186\u0187\79\2\2\u0187\u0188\5(\25\2\u0188")
        buf.write("\u0190\3\2\2\2\u0189\u018a\7C\2\2\u018a\u018b\7;\2\2\u018b")
        buf.write("\u018c\5l\67\2\u018c\u018d\7.\2\2\u018d\u018e\5(\25\2")
        buf.write("\u018e\u0190\3\2\2\2\u018f\u0183\3\2\2\2\u018f\u0189\3")
        buf.write("\2\2\2\u0190I\3\2\2\2\u0191\u0192\5b\62\2\u0192\u0194")
        buf.write("\7;\2\2\u0193\u0195\5L\'\2\u0194\u0193\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\5l\67\2\u0197")
        buf.write("K\3\2\2\2\u0198\u0199\7>\2\2\u0199\u019a\7E\2\2\u019a")
        buf.write("\u019b\7?\2\2\u019bM\3\2\2\2\u019c\u019e\7\20\2\2\u019d")
        buf.write("\u019f\5\\/\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a1\5(\25\2\u01a1\u01a4\5")
        buf.write("\\/\2\u01a2\u01a3\7\21\2\2\u01a3\u01a5\5\\/\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5O\3\2\2\2\u01a6\u01a7")
        buf.write("\7\22\2\2\u01a7\u01a8\5F$\2\u01a8\u01a9\7:\2\2\u01a9\u01aa")
        buf.write("\5(\25\2\u01aa\u01ab\7:\2\2\u01ab\u01ac\5F$\2\u01ac\u01ad")
        buf.write("\5\\/\2\u01adQ\3\2\2\2\u01ae\u01af\7\16\2\2\u01af\u01b0")
        buf.write("\7:\2\2\u01b0S\3\2\2\2\u01b1\u01b2\7\17\2\2\u01b2\u01b3")
        buf.write("\7:\2\2\u01b3U\3\2\2\2\u01b4\u01b5\7\31\2\2\u01b5\u01b6")
        buf.write("\5(\25\2\u01b6\u01b7\7:\2\2\u01b7W\3\2\2\2\u01b8\u01b9")
        buf.write("\58\35\2\u01b9\u01ba\7:\2\2\u01baY\3\2\2\2\u01bb\u01bc")
        buf.write("\5:\36\2\u01bc\u01bd\7:\2\2\u01bd[\3\2\2\2\u01be\u01c2")
        buf.write("\7@\2\2\u01bf\u01c1\5@!\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7A\2\2")
        buf.write("\u01c6]\3\2\2\2\u01c7\u01ca\7C\2\2\u01c8\u01ca\5`\61\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca_\3\2\2")
        buf.write("\2\u01cb\u01cc\7C\2\2\u01cc\u01cd\7>\2\2\u01cd\u01ce\5")
        buf.write("(\25\2\u01ce\u01cf\7?\2\2\u01cfa\3\2\2\2\u01d0\u01d5\7")
        buf.write("C\2\2\u01d1\u01d2\79\2\2\u01d2\u01d4\7C\2\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d6\3\2\2\2\u01d6c\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8")
        buf.write("\u01d9\7\3\2\2\u01d9\u01da\5f\64\2\u01da\u01db\7:\2\2")
        buf.write("\u01dbe\3\2\2\2\u01dc\u01f5\7\4\2\2\u01dd\u01de\7\5\2")
        buf.write("\2\u01de\u01df\7=\2\2\u01df\u01e0\5(\25\2\u01e0\u01e1")
        buf.write("\7<\2\2\u01e1\u01f5\3\2\2\2\u01e2\u01f5\7\6\2\2\u01e3")
        buf.write("\u01e4\7\7\2\2\u01e4\u01e5\7=\2\2\u01e5\u01e6\5(\25\2")
        buf.write("\u01e6\u01e7\7<\2\2\u01e7\u01f5\3\2\2\2\u01e8\u01f5\7")
        buf.write("\b\2\2\u01e9\u01ea\7\t\2\2\u01ea\u01eb\7=\2\2\u01eb\u01ec")
        buf.write("\5(\25\2\u01ec\u01ed\7<\2\2\u01ed\u01f5\3\2\2\2\u01ee")
        buf.write("\u01f5\7\n\2\2\u01ef\u01f0\7\13\2\2\u01f0\u01f1\7=\2\2")
        buf.write("\u01f1\u01f2\5(\25\2\u01f2\u01f3\7<\2\2\u01f3\u01f5\3")
        buf.write("\2\2\2\u01f4\u01dc\3\2\2\2\u01f4\u01dd\3\2\2\2\u01f4\u01e2")
        buf.write("\3\2\2\2\u01f4\u01e3\3\2\2\2\u01f4\u01e8\3\2\2\2\u01f4")
        buf.write("\u01e9\3\2\2\2\u01f4\u01ee\3\2\2\2\u01f4\u01ef\3\2\2\2")
        buf.write("\u01f5g\3\2\2\2\u01f6\u01f7\t\7\2\2\u01f7i\3\2\2\2\u01f8")
        buf.write("\u01f9\t\b\2\2\u01f9k\3\2\2\2\u01fa\u01fb\t\t\2\2\u01fb")
        buf.write("m\3\2\2\2\u01fc\u0202\7E\2\2\u01fd\u0202\7D\2\2\u01fe")
        buf.write("\u0202\7F\2\2\u01ff\u0202\7B\2\2\u0200\u0202\5p9\2\u0201")
        buf.write("\u01fc\3\2\2\2\u0201\u01fd\3\2\2\2\u0201\u01fe\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0201\u0200\3\2\2\2\u0202o\3\2\2")
        buf.write("\2\u0203\u0204\7>\2\2\u0204\u0209\5n8\2\u0205\u0206\7")
        buf.write("9\2\2\u0206\u0208\5n8\2\u0207\u0205\3\2\2\2\u0208\u020b")
        buf.write("\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u020c\3\2\2\2\u020b\u0209\3\2\2\2\u020c\u020d\7?\2\2")
        buf.write("\u020dq\3\2\2\2)u}\u0086\u008b\u0094\u0096\u009e\u00b5")
        buf.write("\u00b9\u00c9\u00d4\u00d8\u00e2\u00ee\u00fa\u0106\u0112")
        buf.write("\u011a\u011f\u012b\u013b\u013d\u0145\u014d\u0156\u015f")
        buf.write("\u016b\u017a\u017f\u018f\u0194\u019e\u01a4\u01c2\u01c9")
        buf.write("\u01d5\u01f4\u0201\u0209")
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
                      "LBRACK", "RBRACK", "LBRASE", "RBRASE", "STRING_LITERAL", 
                      "ID", "FLOAT_LITERAL", "INT_LITERAL", "BOOL_LITERAL", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_gb = 1
    RULE_static_attribute_decl = 2
    RULE_class_lst = 3
    RULE_class_dcl = 4
    RULE_class_body = 5
    RULE_method_lst = 6
    RULE_method_dcl = 7
    RULE_constructor_decl = 8
    RULE_param_lst = 9
    RULE_param = 10
    RULE_multiplying = 11
    RULE_adding = 12
    RULE_logical_bin = 13
    RULE_logical_not = 14
    RULE_relational = 15
    RULE_relat_bool = 16
    RULE_relat_int_float = 17
    RULE_expr_lst = 18
    RULE_expr = 19
    RULE_expr1 = 20
    RULE_expr2 = 21
    RULE_expr3 = 22
    RULE_expr4 = 23
    RULE_expr5 = 24
    RULE_expr6 = 25
    RULE_expr7 = 26
    RULE_expr8 = 27
    RULE_expr9 = 28
    RULE_expr10 = 29
    RULE_expr11 = 30
    RULE_statements = 31
    RULE_assign_decl = 32
    RULE_attribute_assign = 33
    RULE_attribute_decl = 34
    RULE_attribute_init_nom = 35
    RULE_attribute_init_typ = 36
    RULE_array_element_typ = 37
    RULE_if_state = 38
    RULE_for_state = 39
    RULE_break_state = 40
    RULE_continue_state = 41
    RULE_return_state = 42
    RULE_instance_method_invo_access = 43
    RULE_static_method_invo_access = 44
    RULE_block_state = 45
    RULE_lhs = 46
    RULE_index_op = 47
    RULE_id_lst = 48
    RULE_io_st = 49
    RULE_io = 50
    RULE_fm = 51
    RULE_boolean = 52
    RULE_typ = 53
    RULE_literal = 54
    RULE_array = 55

    ruleNames =  [ "program", "gb", "static_attribute_decl", "class_lst", 
                   "class_dcl", "class_body", "method_lst", "method_dcl", 
                   "constructor_decl", "param_lst", "param", "multiplying", 
                   "adding", "logical_bin", "logical_not", "relational", 
                   "relat_bool", "relat_int_float", "expr_lst", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "expr11", "statements", 
                   "assign_decl", "attribute_assign", "attribute_decl", 
                   "attribute_init_nom", "attribute_init_typ", "array_element_typ", 
                   "if_state", "for_state", "break_state", "continue_state", 
                   "return_state", "instance_method_invo_access", "static_method_invo_access", 
                   "block_state", "lhs", "index_op", "id_lst", "io_st", 
                   "io", "fm", "boolean", "typ", "literal", "array" ]

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
    STRING_LITERAL=64
    ID=65
    FLOAT_LITERAL=66
    INT_LITERAL=67
    BOOL_LITERAL=68
    WS=69
    ERROR_CHAR=70
    UNCLOSE_STRING=71
    ILLEGAL_ESCAPE=72

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

        def gb(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.GbContext)
            else:
                return self.getTypedRuleContext(CSlangParser.GbContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CLASS) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 112
                self.gb()
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


    class GbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_lst(self):
            return self.getTypedRuleContext(CSlangParser.Class_lstContext,0)


        def method_lst(self):
            return self.getTypedRuleContext(CSlangParser.Method_lstContext,0)


        def static_attribute_decl(self):
            return self.getTypedRuleContext(CSlangParser.Static_attribute_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_gb




    def gb(self):

        localctx = CSlangParser.GbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_gb)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.class_lst()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.method_lst()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.static_attribute_decl()
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


    class Static_attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def attribute_init_nom(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_init_nomContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_attribute_decl




    def static_attribute_decl(self):

        localctx = CSlangParser.Static_attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_static_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(CSlangParser.CONST)

            self.state = 126
            self.attribute_init_nom()
            self.state = 127
            self.match(CSlangParser.SEMICOLON)
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




    def class_lst(self):

        localctx = CSlangParser.Class_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 129
                    self.class_dcl()

                else:
                    raise NoViableAltException(self)
                self.state = 132 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def class_body(self):
            return self.getTypedRuleContext(CSlangParser.Class_bodyContext,0)


        def SUPER_CLASS(self):
            return self.getToken(CSlangParser.SUPER_CLASS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_dcl




    def class_dcl(self):

        localctx = CSlangParser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(CSlangParser.CLASS)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 135
                self.match(CSlangParser.ID)
                self.state = 136
                self.match(CSlangParser.SUPER_CLASS)


            self.state = 139
            self.match(CSlangParser.ID)
            self.state = 140
            self.class_body()
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

        def LBRASE(self):
            return self.getToken(CSlangParser.LBRASE, 0)

        def RBRASE(self):
            return self.getToken(CSlangParser.RBRASE, 0)

        def method_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Method_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Method_dclContext,i)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StatementsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StatementsContext,i)


        def constructor_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Constructor_declContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Constructor_declContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_body




    def class_body(self):

        localctx = CSlangParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(CSlangParser.LBRASE)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.LPAREN) | (1 << CSlangParser.LBRACK))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSlangParser.STRING_LITERAL - 64)) | (1 << (CSlangParser.ID - 64)) | (1 << (CSlangParser.FLOAT_LITERAL - 64)) | (1 << (CSlangParser.INT_LITERAL - 64)) | (1 << (CSlangParser.BOOL_LITERAL - 64)))) != 0):
                self.state = 146
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 143
                    self.method_dcl()
                    pass

                elif la_ == 2:
                    self.state = 144
                    self.statements()
                    pass

                elif la_ == 3:
                    self.state = 145
                    self.constructor_decl()
                    pass


                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(CSlangParser.RBRASE)
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




    def method_lst(self):

        localctx = CSlangParser.Method_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 153
                    self.method_dcl()

                else:
                    raise NoViableAltException(self)
                self.state = 156 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

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


        def getRuleIndex(self):
            return CSlangParser.RULE_method_dcl




    def method_dcl(self):

        localctx = CSlangParser.Method_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(CSlangParser.FUNC)
            self.state = 159
            self.match(CSlangParser.ID)
            self.state = 160
            self.match(CSlangParser.LPAREN)
            self.state = 161
            self.param_lst()
            self.state = 162
            self.match(CSlangParser.RPAREN)
            self.state = 163
            self.match(CSlangParser.COLON)
            self.state = 164
            self.typ()
            self.state = 165
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




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(CSlangParser.FUNC)
            self.state = 168
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 169
            self.match(CSlangParser.LPAREN)
            self.state = 170
            self.param_lst()
            self.state = 171
            self.match(CSlangParser.RPAREN)
            self.state = 172
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




    def param_lst(self):

        localctx = CSlangParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.param()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 175
                    self.match(CSlangParser.COMMA)
                    self.state = 176
                    self.param()
                    self.state = 181
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




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.id_lst()
            self.state = 186
            self.match(CSlangParser.COLON)
            self.state = 187
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




    def multiplying(self):

        localctx = CSlangParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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




    def adding(self):

        localctx = CSlangParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
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




    def logical_bin(self):

        localctx = CSlangParser.Logical_binContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logical_bin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
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




    def logical_not(self):

        localctx = CSlangParser.Logical_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_logical_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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




    def relational(self):

        localctx = CSlangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relational)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.EQUAL, CSlangParser.NOT_EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.relat_bool()
                pass
            elif token in [CSlangParser.LESS, CSlangParser.GREATER, CSlangParser.LESS_EQUAL, CSlangParser.GREATER_EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
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




    def relat_bool(self):

        localctx = CSlangParser.Relat_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_relat_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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




    def relat_int_float(self):

        localctx = CSlangParser.Relat_int_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relat_int_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
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




    def expr_lst(self):

        localctx = CSlangParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr_lst)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.INT_LITERAL, CSlangParser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.expr(0)
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 206
                        self.match(CSlangParser.COMMA)
                        self.state = 207
                        self.expr_lst() 
                    self.state = 212
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [CSlangParser.COMMA, CSlangParser.RPAREN]:
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 219
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 220
                    self.match(CSlangParser.STRING_CONCAT)
                    self.state = 221
                    self.expr(3) 
                self.state = 226
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



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    self.relational()
                    self.state = 232
                    self.expr1(3) 
                self.state = 238
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



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    self.logical_bin()
                    self.state = 244
                    self.expr3(0) 
                self.state = 250
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



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    self.adding()
                    self.state = 256
                    self.expr4(0) 
                self.state = 262
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



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    self.multiplying()
                    self.state = 268
                    self.expr5() 
                self.state = 274
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

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def logical_not(self):
            return self.getTypedRuleContext(CSlangParser.Logical_notContext,0)


        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr5)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.expr6()
                self.state = 276
                self.logical_not()
                self.state = 277
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.expr6()
                pass


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




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr6)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(CSlangParser.MINUS)
                self.state = 283
                self.expr6()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.INT_LITERAL, CSlangParser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
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



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 290
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 291
                    self.match(CSlangParser.LBRACK)
                    self.state = 292
                    self.expr7(0)
                    self.state = 293
                    self.match(CSlangParser.RBRACK) 
                self.state = 299
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

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 313
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 303
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 304
                        self.match(CSlangParser.DOT)
                        self.state = 305
                        self.expr9()
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 306
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 307
                        self.match(CSlangParser.COMMA)
                        self.state = 308
                        self.expr9()

                        self.state = 309
                        self.match(CSlangParser.LPAREN)
                        self.state = 310
                        self.expr_lst()
                        self.state = 311
                        self.match(CSlangParser.RPAREN)
                        pass

             
                self.state = 317
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

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




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr9)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(CSlangParser.ID)
                self.state = 319
                self.match(CSlangParser.DOT)
                self.state = 320
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 321
                    self.match(CSlangParser.ID)
                    self.state = 322
                    self.match(CSlangParser.DOT)


                self.state = 325
                self.match(CSlangParser.ID)

                self.state = 326
                self.match(CSlangParser.LPAREN)
                self.state = 327
                self.expr_lst()
                self.state = 328
                self.match(CSlangParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
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




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr10)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(CSlangParser.NEW)
                self.state = 334
                self.match(CSlangParser.ID)

                self.state = 335
                self.match(CSlangParser.LPAREN)
                self.state = 336
                self.expr_lst()
                self.state = 337
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.LPAREN, CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.ID, CSlangParser.FLOAT_LITERAL, CSlangParser.INT_LITERAL, CSlangParser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
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

        def getRuleIndex(self):
            return CSlangParser.RULE_expr11




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr11)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(CSlangParser.LPAREN)
                self.state = 343
                self.expr(0)
                self.state = 344
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.LBRACK, CSlangParser.STRING_LITERAL, CSlangParser.FLOAT_LITERAL, CSlangParser.INT_LITERAL, CSlangParser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self.match(CSlangParser.ID)
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




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statements)
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.assign_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.if_state()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.for_state()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.break_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 356
                self.continue_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 357
                self.return_state()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
                self.instance_method_invo_access()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 359
                self.static_method_invo_access()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 360
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




    def assign_decl(self):

        localctx = CSlangParser.Assign_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assign_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.attribute_assign()
            self.state = 364
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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def attribute_assign(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_assign




    def attribute_assign(self):

        localctx = CSlangParser.Attribute_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_attribute_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 366
                self.lhs()
                self.state = 367
                self.match(CSlangParser.COMMA)
                self.state = 368
                self.attribute_assign()
                self.state = 369
                self.match(CSlangParser.COMMA)
                self.state = 370
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 372
                self.lhs()
                self.state = 373
                self.match(CSlangParser.ASSIGN)
                self.state = 374
                self.expr(0)
                pass


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




    def attribute_decl(self):

        localctx = CSlangParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.fm()
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 379
                self.attribute_init_nom()
                pass

            elif la_ == 2:
                self.state = 380
                self.attribute_init_typ()
                pass


            self.state = 383
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

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

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def INITIAL(self):
            return self.getToken(CSlangParser.INITIAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_init_nom




    def attribute_init_nom(self):

        localctx = CSlangParser.Attribute_init_nomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_attribute_init_nom)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(CSlangParser.ID)
                self.state = 386
                self.match(CSlangParser.COMMA)
                self.state = 387
                self.attribute_init_nom()
                self.state = 388
                self.match(CSlangParser.COMMA)
                self.state = 389
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(CSlangParser.ID)
                self.state = 392
                self.match(CSlangParser.COLON)
                self.state = 393
                self.typ()
                self.state = 394
                self.match(CSlangParser.INITIAL)
                self.state = 395
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

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def array_element_typ(self):
            return self.getTypedRuleContext(CSlangParser.Array_element_typContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_init_typ




    def attribute_init_typ(self):

        localctx = CSlangParser.Attribute_init_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_attribute_init_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.id_lst()
            self.state = 400
            self.match(CSlangParser.COLON)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBRACK:
                self.state = 401
                self.array_element_typ()


            self.state = 404
            self.typ()
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

        def INT_LITERAL(self):
            return self.getToken(CSlangParser.INT_LITERAL, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_element_typ




    def array_element_typ(self):

        localctx = CSlangParser.Array_element_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_array_element_typ)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(CSlangParser.LBRACK)
            self.state = 407
            self.match(CSlangParser.INT_LITERAL)
            self.state = 408
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




    def if_state(self):

        localctx = CSlangParser.If_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(CSlangParser.IF)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LBRASE:
                self.state = 411
                self.block_state()


            self.state = 414
            self.expr(0)
            self.state = 415
            self.block_state()
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 416
                self.match(CSlangParser.ELSE)
                self.state = 417
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

        def attribute_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Attribute_declContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Attribute_declContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMICOLON)
            else:
                return self.getToken(CSlangParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block_state(self):
            return self.getTypedRuleContext(CSlangParser.Block_stateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_state




    def for_state(self):

        localctx = CSlangParser.For_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_for_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(CSlangParser.FOR)
            self.state = 421
            self.attribute_decl()
            self.state = 422
            self.match(CSlangParser.SEMICOLON)
            self.state = 423
            self.expr(0)
            self.state = 424
            self.match(CSlangParser.SEMICOLON)
            self.state = 425
            self.attribute_decl()
            self.state = 426
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




    def break_state(self):

        localctx = CSlangParser.Break_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(CSlangParser.BREAK)
            self.state = 429
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




    def continue_state(self):

        localctx = CSlangParser.Continue_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(CSlangParser.CONTINUE)
            self.state = 432
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




    def return_state(self):

        localctx = CSlangParser.Return_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(CSlangParser.RETURN)
            self.state = 435
            self.expr(0)
            self.state = 436
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




    def instance_method_invo_access(self):

        localctx = CSlangParser.Instance_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_instance_method_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.expr8(0)
            self.state = 439
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




    def static_method_invo_access(self):

        localctx = CSlangParser.Static_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_static_method_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.expr9()
            self.state = 442
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




    def block_state(self):

        localctx = CSlangParser.Block_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_block_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(CSlangParser.LBRASE)
            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.LPAREN) | (1 << CSlangParser.LBRACK))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSlangParser.STRING_LITERAL - 64)) | (1 << (CSlangParser.ID - 64)) | (1 << (CSlangParser.FLOAT_LITERAL - 64)) | (1 << (CSlangParser.INT_LITERAL - 64)) | (1 << (CSlangParser.BOOL_LITERAL - 64)))) != 0):
                self.state = 445
                self.statements()
                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 451
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def index_op(self):
            return self.getTypedRuleContext(CSlangParser.Index_opContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhs




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_lhs)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.index_op()
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_index_op




    def index_op(self):

        localctx = CSlangParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(CSlangParser.ID)
            self.state = 458
            self.match(CSlangParser.LBRACK)
            self.state = 459
            self.expr(0)
            self.state = 460
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_id_lst




    def id_lst(self):

        localctx = CSlangParser.Id_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_id_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(CSlangParser.ID)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 463
                self.match(CSlangParser.COMMA)
                self.state = 464
                self.match(CSlangParser.ID)
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def io_st(self):

        localctx = CSlangParser.Io_stContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_io_st)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(CSlangParser.T__0)
            self.state = 471
            self.io()
            self.state = 472
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




    def io(self):

        localctx = CSlangParser.IoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_io)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.match(CSlangParser.T__1)
                pass
            elif token in [CSlangParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.match(CSlangParser.T__2)
                self.state = 476
                self.match(CSlangParser.LPAREN)
                self.state = 477
                self.expr(0)
                self.state = 478
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                self.match(CSlangParser.T__3)
                pass
            elif token in [CSlangParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 481
                self.match(CSlangParser.T__4)
                self.state = 482
                self.match(CSlangParser.LPAREN)
                self.state = 483
                self.expr(0)
                self.state = 484
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 486
                self.match(CSlangParser.T__5)
                pass
            elif token in [CSlangParser.T__6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 487
                self.match(CSlangParser.T__6)
                self.state = 488
                self.match(CSlangParser.LPAREN)
                self.state = 489
                self.expr(0)
                self.state = 490
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 492
                self.match(CSlangParser.T__7)
                pass
            elif token in [CSlangParser.T__8]:
                self.enterOuterAlt(localctx, 8)
                self.state = 493
                self.match(CSlangParser.T__8)
                self.state = 494
                self.match(CSlangParser.LPAREN)
                self.state = 495
                self.expr(0)
                self.state = 496
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




    def fm(self):

        localctx = CSlangParser.FmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
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


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(CSlangParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boolean




    def boolean(self):

        localctx = CSlangParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NOT) | (1 << CSlangParser.AND) | (1 << CSlangParser.OR) | (1 << CSlangParser.EQUAL) | (1 << CSlangParser.NOT_EQUAL))) != 0)):
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




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(CSlangParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(CSlangParser.FLOAT_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(CSlangParser.BOOL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(CSlangParser.STRING_LITERAL, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literal)
        try:
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.match(CSlangParser.INT_LITERAL)
                pass
            elif token in [CSlangParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(CSlangParser.FLOAT_LITERAL)
                pass
            elif token in [CSlangParser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.match(CSlangParser.BOOL_LITERAL)
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 509
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 510
                self.array()
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




    def array(self):

        localctx = CSlangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(CSlangParser.LBRACK)
            self.state = 514
            self.literal()
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 515
                self.match(CSlangParser.COMMA)
                self.state = 516
                self.literal()
                self.state = 521
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 522
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
        self._predicates[19] = self.expr_sempred
        self._predicates[20] = self.expr1_sempred
        self._predicates[21] = self.expr2_sempred
        self._predicates[22] = self.expr3_sempred
        self._predicates[23] = self.expr4_sempred
        self._predicates[26] = self.expr7_sempred
        self._predicates[27] = self.expr8_sempred
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
         




