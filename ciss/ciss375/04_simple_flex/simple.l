%option noyywrap

%{
    #include <iostream>
    using namespace std;
%}

DIGIT   [0-9]
LETTER  [a-zA-Z]
WS      [ \n]

%%

"+"|"-"|"="     { cout << "operator: " << yytext << endl; }
{DIGIT}+        { cout << "  number: " << yytext << endl; }
{LETTER}+       { cout << "      id: " << yytext << endl; }
{WS}+           { }

%%

int main(int argc, char** argv)
{
    yyin = stdin;
    yylex();
    return 0;
}
