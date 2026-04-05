grammar WhileLoop;

program
    : (whileStatement)* EOF
    ;

whileStatement
    : 'while' '(' condition ')' '{' body '}' ';'
    ;

condition
    : comparison (logicalOp comparison)*
    ;

comparison
    : ID comparisonOp NUMBER
    ;

logicalOp
    : '||' | '&&'
    ;

comparisonOp
    : '<' | '>' | '==' | '>=' | '<=' | '!='
    ;

body
    : (instruction)*
    ;

instruction
    : ID ('++' | '--') ';'
    ;


ID     : '$' [a-zA-Z_] [a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ;
WS     : [ \t\r\n]+ -> skip ;

UNKNOWN : . ;