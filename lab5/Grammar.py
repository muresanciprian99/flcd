from collections import defaultdict

__separator__ = '~'
__filein__ = 'g1.txt'

class Grammar:
    
    def __init__(self, nonTerminals = None, terminals = None, startSymbol = None, productions = None):
        self.nonTerminals = nonTerminals
        self.terminals = terminals
        self.startSymbol = startSymbol
        self.productions = productions


    def readFromFile(self, file):
        with open(file, 'r') as fd:
            self.nonTerminals = fd.readline().strip('\n').split()
            self.terminals = fd.readline().strip('\n').split()
            self.startSymbol = fd.readline().strip('\n')
            self.productions = defaultdict(list)
            for line in fd:
                nonTerminal, production, *tail = line.strip('\n').split()
                self.productions[nonTerminal].append(production.split(__separator__))


    def getNonTerminals(self):
        return self.nonTerminals

    def getTerminals(self):
        return self.terminals

    def getProductions(self):
        return self.productions
    
    def getProductionsForNonTerminal(self, nonTerminal):
        return self.productions[nonTerminal]

    def getStartSymbol(self):
        return self.startSymbol


if __name__ == '__main__':
    grammar = Grammar()
    grammar.readFromFile(__filein__)
    print(grammar.getNonTerminals())
    print(grammar.getTerminals())
    print(grammar.getStartSymbol())
    print(grammar.getProductions())
    nonTerminal = input('Insert non-terminal to print the production of: ').strip()
    print(grammar.getProductionsForNonTerminal(nonTerminal))