// 2052688
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF ;

KEYWORDS: 'break' | 'continue' | 'if' | 'else' | 'for' | 'true' | 'false' | 'int' | 'float' | 'bool' | 'string' | 'return' | 'null' | 'class' | 'constructor' | 'var' | 'self' | 'new' | 'void' | 'const' | 'constant' | 'func';

ID: (LETTERS | '_') (LETTERS | DIGITS | '_')*;
DIGITS:[0-9]+;
LETTERS: [a-zA-Z]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)} ;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;