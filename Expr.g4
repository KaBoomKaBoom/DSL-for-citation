grammar Expr;
program : 'main' NEWLINE block EOF; 
block : (var_decl | statement)+;
var_decl : type SPACE id NEWLINE | 'string[' decimal_literal ']' SPACE id NEWLINE;
type : 'int' | 'string';
statement :  (var_assign NEWLINE)+ | (expr NEWLINE)+ | for_expr|'break' ;
for_expr : 'for' SPACE id SPACE 'in' SPACE id ':' NEWLINE method_call+;
method_name : 'CiteAPA' | 'CiteMLA' | 'CiteCMS' | 'CiteCSE' | 'CiteISO' | 'CiteIEEE' | 'GenImage';
expr : literal |'print(' id ')' | id | (literal ',' literal)  ;
method_call : method_name '(' (literal | id) ',' SPACE ((literal | id) (',' SPACE)?)* ')';
var_assign: id SPACE assign_op SPACE literal |
            id SPACE assign_op SPACE '[' string_literal','SPACE? NEWLINE? (string_literal ','? SPACE? NEWLINE?)*  ']' | 
            id SPACE assign_op SPACE math_expr;
math_expr: '"' ( (id SPACE)? math_symbol SPACE? ('{'*(id SPACE?| literal SPACE?)('}' SPACE)*)*)* '"';
math_symbol: 'sqrt' | 'frac' | 'pi' | 'int' | 'vec' | 'sum' | 'sin' | 'cos' | 'tan' | 'cot' | 'Delta' | '+' | '-' | '*' | '=';  
operation :  assign_op;
assign_op : '=' | '+=';
literal : int_literal | string_literal;
id : CHAR char_num*;
char_num : CHAR | DIGIT;
int_literal : decimal_literal;
decimal_literal : DIGIT DIGIT*;
string_literal : '"'((CHAR | ':' | '/' | '-') SPACE?)*'"';
CHAR : [a-zA-Z]+;
DIGIT : [0-9]+;
NEWLINE : [\r\n]+ ;
SPACE : ' ' ;
