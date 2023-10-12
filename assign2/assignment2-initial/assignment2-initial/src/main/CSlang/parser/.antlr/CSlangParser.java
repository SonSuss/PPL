// Generated from e:/hocbaidcm/PPL/assignment/assign2/assignment2-initial/assignment2-initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CSlangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, BLOCK_COMMENT=9, 
		LINE_COMMENT=10, BREAK=11, CONTINUE=12, IF=13, ELSE=14, FOR=15, TRUE=16, 
		FALSE=17, INT=18, FLOAT=19, BOOL=20, STRING=21, RETURN=22, NULL=23, CLASS=24, 
		CONSTRUCTOR=25, VAR=26, SELF=27, NEW=28, VOID=29, CONST=30, CONSTANT=31, 
		FUNC=32, NOT=33, AND=34, OR=35, EQUAL=36, NOT_EQUAL=37, LESS=38, GREATER=39, 
		LESS_EQUAL=40, GREATER_EQUAL=41, INITIAL=42, ASSIGN=43, PLUS=44, MINUS=45, 
		MULTIPLY=46, DIVIDE_I=47, DIVIDE_I_L=48, DIVIDE_F=49, SUPER_CLASS=50, 
		STRING_CONCAT=51, DOT=52, COMMA=53, SEMICOLON=54, COLON=55, RPAREN=56, 
		LPAREN=57, LBRACK=58, RBRACK=59, LBRASE=60, RBRASE=61, AT_ID=62, STRING_LITERAL=63, 
		ID=64, FLOAT_LITERAL=65, NON_ZERO_INT=66, INT_LITERAL=67, WS=68, ERROR_CHAR=69, 
		UNCLOSE_STRING=70, ILLEGAL_ESCAPE=71;
	public static final int
		RULE_program = 0, RULE_class_dcl = 1, RULE_class_body = 2, RULE_method_lst = 3, 
		RULE_method_dcl = 4, RULE_constructor_decl = 5, RULE_param_lst = 6, RULE_param = 7, 
		RULE_multiplying = 8, RULE_adding = 9, RULE_logical_bin = 10, RULE_logical_not = 11, 
		RULE_relational = 12, RULE_relat_bool = 13, RULE_relat_int_float = 14, 
		RULE_relational_expr0 = 15, RULE_relational_expr = 16, RULE_expr_lst = 17, 
		RULE_expr = 18, RULE_expr1 = 19, RULE_expr2 = 20, RULE_expr3 = 21, RULE_expr4 = 22, 
		RULE_expr5 = 23, RULE_expr6 = 24, RULE_expr7 = 25, RULE_expr8 = 26, RULE_expr9 = 27, 
		RULE_expr10 = 28, RULE_expr11 = 29, RULE_statements = 30, RULE_assign_decl = 31, 
		RULE_attribute_assign = 32, RULE_attribute_decl = 33, RULE_variable_decl = 34, 
		RULE_constraint_decl = 35, RULE_non_inital_decl = 36, RULE_inital_decl = 37, 
		RULE_array_type = 38, RULE_if_state = 39, RULE_for_state = 40, RULE_break_state = 41, 
		RULE_continue_state = 42, RULE_return_state = 43, RULE_call_state = 44, 
		RULE_instance_method_invo_access = 45, RULE_static_method_invo_access = 46, 
		RULE_block_state = 47, RULE_lhs = 48, RULE_index_op = 49, RULE_id_lst = 50, 
		RULE_id_access = 51, RULE_io_st = 52, RULE_io_mt = 53, RULE_typ = 54, 
		RULE_attri_type = 55, RULE_literal = 56, RULE_bool_literal = 57, RULE_array = 58;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class_dcl", "class_body", "method_lst", "method_dcl", "constructor_decl", 
			"param_lst", "param", "multiplying", "adding", "logical_bin", "logical_not", 
			"relational", "relat_bool", "relat_int_float", "relational_expr0", "relational_expr", 
			"expr_lst", "expr", "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
			"expr7", "expr8", "expr9", "expr10", "expr11", "statements", "assign_decl", 
			"attribute_assign", "attribute_decl", "variable_decl", "constraint_decl", 
			"non_inital_decl", "inital_decl", "array_type", "if_state", "for_state", 
			"break_state", "continue_state", "return_state", "call_state", "instance_method_invo_access", 
			"static_method_invo_access", "block_state", "lhs", "index_op", "id_lst", 
			"id_access", "io_st", "io_mt", "typ", "attri_type", "literal", "bool_literal", 
			"array"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'@readInt'", "'@writeInt'", "'@readFloat'", "'@writeFloat'", "'@readBool'", 
			"'@writeBool'", "'@readString'", "'@writeString'", null, null, "'break'", 
			"'continue'", "'if'", "'else'", "'for'", "'true'", "'false'", "'int'", 
			"'float'", "'bool'", "'string'", "'return'", "'null'", "'class'", "'constructor'", 
			"'var'", "'self'", "'new'", "'void'", "'const'", "'constant'", "'func'", 
			"'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
			"'='", "':='", "'+'", "'-'", "'*'", "'\\'", "'%'", "'/'", "'<-'", "'^'", 
			"'.'", "','", "';'", "':'", "')'", "'('", "'['", "']'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "BLOCK_COMMENT", 
			"LINE_COMMENT", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
			"INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
			"VAR", "SELF", "NEW", "VOID", "CONST", "CONSTANT", "FUNC", "NOT", "AND", 
			"OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
			"INITIAL", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", 
			"DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", 
			"COLON", "RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", "RBRASE", 
			"AT_ID", "STRING_LITERAL", "ID", "FLOAT_LITERAL", "NON_ZERO_INT", "INT_LITERAL", 
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

	@Override
	public String getGrammarFileName() { return "CSlang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CSlangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CSlangParser.EOF, 0); }
		public List<Class_dclContext> class_dcl() {
			return getRuleContexts(Class_dclContext.class);
		}
		public Class_dclContext class_dcl(int i) {
			return getRuleContext(Class_dclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CLASS) {
				{
				{
				setState(118);
				class_dcl();
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(124);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Class_dclContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(CSlangParser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(CSlangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(CSlangParser.ID, i);
		}
		public TerminalNode LBRASE() { return getToken(CSlangParser.LBRASE, 0); }
		public TerminalNode RBRASE() { return getToken(CSlangParser.RBRASE, 0); }
		public TerminalNode SUPER_CLASS() { return getToken(CSlangParser.SUPER_CLASS, 0); }
		public List<Class_bodyContext> class_body() {
			return getRuleContexts(Class_bodyContext.class);
		}
		public Class_bodyContext class_body(int i) {
			return getRuleContext(Class_bodyContext.class,i);
		}
		public Class_dclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_dcl; }
	}

	public final Class_dclContext class_dcl() throws RecognitionException {
		Class_dclContext _localctx = new Class_dclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class_dcl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(CLASS);
			setState(129);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(127);
				match(ID);
				setState(128);
				match(SUPER_CLASS);
				}
				break;
			}
			setState(131);
			match(ID);
			setState(132);
			match(LBRASE);
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5435817984L) != 0)) {
				{
				{
				setState(133);
				class_body();
				}
				}
				setState(138);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(139);
			match(RBRASE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Class_bodyContext extends ParserRuleContext {
		public Method_lstContext method_lst() {
			return getRuleContext(Method_lstContext.class,0);
		}
		public Attribute_declContext attribute_decl() {
			return getRuleContext(Attribute_declContext.class,0);
		}
		public Constructor_declContext constructor_decl() {
			return getRuleContext(Constructor_declContext.class,0);
		}
		public Class_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_body; }
	}

	public final Class_bodyContext class_body() throws RecognitionException {
		Class_bodyContext _localctx = new Class_bodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_class_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(141);
				method_lst();
				}
				break;
			case 2:
				{
				setState(142);
				attribute_decl();
				}
				break;
			case 3:
				{
				setState(143);
				constructor_decl();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Method_lstContext extends ParserRuleContext {
		public List<Method_dclContext> method_dcl() {
			return getRuleContexts(Method_dclContext.class);
		}
		public Method_dclContext method_dcl(int i) {
			return getRuleContext(Method_dclContext.class,i);
		}
		public Method_lstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_lst; }
	}

	public final Method_lstContext method_lst() throws RecognitionException {
		Method_lstContext _localctx = new Method_lstContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_method_lst);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(147); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(146);
					method_dcl();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(149); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Method_dclContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(CSlangParser.FUNC, 0); }
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public Param_lstContext param_lst() {
			return getRuleContext(Param_lstContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(CSlangParser.COLON, 0); }
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public Block_stateContext block_state() {
			return getRuleContext(Block_stateContext.class,0);
		}
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode AT_ID() { return getToken(CSlangParser.AT_ID, 0); }
		public Method_dclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_dcl; }
	}

	public final Method_dclContext method_dcl() throws RecognitionException {
		Method_dclContext _localctx = new Method_dclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_method_dcl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(FUNC);
			setState(152);
			_la = _input.LA(1);
			if ( !(_la==AT_ID || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(153);
			match(LPAREN);
			setState(154);
			param_lst();
			setState(155);
			match(RPAREN);
			setState(156);
			match(COLON);
			setState(157);
			typ();
			setState(158);
			block_state();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Constructor_declContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(CSlangParser.FUNC, 0); }
		public TerminalNode CONSTRUCTOR() { return getToken(CSlangParser.CONSTRUCTOR, 0); }
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public Param_lstContext param_lst() {
			return getRuleContext(Param_lstContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public Block_stateContext block_state() {
			return getRuleContext(Block_stateContext.class,0);
		}
		public Constructor_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructor_decl; }
	}

	public final Constructor_declContext constructor_decl() throws RecognitionException {
		Constructor_declContext _localctx = new Constructor_declContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_constructor_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(FUNC);
			setState(161);
			match(CONSTRUCTOR);
			setState(162);
			match(LPAREN);
			setState(163);
			param_lst();
			setState(164);
			match(RPAREN);
			setState(165);
			block_state();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Param_lstContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CSlangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSlangParser.COMMA, i);
		}
		public Param_lstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_lst; }
	}

	public final Param_lstContext param_lst() throws RecognitionException {
		Param_lstContext _localctx = new Param_lstContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_param_lst);
		int _la;
		try {
			setState(176);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AT_ID:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				param();
				setState(172);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(168);
					match(COMMA);
					setState(169);
					param();
					}
					}
					setState(174);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public Id_lstContext id_lst() {
			return getRuleContext(Id_lstContext.class,0);
		}
		public TerminalNode COLON() { return getToken(CSlangParser.COLON, 0); }
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			id_lst();
			setState(179);
			match(COLON);
			setState(180);
			typ();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplyingContext extends ParserRuleContext {
		public TerminalNode MULTIPLY() { return getToken(CSlangParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE_F() { return getToken(CSlangParser.DIVIDE_F, 0); }
		public TerminalNode DIVIDE_I() { return getToken(CSlangParser.DIVIDE_I, 0); }
		public TerminalNode DIVIDE_I_L() { return getToken(CSlangParser.DIVIDE_I_L, 0); }
		public MultiplyingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplying; }
	}

	public final MultiplyingContext multiplying() throws RecognitionException {
		MultiplyingContext _localctx = new MultiplyingContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_multiplying);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1055531162664960L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddingContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(CSlangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(CSlangParser.MINUS, 0); }
		public AddingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_adding; }
	}

	public final AddingContext adding() throws RecognitionException {
		AddingContext _localctx = new AddingContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_adding);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logical_binContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(CSlangParser.AND, 0); }
		public TerminalNode OR() { return getToken(CSlangParser.OR, 0); }
		public Logical_binContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_bin; }
	}

	public final Logical_binContext logical_bin() throws RecognitionException {
		Logical_binContext _localctx = new Logical_binContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_logical_bin);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logical_notContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(CSlangParser.NOT, 0); }
		public Logical_notContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_not; }
	}

	public final Logical_notContext logical_not() throws RecognitionException {
		Logical_notContext _localctx = new Logical_notContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_logical_not);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			match(NOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelationalContext extends ParserRuleContext {
		public Relat_boolContext relat_bool() {
			return getRuleContext(Relat_boolContext.class,0);
		}
		public Relat_int_floatContext relat_int_float() {
			return getRuleContext(Relat_int_floatContext.class,0);
		}
		public RelationalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational; }
	}

	public final RelationalContext relational() throws RecognitionException {
		RelationalContext _localctx = new RelationalContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_relational);
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUAL:
			case NOT_EQUAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				relat_bool();
				}
				break;
			case LESS:
			case GREATER:
			case LESS_EQUAL:
			case GREATER_EQUAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(191);
				relat_int_float();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Relat_boolContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(CSlangParser.EQUAL, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(CSlangParser.NOT_EQUAL, 0); }
		public Relat_boolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relat_bool; }
	}

	public final Relat_boolContext relat_bool() throws RecognitionException {
		Relat_boolContext _localctx = new Relat_boolContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_relat_bool);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			_la = _input.LA(1);
			if ( !(_la==EQUAL || _la==NOT_EQUAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Relat_int_floatContext extends ParserRuleContext {
		public TerminalNode LESS() { return getToken(CSlangParser.LESS, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(CSlangParser.LESS_EQUAL, 0); }
		public TerminalNode GREATER_EQUAL() { return getToken(CSlangParser.GREATER_EQUAL, 0); }
		public TerminalNode GREATER() { return getToken(CSlangParser.GREATER, 0); }
		public Relat_int_floatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relat_int_float; }
	}

	public final Relat_int_floatContext relat_int_float() throws RecognitionException {
		Relat_int_floatContext _localctx = new Relat_int_floatContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_relat_int_float);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4123168604160L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Relational_expr0Context extends ParserRuleContext {
		public Relational_exprContext relational_expr() {
			return getRuleContext(Relational_exprContext.class,0);
		}
		public Relational_expr0Context relational_expr0() {
			return getRuleContext(Relational_expr0Context.class,0);
		}
		public Logical_binContext logical_bin() {
			return getRuleContext(Logical_binContext.class,0);
		}
		public Relational_expr0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_expr0; }
	}

	public final Relational_expr0Context relational_expr0() throws RecognitionException {
		return relational_expr0(0);
	}

	private Relational_expr0Context relational_expr0(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Relational_expr0Context _localctx = new Relational_expr0Context(_ctx, _parentState);
		Relational_expr0Context _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_relational_expr0, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(199);
			relational_expr();
			}
			_ctx.stop = _input.LT(-1);
			setState(207);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Relational_expr0Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_relational_expr0);
					setState(201);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(202);
					logical_bin();
					setState(203);
					relational_expr();
					}
					} 
				}
				setState(209);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Relational_exprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RelationalContext relational() {
			return getRuleContext(RelationalContext.class,0);
		}
		public Bool_literalContext bool_literal() {
			return getRuleContext(Bool_literalContext.class,0);
		}
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public Relational_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_expr; }
	}

	public final Relational_exprContext relational_expr() throws RecognitionException {
		Relational_exprContext _localctx = new Relational_exprContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_relational_expr);
		try {
			setState(216);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(210);
				expr(0);
				setState(211);
				relational();
				setState(212);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(214);
				bool_literal();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(215);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_lstContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(CSlangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSlangParser.COMMA, i);
		}
		public List<Expr_lstContext> expr_lst() {
			return getRuleContexts(Expr_lstContext.class);
		}
		public Expr_lstContext expr_lst(int i) {
			return getRuleContext(Expr_lstContext.class,i);
		}
		public Expr_lstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_lst; }
	}

	public final Expr_lstContext expr_lst() throws RecognitionException {
		Expr_lstContext _localctx = new Expr_lstContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_expr_lst);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 16)) & ~0x3f) == 0 && ((1L << (_la - 16)) & 4439828489967747L) != 0)) {
				{
				setState(218);
				expr(0);
				setState(223);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(219);
						match(COMMA);
						setState(220);
						expr_lst();
						}
						} 
					}
					setState(225);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public Expr1Context expr1() {
			return getRuleContext(Expr1Context.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode STRING_CONCAT() { return getToken(CSlangParser.STRING_CONCAT, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(229);
			expr1(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(236);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(231);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(232);
					match(STRING_CONCAT);
					setState(233);
					expr(3);
					}
					} 
				}
				setState(238);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr1Context extends ParserRuleContext {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public List<Expr1Context> expr1() {
			return getRuleContexts(Expr1Context.class);
		}
		public Expr1Context expr1(int i) {
			return getRuleContext(Expr1Context.class,i);
		}
		public RelationalContext relational() {
			return getRuleContext(RelationalContext.class,0);
		}
		public Expr1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr1; }
	}

	public final Expr1Context expr1() throws RecognitionException {
		return expr1(0);
	}

	private Expr1Context expr1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr1Context _localctx = new Expr1Context(_ctx, _parentState);
		Expr1Context _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_expr1, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(240);
			expr2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(248);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr1);
					setState(242);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(243);
					relational();
					setState(244);
					expr1(3);
					}
					} 
				}
				setState(250);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr2Context extends ParserRuleContext {
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public Logical_binContext logical_bin() {
			return getRuleContext(Logical_binContext.class,0);
		}
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
	}

	public final Expr2Context expr2() throws RecognitionException {
		return expr2(0);
	}

	private Expr2Context expr2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr2Context _localctx = new Expr2Context(_ctx, _parentState);
		Expr2Context _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_expr2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(252);
			expr3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(260);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr2);
					setState(254);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(255);
					logical_bin();
					setState(256);
					expr3(0);
					}
					} 
				}
				setState(262);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr3Context extends ParserRuleContext {
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public AddingContext adding() {
			return getRuleContext(AddingContext.class,0);
		}
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
	}

	public final Expr3Context expr3() throws RecognitionException {
		return expr3(0);
	}

	private Expr3Context expr3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr3Context _localctx = new Expr3Context(_ctx, _parentState);
		Expr3Context _prevctx = _localctx;
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_expr3, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(264);
			expr4(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(272);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr3);
					setState(266);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(267);
					adding();
					setState(268);
					expr4(0);
					}
					} 
				}
				setState(274);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr4Context extends ParserRuleContext {
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public MultiplyingContext multiplying() {
			return getRuleContext(MultiplyingContext.class,0);
		}
		public Expr4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr4; }
	}

	public final Expr4Context expr4() throws RecognitionException {
		return expr4(0);
	}

	private Expr4Context expr4(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr4Context _localctx = new Expr4Context(_ctx, _parentState);
		Expr4Context _prevctx = _localctx;
		int _startState = 44;
		enterRecursionRule(_localctx, 44, RULE_expr4, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(276);
			expr5();
			}
			_ctx.stop = _input.LT(-1);
			setState(284);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr4Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr4);
					setState(278);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(279);
					multiplying();
					setState(280);
					expr5();
					}
					} 
				}
				setState(286);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr5Context extends ParserRuleContext {
		public Logical_notContext logical_not() {
			return getRuleContext(Logical_notContext.class,0);
		}
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr5; }
	}

	public final Expr5Context expr5() throws RecognitionException {
		Expr5Context _localctx = new Expr5Context(_ctx, getState());
		enterRule(_localctx, 46, RULE_expr5);
		try {
			setState(291);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(287);
				logical_not();
				setState(288);
				expr6();
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case NEW:
			case MINUS:
			case LPAREN:
			case LBRACK:
			case AT_ID:
			case STRING_LITERAL:
			case ID:
			case FLOAT_LITERAL:
			case NON_ZERO_INT:
			case INT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(290);
				expr6();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr6Context extends ParserRuleContext {
		public TerminalNode MINUS() { return getToken(CSlangParser.MINUS, 0); }
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public Expr6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr6; }
	}

	public final Expr6Context expr6() throws RecognitionException {
		Expr6Context _localctx = new Expr6Context(_ctx, getState());
		enterRule(_localctx, 48, RULE_expr6);
		try {
			setState(296);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(293);
				match(MINUS);
				setState(294);
				expr6();
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case NEW:
			case LPAREN:
			case LBRACK:
			case AT_ID:
			case STRING_LITERAL:
			case ID:
			case FLOAT_LITERAL:
			case NON_ZERO_INT:
			case INT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(295);
				expr7(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr7Context extends ParserRuleContext {
		public Expr8Context expr8() {
			return getRuleContext(Expr8Context.class,0);
		}
		public List<Expr7Context> expr7() {
			return getRuleContexts(Expr7Context.class);
		}
		public Expr7Context expr7(int i) {
			return getRuleContext(Expr7Context.class,i);
		}
		public TerminalNode LBRACK() { return getToken(CSlangParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(CSlangParser.RBRACK, 0); }
		public Expr7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr7; }
	}

	public final Expr7Context expr7() throws RecognitionException {
		return expr7(0);
	}

	private Expr7Context expr7(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr7Context _localctx = new Expr7Context(_ctx, _parentState);
		Expr7Context _prevctx = _localctx;
		int _startState = 50;
		enterRecursionRule(_localctx, 50, RULE_expr7, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(299);
			expr8(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(308);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr7Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr7);
					setState(301);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(302);
					match(LBRACK);
					setState(303);
					expr7(0);
					setState(304);
					match(RBRACK);
					}
					} 
				}
				setState(310);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr8Context extends ParserRuleContext {
		public Expr9Context expr9() {
			return getRuleContext(Expr9Context.class,0);
		}
		public Expr8Context expr8() {
			return getRuleContext(Expr8Context.class,0);
		}
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public Expr_lstContext expr_lst() {
			return getRuleContext(Expr_lstContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public Expr8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr8; }
	}

	public final Expr8Context expr8() throws RecognitionException {
		return expr8(0);
	}

	private Expr8Context expr8(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr8Context _localctx = new Expr8Context(_ctx, _parentState);
		Expr8Context _prevctx = _localctx;
		int _startState = 52;
		enterRecursionRule(_localctx, 52, RULE_expr8, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(312);
			expr9();
			}
			_ctx.stop = _input.LT(-1);
			setState(326);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(324);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						_localctx = new Expr8Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr8);
						setState(314);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(315);
						match(DOT);
						setState(316);
						match(ID);
						}
						break;
					case 2:
						{
						_localctx = new Expr8Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr8);
						setState(317);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(318);
						match(DOT);
						setState(319);
						match(ID);
						{
						setState(320);
						match(LPAREN);
						setState(321);
						expr_lst();
						setState(322);
						match(RPAREN);
						}
						}
						break;
					}
					} 
				}
				setState(328);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr9Context extends ParserRuleContext {
		public TerminalNode AT_ID() { return getToken(CSlangParser.AT_ID, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public Expr_lstContext expr_lst() {
			return getRuleContext(Expr_lstContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public Expr10Context expr10() {
			return getRuleContext(Expr10Context.class,0);
		}
		public Expr9Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr9; }
	}

	public final Expr9Context expr9() throws RecognitionException {
		Expr9Context _localctx = new Expr9Context(_ctx, getState());
		enterRule(_localctx, 54, RULE_expr9);
		int _la;
		try {
			setState(344);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(331);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(329);
					match(ID);
					setState(330);
					match(DOT);
					}
				}

				setState(333);
				match(AT_ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(336);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(334);
					match(ID);
					setState(335);
					match(DOT);
					}
				}

				setState(338);
				match(AT_ID);
				{
				setState(339);
				match(LPAREN);
				setState(340);
				expr_lst();
				setState(341);
				match(RPAREN);
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(343);
				expr10();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr10Context extends ParserRuleContext {
		public TerminalNode NEW() { return getToken(CSlangParser.NEW, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public Expr_lstContext expr_lst() {
			return getRuleContext(Expr_lstContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public Expr11Context expr11() {
			return getRuleContext(Expr11Context.class,0);
		}
		public Expr10Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr10; }
	}

	public final Expr10Context expr10() throws RecognitionException {
		Expr10Context _localctx = new Expr10Context(_ctx, getState());
		enterRule(_localctx, 56, RULE_expr10);
		try {
			setState(353);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEW:
				enterOuterAlt(_localctx, 1);
				{
				setState(346);
				match(NEW);
				setState(347);
				match(ID);
				setState(348);
				match(LPAREN);
				setState(349);
				expr_lst();
				setState(350);
				match(RPAREN);
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case SELF:
			case LPAREN:
			case LBRACK:
			case STRING_LITERAL:
			case ID:
			case FLOAT_LITERAL:
			case NON_ZERO_INT:
			case INT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(352);
				expr11();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr11Context extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode SELF() { return getToken(CSlangParser.SELF, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode NULL() { return getToken(CSlangParser.NULL, 0); }
		public Expr11Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr11; }
	}

	public final Expr11Context expr11() throws RecognitionException {
		Expr11Context _localctx = new Expr11Context(_ctx, getState());
		enterRule(_localctx, 58, RULE_expr11);
		try {
			setState(363);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(355);
				match(LPAREN);
				setState(356);
				expr(0);
				setState(357);
				match(RPAREN);
				}
				break;
			case TRUE:
			case FALSE:
			case LBRACK:
			case STRING_LITERAL:
			case FLOAT_LITERAL:
			case NON_ZERO_INT:
			case INT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(359);
				literal();
				}
				break;
			case SELF:
				enterOuterAlt(_localctx, 3);
				{
				setState(360);
				match(SELF);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(361);
				match(ID);
				}
				break;
			case NULL:
				enterOuterAlt(_localctx, 5);
				{
				setState(362);
				match(NULL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementsContext extends ParserRuleContext {
		public Attribute_declContext attribute_decl() {
			return getRuleContext(Attribute_declContext.class,0);
		}
		public Assign_declContext assign_decl() {
			return getRuleContext(Assign_declContext.class,0);
		}
		public If_stateContext if_state() {
			return getRuleContext(If_stateContext.class,0);
		}
		public For_stateContext for_state() {
			return getRuleContext(For_stateContext.class,0);
		}
		public Break_stateContext break_state() {
			return getRuleContext(Break_stateContext.class,0);
		}
		public Continue_stateContext continue_state() {
			return getRuleContext(Continue_stateContext.class,0);
		}
		public Return_stateContext return_state() {
			return getRuleContext(Return_stateContext.class,0);
		}
		public Call_stateContext call_state() {
			return getRuleContext(Call_stateContext.class,0);
		}
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_statements);
		try {
			setState(373);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(365);
				attribute_decl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(366);
				assign_decl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(367);
				if_state();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(368);
				for_state();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(369);
				break_state();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(370);
				continue_state();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(371);
				return_state();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(372);
				call_state();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_declContext extends ParserRuleContext {
		public Attribute_assignContext attribute_assign() {
			return getRuleContext(Attribute_assignContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public Assign_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_decl; }
	}

	public final Assign_declContext assign_decl() throws RecognitionException {
		Assign_declContext _localctx = new Assign_declContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_assign_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			attribute_assign();
			setState(376);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Attribute_assignContext extends ParserRuleContext {
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSlangParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Attribute_assignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_assign; }
	}

	public final Attribute_assignContext attribute_assign() throws RecognitionException {
		Attribute_assignContext _localctx = new Attribute_assignContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_attribute_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			lhs();
			setState(379);
			match(ASSIGN);
			setState(380);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Attribute_declContext extends ParserRuleContext {
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public Variable_declContext variable_decl() {
			return getRuleContext(Variable_declContext.class,0);
		}
		public Constraint_declContext constraint_decl() {
			return getRuleContext(Constraint_declContext.class,0);
		}
		public Attribute_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_decl; }
	}

	public final Attribute_declContext attribute_decl() throws RecognitionException {
		Attribute_declContext _localctx = new Attribute_declContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_attribute_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(382);
				variable_decl();
				}
				break;
			case CONST:
				{
				setState(383);
				constraint_decl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(386);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Variable_declContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(CSlangParser.VAR, 0); }
		public Non_inital_declContext non_inital_decl() {
			return getRuleContext(Non_inital_declContext.class,0);
		}
		public Inital_declContext inital_decl() {
			return getRuleContext(Inital_declContext.class,0);
		}
		public Variable_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_decl; }
	}

	public final Variable_declContext variable_decl() throws RecognitionException {
		Variable_declContext _localctx = new Variable_declContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_variable_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(388);
			match(VAR);
			setState(391);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				{
				setState(389);
				non_inital_decl();
				}
				break;
			case 2:
				{
				setState(390);
				inital_decl();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Constraint_declContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(CSlangParser.CONST, 0); }
		public Inital_declContext inital_decl() {
			return getRuleContext(Inital_declContext.class,0);
		}
		public Constraint_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constraint_decl; }
	}

	public final Constraint_declContext constraint_decl() throws RecognitionException {
		Constraint_declContext _localctx = new Constraint_declContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_constraint_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(393);
			match(CONST);
			setState(394);
			inital_decl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Non_inital_declContext extends ParserRuleContext {
		public Id_lstContext id_lst() {
			return getRuleContext(Id_lstContext.class,0);
		}
		public TerminalNode COLON() { return getToken(CSlangParser.COLON, 0); }
		public Attri_typeContext attri_type() {
			return getRuleContext(Attri_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Non_inital_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_non_inital_decl; }
	}

	public final Non_inital_declContext non_inital_decl() throws RecognitionException {
		Non_inital_declContext _localctx = new Non_inital_declContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_non_inital_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(396);
			id_lst();
			setState(397);
			match(COLON);
			setState(400);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case BOOL:
			case STRING:
			case ID:
				{
				setState(398);
				attri_type();
				}
				break;
			case LBRACK:
				{
				setState(399);
				array_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Inital_declContext extends ParserRuleContext {
		public Id_accessContext id_access() {
			return getRuleContext(Id_accessContext.class,0);
		}
		public TerminalNode COLON() { return getToken(CSlangParser.COLON, 0); }
		public TerminalNode INITIAL() { return getToken(CSlangParser.INITIAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Attri_typeContext attri_type() {
			return getRuleContext(Attri_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(CSlangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSlangParser.COMMA, i);
		}
		public Inital_declContext inital_decl() {
			return getRuleContext(Inital_declContext.class,0);
		}
		public Inital_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inital_decl; }
	}

	public final Inital_declContext inital_decl() throws RecognitionException {
		Inital_declContext _localctx = new Inital_declContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_inital_decl);
		try {
			setState(417);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(402);
				id_access();
				setState(403);
				match(COLON);
				setState(406);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
				case FLOAT:
				case BOOL:
				case STRING:
				case ID:
					{
					setState(404);
					attri_type();
					}
					break;
				case LBRACK:
					{
					setState(405);
					array_type();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(408);
				match(INITIAL);
				setState(409);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(411);
				id_access();
				setState(412);
				match(COMMA);
				setState(413);
				inital_decl();
				setState(414);
				match(COMMA);
				setState(415);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Array_typeContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(CSlangParser.LBRACK, 0); }
		public TerminalNode NON_ZERO_INT() { return getToken(CSlangParser.NON_ZERO_INT, 0); }
		public TerminalNode RBRACK() { return getToken(CSlangParser.RBRACK, 0); }
		public Attri_typeContext attri_type() {
			return getRuleContext(Attri_typeContext.class,0);
		}
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_array_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			match(LBRACK);
			setState(420);
			match(NON_ZERO_INT);
			setState(421);
			match(RBRACK);
			setState(422);
			attri_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_stateContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(CSlangParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<Block_stateContext> block_state() {
			return getRuleContexts(Block_stateContext.class);
		}
		public Block_stateContext block_state(int i) {
			return getRuleContext(Block_stateContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(CSlangParser.ELSE, 0); }
		public If_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_state; }
	}

	public final If_stateContext if_state() throws RecognitionException {
		If_stateContext _localctx = new If_stateContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_if_state);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			match(IF);
			setState(426);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LBRASE) {
				{
				setState(425);
				block_state();
				}
			}

			setState(428);
			expr(0);
			setState(429);
			block_state();
			setState(432);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(430);
				match(ELSE);
				setState(431);
				block_state();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_stateContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(CSlangParser.FOR, 0); }
		public List<Attribute_assignContext> attribute_assign() {
			return getRuleContexts(Attribute_assignContext.class);
		}
		public Attribute_assignContext attribute_assign(int i) {
			return getRuleContext(Attribute_assignContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CSlangParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CSlangParser.SEMICOLON, i);
		}
		public Relational_expr0Context relational_expr0() {
			return getRuleContext(Relational_expr0Context.class,0);
		}
		public Block_stateContext block_state() {
			return getRuleContext(Block_stateContext.class,0);
		}
		public For_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_state; }
	}

	public final For_stateContext for_state() throws RecognitionException {
		For_stateContext _localctx = new For_stateContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_for_state);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(434);
			match(FOR);
			setState(435);
			attribute_assign();
			setState(436);
			match(SEMICOLON);
			setState(437);
			relational_expr0(0);
			setState(438);
			match(SEMICOLON);
			setState(439);
			attribute_assign();
			setState(440);
			block_state();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Break_stateContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(CSlangParser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public Break_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_state; }
	}

	public final Break_stateContext break_state() throws RecognitionException {
		Break_stateContext _localctx = new Break_stateContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_break_state);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(442);
			match(BREAK);
			setState(443);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Continue_stateContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(CSlangParser.CONTINUE, 0); }
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public Continue_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_state; }
	}

	public final Continue_stateContext continue_state() throws RecognitionException {
		Continue_stateContext _localctx = new Continue_stateContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_continue_state);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(445);
			match(CONTINUE);
			setState(446);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_stateContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(CSlangParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public Return_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_state; }
	}

	public final Return_stateContext return_state() throws RecognitionException {
		Return_stateContext _localctx = new Return_stateContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_return_state);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(448);
			match(RETURN);
			setState(449);
			expr(0);
			setState(450);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Call_stateContext extends ParserRuleContext {
		public Instance_method_invo_accessContext instance_method_invo_access() {
			return getRuleContext(Instance_method_invo_accessContext.class,0);
		}
		public Static_method_invo_accessContext static_method_invo_access() {
			return getRuleContext(Static_method_invo_accessContext.class,0);
		}
		public Io_stContext io_st() {
			return getRuleContext(Io_stContext.class,0);
		}
		public Call_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_state; }
	}

	public final Call_stateContext call_state() throws RecognitionException {
		Call_stateContext _localctx = new Call_stateContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_call_state);
		try {
			setState(455);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(452);
				instance_method_invo_access();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(453);
				static_method_invo_access();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(454);
				io_st();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Instance_method_invo_accessContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public Expr_lstContext expr_lst() {
			return getRuleContext(Expr_lstContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public Instance_method_invo_accessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance_method_invo_access; }
	}

	public final Instance_method_invo_accessContext instance_method_invo_access() throws RecognitionException {
		Instance_method_invo_accessContext _localctx = new Instance_method_invo_accessContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_instance_method_invo_access);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(457);
			expr(0);
			setState(458);
			match(DOT);
			setState(459);
			match(ID);
			{
			setState(460);
			match(LPAREN);
			setState(461);
			expr_lst();
			setState(462);
			match(RPAREN);
			}
			setState(464);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Static_method_invo_accessContext extends ParserRuleContext {
		public TerminalNode AT_ID() { return getToken(CSlangParser.AT_ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public Expr_lstContext expr_lst() {
			return getRuleContext(Expr_lstContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public Static_method_invo_accessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_static_method_invo_access; }
	}

	public final Static_method_invo_accessContext static_method_invo_access() throws RecognitionException {
		Static_method_invo_accessContext _localctx = new Static_method_invo_accessContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_static_method_invo_access);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(468);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(466);
				match(ID);
				setState(467);
				match(DOT);
				}
			}

			setState(470);
			match(AT_ID);
			{
			setState(471);
			match(LPAREN);
			setState(472);
			expr_lst();
			setState(473);
			match(RPAREN);
			}
			setState(475);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Block_stateContext extends ParserRuleContext {
		public TerminalNode LBRASE() { return getToken(CSlangParser.LBRASE, 0); }
		public TerminalNode RBRASE() { return getToken(CSlangParser.RBRASE, 0); }
		public List<StatementsContext> statements() {
			return getRuleContexts(StatementsContext.class);
		}
		public StatementsContext statements(int i) {
			return getRuleContext(StatementsContext.class,i);
		}
		public Block_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_state; }
	}

	public final Block_stateContext block_state() throws RecognitionException {
		Block_stateContext _localctx = new Block_stateContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_block_state);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(477);
			match(LBRASE);
			setState(481);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 11)) & ~0x3f) == 0 && ((1L << (_la - 11)) & 142074511679527031L) != 0)) {
				{
				{
				setState(478);
				statements();
				}
				}
				setState(483);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(484);
			match(RBRASE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LhsContext extends ParserRuleContext {
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Id_accessContext id_access() {
			return getRuleContext(Id_accessContext.class,0);
		}
		public LhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs; }
	}

	public final LhsContext lhs() throws RecognitionException {
		LhsContext _localctx = new LhsContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_lhs);
		try {
			setState(488);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(486);
				index_op();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(487);
				id_access();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Index_opContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LBRACK() { return getToken(CSlangParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(CSlangParser.RBRACK, 0); }
		public Index_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_op; }
	}

	public final Index_opContext index_op() throws RecognitionException {
		Index_opContext _localctx = new Index_opContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_index_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(490);
			expr(0);
			setState(491);
			match(LBRACK);
			setState(492);
			expr(0);
			setState(493);
			match(RBRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Id_lstContext extends ParserRuleContext {
		public List<Id_accessContext> id_access() {
			return getRuleContexts(Id_accessContext.class);
		}
		public Id_accessContext id_access(int i) {
			return getRuleContext(Id_accessContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CSlangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSlangParser.COMMA, i);
		}
		public Id_lstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_lst; }
	}

	public final Id_lstContext id_lst() throws RecognitionException {
		Id_lstContext _localctx = new Id_lstContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_id_lst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(495);
			id_access();
			setState(500);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(496);
				match(COMMA);
				setState(497);
				id_access();
				}
				}
				setState(502);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Id_accessContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TerminalNode AT_ID() { return getToken(CSlangParser.AT_ID, 0); }
		public Id_accessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_access; }
	}

	public final Id_accessContext id_access() throws RecognitionException {
		Id_accessContext _localctx = new Id_accessContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_id_access);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(503);
			_la = _input.LA(1);
			if ( !(_la==AT_ID || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Io_stContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DOT() { return getToken(CSlangParser.DOT, 0); }
		public Io_mtContext io_mt() {
			return getRuleContext(Io_mtContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(CSlangParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CSlangParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(CSlangParser.SEMICOLON, 0); }
		public Io_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_io_st; }
	}

	public final Io_stContext io_st() throws RecognitionException {
		Io_stContext _localctx = new Io_stContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_io_st);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(505);
			expr(0);
			setState(506);
			match(DOT);
			setState(507);
			io_mt();
			setState(508);
			match(LPAREN);
			setState(510);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 16)) & ~0x3f) == 0 && ((1L << (_la - 16)) & 4439828489967747L) != 0)) {
				{
				setState(509);
				expr(0);
				}
			}

			setState(512);
			match(RPAREN);
			setState(513);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Io_mtContext extends ParserRuleContext {
		public Io_mtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_io_mt; }
	}

	public final Io_mtContext io_mt() throws RecognitionException {
		Io_mtContext _localctx = new Io_mtContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_io_mt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(515);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 510L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CSlangParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(CSlangParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(CSlangParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(CSlangParser.STRING, 0); }
		public TerminalNode VOID() { return getToken(CSlangParser.VOID, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public TypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typ; }
	}

	public final TypContext typ() throws RecognitionException {
		TypContext _localctx = new TypContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_typ);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(517);
			_la = _input.LA(1);
			if ( !(((((_la - 18)) & ~0x3f) == 0 && ((1L << (_la - 18)) & 70368744179727L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Attri_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CSlangParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(CSlangParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(CSlangParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(CSlangParser.STRING, 0); }
		public TerminalNode ID() { return getToken(CSlangParser.ID, 0); }
		public Attri_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attri_type; }
	}

	public final Attri_typeContext attri_type() throws RecognitionException {
		Attri_typeContext _localctx = new Attri_typeContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_attri_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(519);
			_la = _input.LA(1);
			if ( !(((((_la - 18)) & ~0x3f) == 0 && ((1L << (_la - 18)) & 70368744177679L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT_LITERAL() { return getToken(CSlangParser.INT_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(CSlangParser.FLOAT_LITERAL, 0); }
		public Bool_literalContext bool_literal() {
			return getRuleContext(Bool_literalContext.class,0);
		}
		public TerminalNode STRING_LITERAL() { return getToken(CSlangParser.STRING_LITERAL, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public TerminalNode NON_ZERO_INT() { return getToken(CSlangParser.NON_ZERO_INT, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_literal);
		try {
			setState(527);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(521);
				match(INT_LITERAL);
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(522);
				match(FLOAT_LITERAL);
				}
				break;
			case TRUE:
			case FALSE:
				enterOuterAlt(_localctx, 3);
				{
				setState(523);
				bool_literal();
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(524);
				match(STRING_LITERAL);
				}
				break;
			case LBRACK:
				enterOuterAlt(_localctx, 5);
				{
				setState(525);
				array();
				}
				break;
			case NON_ZERO_INT:
				enterOuterAlt(_localctx, 6);
				{
				setState(526);
				match(NON_ZERO_INT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Bool_literalContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(CSlangParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(CSlangParser.FALSE, 0); }
		public Bool_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_literal; }
	}

	public final Bool_literalContext bool_literal() throws RecognitionException {
		Bool_literalContext _localctx = new Bool_literalContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_bool_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(529);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(CSlangParser.LBRACK, 0); }
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public TerminalNode RBRACK() { return getToken(CSlangParser.RBRACK, 0); }
		public List<TerminalNode> COMMA() { return getTokens(CSlangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSlangParser.COMMA, i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(531);
			match(LBRACK);
			setState(532);
			literal();
			setState(537);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(533);
				match(COMMA);
				setState(534);
				literal();
				}
				}
				setState(539);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(540);
			match(RBRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 15:
			return relational_expr0_sempred((Relational_expr0Context)_localctx, predIndex);
		case 18:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 19:
			return expr1_sempred((Expr1Context)_localctx, predIndex);
		case 20:
			return expr2_sempred((Expr2Context)_localctx, predIndex);
		case 21:
			return expr3_sempred((Expr3Context)_localctx, predIndex);
		case 22:
			return expr4_sempred((Expr4Context)_localctx, predIndex);
		case 25:
			return expr7_sempred((Expr7Context)_localctx, predIndex);
		case 26:
			return expr8_sempred((Expr8Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean relational_expr0_sempred(Relational_expr0Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr1_sempred(Expr1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr2_sempred(Expr2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr3_sempred(Expr3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr4_sempred(Expr4Context _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr7_sempred(Expr7Context _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr8_sempred(Expr8Context _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return precpred(_ctx, 3);
		case 8:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001G\u021f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u00071\u0002"+
		"2\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u00076\u0002"+
		"7\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0001\u0000\u0005\u0000"+
		"x\b\u0000\n\u0000\f\u0000{\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\u0082\b\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0005\u0001\u0087\b\u0001\n\u0001\f\u0001\u008a\t\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002\u0091"+
		"\b\u0002\u0001\u0003\u0004\u0003\u0094\b\u0003\u000b\u0003\f\u0003\u0095"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0005\u0006\u00ab\b\u0006\n\u0006\f\u0006\u00ae\t\u0006\u0001"+
		"\u0006\u0003\u0006\u00b1\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0003\f\u00c1\b\f\u0001\r\u0001\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0005\u000f\u00ce\b\u000f\n\u000f\f\u000f\u00d1\t\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u00d9\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011"+
		"\u00de\b\u0011\n\u0011\f\u0011\u00e1\t\u0011\u0003\u0011\u00e3\b\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0005\u0012\u00eb\b\u0012\n\u0012\f\u0012\u00ee\t\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0005"+
		"\u0013\u00f7\b\u0013\n\u0013\f\u0013\u00fa\t\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0005\u0014"+
		"\u0103\b\u0014\n\u0014\f\u0014\u0106\t\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0005\u0015\u010f"+
		"\b\u0015\n\u0015\f\u0015\u0112\t\u0015\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u011b\b\u0016"+
		"\n\u0016\f\u0016\u011e\t\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0003\u0017\u0124\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0003"+
		"\u0018\u0129\b\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019\u0133\b\u0019\n"+
		"\u0019\f\u0019\u0136\t\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u0145\b\u001a\n"+
		"\u001a\f\u001a\u0148\t\u001a\u0001\u001b\u0001\u001b\u0003\u001b\u014c"+
		"\b\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u0151\b\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0003\u001b\u0159\b\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u0162\b\u001c\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0003\u001d\u016c\b\u001d\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e"+
		"\u0176\b\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001"+
		" \u0001 \u0001!\u0001!\u0003!\u0181\b!\u0001!\u0001!\u0001\"\u0001\"\u0001"+
		"\"\u0003\"\u0188\b\"\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$"+
		"\u0003$\u0191\b$\u0001%\u0001%\u0001%\u0001%\u0003%\u0197\b%\u0001%\u0001"+
		"%\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0003%\u01a2\b%\u0001"+
		"&\u0001&\u0001&\u0001&\u0001&\u0001\'\u0001\'\u0003\'\u01ab\b\'\u0001"+
		"\'\u0001\'\u0001\'\u0001\'\u0003\'\u01b1\b\'\u0001(\u0001(\u0001(\u0001"+
		"(\u0001(\u0001(\u0001(\u0001(\u0001)\u0001)\u0001)\u0001*\u0001*\u0001"+
		"*\u0001+\u0001+\u0001+\u0001+\u0001,\u0001,\u0001,\u0003,\u01c8\b,\u0001"+
		"-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001.\u0001"+
		".\u0003.\u01d5\b.\u0001.\u0001.\u0001.\u0001.\u0001.\u0001.\u0001.\u0001"+
		"/\u0001/\u0005/\u01e0\b/\n/\f/\u01e3\t/\u0001/\u0001/\u00010\u00010\u0003"+
		"0\u01e9\b0\u00011\u00011\u00011\u00011\u00011\u00012\u00012\u00012\u0005"+
		"2\u01f3\b2\n2\f2\u01f6\t2\u00013\u00013\u00014\u00014\u00014\u00014\u0001"+
		"4\u00034\u01ff\b4\u00014\u00014\u00014\u00015\u00015\u00016\u00016\u0001"+
		"7\u00017\u00018\u00018\u00018\u00018\u00018\u00018\u00038\u0210\b8\u0001"+
		"9\u00019\u0001:\u0001:\u0001:\u0001:\u0005:\u0218\b:\n:\f:\u021b\t:\u0001"+
		":\u0001:\u0001:\u0000\b\u001e$&(*,24;\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDF"+
		"HJLNPRTVXZ\\^`bdfhjlnprt\u0000\n\u0002\u0000>>@@\u0001\u0000.1\u0001\u0000"+
		",-\u0001\u0000\"#\u0001\u0000$%\u0001\u0000&)\u0001\u0000\u0001\b\u0003"+
		"\u0000\u0012\u0015\u001d\u001d@@\u0002\u0000\u0012\u0015@@\u0001\u0000"+
		"\u0010\u0011\u021f\u0000y\u0001\u0000\u0000\u0000\u0002~\u0001\u0000\u0000"+
		"\u0000\u0004\u0090\u0001\u0000\u0000\u0000\u0006\u0093\u0001\u0000\u0000"+
		"\u0000\b\u0097\u0001\u0000\u0000\u0000\n\u00a0\u0001\u0000\u0000\u0000"+
		"\f\u00b0\u0001\u0000\u0000\u0000\u000e\u00b2\u0001\u0000\u0000\u0000\u0010"+
		"\u00b6\u0001\u0000\u0000\u0000\u0012\u00b8\u0001\u0000\u0000\u0000\u0014"+
		"\u00ba\u0001\u0000\u0000\u0000\u0016\u00bc\u0001\u0000\u0000\u0000\u0018"+
		"\u00c0\u0001\u0000\u0000\u0000\u001a\u00c2\u0001\u0000\u0000\u0000\u001c"+
		"\u00c4\u0001\u0000\u0000\u0000\u001e\u00c6\u0001\u0000\u0000\u0000 \u00d8"+
		"\u0001\u0000\u0000\u0000\"\u00e2\u0001\u0000\u0000\u0000$\u00e4\u0001"+
		"\u0000\u0000\u0000&\u00ef\u0001\u0000\u0000\u0000(\u00fb\u0001\u0000\u0000"+
		"\u0000*\u0107\u0001\u0000\u0000\u0000,\u0113\u0001\u0000\u0000\u0000."+
		"\u0123\u0001\u0000\u0000\u00000\u0128\u0001\u0000\u0000\u00002\u012a\u0001"+
		"\u0000\u0000\u00004\u0137\u0001\u0000\u0000\u00006\u0158\u0001\u0000\u0000"+
		"\u00008\u0161\u0001\u0000\u0000\u0000:\u016b\u0001\u0000\u0000\u0000<"+
		"\u0175\u0001\u0000\u0000\u0000>\u0177\u0001\u0000\u0000\u0000@\u017a\u0001"+
		"\u0000\u0000\u0000B\u0180\u0001\u0000\u0000\u0000D\u0184\u0001\u0000\u0000"+
		"\u0000F\u0189\u0001\u0000\u0000\u0000H\u018c\u0001\u0000\u0000\u0000J"+
		"\u01a1\u0001\u0000\u0000\u0000L\u01a3\u0001\u0000\u0000\u0000N\u01a8\u0001"+
		"\u0000\u0000\u0000P\u01b2\u0001\u0000\u0000\u0000R\u01ba\u0001\u0000\u0000"+
		"\u0000T\u01bd\u0001\u0000\u0000\u0000V\u01c0\u0001\u0000\u0000\u0000X"+
		"\u01c7\u0001\u0000\u0000\u0000Z\u01c9\u0001\u0000\u0000\u0000\\\u01d4"+
		"\u0001\u0000\u0000\u0000^\u01dd\u0001\u0000\u0000\u0000`\u01e8\u0001\u0000"+
		"\u0000\u0000b\u01ea\u0001\u0000\u0000\u0000d\u01ef\u0001\u0000\u0000\u0000"+
		"f\u01f7\u0001\u0000\u0000\u0000h\u01f9\u0001\u0000\u0000\u0000j\u0203"+
		"\u0001\u0000\u0000\u0000l\u0205\u0001\u0000\u0000\u0000n\u0207\u0001\u0000"+
		"\u0000\u0000p\u020f\u0001\u0000\u0000\u0000r\u0211\u0001\u0000\u0000\u0000"+
		"t\u0213\u0001\u0000\u0000\u0000vx\u0003\u0002\u0001\u0000wv\u0001\u0000"+
		"\u0000\u0000x{\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000yz\u0001"+
		"\u0000\u0000\u0000z|\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000"+
		"|}\u0005\u0000\u0000\u0001}\u0001\u0001\u0000\u0000\u0000~\u0081\u0005"+
		"\u0018\u0000\u0000\u007f\u0080\u0005@\u0000\u0000\u0080\u0082\u00052\u0000"+
		"\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000"+
		"\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0084\u0005@\u0000\u0000"+
		"\u0084\u0088\u0005<\u0000\u0000\u0085\u0087\u0003\u0004\u0002\u0000\u0086"+
		"\u0085\u0001\u0000\u0000\u0000\u0087\u008a\u0001\u0000\u0000\u0000\u0088"+
		"\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089"+
		"\u008b\u0001\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008b"+
		"\u008c\u0005=\u0000\u0000\u008c\u0003\u0001\u0000\u0000\u0000\u008d\u0091"+
		"\u0003\u0006\u0003\u0000\u008e\u0091\u0003B!\u0000\u008f\u0091\u0003\n"+
		"\u0005\u0000\u0090\u008d\u0001\u0000\u0000\u0000\u0090\u008e\u0001\u0000"+
		"\u0000\u0000\u0090\u008f\u0001\u0000\u0000\u0000\u0091\u0005\u0001\u0000"+
		"\u0000\u0000\u0092\u0094\u0003\b\u0004\u0000\u0093\u0092\u0001\u0000\u0000"+
		"\u0000\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000"+
		"\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096\u0007\u0001\u0000\u0000"+
		"\u0000\u0097\u0098\u0005 \u0000\u0000\u0098\u0099\u0007\u0000\u0000\u0000"+
		"\u0099\u009a\u00059\u0000\u0000\u009a\u009b\u0003\f\u0006\u0000\u009b"+
		"\u009c\u00058\u0000\u0000\u009c\u009d\u00057\u0000\u0000\u009d\u009e\u0003"+
		"l6\u0000\u009e\u009f\u0003^/\u0000\u009f\t\u0001\u0000\u0000\u0000\u00a0"+
		"\u00a1\u0005 \u0000\u0000\u00a1\u00a2\u0005\u0019\u0000\u0000\u00a2\u00a3"+
		"\u00059\u0000\u0000\u00a3\u00a4\u0003\f\u0006\u0000\u00a4\u00a5\u0005"+
		"8\u0000\u0000\u00a5\u00a6\u0003^/\u0000\u00a6\u000b\u0001\u0000\u0000"+
		"\u0000\u00a7\u00ac\u0003\u000e\u0007\u0000\u00a8\u00a9\u00055\u0000\u0000"+
		"\u00a9\u00ab\u0003\u000e\u0007\u0000\u00aa\u00a8\u0001\u0000\u0000\u0000"+
		"\u00ab\u00ae\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00b1\u0001\u0000\u0000\u0000"+
		"\u00ae\u00ac\u0001\u0000\u0000\u0000\u00af\u00b1\u0001\u0000\u0000\u0000"+
		"\u00b0\u00a7\u0001\u0000\u0000\u0000\u00b0\u00af\u0001\u0000\u0000\u0000"+
		"\u00b1\r\u0001\u0000\u0000\u0000\u00b2\u00b3\u0003d2\u0000\u00b3\u00b4"+
		"\u00057\u0000\u0000\u00b4\u00b5\u0003l6\u0000\u00b5\u000f\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b7\u0007\u0001\u0000\u0000\u00b7\u0011\u0001\u0000"+
		"\u0000\u0000\u00b8\u00b9\u0007\u0002\u0000\u0000\u00b9\u0013\u0001\u0000"+
		"\u0000\u0000\u00ba\u00bb\u0007\u0003\u0000\u0000\u00bb\u0015\u0001\u0000"+
		"\u0000\u0000\u00bc\u00bd\u0005!\u0000\u0000\u00bd\u0017\u0001\u0000\u0000"+
		"\u0000\u00be\u00c1\u0003\u001a\r\u0000\u00bf\u00c1\u0003\u001c\u000e\u0000"+
		"\u00c0\u00be\u0001\u0000\u0000\u0000\u00c0\u00bf\u0001\u0000\u0000\u0000"+
		"\u00c1\u0019\u0001\u0000\u0000\u0000\u00c2\u00c3\u0007\u0004\u0000\u0000"+
		"\u00c3\u001b\u0001\u0000\u0000\u0000\u00c4\u00c5\u0007\u0005\u0000\u0000"+
		"\u00c5\u001d\u0001\u0000\u0000\u0000\u00c6\u00c7\u0006\u000f\uffff\uffff"+
		"\u0000\u00c7\u00c8\u0003 \u0010\u0000\u00c8\u00cf\u0001\u0000\u0000\u0000"+
		"\u00c9\u00ca\n\u0002\u0000\u0000\u00ca\u00cb\u0003\u0014\n\u0000\u00cb"+
		"\u00cc\u0003 \u0010\u0000\u00cc\u00ce\u0001\u0000\u0000\u0000\u00cd\u00c9"+
		"\u0001\u0000\u0000\u0000\u00ce\u00d1\u0001\u0000\u0000\u0000\u00cf\u00cd"+
		"\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000\u0000\u0000\u00d0\u001f"+
		"\u0001\u0000\u0000\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000\u00d2\u00d3"+
		"\u0003$\u0012\u0000\u00d3\u00d4\u0003\u0018\f\u0000\u00d4\u00d5\u0003"+
		"$\u0012\u0000\u00d5\u00d9\u0001\u0000\u0000\u0000\u00d6\u00d9\u0003r9"+
		"\u0000\u00d7\u00d9\u0005@\u0000\u0000\u00d8\u00d2\u0001\u0000\u0000\u0000"+
		"\u00d8\u00d6\u0001\u0000\u0000\u0000\u00d8\u00d7\u0001\u0000\u0000\u0000"+
		"\u00d9!\u0001\u0000\u0000\u0000\u00da\u00df\u0003$\u0012\u0000\u00db\u00dc"+
		"\u00055\u0000\u0000\u00dc\u00de\u0003\"\u0011\u0000\u00dd\u00db\u0001"+
		"\u0000\u0000\u0000\u00de\u00e1\u0001\u0000\u0000\u0000\u00df\u00dd\u0001"+
		"\u0000\u0000\u0000\u00df\u00e0\u0001\u0000\u0000\u0000\u00e0\u00e3\u0001"+
		"\u0000\u0000\u0000\u00e1\u00df\u0001\u0000\u0000\u0000\u00e2\u00da\u0001"+
		"\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000\u0000\u00e3#\u0001\u0000"+
		"\u0000\u0000\u00e4\u00e5\u0006\u0012\uffff\uffff\u0000\u00e5\u00e6\u0003"+
		"&\u0013\u0000\u00e6\u00ec\u0001\u0000\u0000\u0000\u00e7\u00e8\n\u0002"+
		"\u0000\u0000\u00e8\u00e9\u00053\u0000\u0000\u00e9\u00eb\u0003$\u0012\u0003"+
		"\u00ea\u00e7\u0001\u0000\u0000\u0000\u00eb\u00ee\u0001\u0000\u0000\u0000"+
		"\u00ec\u00ea\u0001\u0000\u0000\u0000\u00ec\u00ed\u0001\u0000\u0000\u0000"+
		"\u00ed%\u0001\u0000\u0000\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ef"+
		"\u00f0\u0006\u0013\uffff\uffff\u0000\u00f0\u00f1\u0003(\u0014\u0000\u00f1"+
		"\u00f8\u0001\u0000\u0000\u0000\u00f2\u00f3\n\u0002\u0000\u0000\u00f3\u00f4"+
		"\u0003\u0018\f\u0000\u00f4\u00f5\u0003&\u0013\u0003\u00f5\u00f7\u0001"+
		"\u0000\u0000\u0000\u00f6\u00f2\u0001\u0000\u0000\u0000\u00f7\u00fa\u0001"+
		"\u0000\u0000\u0000\u00f8\u00f6\u0001\u0000\u0000\u0000\u00f8\u00f9\u0001"+
		"\u0000\u0000\u0000\u00f9\'\u0001\u0000\u0000\u0000\u00fa\u00f8\u0001\u0000"+
		"\u0000\u0000\u00fb\u00fc\u0006\u0014\uffff\uffff\u0000\u00fc\u00fd\u0003"+
		"*\u0015\u0000\u00fd\u0104\u0001\u0000\u0000\u0000\u00fe\u00ff\n\u0002"+
		"\u0000\u0000\u00ff\u0100\u0003\u0014\n\u0000\u0100\u0101\u0003*\u0015"+
		"\u0000\u0101\u0103\u0001\u0000\u0000\u0000\u0102\u00fe\u0001\u0000\u0000"+
		"\u0000\u0103\u0106\u0001\u0000\u0000\u0000\u0104\u0102\u0001\u0000\u0000"+
		"\u0000\u0104\u0105\u0001\u0000\u0000\u0000\u0105)\u0001\u0000\u0000\u0000"+
		"\u0106\u0104\u0001\u0000\u0000\u0000\u0107\u0108\u0006\u0015\uffff\uffff"+
		"\u0000\u0108\u0109\u0003,\u0016\u0000\u0109\u0110\u0001\u0000\u0000\u0000"+
		"\u010a\u010b\n\u0002\u0000\u0000\u010b\u010c\u0003\u0012\t\u0000\u010c"+
		"\u010d\u0003,\u0016\u0000\u010d\u010f\u0001\u0000\u0000\u0000\u010e\u010a"+
		"\u0001\u0000\u0000\u0000\u010f\u0112\u0001\u0000\u0000\u0000\u0110\u010e"+
		"\u0001\u0000\u0000\u0000\u0110\u0111\u0001\u0000\u0000\u0000\u0111+\u0001"+
		"\u0000\u0000\u0000\u0112\u0110\u0001\u0000\u0000\u0000\u0113\u0114\u0006"+
		"\u0016\uffff\uffff\u0000\u0114\u0115\u0003.\u0017\u0000\u0115\u011c\u0001"+
		"\u0000\u0000\u0000\u0116\u0117\n\u0002\u0000\u0000\u0117\u0118\u0003\u0010"+
		"\b\u0000\u0118\u0119\u0003.\u0017\u0000\u0119\u011b\u0001\u0000\u0000"+
		"\u0000\u011a\u0116\u0001\u0000\u0000\u0000\u011b\u011e\u0001\u0000\u0000"+
		"\u0000\u011c\u011a\u0001\u0000\u0000\u0000\u011c\u011d\u0001\u0000\u0000"+
		"\u0000\u011d-\u0001\u0000\u0000\u0000\u011e\u011c\u0001\u0000\u0000\u0000"+
		"\u011f\u0120\u0003\u0016\u000b\u0000\u0120\u0121\u00030\u0018\u0000\u0121"+
		"\u0124\u0001\u0000\u0000\u0000\u0122\u0124\u00030\u0018\u0000\u0123\u011f"+
		"\u0001\u0000\u0000\u0000\u0123\u0122\u0001\u0000\u0000\u0000\u0124/\u0001"+
		"\u0000\u0000\u0000\u0125\u0126\u0005-\u0000\u0000\u0126\u0129\u00030\u0018"+
		"\u0000\u0127\u0129\u00032\u0019\u0000\u0128\u0125\u0001\u0000\u0000\u0000"+
		"\u0128\u0127\u0001\u0000\u0000\u0000\u01291\u0001\u0000\u0000\u0000\u012a"+
		"\u012b\u0006\u0019\uffff\uffff\u0000\u012b\u012c\u00034\u001a\u0000\u012c"+
		"\u0134\u0001\u0000\u0000\u0000\u012d\u012e\n\u0002\u0000\u0000\u012e\u012f"+
		"\u0005:\u0000\u0000\u012f\u0130\u00032\u0019\u0000\u0130\u0131\u0005;"+
		"\u0000\u0000\u0131\u0133\u0001\u0000\u0000\u0000\u0132\u012d\u0001\u0000"+
		"\u0000\u0000\u0133\u0136\u0001\u0000\u0000\u0000\u0134\u0132\u0001\u0000"+
		"\u0000\u0000\u0134\u0135\u0001\u0000\u0000\u0000\u01353\u0001\u0000\u0000"+
		"\u0000\u0136\u0134\u0001\u0000\u0000\u0000\u0137\u0138\u0006\u001a\uffff"+
		"\uffff\u0000\u0138\u0139\u00036\u001b\u0000\u0139\u0146\u0001\u0000\u0000"+
		"\u0000\u013a\u013b\n\u0003\u0000\u0000\u013b\u013c\u00054\u0000\u0000"+
		"\u013c\u0145\u0005@\u0000\u0000\u013d\u013e\n\u0002\u0000\u0000\u013e"+
		"\u013f\u00054\u0000\u0000\u013f\u0140\u0005@\u0000\u0000\u0140\u0141\u0005"+
		"9\u0000\u0000\u0141\u0142\u0003\"\u0011\u0000\u0142\u0143\u00058\u0000"+
		"\u0000\u0143\u0145\u0001\u0000\u0000\u0000\u0144\u013a\u0001\u0000\u0000"+
		"\u0000\u0144\u013d\u0001\u0000\u0000\u0000\u0145\u0148\u0001\u0000\u0000"+
		"\u0000\u0146\u0144\u0001\u0000\u0000\u0000\u0146\u0147\u0001\u0000\u0000"+
		"\u0000\u01475\u0001\u0000\u0000\u0000\u0148\u0146\u0001\u0000\u0000\u0000"+
		"\u0149\u014a\u0005@\u0000\u0000\u014a\u014c\u00054\u0000\u0000\u014b\u0149"+
		"\u0001\u0000\u0000\u0000\u014b\u014c\u0001\u0000\u0000\u0000\u014c\u014d"+
		"\u0001\u0000\u0000\u0000\u014d\u0159\u0005>\u0000\u0000\u014e\u014f\u0005"+
		"@\u0000\u0000\u014f\u0151\u00054\u0000\u0000\u0150\u014e\u0001\u0000\u0000"+
		"\u0000\u0150\u0151\u0001\u0000\u0000\u0000\u0151\u0152\u0001\u0000\u0000"+
		"\u0000\u0152\u0153\u0005>\u0000\u0000\u0153\u0154\u00059\u0000\u0000\u0154"+
		"\u0155\u0003\"\u0011\u0000\u0155\u0156\u00058\u0000\u0000\u0156\u0159"+
		"\u0001\u0000\u0000\u0000\u0157\u0159\u00038\u001c\u0000\u0158\u014b\u0001"+
		"\u0000\u0000\u0000\u0158\u0150\u0001\u0000\u0000\u0000\u0158\u0157\u0001"+
		"\u0000\u0000\u0000\u01597\u0001\u0000\u0000\u0000\u015a\u015b\u0005\u001c"+
		"\u0000\u0000\u015b\u015c\u0005@\u0000\u0000\u015c\u015d\u00059\u0000\u0000"+
		"\u015d\u015e\u0003\"\u0011\u0000\u015e\u015f\u00058\u0000\u0000\u015f"+
		"\u0162\u0001\u0000\u0000\u0000\u0160\u0162\u0003:\u001d\u0000\u0161\u015a"+
		"\u0001\u0000\u0000\u0000\u0161\u0160\u0001\u0000\u0000\u0000\u01629\u0001"+
		"\u0000\u0000\u0000\u0163\u0164\u00059\u0000\u0000\u0164\u0165\u0003$\u0012"+
		"\u0000\u0165\u0166\u00058\u0000\u0000\u0166\u016c\u0001\u0000\u0000\u0000"+
		"\u0167\u016c\u0003p8\u0000\u0168\u016c\u0005\u001b\u0000\u0000\u0169\u016c"+
		"\u0005@\u0000\u0000\u016a\u016c\u0005\u0017\u0000\u0000\u016b\u0163\u0001"+
		"\u0000\u0000\u0000\u016b\u0167\u0001\u0000\u0000\u0000\u016b\u0168\u0001"+
		"\u0000\u0000\u0000\u016b\u0169\u0001\u0000\u0000\u0000\u016b\u016a\u0001"+
		"\u0000\u0000\u0000\u016c;\u0001\u0000\u0000\u0000\u016d\u0176\u0003B!"+
		"\u0000\u016e\u0176\u0003>\u001f\u0000\u016f\u0176\u0003N\'\u0000\u0170"+
		"\u0176\u0003P(\u0000\u0171\u0176\u0003R)\u0000\u0172\u0176\u0003T*\u0000"+
		"\u0173\u0176\u0003V+\u0000\u0174\u0176\u0003X,\u0000\u0175\u016d\u0001"+
		"\u0000\u0000\u0000\u0175\u016e\u0001\u0000\u0000\u0000\u0175\u016f\u0001"+
		"\u0000\u0000\u0000\u0175\u0170\u0001\u0000\u0000\u0000\u0175\u0171\u0001"+
		"\u0000\u0000\u0000\u0175\u0172\u0001\u0000\u0000\u0000\u0175\u0173\u0001"+
		"\u0000\u0000\u0000\u0175\u0174\u0001\u0000\u0000\u0000\u0176=\u0001\u0000"+
		"\u0000\u0000\u0177\u0178\u0003@ \u0000\u0178\u0179\u00056\u0000\u0000"+
		"\u0179?\u0001\u0000\u0000\u0000\u017a\u017b\u0003`0\u0000\u017b\u017c"+
		"\u0005+\u0000\u0000\u017c\u017d\u0003$\u0012\u0000\u017dA\u0001\u0000"+
		"\u0000\u0000\u017e\u0181\u0003D\"\u0000\u017f\u0181\u0003F#\u0000\u0180"+
		"\u017e\u0001\u0000\u0000\u0000\u0180\u017f\u0001\u0000\u0000\u0000\u0181"+
		"\u0182\u0001\u0000\u0000\u0000\u0182\u0183\u00056\u0000\u0000\u0183C\u0001"+
		"\u0000\u0000\u0000\u0184\u0187\u0005\u001a\u0000\u0000\u0185\u0188\u0003"+
		"H$\u0000\u0186\u0188\u0003J%\u0000\u0187\u0185\u0001\u0000\u0000\u0000"+
		"\u0187\u0186\u0001\u0000\u0000\u0000\u0188E\u0001\u0000\u0000\u0000\u0189"+
		"\u018a\u0005\u001e\u0000\u0000\u018a\u018b\u0003J%\u0000\u018bG\u0001"+
		"\u0000\u0000\u0000\u018c\u018d\u0003d2\u0000\u018d\u0190\u00057\u0000"+
		"\u0000\u018e\u0191\u0003n7\u0000\u018f\u0191\u0003L&\u0000\u0190\u018e"+
		"\u0001\u0000\u0000\u0000\u0190\u018f\u0001\u0000\u0000\u0000\u0191I\u0001"+
		"\u0000\u0000\u0000\u0192\u0193\u0003f3\u0000\u0193\u0196\u00057\u0000"+
		"\u0000\u0194\u0197\u0003n7\u0000\u0195\u0197\u0003L&\u0000\u0196\u0194"+
		"\u0001\u0000\u0000\u0000\u0196\u0195\u0001\u0000\u0000\u0000\u0197\u0198"+
		"\u0001\u0000\u0000\u0000\u0198\u0199\u0005*\u0000\u0000\u0199\u019a\u0003"+
		"$\u0012\u0000\u019a\u01a2\u0001\u0000\u0000\u0000\u019b\u019c\u0003f3"+
		"\u0000\u019c\u019d\u00055\u0000\u0000\u019d\u019e\u0003J%\u0000\u019e"+
		"\u019f\u00055\u0000\u0000\u019f\u01a0\u0003$\u0012\u0000\u01a0\u01a2\u0001"+
		"\u0000\u0000\u0000\u01a1\u0192\u0001\u0000\u0000\u0000\u01a1\u019b\u0001"+
		"\u0000\u0000\u0000\u01a2K\u0001\u0000\u0000\u0000\u01a3\u01a4\u0005:\u0000"+
		"\u0000\u01a4\u01a5\u0005B\u0000\u0000\u01a5\u01a6\u0005;\u0000\u0000\u01a6"+
		"\u01a7\u0003n7\u0000\u01a7M\u0001\u0000\u0000\u0000\u01a8\u01aa\u0005"+
		"\r\u0000\u0000\u01a9\u01ab\u0003^/\u0000\u01aa\u01a9\u0001\u0000\u0000"+
		"\u0000\u01aa\u01ab\u0001\u0000\u0000\u0000\u01ab\u01ac\u0001\u0000\u0000"+
		"\u0000\u01ac\u01ad\u0003$\u0012\u0000\u01ad\u01b0\u0003^/\u0000\u01ae"+
		"\u01af\u0005\u000e\u0000\u0000\u01af\u01b1\u0003^/\u0000\u01b0\u01ae\u0001"+
		"\u0000\u0000\u0000\u01b0\u01b1\u0001\u0000\u0000\u0000\u01b1O\u0001\u0000"+
		"\u0000\u0000\u01b2\u01b3\u0005\u000f\u0000\u0000\u01b3\u01b4\u0003@ \u0000"+
		"\u01b4\u01b5\u00056\u0000\u0000\u01b5\u01b6\u0003\u001e\u000f\u0000\u01b6"+
		"\u01b7\u00056\u0000\u0000\u01b7\u01b8\u0003@ \u0000\u01b8\u01b9\u0003"+
		"^/\u0000\u01b9Q\u0001\u0000\u0000\u0000\u01ba\u01bb\u0005\u000b\u0000"+
		"\u0000\u01bb\u01bc\u00056\u0000\u0000\u01bcS\u0001\u0000\u0000\u0000\u01bd"+
		"\u01be\u0005\f\u0000\u0000\u01be\u01bf\u00056\u0000\u0000\u01bfU\u0001"+
		"\u0000\u0000\u0000\u01c0\u01c1\u0005\u0016\u0000\u0000\u01c1\u01c2\u0003"+
		"$\u0012\u0000\u01c2\u01c3\u00056\u0000\u0000\u01c3W\u0001\u0000\u0000"+
		"\u0000\u01c4\u01c8\u0003Z-\u0000\u01c5\u01c8\u0003\\.\u0000\u01c6\u01c8"+
		"\u0003h4\u0000\u01c7\u01c4\u0001\u0000\u0000\u0000\u01c7\u01c5\u0001\u0000"+
		"\u0000\u0000\u01c7\u01c6\u0001\u0000\u0000\u0000\u01c8Y\u0001\u0000\u0000"+
		"\u0000\u01c9\u01ca\u0003$\u0012\u0000\u01ca\u01cb\u00054\u0000\u0000\u01cb"+
		"\u01cc\u0005@\u0000\u0000\u01cc\u01cd\u00059\u0000\u0000\u01cd\u01ce\u0003"+
		"\"\u0011\u0000\u01ce\u01cf\u00058\u0000\u0000\u01cf\u01d0\u0001\u0000"+
		"\u0000\u0000\u01d0\u01d1\u00056\u0000\u0000\u01d1[\u0001\u0000\u0000\u0000"+
		"\u01d2\u01d3\u0005@\u0000\u0000\u01d3\u01d5\u00054\u0000\u0000\u01d4\u01d2"+
		"\u0001\u0000\u0000\u0000\u01d4\u01d5\u0001\u0000\u0000\u0000\u01d5\u01d6"+
		"\u0001\u0000\u0000\u0000\u01d6\u01d7\u0005>\u0000\u0000\u01d7\u01d8\u0005"+
		"9\u0000\u0000\u01d8\u01d9\u0003\"\u0011\u0000\u01d9\u01da\u00058\u0000"+
		"\u0000\u01da\u01db\u0001\u0000\u0000\u0000\u01db\u01dc\u00056\u0000\u0000"+
		"\u01dc]\u0001\u0000\u0000\u0000\u01dd\u01e1\u0005<\u0000\u0000\u01de\u01e0"+
		"\u0003<\u001e\u0000\u01df\u01de\u0001\u0000\u0000\u0000\u01e0\u01e3\u0001"+
		"\u0000\u0000\u0000\u01e1\u01df\u0001\u0000\u0000\u0000\u01e1\u01e2\u0001"+
		"\u0000\u0000\u0000\u01e2\u01e4\u0001\u0000\u0000\u0000\u01e3\u01e1\u0001"+
		"\u0000\u0000\u0000\u01e4\u01e5\u0005=\u0000\u0000\u01e5_\u0001\u0000\u0000"+
		"\u0000\u01e6\u01e9\u0003b1\u0000\u01e7\u01e9\u0003f3\u0000\u01e8\u01e6"+
		"\u0001\u0000\u0000\u0000\u01e8\u01e7\u0001\u0000\u0000\u0000\u01e9a\u0001"+
		"\u0000\u0000\u0000\u01ea\u01eb\u0003$\u0012\u0000\u01eb\u01ec\u0005:\u0000"+
		"\u0000\u01ec\u01ed\u0003$\u0012\u0000\u01ed\u01ee\u0005;\u0000\u0000\u01ee"+
		"c\u0001\u0000\u0000\u0000\u01ef\u01f4\u0003f3\u0000\u01f0\u01f1\u0005"+
		"5\u0000\u0000\u01f1\u01f3\u0003f3\u0000\u01f2\u01f0\u0001\u0000\u0000"+
		"\u0000\u01f3\u01f6\u0001\u0000\u0000\u0000\u01f4\u01f2\u0001\u0000\u0000"+
		"\u0000\u01f4\u01f5\u0001\u0000\u0000\u0000\u01f5e\u0001\u0000\u0000\u0000"+
		"\u01f6\u01f4\u0001\u0000\u0000\u0000\u01f7\u01f8\u0007\u0000\u0000\u0000"+
		"\u01f8g\u0001\u0000\u0000\u0000\u01f9\u01fa\u0003$\u0012\u0000\u01fa\u01fb"+
		"\u00054\u0000\u0000\u01fb\u01fc\u0003j5\u0000\u01fc\u01fe\u00059\u0000"+
		"\u0000\u01fd\u01ff\u0003$\u0012\u0000\u01fe\u01fd\u0001\u0000\u0000\u0000"+
		"\u01fe\u01ff\u0001\u0000\u0000\u0000\u01ff\u0200\u0001\u0000\u0000\u0000"+
		"\u0200\u0201\u00058\u0000\u0000\u0201\u0202\u00056\u0000\u0000\u0202i"+
		"\u0001\u0000\u0000\u0000\u0203\u0204\u0007\u0006\u0000\u0000\u0204k\u0001"+
		"\u0000\u0000\u0000\u0205\u0206\u0007\u0007\u0000\u0000\u0206m\u0001\u0000"+
		"\u0000\u0000\u0207\u0208\u0007\b\u0000\u0000\u0208o\u0001\u0000\u0000"+
		"\u0000\u0209\u0210\u0005C\u0000\u0000\u020a\u0210\u0005A\u0000\u0000\u020b"+
		"\u0210\u0003r9\u0000\u020c\u0210\u0005?\u0000\u0000\u020d\u0210\u0003"+
		"t:\u0000\u020e\u0210\u0005B\u0000\u0000\u020f\u0209\u0001\u0000\u0000"+
		"\u0000\u020f\u020a\u0001\u0000\u0000\u0000\u020f\u020b\u0001\u0000\u0000"+
		"\u0000\u020f\u020c\u0001\u0000\u0000\u0000\u020f\u020d\u0001\u0000\u0000"+
		"\u0000\u020f\u020e\u0001\u0000\u0000\u0000\u0210q\u0001\u0000\u0000\u0000"+
		"\u0211\u0212\u0007\t\u0000\u0000\u0212s\u0001\u0000\u0000\u0000\u0213"+
		"\u0214\u0005:\u0000\u0000\u0214\u0219\u0003p8\u0000\u0215\u0216\u0005"+
		"5\u0000\u0000\u0216\u0218\u0003p8\u0000\u0217\u0215\u0001\u0000\u0000"+
		"\u0000\u0218\u021b\u0001\u0000\u0000\u0000\u0219\u0217\u0001\u0000\u0000"+
		"\u0000\u0219\u021a\u0001\u0000\u0000\u0000\u021a\u021c\u0001\u0000\u0000"+
		"\u0000\u021b\u0219\u0001\u0000\u0000\u0000\u021c\u021d\u0005;\u0000\u0000"+
		"\u021du\u0001\u0000\u0000\u0000+y\u0081\u0088\u0090\u0095\u00ac\u00b0"+
		"\u00c0\u00cf\u00d8\u00df\u00e2\u00ec\u00f8\u0104\u0110\u011c\u0123\u0128"+
		"\u0134\u0144\u0146\u014b\u0150\u0158\u0161\u016b\u0175\u0180\u0187\u0190"+
		"\u0196\u01a1\u01aa\u01b0\u01c7\u01d4\u01e1\u01e8\u01f4\u01fe\u020f\u0219";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}