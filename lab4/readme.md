Documentation for laboratory 4

Github url: https://github.com/muresanciprian99/flcd/tree/main/lab4

EBNF for FA.in  

File -> SetOfStates"\nElements\n"InitialState"\n"FinalStates"\n"{Transition"\n"}  
SetOfStates = State{" "State}  
State = Letter{Letter|Digit} 
Elements=Element{" "Element}  
InitialState = State  
FinalStates = State{" "State}  
Transition = State" "Element" "State  
Element=Digit{Digit}  
Letter = a | b | ... | z | A | B | ... | z  
Digit = 0 | 1 | ... | 9  
