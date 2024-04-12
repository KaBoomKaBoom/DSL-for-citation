grammar Expr;
program : (method_decl)* 'start' NEWLINE block EOF; 
method_decl : 'def' id '('type id*')' ':' block 'return'* expr*;
block : var_decl*  statement*;
var_decl : type id NEWLINE| ('string[' decimal_literal ']' id) NEWLINE;
type : 'int' | 'string' | 'bool' | 'dict';
statement :  var_assign+ NEWLINE | expr+ NEWLINE | 'if' expr ':' NEWLINE expr+ NEWLINE ('else'* ':'* NEWLINE expr+NEWLINE)*  | 'for' expr 'in' expr ':'NEWLINE expr+ NEWLINE  |'break' ;
method_name : id | 'CiteAPA' | 'CiteMLA' | 'CiteCMS' | 'CiteCSE';
expr : method_call | literal |  (id operation literal) | 'print(' id ')' | id | (literal ',' literal) ;
method_call : method_name '(' expr ',' (expr ','?)* ')';
var_assign: type* id assign_op literal | type* id assign_op '[' string_literal',' (string_literal ','?)*  ']';   
operation : arithm_op | rel_op | eq_op | cond_op | assign_op;
arithm_op : '+' | '-' | '*' | '/';
rel_op : '<' | '>' | '<=' | '>=';
eq_op : '==' | '!=';
cond_op : 'and' | 'or';
assign_op : '=' | '+=';
literal : int_literal | bool_literal | string_literal;
id : CHAR char_num*;
char_num : CHAR | DIGIT;
int_literal : decimal_literal;
decimal_literal : DIGIT DIGIT*;
bool_literal : 'True' | 'False';
string_literal : '"'CHAR*'"';
dict : '{'literal ':' literal'}';
CHAR : [a-zA-Z]+;
DIGIT : [0-9]+;
NEWLINE : [\r\n]+ ;
SPACE : ' ' -> skip;
