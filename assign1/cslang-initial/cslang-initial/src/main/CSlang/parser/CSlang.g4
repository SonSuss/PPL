// 2052688
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: ID+ EOF ;

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
/* Boolean type */
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';


PLUS: '+' ;
MINUS: '-' ;
MULTIPLY: '*' ;
DIVIDE_I: '\\' ;
DIVIDE_I_L: '%' ;
DIVIDE_F: '/';

STRING_CONCAT: '^';


/*	separator */
DOT: '.';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

/*LITERAL */
INTEGER_LITERAL: DIGIT+;
FLOAT_LITERAL: DIGIT+ (DECIMAL | EXPONENT | DECIMAL EXPONENT);
BOOL_LITERAL: TRUE | FALSE;
ID: (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)+;

fragment SIGN: PLUS | MINUS;
fragment DECIMAL: DOT DIGIT*;
fragment EXPONENT:  [Ee] SIGN DIGIT+;
fragment UNDERSCORE: '_';
fragment DIGIT:[0-9];
fragment LETTER: [a-zA-Z];


ERROR_CHAR: . {raise ErrorToken(self.text)} ;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;