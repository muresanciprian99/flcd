from ParserLR import ParserLR

class ParserOutput:

    def __init__(self, parserLR : ParserLR):
        self.parserLR = parserLR

    def buildParsingTable(self):
        cannonicalCollection, parsingSteps = self.parserLR.canonicalCollection()
        symbolsGoToResults = {}
        totalSymbols = self.parserLR.getGrammar().getTerminals() + self.parserLR.getGrammar().getNonTerminals()
        rowActionName = [None * totalSymbols]
        for symbol in totalSymbols:
            symbolsGoToResults[symbol] = [None * len(cannonicalCollection)]
        for stateNumber in cannonicalCollection.keys():
            if parsingSteps[stateNumber] == []:
                # check acceptance or reduce for caonnonicalCollection[stateNumber]
                if (len(cannonicalCollection) == 1 and cannonicalCollection[stateNumber] == 'S\'->' + self.grammar.getStartSymbol + '.'): # equals S'->startingSymbol.
                    actionName = 'Acceptance'
                else if (self.parserLR.getGrammar(). )
            else for steps in parsingSteps[stateNumber]:
                symbolsGoToResults[steps[0]][stateNumber] = steps[1] 




