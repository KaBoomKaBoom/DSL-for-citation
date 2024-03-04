grammar Expr;
program : (method_decl)* 'main' block; 
method_decl : 'def' id '('type id*')' ':' block 'return' *expr*;
block : var_decl* var_assign* statement*;
var_decl : type id | ('string[' decimal_literal ']' id)+;
type : 'int' | 'string' | 'bool' | 'dict';
statement : method_call | expr+ | 'if' expr ':' expr+ ('else'* ':'* expr+)*  | 'for' id 'in' expr ':' expr+  |'break'| expr+;
method_name : id;
expr : method_call | literal | var_assign | (id operation literal) | 'print(' id ')';
method_call : method_name '(' id ')';
var_assign: type* id assign_op literal;
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
NEWLINE : [\r\n]+ -> skip;
SPACE : ' ' -> skip;
