grammar Skyline;

root: expr EOF;

expr: exprovar | creaoskyline;

variable: VAR ':=' crea | VAR ':=' skylineope; 

exprovar: VAR ':=' creaoskyline
        | VAR ':=' VAR;

creaoskyline: crea | skylineope;

crea: simple | compost | aleatori;

skylineope: '(' skylineope ')' + (operator skylineope)?
        | '-' skyline
        | skyline '*' skylineope
        | skyline '*' NUM + (operator skylineope)?
        | skyline '+' skylineope 
        | skyline '+' NUM + (operator skylineope)?
        | skyline '-' NUM + (operator skylineope)?
        | skyline;
    
operator: '*' | '+' ;
        
skyline: VAR | crea;

simple: '(' NUM ',' NUM ',' NUM ')';
compost: '[' simple+ (',' simple)* ']';
aleatori: '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}';




NUM:[0-9]+;


VAR : ([a-z] | [A-Z]) + ([a-z] | [A-Z] | [0-9])*;



WS : [ \t\r\n]+ -> skip;