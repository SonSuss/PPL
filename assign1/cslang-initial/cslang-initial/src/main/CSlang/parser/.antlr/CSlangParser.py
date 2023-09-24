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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u0214\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\7\2|\n\2\f\2\16\2\177\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\5\3\u0086\n\3\3\4\6\4\u0089\n\4\r\4\16\4\u008a")
        buf.write("\3\5\3\5\3\5\3\5\5\5\u0091\n\5\3\5\3\5\3\6\3\6\3\6\7\6")
        buf.write("\u0098\n\6\f\6\16\6\u009b\13\6\3\6\3\6\3\7\6\7\u00a0\n")
        buf.write("\7\r\7\16\7\u00a1\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\7\n\u00b6\n\n\f\n")
        buf.write("\16\n\u00b9\13\n\3\n\3\n\3\13\3\13\3\13\7\13\u00c0\n\13")
        buf.write("\f\13\16\13\u00c3\13\13\3\13\5\13\u00c6\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\7\r\u00cf\n\r\f\r\16\r\u00d2\13\r\3")
        buf.write("\r\5\r\u00d5\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00dd")
        buf.write("\n\16\f\16\16\16\u00e0\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00e9\n\17\f\17\16\17\u00ec\13\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00f5\n\20\f\20\16")
        buf.write("\20\u00f8\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21")
        buf.write("\u0101\n\21\f\21\16\21\u0104\13\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u010d\n\22\f\22\16\22\u0110\13\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u0117\n\23\3\24\3\24\3")
        buf.write("\24\5\24\u011c\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u0126\n\25\f\25\16\25\u0129\13\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0131\n\26\f\26\16\26\u0134")
        buf.write("\13\26\3\27\3\27\3\27\3\27\5\27\u013a\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0145\n\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \6 \u0157\n \r \16 \u0158\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\5!\u0163\n!\3\"\5\"\u0166\n\"\3\"\3\"\3")
        buf.write("\"\5\"\u016b\n\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\5")
        buf.write("%\u0179\n%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\5\'\u0186")
        buf.write("\n\'\3\'\3\'\3\'\3\'\5\'\u018c\n\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\5.\u01ab\n.\3.\3.\3.\3.\3.\3.\3/\3/\5/\u01b5")
        buf.write("\n/\3\60\3\60\3\60\7\60\u01ba\n\60\f\60\16\60\u01bd\13")
        buf.write("\60\3\61\3\61\3\61\3\61\5\61\u01c3\n\61\3\62\3\62\5\62")
        buf.write("\u01c7\n\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\65\3\65\5\65\u01d8\n\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\7\66\u01e2\n\66\f")
        buf.write("\66\16\66\u01e5\13\66\3\67\3\67\3\67\3\67\3\67\38\38\5")
        buf.write("8\u01ee\n8\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u020c\n:\3")
        buf.write(";\3;\3<\3<\3=\3=\3=\2\t\32\34\36 \"(*>\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvx\2\n\3\2\61\64\3\2/\60\3\2%")
        buf.write("&\3\2\'(\3\2),\4\2\35\35!!\3\2$(\4\2\25\30  \2\u0212\2")
        buf.write("}\3\2\2\2\4\u0085\3\2\2\2\6\u0088\3\2\2\2\b\u008c\3\2")
        buf.write("\2\2\n\u0094\3\2\2\2\f\u009f\3\2\2\2\16\u00a3\3\2\2\2")
        buf.write("\20\u00ac\3\2\2\2\22\u00b3\3\2\2\2\24\u00c5\3\2\2\2\26")
        buf.write("\u00c7\3\2\2\2\30\u00d4\3\2\2\2\32\u00d6\3\2\2\2\34\u00e1")
        buf.write("\3\2\2\2\36\u00ed\3\2\2\2 \u00f9\3\2\2\2\"\u0105\3\2\2")
        buf.write("\2$\u0116\3\2\2\2&\u011b\3\2\2\2(\u011d\3\2\2\2*\u012a")
        buf.write("\3\2\2\2,\u0139\3\2\2\2.\u0144\3\2\2\2\60\u0146\3\2\2")
        buf.write("\2\62\u0148\3\2\2\2\64\u014a\3\2\2\2\66\u014c\3\2\2\2")
        buf.write("8\u014e\3\2\2\2:\u0151\3\2\2\2<\u0153\3\2\2\2>\u0156\3")
        buf.write("\2\2\2@\u0162\3\2\2\2B\u0165\3\2\2\2D\u016c\3\2\2\2F\u016f")
        buf.write("\3\2\2\2H\u0173\3\2\2\2J\u017c\3\2\2\2L\u0183\3\2\2\2")
        buf.write("N\u018d\3\2\2\2P\u0195\3\2\2\2R\u0198\3\2\2\2T\u019b\3")
        buf.write("\2\2\2V\u019f\3\2\2\2X\u01a3\3\2\2\2Z\u01aa\3\2\2\2\\")
        buf.write("\u01b4\3\2\2\2^\u01b6\3\2\2\2`\u01c2\3\2\2\2b\u01c6\3")
        buf.write("\2\2\2d\u01ca\3\2\2\2f\u01ce\3\2\2\2h\u01d7\3\2\2\2j\u01de")
        buf.write("\3\2\2\2l\u01e6\3\2\2\2n\u01ed\3\2\2\2p\u01ef\3\2\2\2")
        buf.write("r\u020b\3\2\2\2t\u020d\3\2\2\2v\u020f\3\2\2\2x\u0211\3")
        buf.write("\2\2\2z|\5\4\3\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3")
        buf.write("\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081\7\2\2\3")
        buf.write("\u0081\3\3\2\2\2\u0082\u0086\5\6\4\2\u0083\u0086\5\f\7")
        buf.write("\2\u0084\u0086\5> \2\u0085\u0082\3\2\2\2\u0085\u0083\3")
        buf.write("\2\2\2\u0085\u0084\3\2\2\2\u0086\5\3\2\2\2\u0087\u0089")
        buf.write("\5\b\5\2\u0088\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\7\3\2\2\2\u008c")
        buf.write("\u008d\7\33\2\2\u008d\u0090\7B\2\2\u008e\u008f\7\65\2")
        buf.write("\2\u008f\u0091\7B\2\2\u0090\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\5\n\6\2\u0093")
        buf.write("\t\3\2\2\2\u0094\u0099\7?\2\2\u0095\u0098\5\16\b\2\u0096")
        buf.write("\u0098\5> \2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7")
        buf.write("@\2\2\u009d\13\3\2\2\2\u009e\u00a0\5\16\b\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\r\3\2\2\2\u00a3\u00a4\7#\2\2\u00a4")
        buf.write("\u00a5\7B\2\2\u00a5\u00a6\7<\2\2\u00a6\u00a7\5\24\13\2")
        buf.write("\u00a7\u00a8\7;\2\2\u00a8\u00a9\7:\2\2\u00a9\u00aa\5x")
        buf.write("=\2\u00aa\u00ab\5\22\n\2\u00ab\17\3\2\2\2\u00ac\u00ad")
        buf.write("\7#\2\2\u00ad\u00ae\7\34\2\2\u00ae\u00af\7<\2\2\u00af")
        buf.write("\u00b0\5\24\13\2\u00b0\u00b1\7;\2\2\u00b1\u00b2\5\22\n")
        buf.write("\2\u00b2\21\3\2\2\2\u00b3\u00b7\7?\2\2\u00b4\u00b6\5>")
        buf.write(" \2\u00b5\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00bb\7@\2\2\u00bb\23\3\2\2\2\u00bc")
        buf.write("\u00c1\5\26\f\2\u00bd\u00be\78\2\2\u00be\u00c0\5\26\f")
        buf.write("\2\u00bf\u00bd\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c6\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00bc\3\2\2\2")
        buf.write("\u00c5\u00c4\3\2\2\2\u00c6\25\3\2\2\2\u00c7\u00c8\5j\66")
        buf.write("\2\u00c8\u00c9\7:\2\2\u00c9\u00ca\5x=\2\u00ca\27\3\2\2")
        buf.write("\2\u00cb\u00d0\5\32\16\2\u00cc\u00cd\78\2\2\u00cd\u00cf")
        buf.write("\5\30\r\2\u00ce\u00cc\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d5\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00cb\3")
        buf.write("\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\31\3\2\2\2\u00d6\u00d7")
        buf.write("\b\16\1\2\u00d7\u00d8\5\34\17\2\u00d8\u00de\3\2\2\2\u00d9")
        buf.write("\u00da\f\4\2\2\u00da\u00db\7\66\2\2\u00db\u00dd\5\32\16")
        buf.write("\5\u00dc\u00d9\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\33\3\2\2\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e1\u00e2\b\17\1\2\u00e2\u00e3\5\36\20\2\u00e3")
        buf.write("\u00ea\3\2\2\2\u00e4\u00e5\f\4\2\2\u00e5\u00e6\58\35\2")
        buf.write("\u00e6\u00e7\5\34\17\5\u00e7\u00e9\3\2\2\2\u00e8\u00e4")
        buf.write("\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\35\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed")
        buf.write("\u00ee\b\20\1\2\u00ee\u00ef\5 \21\2\u00ef\u00f6\3\2\2")
        buf.write("\2\u00f0\u00f1\f\4\2\2\u00f1\u00f2\5\64\33\2\u00f2\u00f3")
        buf.write("\5 \21\2\u00f3\u00f5\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f5")
        buf.write("\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\37\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\b\21")
        buf.write("\1\2\u00fa\u00fb\5\"\22\2\u00fb\u0102\3\2\2\2\u00fc\u00fd")
        buf.write("\f\4\2\2\u00fd\u00fe\5\62\32\2\u00fe\u00ff\5\"\22\2\u00ff")
        buf.write("\u0101\3\2\2\2\u0100\u00fc\3\2\2\2\u0101\u0104\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103!\3\2\2")
        buf.write("\2\u0104\u0102\3\2\2\2\u0105\u0106\b\22\1\2\u0106\u0107")
        buf.write("\5$\23\2\u0107\u010e\3\2\2\2\u0108\u0109\f\4\2\2\u0109")
        buf.write("\u010a\5\60\31\2\u010a\u010b\5$\23\2\u010b\u010d\3\2\2")
        buf.write("\2\u010c\u0108\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f#\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0111\u0112\5&\24\2\u0112\u0113\5\66\34\2\u0113")
        buf.write("\u0114\5$\23\2\u0114\u0117\3\2\2\2\u0115\u0117\5&\24\2")
        buf.write("\u0116\u0111\3\2\2\2\u0116\u0115\3\2\2\2\u0117%\3\2\2")
        buf.write("\2\u0118\u0119\7\60\2\2\u0119\u011c\5(\25\2\u011a\u011c")
        buf.write("\5(\25\2\u011b\u0118\3\2\2\2\u011b\u011a\3\2\2\2\u011c")
        buf.write("\'\3\2\2\2\u011d\u011e\b\25\1\2\u011e\u011f\5*\26\2\u011f")
        buf.write("\u0127\3\2\2\2\u0120\u0121\f\4\2\2\u0121\u0122\7=\2\2")
        buf.write("\u0122\u0123\5\30\r\2\u0123\u0124\7>\2\2\u0124\u0126\3")
        buf.write("\2\2\2\u0125\u0120\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128)\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u012a\u012b\b\26\1\2\u012b\u012c\5,\27\2\u012c")
        buf.write("\u0132\3\2\2\2\u012d\u012e\f\4\2\2\u012e\u012f\7\67\2")
        buf.write("\2\u012f\u0131\7B\2\2\u0130\u012d\3\2\2\2\u0131\u0134")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("+\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\7\37\2\2\u0136")
        buf.write("\u0137\7B\2\2\u0137\u013a\5\30\r\2\u0138\u013a\5.\30\2")
        buf.write("\u0139\u0135\3\2\2\2\u0139\u0138\3\2\2\2\u013a-\3\2\2")
        buf.write("\2\u013b\u0145\5b\62\2\u013c\u0145\5l\67\2\u013d\u013e")
        buf.write("\7<\2\2\u013e\u013f\5\32\16\2\u013f\u0140\7;\2\2\u0140")
        buf.write("\u0145\3\2\2\2\u0141\u0145\7G\2\2\u0142\u0145\7A\2\2\u0143")
        buf.write("\u0145\7\36\2\2\u0144\u013b\3\2\2\2\u0144\u013c\3\2\2")
        buf.write("\2\u0144\u013d\3\2\2\2\u0144\u0141\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0144\u0143\3\2\2\2\u0145/\3\2\2\2\u0146\u0147")
        buf.write("\t\2\2\2\u0147\61\3\2\2\2\u0148\u0149\t\3\2\2\u0149\63")
        buf.write("\3\2\2\2\u014a\u014b\t\4\2\2\u014b\65\3\2\2\2\u014c\u014d")
        buf.write("\7$\2\2\u014d\67\3\2\2\2\u014e\u014f\5:\36\2\u014f\u0150")
        buf.write("\5<\37\2\u01509\3\2\2\2\u0151\u0152\t\5\2\2\u0152;\3\2")
        buf.write("\2\2\u0153\u0154\t\6\2\2\u0154=\3\2\2\2\u0155\u0157\5")
        buf.write("@!\2\u0156\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159?\3\2\2\2\u015a\u0163")
        buf.write("\5B\"\2\u015b\u0163\5L\'\2\u015c\u0163\5N(\2\u015d\u0163")
        buf.write("\5R*\2\u015e\u0163\5Z.\2\u015f\u0163\5T+\2\u0160\u0163")
        buf.write("\5P)\2\u0161\u0163\5p9\2\u0162\u015a\3\2\2\2\u0162\u015b")
        buf.write("\3\2\2\2\u0162\u015c\3\2\2\2\u0162\u015d\3\2\2\2\u0162")
        buf.write("\u015e\3\2\2\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0163A\3\2\2\2\u0164\u0166\5t;\2")
        buf.write("\u0165\u0164\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u016a\3")
        buf.write("\2\2\2\u0167\u016b\5D#\2\u0168\u016b\5H%\2\u0169\u016b")
        buf.write("\5J&\2\u016a\u0167\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016bC\3\2\2\2\u016c\u016d\5F$\2\u016d\u016e")
        buf.write("\79\2\2\u016eE\3\2\2\2\u016f\u0170\5\\/\2\u0170\u0171")
        buf.write("\7.\2\2\u0171\u0172\5\32\16\2\u0172G\3\2\2\2\u0173\u0174")
        buf.write("\5\\/\2\u0174\u0175\7:\2\2\u0175\u0178\5x=\2\u0176\u0177")
        buf.write("\7-\2\2\u0177\u0179\5\32\16\2\u0178\u0176\3\2\2\2\u0178")
        buf.write("\u0179\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b\79\2\2")
        buf.write("\u017bI\3\2\2\2\u017c\u017d\5\\/\2\u017d\u017e\7:\2\2")
        buf.write("\u017e\u017f\7=\2\2\u017f\u0180\7\25\2\2\u0180\u0181\7")
        buf.write(">\2\2\u0181\u0182\79\2\2\u0182K\3\2\2\2\u0183\u0185\7")
        buf.write("\20\2\2\u0184\u0186\5V,\2\u0185\u0184\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\5\32\16\2\u0188")
        buf.write("\u018b\5X-\2\u0189\u018a\7\21\2\2\u018a\u018c\5X-\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cM\3\2\2\2\u018d")
        buf.write("\u018e\7\22\2\2\u018e\u018f\5F$\2\u018f\u0190\79\2\2\u0190")
        buf.write("\u0191\5\32\16\2\u0191\u0192\79\2\2\u0192\u0193\5F$\2")
        buf.write("\u0193\u0194\5V,\2\u0194O\3\2\2\2\u0195\u0196\7\16\2\2")
        buf.write("\u0196\u0197\79\2\2\u0197Q\3\2\2\2\u0198\u0199\7\17\2")
        buf.write("\2\u0199\u019a\79\2\2\u019aS\3\2\2\2\u019b\u019c\7\31")
        buf.write("\2\2\u019c\u019d\5\32\16\2\u019d\u019e\79\2\2\u019eU\3")
        buf.write("\2\2\2\u019f\u01a0\7<\2\2\u01a0\u01a1\5> \2\u01a1\u01a2")
        buf.write("\7;\2\2\u01a2W\3\2\2\2\u01a3\u01a4\7?\2\2\u01a4\u01a5")
        buf.write("\5> \2\u01a5\u01a6\7@\2\2\u01a6Y\3\2\2\2\u01a7\u01a8\5")
        buf.write("\32\16\2\u01a8\u01a9\7\67\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01a7\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u01ad\7B\2\2\u01ad\u01ae\7<\2\2\u01ae\u01af\5\30")
        buf.write("\r\2\u01af\u01b0\7;\2\2\u01b0\u01b1\79\2\2\u01b1[\3\2")
        buf.write("\2\2\u01b2\u01b5\5j\66\2\u01b3\u01b5\5^\60\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5]\3\2\2\2\u01b6\u01bb")
        buf.write("\5`\61\2\u01b7\u01b8\78\2\2\u01b8\u01ba\5`\61\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bb\u01bc\3\2\2\2\u01bc_\3\2\2\2\u01bd\u01bb\3\2\2")
        buf.write("\2\u01be\u01c3\5d\63\2\u01bf\u01c3\5b\62\2\u01c0\u01c3")
        buf.write("\5f\64\2\u01c1\u01c3\3\2\2\2\u01c2\u01be\3\2\2\2\u01c2")
        buf.write("\u01bf\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2")
        buf.write("\u01c3a\3\2\2\2\u01c4\u01c5\7B\2\2\u01c5\u01c7\7\67\2")
        buf.write("\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c9\7B\2\2\u01c9c\3\2\2\2\u01ca\u01cb")
        buf.write("\5\32\16\2\u01cb\u01cc\7\67\2\2\u01cc\u01cd\7B\2\2\u01cd")
        buf.write("e\3\2\2\2\u01ce\u01cf\5\32\16\2\u01cf\u01d0\7\67\2\2\u01d0")
        buf.write("\u01d1\7B\2\2\u01d1\u01d2\7<\2\2\u01d2\u01d3\5\30\r\2")
        buf.write("\u01d3\u01d4\7;\2\2\u01d4g\3\2\2\2\u01d5\u01d6\7B\2\2")
        buf.write("\u01d6\u01d8\7\67\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\7B\2\2\u01da")
        buf.write("\u01db\7<\2\2\u01db\u01dc\5\30\r\2\u01dc\u01dd\7;\2\2")
        buf.write("\u01ddi\3\2\2\2\u01de\u01e3\5n8\2\u01df\u01e0\78\2\2\u01e0")
        buf.write("\u01e2\5n8\2\u01e1\u01df\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4k\3\2\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e7\7B\2\2\u01e7\u01e8\7=\2\2\u01e8")
        buf.write("\u01e9\5\32\16\2\u01e9\u01ea\7>\2\2\u01eam\3\2\2\2\u01eb")
        buf.write("\u01ee\7B\2\2\u01ec\u01ee\5l\67\2\u01ed\u01eb\3\2\2\2")
        buf.write("\u01ed\u01ec\3\2\2\2\u01eeo\3\2\2\2\u01ef\u01f0\7\3\2")
        buf.write("\2\u01f0\u01f1\5r:\2\u01f1\u01f2\79\2\2\u01f2q\3\2\2\2")
        buf.write("\u01f3\u020c\7\4\2\2\u01f4\u01f5\7\5\2\2\u01f5\u01f6\7")
        buf.write("<\2\2\u01f6\u01f7\5\32\16\2\u01f7\u01f8\7;\2\2\u01f8\u020c")
        buf.write("\3\2\2\2\u01f9\u020c\7\6\2\2\u01fa\u01fb\7\7\2\2\u01fb")
        buf.write("\u01fc\7<\2\2\u01fc\u01fd\5\32\16\2\u01fd\u01fe\7;\2\2")
        buf.write("\u01fe\u020c\3\2\2\2\u01ff\u020c\7\b\2\2\u0200\u0201\7")
        buf.write("\t\2\2\u0201\u0202\7<\2\2\u0202\u0203\5\32\16\2\u0203")
        buf.write("\u0204\7;\2\2\u0204\u020c\3\2\2\2\u0205\u020c\7\n\2\2")
        buf.write("\u0206\u0207\7\13\2\2\u0207\u0208\7<\2\2\u0208\u0209\5")
        buf.write("\32\16\2\u0209\u020a\7;\2\2\u020a\u020c\3\2\2\2\u020b")
        buf.write("\u01f3\3\2\2\2\u020b\u01f4\3\2\2\2\u020b\u01f9\3\2\2\2")
        buf.write("\u020b\u01fa\3\2\2\2\u020b\u01ff\3\2\2\2\u020b\u0200\3")
        buf.write("\2\2\2\u020b\u0205\3\2\2\2\u020b\u0206\3\2\2\2\u020cs")
        buf.write("\3\2\2\2\u020d\u020e\t\7\2\2\u020eu\3\2\2\2\u020f\u0210")
        buf.write("\t\b\2\2\u0210w\3\2\2\2\u0211\u0212\t\t\2\2\u0212y\3\2")
        buf.write("\2\2)}\u0085\u008a\u0090\u0097\u0099\u00a1\u00b7\u00c1")
        buf.write("\u00c5\u00d0\u00d4\u00de\u00ea\u00f6\u0102\u010e\u0116")
        buf.write("\u011b\u0127\u0132\u0139\u0144\u0158\u0162\u0165\u016a")
        buf.write("\u0178\u0185\u018b\u01aa\u01b4\u01bb\u01c2\u01c6\u01d7")
        buf.write("\u01e3\u01ed\u020b")
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
                     "'void'", "'const'", "'constant'", "'func'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'='", "':='", "'+'", "'-'", "'*'", "'\\'", 
                     "'%'", "'/'", "'<-'", "'^'", "'.'", "','", "';'", "':'", 
                     "')'", "'('", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                      "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", 
                      "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
                      "VOID", "CONST", "CONSTANT", "FUNC", "NOT", "AND", 
                      "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", 
                      "GREATER_EQUAL", "INITIAL", "ASSIGN", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", 
                      "SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", 
                      "COLON", "RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", 
                      "RBRASE", "LITERAL", "ID", "FLOAT_LITERAL", "INT_LITERAL", 
                      "BOOL_LITERAL", "STRING_LITERAL", "ARRAY", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_gb = 1
    RULE_class_lst = 2
    RULE_class_dcl = 3
    RULE_class_body = 4
    RULE_menthod_lst = 5
    RULE_menthod_dcl = 6
    RULE_constructor_decl = 7
    RULE_menthod_body = 8
    RULE_param_lst = 9
    RULE_param = 10
    RULE_expr_lst = 11
    RULE_expr = 12
    RULE_expr1 = 13
    RULE_expr2 = 14
    RULE_expr3 = 15
    RULE_expr4 = 16
    RULE_expr5 = 17
    RULE_expr6 = 18
    RULE_expr7 = 19
    RULE_expr8 = 20
    RULE_expr9 = 21
    RULE_expr10 = 22
    RULE_multiplying = 23
    RULE_adding = 24
    RULE_logical_bin = 25
    RULE_logical_not = 26
    RULE_relational = 27
    RULE_relat_bool = 28
    RULE_relat_int_float = 29
    RULE_statement_lst = 30
    RULE_statements = 31
    RULE_decl_state = 32
    RULE_assign = 33
    RULE_assign_form = 34
    RULE_decl_typ = 35
    RULE_decl_array = 36
    RULE_if_state = 37
    RULE_for_state = 38
    RULE_break_state = 39
    RULE_continue_state = 40
    RULE_return_state = 41
    RULE_block_state = 42
    RULE_if_block = 43
    RULE_menthod_invo_state = 44
    RULE_lhs = 45
    RULE_access_lst = 46
    RULE_access = 47
    RULE_static_access = 48
    RULE_instance_access = 49
    RULE_instance_menthod_invo_access = 50
    RULE_static_menthod_invo_access = 51
    RULE_idlist = 52
    RULE_index_op = 53
    RULE_identifier = 54
    RULE_io_st = 55
    RULE_io = 56
    RULE_fm = 57
    RULE_boolean = 58
    RULE_typ = 59

    ruleNames =  [ "program", "gb", "class_lst", "class_dcl", "class_body", 
                   "menthod_lst", "menthod_dcl", "constructor_decl", "menthod_body", 
                   "param_lst", "param", "expr_lst", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "expr9", "expr10", "multiplying", "adding", "logical_bin", 
                   "logical_not", "relational", "relat_bool", "relat_int_float", 
                   "statement_lst", "statements", "decl_state", "assign", 
                   "assign_form", "decl_typ", "decl_array", "if_state", 
                   "for_state", "break_state", "continue_state", "return_state", 
                   "block_state", "if_block", "menthod_invo_state", "lhs", 
                   "access_lst", "access", "static_access", "instance_access", 
                   "instance_menthod_invo_access", "static_menthod_invo_access", 
                   "idlist", "index_op", "identifier", "io_st", "io", "fm", 
                   "boolean", "typ" ]

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
    NOT=34
    AND=35
    OR=36
    EQUAL=37
    NOT_EQUAL=38
    LESS=39
    GREATER=40
    LESS_EQUAL=41
    GREATER_EQUAL=42
    INITIAL=43
    ASSIGN=44
    PLUS=45
    MINUS=46
    MULTIPLY=47
    DIVIDE_I=48
    DIVIDE_I_L=49
    DIVIDE_F=50
    SUPER_CLASS=51
    STRING_CONCAT=52
    DOT=53
    COMMA=54
    SEMICOLON=55
    COLON=56
    RPAREN=57
    LPAREN=58
    LBRACK=59
    RBRACK=60
    LBRASE=61
    RBRASE=62
    LITERAL=63
    ID=64
    FLOAT_LITERAL=65
    INT_LITERAL=66
    BOOL_LITERAL=67
    STRING_LITERAL=68
    ARRAY=69
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
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.ASSIGN) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.COMMA) | (1 << CSlangParser.COLON) | (1 << CSlangParser.LPAREN) | (1 << CSlangParser.LITERAL))) != 0) or _la==CSlangParser.ID or _la==CSlangParser.ARRAY:
                self.state = 120
                self.gb()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
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


        def menthod_lst(self):
            return self.getTypedRuleContext(CSlangParser.Menthod_lstContext,0)


        def statement_lst(self):
            return self.getTypedRuleContext(CSlangParser.Statement_lstContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_gb




    def gb(self):

        localctx = CSlangParser.GbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_gb)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.class_lst()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.menthod_lst()
                pass
            elif token in [CSlangParser.T__0, CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.ASSIGN, CSlangParser.MINUS, CSlangParser.COMMA, CSlangParser.COLON, CSlangParser.LPAREN, CSlangParser.LITERAL, CSlangParser.ID, CSlangParser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.statement_lst()
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
        self.enterRule(localctx, 4, self.RULE_class_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 133
                    self.class_dcl()

                else:
                    raise NoViableAltException(self)
                self.state = 136 
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
        self.enterRule(localctx, 6, self.RULE_class_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(CSlangParser.CLASS)
            self.state = 139
            self.match(CSlangParser.ID)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.SUPER_CLASS:
                self.state = 140
                self.match(CSlangParser.SUPER_CLASS)
                self.state = 141
                self.match(CSlangParser.ID)


            self.state = 144
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

        def menthod_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Menthod_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Menthod_dclContext,i)


        def statement_lst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Statement_lstContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Statement_lstContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_body




    def class_body(self):

        localctx = CSlangParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(CSlangParser.LBRASE)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.ASSIGN) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.COMMA) | (1 << CSlangParser.COLON) | (1 << CSlangParser.LPAREN) | (1 << CSlangParser.LITERAL))) != 0) or _la==CSlangParser.ID or _la==CSlangParser.ARRAY:
                self.state = 149
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.FUNC]:
                    self.state = 147
                    self.menthod_dcl()
                    pass
                elif token in [CSlangParser.T__0, CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.ASSIGN, CSlangParser.MINUS, CSlangParser.COMMA, CSlangParser.COLON, CSlangParser.LPAREN, CSlangParser.LITERAL, CSlangParser.ID, CSlangParser.ARRAY]:
                    self.state = 148
                    self.statement_lst()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(CSlangParser.RBRASE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Menthod_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def menthod_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Menthod_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Menthod_dclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_menthod_lst




    def menthod_lst(self):

        localctx = CSlangParser.Menthod_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_menthod_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 156
                    self.menthod_dcl()

                else:
                    raise NoViableAltException(self)
                self.state = 159 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Menthod_dclContext(ParserRuleContext):
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


        def menthod_body(self):
            return self.getTypedRuleContext(CSlangParser.Menthod_bodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_menthod_dcl




    def menthod_dcl(self):

        localctx = CSlangParser.Menthod_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_menthod_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(CSlangParser.FUNC)
            self.state = 162
            self.match(CSlangParser.ID)
            self.state = 163
            self.match(CSlangParser.LPAREN)
            self.state = 164
            self.param_lst()
            self.state = 165
            self.match(CSlangParser.RPAREN)
            self.state = 166
            self.match(CSlangParser.COLON)
            self.state = 167
            self.typ()
            self.state = 168
            self.menthod_body()
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

        def menthod_body(self):
            return self.getTypedRuleContext(CSlangParser.Menthod_bodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(CSlangParser.FUNC)
            self.state = 171
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 172
            self.match(CSlangParser.LPAREN)
            self.state = 173
            self.param_lst()
            self.state = 174
            self.match(CSlangParser.RPAREN)
            self.state = 175
            self.menthod_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Menthod_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRASE(self):
            return self.getToken(CSlangParser.LBRASE, 0)

        def RBRASE(self):
            return self.getToken(CSlangParser.RBRASE, 0)

        def statement_lst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Statement_lstContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Statement_lstContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_menthod_body




    def menthod_body(self):

        localctx = CSlangParser.Menthod_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_menthod_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(CSlangParser.LBRASE)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.ASSIGN) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.COMMA) | (1 << CSlangParser.COLON) | (1 << CSlangParser.LPAREN) | (1 << CSlangParser.LITERAL))) != 0) or _la==CSlangParser.ID or _la==CSlangParser.ARRAY:
                self.state = 178
                self.statement_lst()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(CSlangParser.RBRASE)
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.param()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 187
                    self.match(CSlangParser.COMMA)
                    self.state = 188
                    self.param()
                    self.state = 193
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

        def idlist(self):
            return self.getTypedRuleContext(CSlangParser.IdlistContext,0)


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
            self.state = 197
            self.idlist()
            self.state = 198
            self.match(CSlangParser.COLON)
            self.state = 199
            self.typ()
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
        self.enterRule(localctx, 22, self.RULE_expr_lst)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.expr(0)
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 202
                        self.match(CSlangParser.COMMA)
                        self.state = 203
                        self.expr_lst() 
                    self.state = 208
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 215
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 216
                    self.match(CSlangParser.STRING_CONCAT)
                    self.state = 217
                    self.expr(3) 
                self.state = 222
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 226
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 227
                    self.relational()
                    self.state = 228
                    self.expr1(3) 
                self.state = 234
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 238
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 239
                    self.logical_bin()
                    self.state = 240
                    self.expr3(0) 
                self.state = 246
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    self.adding()
                    self.state = 252
                    self.expr4(0) 
                self.state = 258
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 262
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 263
                    self.multiplying()
                    self.state = 264
                    self.expr5() 
                self.state = 270
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
        self.enterRule(localctx, 34, self.RULE_expr5)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.expr6()
                self.state = 272
                self.logical_not()
                self.state = 273
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
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

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr6)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(CSlangParser.MINUS)
                self.state = 279
                self.expr7(0)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LPAREN, CSlangParser.LITERAL, CSlangParser.ID, CSlangParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    self.match(CSlangParser.LBRACK)
                    self.state = 288
                    self.expr_lst()
                    self.state = 289
                    self.match(CSlangParser.RBRACK) 
                self.state = 295
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

        def getRuleIndex(self):
            return CSlangParser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    self.match(CSlangParser.DOT)
                    self.state = 301
                    self.match(CSlangParser.ID) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr9




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr9)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(CSlangParser.NEW)
                self.state = 308
                self.match(CSlangParser.ID)
                self.state = 309
                self.expr_lst()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.LPAREN, CSlangParser.LITERAL, CSlangParser.ID, CSlangParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.expr10()
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


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_accessContext,0)


        def index_op(self):
            return self.getTypedRuleContext(CSlangParser.Index_opContext,0)


        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def ARRAY(self):
            return self.getToken(CSlangParser.ARRAY, 0)

        def LITERAL(self):
            return self.getToken(CSlangParser.LITERAL, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr10




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr10)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.static_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.index_op()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.match(CSlangParser.LPAREN)
                self.state = 316
                self.expr(0)
                self.state = 317
                self.match(CSlangParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
                self.match(CSlangParser.ARRAY)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 320
                self.match(CSlangParser.LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 321
                self.match(CSlangParser.SELF)
                pass


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
        self.enterRule(localctx, 46, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
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
        self.enterRule(localctx, 48, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
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
        self.enterRule(localctx, 50, self.RULE_logical_bin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
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
        self.enterRule(localctx, 52, self.RULE_logical_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
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
        self.enterRule(localctx, 54, self.RULE_relational)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.relat_bool()
            self.state = 333
            self.relat_int_float()
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
        self.enterRule(localctx, 56, self.RULE_relat_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
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
        self.enterRule(localctx, 58, self.RULE_relat_int_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
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


    class Statement_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StatementsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StatementsContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_statement_lst




    def statement_lst(self):

        localctx = CSlangParser.Statement_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 339
                    self.statements()

                else:
                    raise NoViableAltException(self)
                self.state = 342 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def decl_state(self):
            return self.getTypedRuleContext(CSlangParser.Decl_stateContext,0)


        def if_state(self):
            return self.getTypedRuleContext(CSlangParser.If_stateContext,0)


        def for_state(self):
            return self.getTypedRuleContext(CSlangParser.For_stateContext,0)


        def continue_state(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stateContext,0)


        def menthod_invo_state(self):
            return self.getTypedRuleContext(CSlangParser.Menthod_invo_stateContext,0)


        def return_state(self):
            return self.getTypedRuleContext(CSlangParser.Return_stateContext,0)


        def break_state(self):
            return self.getTypedRuleContext(CSlangParser.Break_stateContext,0)


        def io_st(self):
            return self.getTypedRuleContext(CSlangParser.Io_stContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statements




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statements)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.decl_state()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.if_state()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.for_state()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.continue_state()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 348
                self.menthod_invo_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 349
                self.return_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 350
                self.break_state()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 351
                self.io_st()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(CSlangParser.AssignContext,0)


        def decl_typ(self):
            return self.getTypedRuleContext(CSlangParser.Decl_typContext,0)


        def decl_array(self):
            return self.getTypedRuleContext(CSlangParser.Decl_arrayContext,0)


        def fm(self):
            return self.getTypedRuleContext(CSlangParser.FmContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decl_state




    def decl_state(self):

        localctx = CSlangParser.Decl_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_decl_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.VAR or _la==CSlangParser.CONST:
                self.state = 354
                self.fm()


            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 357
                self.assign()
                pass

            elif la_ == 2:
                self.state = 358
                self.decl_typ()
                pass

            elif la_ == 3:
                self.state = 359
                self.decl_array()
                pass


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

        def assign_form(self):
            return self.getTypedRuleContext(CSlangParser.Assign_formContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assign




    def assign(self):

        localctx = CSlangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.assign_form()
            self.state = 363
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_formContext(ParserRuleContext):
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
            return CSlangParser.RULE_assign_form




    def assign_form(self):

        localctx = CSlangParser.Assign_formContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assign_form)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.lhs()
            self.state = 366
            self.match(CSlangParser.ASSIGN)
            self.state = 367
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def INITIAL(self):
            return self.getToken(CSlangParser.INITIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decl_typ




    def decl_typ(self):

        localctx = CSlangParser.Decl_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_decl_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.lhs()
            self.state = 370
            self.match(CSlangParser.COLON)
            self.state = 371
            self.typ()
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.INITIAL:
                self.state = 372
                self.match(CSlangParser.INITIAL)
                self.state = 373
                self.expr(0)


            self.state = 376
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_decl_array




    def decl_array(self):

        localctx = CSlangParser.Decl_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_decl_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.lhs()
            self.state = 379
            self.match(CSlangParser.COLON)
            self.state = 380
            self.match(CSlangParser.LBRACK)
            self.state = 381
            self.match(CSlangParser.INT)
            self.state = 382
            self.match(CSlangParser.RBRACK)
            self.state = 383
            self.match(CSlangParser.SEMICOLON)
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


        def if_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.If_blockContext)
            else:
                return self.getTypedRuleContext(CSlangParser.If_blockContext,i)


        def block_state(self):
            return self.getTypedRuleContext(CSlangParser.Block_stateContext,0)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_state




    def if_state(self):

        localctx = CSlangParser.If_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_if_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(CSlangParser.IF)
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 386
                self.block_state()


            self.state = 389
            self.expr(0)
            self.state = 390
            self.if_block()
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 391
                self.match(CSlangParser.ELSE)
                self.state = 392
                self.if_block()


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

        def assign_form(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Assign_formContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Assign_formContext,i)


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
        self.enterRule(localctx, 76, self.RULE_for_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(CSlangParser.FOR)
            self.state = 396
            self.assign_form()
            self.state = 397
            self.match(CSlangParser.SEMICOLON)
            self.state = 398
            self.expr(0)
            self.state = 399
            self.match(CSlangParser.SEMICOLON)
            self.state = 400
            self.assign_form()
            self.state = 401
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
        self.enterRule(localctx, 78, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(CSlangParser.BREAK)
            self.state = 404
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
        self.enterRule(localctx, 80, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(CSlangParser.CONTINUE)
            self.state = 407
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
        self.enterRule(localctx, 82, self.RULE_return_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(CSlangParser.RETURN)
            self.state = 410
            self.expr(0)
            self.state = 411
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

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def statement_lst(self):
            return self.getTypedRuleContext(CSlangParser.Statement_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_block_state




    def block_state(self):

        localctx = CSlangParser.Block_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_block_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(CSlangParser.LPAREN)
            self.state = 414
            self.statement_lst()
            self.state = 415
            self.match(CSlangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRASE(self):
            return self.getToken(CSlangParser.LBRASE, 0)

        def statement_lst(self):
            return self.getTypedRuleContext(CSlangParser.Statement_lstContext,0)


        def RBRASE(self):
            return self.getToken(CSlangParser.RBRASE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_block




    def if_block(self):

        localctx = CSlangParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_if_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(CSlangParser.LBRASE)
            self.state = 418
            self.statement_lst()
            self.state = 419
            self.match(CSlangParser.RBRASE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Menthod_invo_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_menthod_invo_state




    def menthod_invo_state(self):

        localctx = CSlangParser.Menthod_invo_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_menthod_invo_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 421
                self.expr(0)
                self.state = 422
                self.match(CSlangParser.DOT)


            self.state = 426
            self.match(CSlangParser.ID)
            self.state = 427
            self.match(CSlangParser.LPAREN)
            self.state = 428
            self.expr_lst()
            self.state = 429
            self.match(CSlangParser.RPAREN)
            self.state = 430
            self.match(CSlangParser.SEMICOLON)
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

        def idlist(self):
            return self.getTypedRuleContext(CSlangParser.IdlistContext,0)


        def access_lst(self):
            return self.getTypedRuleContext(CSlangParser.Access_lstContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhs




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lhs)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.access_lst()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.AccessContext)
            else:
                return self.getTypedRuleContext(CSlangParser.AccessContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_access_lst




    def access_lst(self):

        localctx = CSlangParser.Access_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_access_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.access()
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 437
                self.match(CSlangParser.COMMA)
                self.state = 438
                self.access()
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_access(self):
            return self.getTypedRuleContext(CSlangParser.Instance_accessContext,0)


        def static_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_accessContext,0)


        def instance_menthod_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Instance_menthod_invo_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_access




    def access(self):

        localctx = CSlangParser.AccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_access)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.instance_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.static_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
                self.instance_menthod_invo_access()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_accessContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return CSlangParser.RULE_static_access




    def static_access(self):

        localctx = CSlangParser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_static_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 450
                self.match(CSlangParser.ID)
                self.state = 451
                self.match(CSlangParser.DOT)


            self.state = 454
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_accessContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return CSlangParser.RULE_instance_access




    def instance_access(self):

        localctx = CSlangParser.Instance_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.expr(0)
            self.state = 457
            self.match(CSlangParser.DOT)
            self.state = 458
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_menthod_invo_accessContext(ParserRuleContext):
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

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instance_menthod_invo_access




    def instance_menthod_invo_access(self):

        localctx = CSlangParser.Instance_menthod_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_instance_menthod_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.expr(0)
            self.state = 461
            self.match(CSlangParser.DOT)
            self.state = 462
            self.match(CSlangParser.ID)
            self.state = 463
            self.match(CSlangParser.LPAREN)
            self.state = 464
            self.expr_lst()
            self.state = 465
            self.match(CSlangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_menthod_invo_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_static_menthod_invo_access




    def static_menthod_invo_access(self):

        localctx = CSlangParser.Static_menthod_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_static_menthod_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 467
                self.match(CSlangParser.ID)
                self.state = 468
                self.match(CSlangParser.DOT)


            self.state = 471
            self.match(CSlangParser.ID)
            self.state = 472
            self.match(CSlangParser.LPAREN)
            self.state = 473
            self.expr_lst()
            self.state = 474
            self.match(CSlangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSlangParser.IdentifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_idlist




    def idlist(self):

        localctx = CSlangParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.identifier()
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 477
                self.match(CSlangParser.COMMA)
                self.state = 478
                self.identifier()
                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 106, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(CSlangParser.ID)
            self.state = 485
            self.match(CSlangParser.LBRACK)
            self.state = 486
            self.expr(0)
            self.state = 487
            self.match(CSlangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def index_op(self):
            return self.getTypedRuleContext(CSlangParser.Index_opContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_identifier




    def identifier(self):

        localctx = CSlangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_identifier)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.index_op()
                pass


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
        self.enterRule(localctx, 110, self.RULE_io_st)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(CSlangParser.T__0)
            self.state = 494
            self.io()
            self.state = 495
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
        self.enterRule(localctx, 112, self.RULE_io)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.match(CSlangParser.T__1)
                pass
            elif token in [CSlangParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.match(CSlangParser.T__2)
                self.state = 499
                self.match(CSlangParser.LPAREN)
                self.state = 500
                self.expr(0)
                self.state = 501
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 503
                self.match(CSlangParser.T__3)
                pass
            elif token in [CSlangParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 504
                self.match(CSlangParser.T__4)
                self.state = 505
                self.match(CSlangParser.LPAREN)
                self.state = 506
                self.expr(0)
                self.state = 507
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 509
                self.match(CSlangParser.T__5)
                pass
            elif token in [CSlangParser.T__6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 510
                self.match(CSlangParser.T__6)
                self.state = 511
                self.match(CSlangParser.LPAREN)
                self.state = 512
                self.expr(0)
                self.state = 513
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [CSlangParser.T__7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 515
                self.match(CSlangParser.T__7)
                pass
            elif token in [CSlangParser.T__8]:
                self.enterOuterAlt(localctx, 8)
                self.state = 516
                self.match(CSlangParser.T__8)
                self.state = 517
                self.match(CSlangParser.LPAREN)
                self.state = 518
                self.expr(0)
                self.state = 519
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
        self.enterRule(localctx, 114, self.RULE_fm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
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
        self.enterRule(localctx, 116, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
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

        def getRuleIndex(self):
            return CSlangParser.RULE_typ




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING) | (1 << CSlangParser.VOID))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        self._predicates[13] = self.expr1_sempred
        self._predicates[14] = self.expr2_sempred
        self._predicates[15] = self.expr3_sempred
        self._predicates[16] = self.expr4_sempred
        self._predicates[19] = self.expr7_sempred
        self._predicates[20] = self.expr8_sempred
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
                return self.precpred(self._ctx, 2)
         




