from Grammar import Grammar
from ParserLR import ParserLR
from ParserOutput import ParserOutput


__filein__ = 'g1.txt'

if __name__ == '__main__':
    grammar = Grammar()
    grammar.readFromFile(__filein__)
    parserLR = ParserLR(grammar)
    # print(grammar.getNonTerminals())
    # print(grammar.getTerminals())
    # print(grammar.getStartSymbol())
    # print(grammar.getProductions())
    # nonTerminal = input('Insert non-terminal to print the production of: ').strip()
    # print(grammar.getProductionsForNonTerminal(nonTerminal))
    # print(parserLR.closure('S\'->.S'))
    # s0 = parserLR.closure('S\'->.S')
    # print(s0)
    # print(parserLR.goto(s0, 'a'))
    # print(parserLR.goto(['C->aA.'], 'a'))
    for key, value in parserLR.canonicalCollection()[0].items():
        print('s' + str(key), value)
    # parserOutput = ParserOutput(parserLR)
    # parserOutput.buildParsingTable()