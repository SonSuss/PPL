// 2052688
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: class_dcl* EOF ;


class_dcl: CLASS (ID SUPER_CLASS)? ID LBRASE class_body* RBRASE;
class_body:  (method_dcl|constructor_decl|storedecl);

method_dcl: FUNC (ID|AT_ID) LPAREN param_lst RPAREN COLON (typ |VOID) block ;
constructor_decl: FUNC CONSTRUCTOR LPAREN param_lst RPAREN block ;
param_lst: param (COMMA param)* | idlst COLON typ |;
param: iden COLON typ;

statements: storedecl
    | assigndecl
    | ifstmt
    | forstmt
    | break_state
    | continue_state
    | return_state  
    | callstmt;

storedecl: (constdecl | vardecl) SEMICOLON;
constdecl:  CONST (non_inital_decl | inital_decl);
vardecl: VAR (non_inital_decl | inital_decl);
non_inital_decl: idlst COLON (typ|array_type);
inital_decl: iden COLON (typ|array_type) INITIAL expr | iden COMMA inital_decl COMMA expr;
assigndecl: assign SEMICOLON;
assign:lhs ASSIGN expr;
ifstmt: IF block? expr block (ELSE block)?;
forstmt: FOR assign SEMICOLON expr SEMICOLON assign block;
continue_state: CONTINUE SEMICOLON ;
return_state: RETURN expr SEMICOLON ;
break_state: BREAK SEMICOLON ;
callstmt: (instance_method_invo_access | static_method_invo_access | io_st) SEMICOLON;
instance_method_invo_access:  expr DOT ID (LPAREN expr_lst RPAREN)  ;  
static_method_invo_access:  (ID DOT)? AT_ID (LPAREN expr_lst RPAREN);
io_st: expr DOT io_mt ;
block: LBRASE statements* RBRASE ;

io_mt: '@readInt' LPAREN RPAREN
    | '@writeInt' LPAREN expr_lst RPAREN
    | '@readFloat' LPAREN RPAREN
    | '@writeFloat' LPAREN expr_lst RPAREN
    | '@readBool' LPAREN RPAREN
    | '@writeBool' LPAREN expr_lst RPAREN
    | '@readString' LPAREN RPAREN
    | '@writeString' LPAREN expr_lst RPAREN
;

lhs:  iden | arraycell | fieldaccess;
arraycell: expr8 LBRACK expr RBRACK ;
fieldaccess : expr8 DOT ID | (ID DOT)? AT_ID;
idlst : iden (COMMA iden)*;
iden :ID |AT_ID;


expr_lst : expr (COMMA expr)* | ;
expr: expr1 STRING_CONCAT expr1 | expr1 ; //string operator
expr1: expr2 relational expr2 | expr2 ; //relational operator
expr2: expr2 logical_bin expr3 | expr3; //logical_bin operator
expr3: expr3 adding expr4 | expr4 ; //additional operator
expr4: expr4 multiplying expr5 | expr5; //multiplication operator
expr5: logical_not expr5 | expr6; // logical not
expr6: MINUS expr6 | expr7; // MINUS operator
expr7: expr8 LBRACK expr RBRACK | expr8; // index operator
expr8: expr8 DOT ID (LPAREN expr_lst RPAREN)? |  expr9; //instance access operator
expr9: (ID DOT)? AT_ID (LPAREN expr_lst RPAREN)? | expr10; //static access operator
expr10: NEW ID LPAREN expr_lst RPAREN | expr11; //object creation operator
expr11: LPAREN expr RPAREN | literal | ID;



/*relational */
relational: relat_bool | relat_int_float;
relat_bool:EQUAL | NOT_EQUAL;
relat_int_float: LESS | LESS_EQUAL|GREATER_EQUAL|GREATER ;

multiplying: MULTIPLY| DIVIDE_F | DIVIDE_I | DIVIDE_I_L;
adding: PLUS | MINUS;
logical_bin: AND | OR ;
logical_not: NOT;

/*TYPE */
typ: INT| FLOAT| BOOL |STRING | ID ;
array_type:  LBRACK NON_ZERO_INT RBRACK typ ;



/* Comment */
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT : '//' ~[\r\n|EOF]* [\n\r] ->skip;


/* KEYWORDS */
BREAK: 'break';
CONTINUE: 'continue' ;
IF: 'if' ;
ELSE: 'else' ;
FOR: 'for' ;
TRUE: 'true' ;
FALSE: 'false' ;
INT: 'int' ;
FLOAT: 'float' ;
BOOL: 'bool' ;
STRING: 'string' ;
RETURN: 'return' ;
NULL: 'null' ;
CLASS: 'class' ;
CONSTRUCTOR: 'constructor' ;
VAR: 'var' ;
SELF: 'self' ;
NEW: 'new' ;
VOID: 'void' ;
CONST: 'const' ;
CONSTANT: 'constant' ;
FUNC: 'func';

/*  operaters */
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
INITIAL: '=';
ASSIGN: ':=';
PLUS: '+' ;
MINUS: '-' ;
MULTIPLY: '*' ;
DIVIDE_I: '\\' ;
DIVIDE_I_L: '%' ;
DIVIDE_F: '/';
SUPER_CLASS: '<-';
STRING_CONCAT: '^';


/*	separator */
DOT: '.';
COMMA: ',' ;
SEMICOLON: ';' ;
COLON: ':';
RPAREN: ')';
LPAREN: '(';
LBRACK: '[';
RBRACK: ']';
LBRASE: '{';
RBRASE: '}';


/*LITERAL */
literal:  INT_LITERAL | FLOAT_LITERAL | bool_literal |STRING_LITERAL | array |NON_ZERO_INT |NULL| SELF;
AT_ID:'@' ID;
STRING_LITERAL: '"' (ESC_SEQ | ~[\b\t\f\r\n"\\] )* '"' {self.text = self.text[1:-1]};
ID: [_a-zA-Z][_a-zA-Z0-9]* ;
FLOAT_LITERAL: DIGIT+ (DECIMAL | EXPONENT | DECIMAL EXPONENT);
NON_ZERO_INT: [1-9] [0-9]*;
INT_LITERAL: DIGIT+;    
bool_literal: TRUE | FALSE;
array: LBRACK  literal  (COMMA  literal )* RBRACK ;


fragment SIGN: PLUS | MINUS;
fragment DECIMAL: DOT DIGIT*;
fragment EXPONENT:  [Ee] SIGN? DIGIT+;
fragment DIGIT: [0-9];
fragment ESC_SEQ: '\\\\'| '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' ;
fragment ILL_ESQ: '\\' ~[bfrnt] | '\\' ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)} ;
UNCLOSE_STRING: '"' (ESC_SEQ | ~[\b\t\f\r\n"\\])* ([ \b\t\f\n\r] | EOF){
unclose_string= str(self.text);
whatif =['\b', '\t', '\f', '\n', '\r', '\\']
if unclose_string[-1] in whatif:
    raise UncloseString(unclose_string[1:-1])
else:
    raise UncloseString(unclose_string[1:])
};

ILLEGAL_ESCAPE:  '"' (ESC_SEQ | ~[\b\t\f\r\n"\\])* ILL_ESQ {
raise IllegalEscape(self.text[1:])
};