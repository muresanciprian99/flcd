from copy import deepcopy
from Grammar import Grammar
from collections import defaultdict

class ParserLR:
    __startingProduction__ = 'S\'->.S'

    def __init__(self, grammar : Grammar):
        self.grammar = grammar
        __startingProduction__ = 'S\'->' + grammar.getStartSymbol()

    def goto(self, state, symbol):
        # determine from the input state which production element contains the input symbol
        result = []
        for production in state:
            lhsOfProduction, rhsOfProduction  = production.split('->')
            if rhsOfProduction.find('.' + symbol) == -1:
                continue
            # if we found a production that contains the input symbol right after a dot, we move the
            # dot after the symbol and return closure for new production
            rhsOfProduction = rhsOfProduction.replace('.' + symbol, symbol + '.')
            result.extend(self.closure(lhsOfProduction + '->' + rhsOfProduction))
        return result

    def closure(self, startingProduction):
        c = [startingProduction] # s'->.s
        collectionChanged = True
        while collectionChanged:
            collectionChanged = False
            for production in c:
                indexOfDot = production.find('.')
                if -1 < indexOfDot < len(production) - 1 and production[indexOfDot + 1] in self.grammar.getNonTerminals():
                    nonTerminal = production[indexOfDot + 1]
                    productionsOfNonTerminal = self.grammar.getProductionsForNonTerminal(nonTerminal)
                    for nonTerminalProduction in productionsOfNonTerminal:
                        if nonTerminal + '->.' + ''.join(nonTerminalProduction) not in c:
                            c.append(nonTerminal + '->.' + ''.join(nonTerminalProduction))
                            changed = True
        return c

    # uses the grammar given at initialization to determine the cannonical collection for it
    def canonicalCollection(self):
        collection = {}
        parsingSteps = defaultdict(list)
        stateNumber = 0
        s0 = self.closure(self.__startingProduction__)
        collection[stateNumber] = s0
        stateNumber += 1
        collectionChanged = True
        grammarSymbols = self.grammar.getNonTerminals() + self.grammar.getTerminals()
        while collectionChanged:
            collectionChanged = False
            currentStates = collection.copy()
            for startingStateNumber in currentStates.keys():
                state = currentStates[startingStateNumber]
                for symbol in grammarSymbols:
                    result = self.goto(state, symbol)
                    if result != []:
                        parsingSteps[startingStateNumber].append((symbol, stateNumber)) # 0 : S 1
                    if result != [] and result not in currentStates.values():
                        collection[stateNumber] = result
                        stateNumber += 1
                        collectionChanged = True
        return collection, parsingSteps

    def getGrammar(self):
        return self.grammar