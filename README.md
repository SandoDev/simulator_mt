# Simulator MT

Basado en https://morphett.info/turing/turing.html

1. Genere un archivo input.txt con las quintuplas para simular la Maquina de Turing
2. corra el main.py

Syntax:
Each line should contain one tuple of the form '<current state> <current symbol> <new symbol> <direction> <new state>'.
You can use any number or word for <current state> and <new state>, eg. 10, a, state1. State labels are case-sensitive.
You can use almost any character for <current symbol> and <new symbol>, or '_' to represent blank (space). Symbols are case-sensitive.
You can't use ';', '*', '_' or whitespace as symbols.
<direction> should be 'l', 'r' or '*', denoting 'move left', 'move right' or 'do not move', respectively.
Anything after a ';' is a comment and is ignored.
The machine halts when it reaches any state starting with 'halt', eg. halt, halt-accept.

Also:
'*' can be used as a wildcard in <current symbol> or <current state> to match any character or state.
'*' can be used in <new symbol> or <new state> to mean 'no change'.
'!' can be used at the end of a line to set a breakpoint, eg '1 a b r 2 !'. The machine will automatically pause after executing this line.
You can specify the starting position for the head using '*' in the initial input.