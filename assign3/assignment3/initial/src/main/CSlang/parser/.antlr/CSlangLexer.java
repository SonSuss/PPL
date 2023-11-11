// Generated from e:/hocbaidcm/PPL/assignment/assign3/assignment3/initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1

from lexererr import *

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CSlangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, BLOCK_COMMENT=9, 
		LINE_COMMENT=10, BREAK=11, CONTINUE=12, IF=13, ELSE=14, FOR=15, TRUE=16, 
		FALSE=17, INT=18, FLOAT=19, BOOL=20, STRING=21, RETURN=22, NULL=23, CLASS=24, 
		CONSTRUCTOR=25, VAR=26, SELF=27, NEW=28, VOID=29, CONST=30, FUNC=31, NOT=32, 
		AND=33, OR=34, EQUAL=35, NOT_EQUAL=36, LESS=37, GREATER=38, LESS_EQUAL=39, 
		GREATER_EQUAL=40, INITIAL=41, ASSIGN=42, PLUS=43, MINUS=44, MULTIPLY=45, 
		DIVIDE_I=46, DIVIDE_I_L=47, DIVIDE_F=48, SUPER_CLASS=49, STRING_CONCAT=50, 
		DOT=51, COMMA=52, SEMICOLON=53, COLON=54, RPAREN=55, LPAREN=56, LBRACK=57, 
		RBRACK=58, LBRASE=59, RBRASE=60, AT_ID=61, STRING_LITERAL=62, ID=63, FLOAT_LITERAL=64, 
		NON_ZERO_INT=65, INT_LITERAL=66, WS=67, ERROR_CHAR=68, UNCLOSE_STRING=69, 
		ILLEGAL_ESCAPE=70;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "BLOCK_COMMENT", 
			"LINE_COMMENT", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
			"INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
			"VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "NOT", "AND", "OR", "EQUAL", 
			"NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "INITIAL", 
			"ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", 
			"SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", "COLON", 
			"RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", "RBRASE", "AT_ID", 
			"STRING_LITERAL", "ID", "FLOAT_LITERAL", "NON_ZERO_INT", "INT_LITERAL", 
			"SIGN", "DECIMAL", "EXPONENT", "DIGIT", "ESC_SEQ", "ILL_ESQ", "WS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'@readInt'", "'@writeInt'", "'@readFloat'", "'@writeFloat'", "'@readBool'", 
			"'@writeBool'", "'@readString'", "'@writeString'", null, null, "'break'", 
			"'continue'", "'if'", "'else'", "'for'", "'true'", "'false'", "'int'", 
			"'float'", "'bool'", "'string'", "'return'", "'null'", "'class'", "'constructor'", 
			"'var'", "'self'", "'new'", "'void'", "'const'", "'func'", "'!'", "'&&'", 
			"'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", "':='", 
			"'+'", "'-'", "'*'", "'\\'", "'%'", "'/'", "'<-'", "'^'", "'.'", "','", 
			"';'", "':'", "')'", "'('", "'['", "']'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "BLOCK_COMMENT", 
			"LINE_COMMENT", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
			"INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
			"VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "NOT", "AND", "OR", "EQUAL", 
			"NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "INITIAL", 
			"ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", 
			"SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", "COLON", 
			"RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", "RBRASE", "AT_ID", 
			"STRING_LITERAL", "ID", "FLOAT_LITERAL", "NON_ZERO_INT", "INT_LITERAL", 
			"WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CSlangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CSlang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 61:
			STRING_LITERAL_action((RuleContext)_localctx, actionIndex);
			break;
		case 73:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		case 74:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 75:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void STRING_LITERAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self.text = self.text[1:-1]
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			raise ErrorToken(self.text)
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:

			unclose_string= str(self.text);
			whatif =['\b', '\t', '\f', '\n', '\r', '\\']
			if unclose_string[-1] in whatif:
			    raise UncloseString(unclose_string[1:-1])
			else:
			    raise UncloseString(unclose_string[1:])

			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:

			raise IllegalEscape(self.text[1:])

			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000F\u023f\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u00021\u00071\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u0007"+
		"5\u00026\u00076\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007"+
		":\u0002;\u0007;\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007"+
		"?\u0002@\u0007@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007"+
		"D\u0002E\u0007E\u0002F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007"+
		"I\u0002J\u0007J\u0002K\u0007K\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u00f6\b\b\n\b\f\b\u00f9"+
		"\t\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0005\t\u0104\b\t\n\t\f\t\u0107\t\t\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001"+
		"\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001"+
		"&\u0001&\u0001&\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0001)\u0001)\u0001"+
		")\u0001*\u0001*\u0001+\u0001+\u0001,\u0001,\u0001-\u0001-\u0001.\u0001"+
		".\u0001/\u0001/\u00010\u00010\u00010\u00011\u00011\u00012\u00012\u0001"+
		"3\u00013\u00014\u00014\u00015\u00015\u00016\u00016\u00017\u00017\u0001"+
		"8\u00018\u00019\u00019\u0001:\u0001:\u0001;\u0001;\u0001<\u0001<\u0001"+
		"<\u0001=\u0001=\u0001=\u0005=\u01cc\b=\n=\f=\u01cf\t=\u0001=\u0001=\u0001"+
		"=\u0001>\u0001>\u0005>\u01d6\b>\n>\f>\u01d9\t>\u0001?\u0004?\u01dc\b?"+
		"\u000b?\f?\u01dd\u0001?\u0001?\u0001?\u0001?\u0001?\u0003?\u01e5\b?\u0001"+
		"@\u0001@\u0005@\u01e9\b@\n@\f@\u01ec\t@\u0001A\u0004A\u01ef\bA\u000bA"+
		"\fA\u01f0\u0001B\u0001B\u0003B\u01f5\bB\u0001C\u0001C\u0005C\u01f9\bC"+
		"\nC\fC\u01fc\tC\u0001D\u0001D\u0003D\u0200\bD\u0001D\u0004D\u0203\bD\u000b"+
		"D\fD\u0204\u0001E\u0001E\u0001F\u0001F\u0001F\u0001F\u0001F\u0001F\u0001"+
		"F\u0001F\u0001F\u0001F\u0001F\u0001F\u0001F\u0001F\u0003F\u0217\bF\u0001"+
		"G\u0001G\u0001G\u0003G\u021c\bG\u0001H\u0004H\u021f\bH\u000bH\fH\u0220"+
		"\u0001H\u0001H\u0001I\u0001I\u0001I\u0001J\u0001J\u0001J\u0005J\u022b"+
		"\bJ\nJ\fJ\u022e\tJ\u0001J\u0003J\u0231\bJ\u0001J\u0001J\u0001K\u0001K"+
		"\u0001K\u0005K\u0238\bK\nK\fK\u023b\tK\u0001K\u0001K\u0001K\u0001\u00f7"+
		"\u0000L\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b"+
		"\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016"+
		"-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f? A!C\""+
		"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_0a1c2e3g4i5k6m7o8q9s:u;w<y={>}?\u007f@\u0081"+
		"A\u0083B\u0085\u0000\u0087\u0000\u0089\u0000\u008b\u0000\u008d\u0000\u008f"+
		"\u0000\u0091C\u0093D\u0095E\u0097F\u0001\u0000\u000b\u0005\u0000\n\n\r"+
		"\rEFOO||\u0002\u0000\n\n\r\r\u0004\u0000\b\n\f\r\"\"\\\\\u0003\u0000A"+
		"Z__az\u0004\u000009AZ__az\u0001\u000019\u0001\u000009\u0002\u0000EEee"+
		"\u0005\u0000bbffnnrrtt\u0003\u0000\t\n\r\r  \u0003\u0001\b\n\f\r  \u0252"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/"+
		"\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000"+
		"\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000"+
		"\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000\u0000\u0000="+
		"\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000A\u0001\u0000"+
		"\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000E\u0001\u0000\u0000\u0000"+
		"\u0000G\u0001\u0000\u0000\u0000\u0000I\u0001\u0000\u0000\u0000\u0000K"+
		"\u0001\u0000\u0000\u0000\u0000M\u0001\u0000\u0000\u0000\u0000O\u0001\u0000"+
		"\u0000\u0000\u0000Q\u0001\u0000\u0000\u0000\u0000S\u0001\u0000\u0000\u0000"+
		"\u0000U\u0001\u0000\u0000\u0000\u0000W\u0001\u0000\u0000\u0000\u0000Y"+
		"\u0001\u0000\u0000\u0000\u0000[\u0001\u0000\u0000\u0000\u0000]\u0001\u0000"+
		"\u0000\u0000\u0000_\u0001\u0000\u0000\u0000\u0000a\u0001\u0000\u0000\u0000"+
		"\u0000c\u0001\u0000\u0000\u0000\u0000e\u0001\u0000\u0000\u0000\u0000g"+
		"\u0001\u0000\u0000\u0000\u0000i\u0001\u0000\u0000\u0000\u0000k\u0001\u0000"+
		"\u0000\u0000\u0000m\u0001\u0000\u0000\u0000\u0000o\u0001\u0000\u0000\u0000"+
		"\u0000q\u0001\u0000\u0000\u0000\u0000s\u0001\u0000\u0000\u0000\u0000u"+
		"\u0001\u0000\u0000\u0000\u0000w\u0001\u0000\u0000\u0000\u0000y\u0001\u0000"+
		"\u0000\u0000\u0000{\u0001\u0000\u0000\u0000\u0000}\u0001\u0000\u0000\u0000"+
		"\u0000\u007f\u0001\u0000\u0000\u0000\u0000\u0081\u0001\u0000\u0000\u0000"+
		"\u0000\u0083\u0001\u0000\u0000\u0000\u0000\u0091\u0001\u0000\u0000\u0000"+
		"\u0000\u0093\u0001\u0000\u0000\u0000\u0000\u0095\u0001\u0000\u0000\u0000"+
		"\u0000\u0097\u0001\u0000\u0000\u0000\u0001\u0099\u0001\u0000\u0000\u0000"+
		"\u0003\u00a2\u0001\u0000\u0000\u0000\u0005\u00ac\u0001\u0000\u0000\u0000"+
		"\u0007\u00b7\u0001\u0000\u0000\u0000\t\u00c3\u0001\u0000\u0000\u0000\u000b"+
		"\u00cd\u0001\u0000\u0000\u0000\r\u00d8\u0001\u0000\u0000\u0000\u000f\u00e4"+
		"\u0001\u0000\u0000\u0000\u0011\u00f1\u0001\u0000\u0000\u0000\u0013\u00ff"+
		"\u0001\u0000\u0000\u0000\u0015\u010c\u0001\u0000\u0000\u0000\u0017\u0112"+
		"\u0001\u0000\u0000\u0000\u0019\u011b\u0001\u0000\u0000\u0000\u001b\u011e"+
		"\u0001\u0000\u0000\u0000\u001d\u0123\u0001\u0000\u0000\u0000\u001f\u0127"+
		"\u0001\u0000\u0000\u0000!\u012c\u0001\u0000\u0000\u0000#\u0132\u0001\u0000"+
		"\u0000\u0000%\u0136\u0001\u0000\u0000\u0000\'\u013c\u0001\u0000\u0000"+
		"\u0000)\u0141\u0001\u0000\u0000\u0000+\u0148\u0001\u0000\u0000\u0000-"+
		"\u014f\u0001\u0000\u0000\u0000/\u0154\u0001\u0000\u0000\u00001\u015a\u0001"+
		"\u0000\u0000\u00003\u0166\u0001\u0000\u0000\u00005\u016a\u0001\u0000\u0000"+
		"\u00007\u016f\u0001\u0000\u0000\u00009\u0173\u0001\u0000\u0000\u0000;"+
		"\u0178\u0001\u0000\u0000\u0000=\u017e\u0001\u0000\u0000\u0000?\u0183\u0001"+
		"\u0000\u0000\u0000A\u0185\u0001\u0000\u0000\u0000C\u0188\u0001\u0000\u0000"+
		"\u0000E\u018b\u0001\u0000\u0000\u0000G\u018e\u0001\u0000\u0000\u0000I"+
		"\u0191\u0001\u0000\u0000\u0000K\u0193\u0001\u0000\u0000\u0000M\u0195\u0001"+
		"\u0000\u0000\u0000O\u0198\u0001\u0000\u0000\u0000Q\u019b\u0001\u0000\u0000"+
		"\u0000S\u019d\u0001\u0000\u0000\u0000U\u01a0\u0001\u0000\u0000\u0000W"+
		"\u01a2\u0001\u0000\u0000\u0000Y\u01a4\u0001\u0000\u0000\u0000[\u01a6\u0001"+
		"\u0000\u0000\u0000]\u01a8\u0001\u0000\u0000\u0000_\u01aa\u0001\u0000\u0000"+
		"\u0000a\u01ac\u0001\u0000\u0000\u0000c\u01af\u0001\u0000\u0000\u0000e"+
		"\u01b1\u0001\u0000\u0000\u0000g\u01b3\u0001\u0000\u0000\u0000i\u01b5\u0001"+
		"\u0000\u0000\u0000k\u01b7\u0001\u0000\u0000\u0000m\u01b9\u0001\u0000\u0000"+
		"\u0000o\u01bb\u0001\u0000\u0000\u0000q\u01bd\u0001\u0000\u0000\u0000s"+
		"\u01bf\u0001\u0000\u0000\u0000u\u01c1\u0001\u0000\u0000\u0000w\u01c3\u0001"+
		"\u0000\u0000\u0000y\u01c5\u0001\u0000\u0000\u0000{\u01c8\u0001\u0000\u0000"+
		"\u0000}\u01d3\u0001\u0000\u0000\u0000\u007f\u01db\u0001\u0000\u0000\u0000"+
		"\u0081\u01e6\u0001\u0000\u0000\u0000\u0083\u01ee\u0001\u0000\u0000\u0000"+
		"\u0085\u01f4\u0001\u0000\u0000\u0000\u0087\u01f6\u0001\u0000\u0000\u0000"+
		"\u0089\u01fd\u0001\u0000\u0000\u0000\u008b\u0206\u0001\u0000\u0000\u0000"+
		"\u008d\u0216\u0001\u0000\u0000\u0000\u008f\u021b\u0001\u0000\u0000\u0000"+
		"\u0091\u021e\u0001\u0000\u0000\u0000\u0093\u0224\u0001\u0000\u0000\u0000"+
		"\u0095\u0227\u0001\u0000\u0000\u0000\u0097\u0234\u0001\u0000\u0000\u0000"+
		"\u0099\u009a\u0005@\u0000\u0000\u009a\u009b\u0005r\u0000\u0000\u009b\u009c"+
		"\u0005e\u0000\u0000\u009c\u009d\u0005a\u0000\u0000\u009d\u009e\u0005d"+
		"\u0000\u0000\u009e\u009f\u0005I\u0000\u0000\u009f\u00a0\u0005n\u0000\u0000"+
		"\u00a0\u00a1\u0005t\u0000\u0000\u00a1\u0002\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a3\u0005@\u0000\u0000\u00a3\u00a4\u0005w\u0000\u0000\u00a4\u00a5\u0005"+
		"r\u0000\u0000\u00a5\u00a6\u0005i\u0000\u0000\u00a6\u00a7\u0005t\u0000"+
		"\u0000\u00a7\u00a8\u0005e\u0000\u0000\u00a8\u00a9\u0005I\u0000\u0000\u00a9"+
		"\u00aa\u0005n\u0000\u0000\u00aa\u00ab\u0005t\u0000\u0000\u00ab\u0004\u0001"+
		"\u0000\u0000\u0000\u00ac\u00ad\u0005@\u0000\u0000\u00ad\u00ae\u0005r\u0000"+
		"\u0000\u00ae\u00af\u0005e\u0000\u0000\u00af\u00b0\u0005a\u0000\u0000\u00b0"+
		"\u00b1\u0005d\u0000\u0000\u00b1\u00b2\u0005F\u0000\u0000\u00b2\u00b3\u0005"+
		"l\u0000\u0000\u00b3\u00b4\u0005o\u0000\u0000\u00b4\u00b5\u0005a\u0000"+
		"\u0000\u00b5\u00b6\u0005t\u0000\u0000\u00b6\u0006\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b8\u0005@\u0000\u0000\u00b8\u00b9\u0005w\u0000\u0000\u00b9\u00ba"+
		"\u0005r\u0000\u0000\u00ba\u00bb\u0005i\u0000\u0000\u00bb\u00bc\u0005t"+
		"\u0000\u0000\u00bc\u00bd\u0005e\u0000\u0000\u00bd\u00be\u0005F\u0000\u0000"+
		"\u00be\u00bf\u0005l\u0000\u0000\u00bf\u00c0\u0005o\u0000\u0000\u00c0\u00c1"+
		"\u0005a\u0000\u0000\u00c1\u00c2\u0005t\u0000\u0000\u00c2\b\u0001\u0000"+
		"\u0000\u0000\u00c3\u00c4\u0005@\u0000\u0000\u00c4\u00c5\u0005r\u0000\u0000"+
		"\u00c5\u00c6\u0005e\u0000\u0000\u00c6\u00c7\u0005a\u0000\u0000\u00c7\u00c8"+
		"\u0005d\u0000\u0000\u00c8\u00c9\u0005B\u0000\u0000\u00c9\u00ca\u0005o"+
		"\u0000\u0000\u00ca\u00cb\u0005o\u0000\u0000\u00cb\u00cc\u0005l\u0000\u0000"+
		"\u00cc\n\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005@\u0000\u0000\u00ce"+
		"\u00cf\u0005w\u0000\u0000\u00cf\u00d0\u0005r\u0000\u0000\u00d0\u00d1\u0005"+
		"i\u0000\u0000\u00d1\u00d2\u0005t\u0000\u0000\u00d2\u00d3\u0005e\u0000"+
		"\u0000\u00d3\u00d4\u0005B\u0000\u0000\u00d4\u00d5\u0005o\u0000\u0000\u00d5"+
		"\u00d6\u0005o\u0000\u0000\u00d6\u00d7\u0005l\u0000\u0000\u00d7\f\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d9\u0005@\u0000\u0000\u00d9\u00da\u0005r\u0000"+
		"\u0000\u00da\u00db\u0005e\u0000\u0000\u00db\u00dc\u0005a\u0000\u0000\u00dc"+
		"\u00dd\u0005d\u0000\u0000\u00dd\u00de\u0005S\u0000\u0000\u00de\u00df\u0005"+
		"t\u0000\u0000\u00df\u00e0\u0005r\u0000\u0000\u00e0\u00e1\u0005i\u0000"+
		"\u0000\u00e1\u00e2\u0005n\u0000\u0000\u00e2\u00e3\u0005g\u0000\u0000\u00e3"+
		"\u000e\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005@\u0000\u0000\u00e5\u00e6"+
		"\u0005w\u0000\u0000\u00e6\u00e7\u0005r\u0000\u0000\u00e7\u00e8\u0005i"+
		"\u0000\u0000\u00e8\u00e9\u0005t\u0000\u0000\u00e9\u00ea\u0005e\u0000\u0000"+
		"\u00ea\u00eb\u0005S\u0000\u0000\u00eb\u00ec\u0005t\u0000\u0000\u00ec\u00ed"+
		"\u0005r\u0000\u0000\u00ed\u00ee\u0005i\u0000\u0000\u00ee\u00ef\u0005n"+
		"\u0000\u0000\u00ef\u00f0\u0005g\u0000\u0000\u00f0\u0010\u0001\u0000\u0000"+
		"\u0000\u00f1\u00f2\u0005/\u0000\u0000\u00f2\u00f3\u0005*\u0000\u0000\u00f3"+
		"\u00f7\u0001\u0000\u0000\u0000\u00f4\u00f6\t\u0000\u0000\u0000\u00f5\u00f4"+
		"\u0001\u0000\u0000\u0000\u00f6\u00f9\u0001\u0000\u0000\u0000\u00f7\u00f8"+
		"\u0001\u0000\u0000\u0000\u00f7\u00f5\u0001\u0000\u0000\u0000\u00f8\u00fa"+
		"\u0001\u0000\u0000\u0000\u00f9\u00f7\u0001\u0000\u0000\u0000\u00fa\u00fb"+
		"\u0005*\u0000\u0000\u00fb\u00fc\u0005/\u0000\u0000\u00fc\u00fd\u0001\u0000"+
		"\u0000\u0000\u00fd\u00fe\u0006\b\u0000\u0000\u00fe\u0012\u0001\u0000\u0000"+
		"\u0000\u00ff\u0100\u0005/\u0000\u0000\u0100\u0101\u0005/\u0000\u0000\u0101"+
		"\u0105\u0001\u0000\u0000\u0000\u0102\u0104\b\u0000\u0000\u0000\u0103\u0102"+
		"\u0001\u0000\u0000\u0000\u0104\u0107\u0001\u0000\u0000\u0000\u0105\u0103"+
		"\u0001\u0000\u0000\u0000\u0105\u0106\u0001\u0000\u0000\u0000\u0106\u0108"+
		"\u0001\u0000\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0108\u0109"+
		"\u0007\u0001\u0000\u0000\u0109\u010a\u0001\u0000\u0000\u0000\u010a\u010b"+
		"\u0006\t\u0000\u0000\u010b\u0014\u0001\u0000\u0000\u0000\u010c\u010d\u0005"+
		"b\u0000\u0000\u010d\u010e\u0005r\u0000\u0000\u010e\u010f\u0005e\u0000"+
		"\u0000\u010f\u0110\u0005a\u0000\u0000\u0110\u0111\u0005k\u0000\u0000\u0111"+
		"\u0016\u0001\u0000\u0000\u0000\u0112\u0113\u0005c\u0000\u0000\u0113\u0114"+
		"\u0005o\u0000\u0000\u0114\u0115\u0005n\u0000\u0000\u0115\u0116\u0005t"+
		"\u0000\u0000\u0116\u0117\u0005i\u0000\u0000\u0117\u0118\u0005n\u0000\u0000"+
		"\u0118\u0119\u0005u\u0000\u0000\u0119\u011a\u0005e\u0000\u0000\u011a\u0018"+
		"\u0001\u0000\u0000\u0000\u011b\u011c\u0005i\u0000\u0000\u011c\u011d\u0005"+
		"f\u0000\u0000\u011d\u001a\u0001\u0000\u0000\u0000\u011e\u011f\u0005e\u0000"+
		"\u0000\u011f\u0120\u0005l\u0000\u0000\u0120\u0121\u0005s\u0000\u0000\u0121"+
		"\u0122\u0005e\u0000\u0000\u0122\u001c\u0001\u0000\u0000\u0000\u0123\u0124"+
		"\u0005f\u0000\u0000\u0124\u0125\u0005o\u0000\u0000\u0125\u0126\u0005r"+
		"\u0000\u0000\u0126\u001e\u0001\u0000\u0000\u0000\u0127\u0128\u0005t\u0000"+
		"\u0000\u0128\u0129\u0005r\u0000\u0000\u0129\u012a\u0005u\u0000\u0000\u012a"+
		"\u012b\u0005e\u0000\u0000\u012b \u0001\u0000\u0000\u0000\u012c\u012d\u0005"+
		"f\u0000\u0000\u012d\u012e\u0005a\u0000\u0000\u012e\u012f\u0005l\u0000"+
		"\u0000\u012f\u0130\u0005s\u0000\u0000\u0130\u0131\u0005e\u0000\u0000\u0131"+
		"\"\u0001\u0000\u0000\u0000\u0132\u0133\u0005i\u0000\u0000\u0133\u0134"+
		"\u0005n\u0000\u0000\u0134\u0135\u0005t\u0000\u0000\u0135$\u0001\u0000"+
		"\u0000\u0000\u0136\u0137\u0005f\u0000\u0000\u0137\u0138\u0005l\u0000\u0000"+
		"\u0138\u0139\u0005o\u0000\u0000\u0139\u013a\u0005a\u0000\u0000\u013a\u013b"+
		"\u0005t\u0000\u0000\u013b&\u0001\u0000\u0000\u0000\u013c\u013d\u0005b"+
		"\u0000\u0000\u013d\u013e\u0005o\u0000\u0000\u013e\u013f\u0005o\u0000\u0000"+
		"\u013f\u0140\u0005l\u0000\u0000\u0140(\u0001\u0000\u0000\u0000\u0141\u0142"+
		"\u0005s\u0000\u0000\u0142\u0143\u0005t\u0000\u0000\u0143\u0144\u0005r"+
		"\u0000\u0000\u0144\u0145\u0005i\u0000\u0000\u0145\u0146\u0005n\u0000\u0000"+
		"\u0146\u0147\u0005g\u0000\u0000\u0147*\u0001\u0000\u0000\u0000\u0148\u0149"+
		"\u0005r\u0000\u0000\u0149\u014a\u0005e\u0000\u0000\u014a\u014b\u0005t"+
		"\u0000\u0000\u014b\u014c\u0005u\u0000\u0000\u014c\u014d\u0005r\u0000\u0000"+
		"\u014d\u014e\u0005n\u0000\u0000\u014e,\u0001\u0000\u0000\u0000\u014f\u0150"+
		"\u0005n\u0000\u0000\u0150\u0151\u0005u\u0000\u0000\u0151\u0152\u0005l"+
		"\u0000\u0000\u0152\u0153\u0005l\u0000\u0000\u0153.\u0001\u0000\u0000\u0000"+
		"\u0154\u0155\u0005c\u0000\u0000\u0155\u0156\u0005l\u0000\u0000\u0156\u0157"+
		"\u0005a\u0000\u0000\u0157\u0158\u0005s\u0000\u0000\u0158\u0159\u0005s"+
		"\u0000\u0000\u01590\u0001\u0000\u0000\u0000\u015a\u015b\u0005c\u0000\u0000"+
		"\u015b\u015c\u0005o\u0000\u0000\u015c\u015d\u0005n\u0000\u0000\u015d\u015e"+
		"\u0005s\u0000\u0000\u015e\u015f\u0005t\u0000\u0000\u015f\u0160\u0005r"+
		"\u0000\u0000\u0160\u0161\u0005u\u0000\u0000\u0161\u0162\u0005c\u0000\u0000"+
		"\u0162\u0163\u0005t\u0000\u0000\u0163\u0164\u0005o\u0000\u0000\u0164\u0165"+
		"\u0005r\u0000\u0000\u01652\u0001\u0000\u0000\u0000\u0166\u0167\u0005v"+
		"\u0000\u0000\u0167\u0168\u0005a\u0000\u0000\u0168\u0169\u0005r\u0000\u0000"+
		"\u01694\u0001\u0000\u0000\u0000\u016a\u016b\u0005s\u0000\u0000\u016b\u016c"+
		"\u0005e\u0000\u0000\u016c\u016d\u0005l\u0000\u0000\u016d\u016e\u0005f"+
		"\u0000\u0000\u016e6\u0001\u0000\u0000\u0000\u016f\u0170\u0005n\u0000\u0000"+
		"\u0170\u0171\u0005e\u0000\u0000\u0171\u0172\u0005w\u0000\u0000\u01728"+
		"\u0001\u0000\u0000\u0000\u0173\u0174\u0005v\u0000\u0000\u0174\u0175\u0005"+
		"o\u0000\u0000\u0175\u0176\u0005i\u0000\u0000\u0176\u0177\u0005d\u0000"+
		"\u0000\u0177:\u0001\u0000\u0000\u0000\u0178\u0179\u0005c\u0000\u0000\u0179"+
		"\u017a\u0005o\u0000\u0000\u017a\u017b\u0005n\u0000\u0000\u017b\u017c\u0005"+
		"s\u0000\u0000\u017c\u017d\u0005t\u0000\u0000\u017d<\u0001\u0000\u0000"+
		"\u0000\u017e\u017f\u0005f\u0000\u0000\u017f\u0180\u0005u\u0000\u0000\u0180"+
		"\u0181\u0005n\u0000\u0000\u0181\u0182\u0005c\u0000\u0000\u0182>\u0001"+
		"\u0000\u0000\u0000\u0183\u0184\u0005!\u0000\u0000\u0184@\u0001\u0000\u0000"+
		"\u0000\u0185\u0186\u0005&\u0000\u0000\u0186\u0187\u0005&\u0000\u0000\u0187"+
		"B\u0001\u0000\u0000\u0000\u0188\u0189\u0005|\u0000\u0000\u0189\u018a\u0005"+
		"|\u0000\u0000\u018aD\u0001\u0000\u0000\u0000\u018b\u018c\u0005=\u0000"+
		"\u0000\u018c\u018d\u0005=\u0000\u0000\u018dF\u0001\u0000\u0000\u0000\u018e"+
		"\u018f\u0005!\u0000\u0000\u018f\u0190\u0005=\u0000\u0000\u0190H\u0001"+
		"\u0000\u0000\u0000\u0191\u0192\u0005<\u0000\u0000\u0192J\u0001\u0000\u0000"+
		"\u0000\u0193\u0194\u0005>\u0000\u0000\u0194L\u0001\u0000\u0000\u0000\u0195"+
		"\u0196\u0005<\u0000\u0000\u0196\u0197\u0005=\u0000\u0000\u0197N\u0001"+
		"\u0000\u0000\u0000\u0198\u0199\u0005>\u0000\u0000\u0199\u019a\u0005=\u0000"+
		"\u0000\u019aP\u0001\u0000\u0000\u0000\u019b\u019c\u0005=\u0000\u0000\u019c"+
		"R\u0001\u0000\u0000\u0000\u019d\u019e\u0005:\u0000\u0000\u019e\u019f\u0005"+
		"=\u0000\u0000\u019fT\u0001\u0000\u0000\u0000\u01a0\u01a1\u0005+\u0000"+
		"\u0000\u01a1V\u0001\u0000\u0000\u0000\u01a2\u01a3\u0005-\u0000\u0000\u01a3"+
		"X\u0001\u0000\u0000\u0000\u01a4\u01a5\u0005*\u0000\u0000\u01a5Z\u0001"+
		"\u0000\u0000\u0000\u01a6\u01a7\u0005\\\u0000\u0000\u01a7\\\u0001\u0000"+
		"\u0000\u0000\u01a8\u01a9\u0005%\u0000\u0000\u01a9^\u0001\u0000\u0000\u0000"+
		"\u01aa\u01ab\u0005/\u0000\u0000\u01ab`\u0001\u0000\u0000\u0000\u01ac\u01ad"+
		"\u0005<\u0000\u0000\u01ad\u01ae\u0005-\u0000\u0000\u01aeb\u0001\u0000"+
		"\u0000\u0000\u01af\u01b0\u0005^\u0000\u0000\u01b0d\u0001\u0000\u0000\u0000"+
		"\u01b1\u01b2\u0005.\u0000\u0000\u01b2f\u0001\u0000\u0000\u0000\u01b3\u01b4"+
		"\u0005,\u0000\u0000\u01b4h\u0001\u0000\u0000\u0000\u01b5\u01b6\u0005;"+
		"\u0000\u0000\u01b6j\u0001\u0000\u0000\u0000\u01b7\u01b8\u0005:\u0000\u0000"+
		"\u01b8l\u0001\u0000\u0000\u0000\u01b9\u01ba\u0005)\u0000\u0000\u01ban"+
		"\u0001\u0000\u0000\u0000\u01bb\u01bc\u0005(\u0000\u0000\u01bcp\u0001\u0000"+
		"\u0000\u0000\u01bd\u01be\u0005[\u0000\u0000\u01ber\u0001\u0000\u0000\u0000"+
		"\u01bf\u01c0\u0005]\u0000\u0000\u01c0t\u0001\u0000\u0000\u0000\u01c1\u01c2"+
		"\u0005{\u0000\u0000\u01c2v\u0001\u0000\u0000\u0000\u01c3\u01c4\u0005}"+
		"\u0000\u0000\u01c4x\u0001\u0000\u0000\u0000\u01c5\u01c6\u0005@\u0000\u0000"+
		"\u01c6\u01c7\u0003}>\u0000\u01c7z\u0001\u0000\u0000\u0000\u01c8\u01cd"+
		"\u0005\"\u0000\u0000\u01c9\u01cc\u0003\u008dF\u0000\u01ca\u01cc\b\u0002"+
		"\u0000\u0000\u01cb\u01c9\u0001\u0000\u0000\u0000\u01cb\u01ca\u0001\u0000"+
		"\u0000\u0000\u01cc\u01cf\u0001\u0000\u0000\u0000\u01cd\u01cb\u0001\u0000"+
		"\u0000\u0000\u01cd\u01ce\u0001\u0000\u0000\u0000\u01ce\u01d0\u0001\u0000"+
		"\u0000\u0000\u01cf\u01cd\u0001\u0000\u0000\u0000\u01d0\u01d1\u0005\"\u0000"+
		"\u0000\u01d1\u01d2\u0006=\u0001\u0000\u01d2|\u0001\u0000\u0000\u0000\u01d3"+
		"\u01d7\u0007\u0003\u0000\u0000\u01d4\u01d6\u0007\u0004\u0000\u0000\u01d5"+
		"\u01d4\u0001\u0000\u0000\u0000\u01d6\u01d9\u0001\u0000\u0000\u0000\u01d7"+
		"\u01d5\u0001\u0000\u0000\u0000\u01d7\u01d8\u0001\u0000\u0000\u0000\u01d8"+
		"~\u0001\u0000\u0000\u0000\u01d9\u01d7\u0001\u0000\u0000\u0000\u01da\u01dc"+
		"\u0003\u008bE\u0000\u01db\u01da\u0001\u0000\u0000\u0000\u01dc\u01dd\u0001"+
		"\u0000\u0000\u0000\u01dd\u01db\u0001\u0000\u0000\u0000\u01dd\u01de\u0001"+
		"\u0000\u0000\u0000\u01de\u01e4\u0001\u0000\u0000\u0000\u01df\u01e5\u0003"+
		"\u0087C\u0000\u01e0\u01e5\u0003\u0089D\u0000\u01e1\u01e2\u0003\u0087C"+
		"\u0000\u01e2\u01e3\u0003\u0089D\u0000\u01e3\u01e5\u0001\u0000\u0000\u0000"+
		"\u01e4\u01df\u0001\u0000\u0000\u0000\u01e4\u01e0\u0001\u0000\u0000\u0000"+
		"\u01e4\u01e1\u0001\u0000\u0000\u0000\u01e5\u0080\u0001\u0000\u0000\u0000"+
		"\u01e6\u01ea\u0007\u0005\u0000\u0000\u01e7\u01e9\u0007\u0006\u0000\u0000"+
		"\u01e8\u01e7\u0001\u0000\u0000\u0000\u01e9\u01ec\u0001\u0000\u0000\u0000"+
		"\u01ea\u01e8\u0001\u0000\u0000\u0000\u01ea\u01eb\u0001\u0000\u0000\u0000"+
		"\u01eb\u0082\u0001\u0000\u0000\u0000\u01ec\u01ea\u0001\u0000\u0000\u0000"+
		"\u01ed\u01ef\u0003\u008bE\u0000\u01ee\u01ed\u0001\u0000\u0000\u0000\u01ef"+
		"\u01f0\u0001\u0000\u0000\u0000\u01f0\u01ee\u0001\u0000\u0000\u0000\u01f0"+
		"\u01f1\u0001\u0000\u0000\u0000\u01f1\u0084\u0001\u0000\u0000\u0000\u01f2"+
		"\u01f5\u0003U*\u0000\u01f3\u01f5\u0003W+\u0000\u01f4\u01f2\u0001\u0000"+
		"\u0000\u0000\u01f4\u01f3\u0001\u0000\u0000\u0000\u01f5\u0086\u0001\u0000"+
		"\u0000\u0000\u01f6\u01fa\u0003e2\u0000\u01f7\u01f9\u0003\u008bE\u0000"+
		"\u01f8\u01f7\u0001\u0000\u0000\u0000\u01f9\u01fc\u0001\u0000\u0000\u0000"+
		"\u01fa\u01f8\u0001\u0000\u0000\u0000\u01fa\u01fb\u0001\u0000\u0000\u0000"+
		"\u01fb\u0088\u0001\u0000\u0000\u0000\u01fc\u01fa\u0001\u0000\u0000\u0000"+
		"\u01fd\u01ff\u0007\u0007\u0000\u0000\u01fe\u0200\u0003\u0085B\u0000\u01ff"+
		"\u01fe\u0001\u0000\u0000\u0000\u01ff\u0200\u0001\u0000\u0000\u0000\u0200"+
		"\u0202\u0001\u0000\u0000\u0000\u0201\u0203\u0003\u008bE\u0000\u0202\u0201"+
		"\u0001\u0000\u0000\u0000\u0203\u0204\u0001\u0000\u0000\u0000\u0204\u0202"+
		"\u0001\u0000\u0000\u0000\u0204\u0205\u0001\u0000\u0000\u0000\u0205\u008a"+
		"\u0001\u0000\u0000\u0000\u0206\u0207\u0007\u0006\u0000\u0000\u0207\u008c"+
		"\u0001\u0000\u0000\u0000\u0208\u0209\u0005\\\u0000\u0000\u0209\u0217\u0005"+
		"\\\u0000\u0000\u020a\u020b\u0005\\\u0000\u0000\u020b\u0217\u0005b\u0000"+
		"\u0000\u020c\u020d\u0005\\\u0000\u0000\u020d\u0217\u0005f\u0000\u0000"+
		"\u020e\u020f\u0005\\\u0000\u0000\u020f\u0217\u0005r\u0000\u0000\u0210"+
		"\u0211\u0005\\\u0000\u0000\u0211\u0217\u0005n\u0000\u0000\u0212\u0213"+
		"\u0005\\\u0000\u0000\u0213\u0217\u0005t\u0000\u0000\u0214\u0215\u0005"+
		"\\\u0000\u0000\u0215\u0217\u0005\"\u0000\u0000\u0216\u0208\u0001\u0000"+
		"\u0000\u0000\u0216\u020a\u0001\u0000\u0000\u0000\u0216\u020c\u0001\u0000"+
		"\u0000\u0000\u0216\u020e\u0001\u0000\u0000\u0000\u0216\u0210\u0001\u0000"+
		"\u0000\u0000\u0216\u0212\u0001\u0000\u0000\u0000\u0216\u0214\u0001\u0000"+
		"\u0000\u0000\u0217\u008e\u0001\u0000\u0000\u0000\u0218\u0219\u0005\\\u0000"+
		"\u0000\u0219\u021c\b\b\u0000\u0000\u021a\u021c\u0005\\\u0000\u0000\u021b"+
		"\u0218\u0001\u0000\u0000\u0000\u021b\u021a\u0001\u0000\u0000\u0000\u021c"+
		"\u0090\u0001\u0000\u0000\u0000\u021d\u021f\u0007\t\u0000\u0000\u021e\u021d"+
		"\u0001\u0000\u0000\u0000\u021f\u0220\u0001\u0000\u0000\u0000\u0220\u021e"+
		"\u0001\u0000\u0000\u0000\u0220\u0221\u0001\u0000\u0000\u0000\u0221\u0222"+
		"\u0001\u0000\u0000\u0000\u0222\u0223\u0006H\u0000\u0000\u0223\u0092\u0001"+
		"\u0000\u0000\u0000\u0224\u0225\t\u0000\u0000\u0000\u0225\u0226\u0006I"+
		"\u0002\u0000\u0226\u0094\u0001\u0000\u0000\u0000\u0227\u022c\u0005\"\u0000"+
		"\u0000\u0228\u022b\u0003\u008dF\u0000\u0229\u022b\b\u0002\u0000\u0000"+
		"\u022a\u0228\u0001\u0000\u0000\u0000\u022a\u0229\u0001\u0000\u0000\u0000"+
		"\u022b\u022e\u0001\u0000\u0000\u0000\u022c\u022a\u0001\u0000\u0000\u0000"+
		"\u022c\u022d\u0001\u0000\u0000\u0000\u022d\u0230\u0001\u0000\u0000\u0000"+
		"\u022e\u022c\u0001\u0000\u0000\u0000\u022f\u0231\u0007\n\u0000\u0000\u0230"+
		"\u022f\u0001\u0000\u0000\u0000\u0231\u0232\u0001\u0000\u0000\u0000\u0232"+
		"\u0233\u0006J\u0003\u0000\u0233\u0096\u0001\u0000\u0000\u0000\u0234\u0239"+
		"\u0005\"\u0000\u0000\u0235\u0238\u0003\u008dF\u0000\u0236\u0238\b\u0002"+
		"\u0000\u0000\u0237\u0235\u0001\u0000\u0000\u0000\u0237\u0236\u0001\u0000"+
		"\u0000\u0000\u0238\u023b\u0001\u0000\u0000\u0000\u0239\u0237\u0001\u0000"+
		"\u0000\u0000\u0239\u023a\u0001\u0000\u0000\u0000\u023a\u023c\u0001\u0000"+
		"\u0000\u0000\u023b\u0239\u0001\u0000\u0000\u0000\u023c\u023d\u0003\u008f"+
		"G\u0000\u023d\u023e\u0006K\u0004\u0000\u023e\u0098\u0001\u0000\u0000\u0000"+
		"\u0016\u0000\u00f7\u0105\u01cb\u01cd\u01d7\u01dd\u01e4\u01ea\u01f0\u01f4"+
		"\u01fa\u01ff\u0204\u0216\u021b\u0220\u022a\u022c\u0230\u0237\u0239\u0005"+
		"\u0006\u0000\u0000\u0001=\u0000\u0001I\u0001\u0001J\u0002\u0001K\u0003";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}