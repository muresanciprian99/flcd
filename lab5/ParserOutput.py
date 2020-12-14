from ParserLR import ParserLR
from collections import defaultdict

class ParserOutput:

    def __init__(self, parserLR):
        self.parserLR = parserLR

    def buildParsingTable(self):
        cannonicalCollection, parsingSteps = self.parserLR.canonicalCollection()
        print(parsingSteps)
        totalSymbols = self.parserLR.getGrammar().getTerminals() + self.parserLR.getGrammar().getNonTerminals()
        stepsForSymbol = {}
        rowsAction = [''] * len(cannonicalCollection)
        for symbol in totalSymbols:
            stepsForSymbol[symbol] = [-1 * len(cannonicalCollection)]
        for stateNumber in cannonicalCollection.keys():
            if len(cannonicalCollection[stateNumber]) == 1:
                production = cannonicalCollection[stateNumber][0]
                if production == 'S\'->' + self.parserLR.getGrammar().getStartSymbol() + '.':
                    rowsAction[stateNumber] = 'Acceptance'
                if self.parserLR.getGrammar().findProductionWithDot(production) != -1:
                    rowsAction[stateNumber] = 'Reduce ' + str(self.parserLR.getGrammar().findProductionWithDot(production))
            for symbol in totalSymbols:
                newState = self.parserLR.goto(cannonicalCollection[stateNumber], symbol)
                if len(newState) != 0:
                    keys = [*cannonicalCollection]
                    values = [*cannonicalCollection.values()]
                    newStateNumber = keys[values.index(newState)]
                    stepsForSymbol[symbol][stateNumber] = newStateNumber
                





