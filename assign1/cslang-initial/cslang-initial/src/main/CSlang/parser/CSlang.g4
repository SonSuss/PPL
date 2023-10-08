// 2052688
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: class_lst* EOF ;



class_lst: class_dcl+;
class_dcl: CLASS (ID SUPER_CLASS)? ID LBRASE class_body* RBRASE;
class_body:  (method_lst|attribute_decl|constructor_decl);

method_lst: method_dcl+;
method_dcl: FUNC (ID|AT_ID) LPAREN param_lst RPAREN COLON typ block_state ;
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

relational_expr:expr (relational|logical_bin) expr | bool_literal | ID;

expr_lst: expr (COMMA expr_lst)*;
expr: expr STRING_CONCAT expr | expr1;
expr1: expr1 relational expr1 | expr2 ;
expr2: expr2 logical_bin expr3 | expr3;
expr3: expr3 adding expr4 | expr4 ;
expr4: expr4 multiplying expr5 | expr5;
expr5: logical_not expr6 | expr6;
expr6: MINUS expr6 | expr7;
expr7: expr7 LBRACK expr7 RBRACK | expr8;
expr8: expr8 DOT ID | expr8 DOT ID (LPAREN expr_lst? RPAREN) |  expr9;
expr9: (ID DOT)? AT_ID | (ID DOT)? AT_ID (LPAREN expr_lst? RPAREN) | expr10; 
expr10: NEW ID (LPAREN expr_lst? RPAREN) | expr11;
expr11: LPAREN expr RPAREN | literal | SELF | ID | NULL ;

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
attribute_assign:  lhs ASSIGN expr  ;

attribute_decl: fm ( attribute_init_nom | attribute_init_typ ) SEMICOLON ;
attribute_init_nom:  id_access COMMA attribute_init_nom COMMA expr | id_access COLON array_element_typ? attri_type INITIAL expr ;
attribute_init_typ:  id_lst COLON array_element_typ? attri_type;
array_element_typ: LBRACK NON_ZERO_INT RBRACK;


if_state: IF block_state? relational_expr block_state (ELSE block_state)? ;
for_state: FOR attribute_assign SEMICOLON relational_expr SEMICOLON attribute_assign block_state;
break_state: BREAK SEMICOLON ;
continue_state: CONTINUE SEMICOLON ;
return_state: RETURN expr SEMICOLON ;
instance_method_invo_access: expr8 SEMICOLON;  
static_method_invo_access: expr9 SEMICOLON;
block_state: LBRASE statements* RBRASE ;


lhs:  index_op | id_access;
index_op: expr LBRACK expr RBRACK ;
id_lst:id_access (COMMA id_access)* ;
id_access: ID |AT_ID;

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
typ: INT| FLOAT| BOOL |STRING | VOID | ID | ARRAY;
attri_type:INT| FLOAT| BOOL |STRING  | ID | ARRAY;



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
literal:  INT_LITERAL | FLOAT_LITERAL | bool_literal |STRING_LITERAL | array |NON_ZERO_INT ;
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