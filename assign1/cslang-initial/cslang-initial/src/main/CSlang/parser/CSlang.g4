// 2052688
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: gb* EOF ;


gb: class_lst | method_lst | static_attribute_decl;

static_attribute_decl: CONST ( attribute_init_nom ) SEMICOLON ;

class_lst: class_dcl+;
class_dcl: CLASS (ID SUPER_CLASS)? ID class_body ;
class_body: LBRASE ( method_dcl | statements |constructor_decl)* RBRASE;

method_lst: method_dcl+;
method_dcl: FUNC ID LPAREN param_lst RPAREN COLON typ block_state ;
constructor_decl: FUNC CONSTRUCTOR LPAREN param_lst RPAREN block_state ;
param_lst: param (COMMA param)* | ;
param: id_lst COLON typ;


multiplying: MULTIPLY| DIVIDE_F | DIVIDE_I | DIVIDE_I_L;
adding: PLUS | MINUS;
logical_bin: AND | OR ;
logical_not: NOT;
relational: relat_bool | relat_int_float;
relat_bool:EQUAL | NOT_EQUAL;
relat_int_float: LESS | LESS_EQUAL|GREATER_EQUAL|GREATER ;

expr_lst: expr (COMMA expr_lst)* | ;
expr: expr STRING_CONCAT expr | expr1;
expr1: expr1 relational expr1 | expr2 ;
expr2: expr2 logical_bin expr3 | expr3;
expr3: expr3 adding expr4 | expr4 ;
expr4: expr4 multiplying expr5 | expr5;
expr5: expr6 logical_not expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: expr7 LBRACK expr7 RBRACK | expr8;
expr8: expr8 DOT expr9 | expr8 COMMA expr9 (LPAREN expr_lst RPAREN) |  expr9;
expr9: ID DOT ID | (ID DOT)? ID (LPAREN expr_lst RPAREN) | expr10; 
expr10: NEW ID (LPAREN expr_lst RPAREN) | expr11;
expr11: LPAREN expr RPAREN | literal | SELF | ID ;

statements: attribute_decl
    | assign_decl
    | if_state
    | for_state
    | break_state
    | continue_state
    | return_state  
    | instance_method_invo_access
    | static_method_invo_access
    | io_st;

assign_decl: attribute_assign SEMICOLON ;
attribute_assign:  (lhs COMMA attribute_assign COMMA expr | lhs ASSIGN expr  );

attribute_decl: fm ( attribute_init_nom | attribute_init_typ ) SEMICOLON ;
attribute_init_nom:  ID COMMA attribute_init_nom COMMA expr | ID COLON typ INITIAL expr ;
attribute_init_typ:  id_lst COLON array_element_typ? typ;
array_element_typ: LBRACK INT_LITERAL RBRACK;


if_state: IF block_state? expr block_state (ELSE block_state)? ;
for_state: FOR attribute_decl SEMICOLON expr SEMICOLON attribute_decl block_state;
break_state: BREAK SEMICOLON ;
continue_state: CONTINUE SEMICOLON ;
return_state: RETURN expr SEMICOLON ;
instance_method_invo_access: expr8 SEMICOLON;  
static_method_invo_access: expr9 SEMICOLON;
block_state: LBRASE statements* RBRASE ;

lhs: ID | index_op;
index_op: ID LBRACK expr RBRACK;
id_lst:ID (COMMA ID)* ;

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
typ: INT| FLOAT| BOOL |STRING | VOID | ID | ARRAY;



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
ARRAY:'array' ;

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
literal:  INT_LITERAL | FLOAT_LITERAL | BOOL_LITERAL |STRING_LITERAL | array ;
STRING_LITERAL: '"' (ESC_SEQ | ~[\r\n"])* '"' {self.text = self.text[1:-1]};
ID: '@'?[_a-zA-Z][_a-zA-Z0-9]* ;
FLOAT_LITERAL: DIGIT+ (DECIMAL | EXPONENT | DECIMAL EXPONENT);
INT_LITERAL: DIGIT+;    
BOOL_LITERAL: TRUE | FALSE;
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