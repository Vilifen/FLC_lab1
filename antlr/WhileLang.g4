grammar WhileLang;

program
    : whileStmt EOF
    ;

whileStmt
    : WHILE LPAR condition RPAR LBRACE body RBRACE SEMI?
    ;

condition
    : simpleExpr
    ;

simpleExpr
    : variable REL_OP value
    ;

value
    : variable
    | NUMBER
    ;

variable
    : ID
    ;

body
    : (incStmt)+
    ;

incStmt
    : ID INC_OP SEMI
    ;

WHILE   : 'while';
INC_OP  : '++' | '--';
REL_OP  : '<=' | '>=' | '==' | '!=' | '<' | '>';
LPAR    : '(';
RPAR    : ')';
LBRACE  : '{';
RBRACE  : '}';
SEMI    : ';';

ID      : '$' [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER  : [0-9]+ ;
WORD    : [a-zA-Z_][a-zA-Z0-9_]* ;

WS      : [ \t\r\n]+ -> skip ;
