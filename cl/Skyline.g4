grammar Skyline;

root: expr EOF;

expr: exprovar | creaoskyline;

variable: VAR ':=' crea | VAR ':=' skylineope; 

exprovar: VAR ':=' VAR
        |VAR ':=' creaoskyline;
        

creaoskyline: crea | skylineope;

crea: simple | compost | aleatori;

skylineope: '(' skylineope ')' 
        | '-' skylineope
        | skylineope '*' skylineope
        | skylineope '*' NUM 
        | skylineope '+' skylineope 
        | skylineope '+' NUM 
        | skylineope '-' NUM 
        | skyline;
    

        
skyline: VAR | crea;

simple: '(' NUM ',' NUM ',' NUM ')';
compost: '[' simple+ (',' simple)* ']';
aleatori: '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}';


NUM:[0-9]+;

VAR : ([a-z] | [A-Z]) + ([a-z] | [A-Z] | [0-9])*;

WS : [ \t\r\n]+ -> skip;