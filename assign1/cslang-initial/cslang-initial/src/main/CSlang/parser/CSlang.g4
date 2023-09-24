// 2052688
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: gb* EOF ;


gb: class_lst | menthod_lst |statement_lst;

class_lst: class_dcl+;
class_dcl: CLASS ID (SUPER_CLASS ID)? class_body ;
class_body: LBRASE ( menthod_dcl | statement_lst)* RBRASE;


menthod_lst: menthod_dcl+;
menthod_dcl: FUNC ID LPAREN param_lst RPAREN COLON typ menthod_body ;
constructor_decl: FUNC CONSTRUCTOR LPAREN param_lst RPAREN menthod_body ;
menthod_body: LBRASE statement_lst* RBRASE;
param_lst: param (COMMA param)* | ;
param: idlist COLON typ ;


expr_lst: expr (COMMA expr_lst)* |;
expr: expr STRING_CONCAT expr | expr1;
expr1: expr1 relational expr1 | expr2 ;
expr2: expr2 logical_bin expr3 | expr3;
expr3: expr3 adding expr4 | expr4 ;
expr4: expr4 multiplying expr5 | expr5;
expr5: expr6 logical_not expr5 | expr6;
expr6: MINUS expr7 | expr7;
expr7: expr7 LBRACK expr_lst RBRACK | expr8;
expr8: expr8 DOT ID | expr9;
expr9: NEW ID expr_lst | expr10;
expr10: static_access|  index_op | LPAREN expr RPAREN | ARRAY | LITERAL | SELF;


multiplying: MULTIPLY| DIVIDE_F | DIVIDE_I | DIVIDE_I_L;
adding: PLUS | MINUS;
logical_bin: AND | OR ;
logical_not: NOT;
relational: relat_bool relat_int_float;
relat_bool:EQUAL | NOT_EQUAL;
relat_int_float: LESS|LESS_EQUAL|GREATER_EQUAL|GREATER ;


statement_lst: statements+ ;
statements: decl_state 
    | if_state 
    | for_state 
    | continue_state 
    | menthod_invo_state 
    | return_state 
    | break_state
    | io_st;
decl_state: fm? (assign | decl_typ | decl_array) ;
assign: assign_form SEMICOLON;
assign_form: lhs ASSIGN expr ;
decl_typ: lhs COLON typ ( INITIAL expr )? SEMICOLON;
decl_array: lhs COLON LBRACK INT RBRACK SEMICOLON;
if_state: IF block_state? expr if_block (ELSE if_block)? ;
for_state: FOR assign_form SEMICOLON expr SEMICOLON assign_form block_state;
break_state: BREAK SEMICOLON ;
continue_state: CONTINUE SEMICOLON ;
return_state: RETURN expr SEMICOLON ;
block_state: LPAREN statement_lst RPAREN ;
if_block: LBRASE statement_lst RBRASE;
menthod_invo_state: (expr DOT)? ID LPAREN expr_lst RPAREN SEMICOLON ; 
lhs:  idlist
    | access_lst
    ;
access_lst: access (COMMA access)*; 
access: instance_access 
    | static_access
    | instance_menthod_invo_access
    | 
;
static_access: (ID DOT)? ID ;
instance_access: expr DOT ID;
instance_menthod_invo_access: expr DOT ID LPAREN expr_lst RPAREN ;  
static_menthod_invo_access: (ID DOT)? ID LPAREN expr_lst RPAREN ;

idlist: identifier (COMMA identifier)*;
index_op: ID LBRACK expr RBRACK; //a[1]
identifier: ID | index_op ;


io_st: 'io.' io SEMICOLON;
io: '@readInt()'
    | '@writeInt' LPAREN expr RPAREN
    | '@readFloat()'
    | '@writeFloat'LPAREN expr RPAREN
    | '@readBool()'
    | '@writeBool'LPAREN  expr RPAREN
    | '@readString()'
    | '@writeString'LPAREN  expr RPAREN
;
fm: VAR | CONST;

/*TYPE */
boolean: NOT | AND | OR | EQUAL | NOT_EQUAL ;
typ: INT| FLOAT| BOOL |STRING | VOID;



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

LITERAL:  INT_LITERAL | FLOAT_LITERAL | BOOL_LITERAL |STRING_LITERAL ;
ID: '@'?[_a-zA-Z][_a-zA-Z0-9]*;
FLOAT_LITERAL: DIGIT+ (DECIMAL | EXPONENT | DECIMAL EXPONENT);
INT_LITERAL: DIGIT+;
BOOL_LITERAL: TRUE | FALSE;
STRING_LITERAL: '"' (ESC_SEQ | ~[\r\n"])* '"' {self.text=self.text[1:-1]};
ARRAY: LBRACK ' '* LITERAL ' '* (COMMA ' '* LITERAL ' '*)* RBRACK ;


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