class FiniteAutomata:
    
    def __init__(self, states = None, alphabet = None, initialState = None,
    finalStates = None, transitions = None):
        self.states = states
        self.alphabet = alphabet
        self.initialState = initialState
        self.finalStates = finalStates
        self.transitions = transitions

    def initFromFile(self, inputFile):
        fd = open(inputFile, 'r')
        self.states = fd.readline().split()
        self.alphabet = fd.readline().split()
        self.initialState = fd.readline().strip()
        self.finalStates = fd.readline().split()
        self.transitions = []
        for line in fd.read().split('\n'):
            parsedLine = line.split(' ')
            self.transitions.append([(parsedLine[0], parsedLine[1]), parsedLine[2]]) 

    def getStates(self):
        return self.states

    def getInitialState(self):
        return self.initialState

    def getFinalStates(self):
        return self.finalStates

    def getTransitions(self):
        return self.transitions
    
    def getAlphabet(self):
        return self.alphabet

    def isValidSequence(self, sequence):
        currentState = self.initialState
        lenSeq = len(sequence)
        validSeq = False
        for seqElem in sequence:
            validSeq = False
            for transition in self.transitions:
                if currentState == transition[0][0] and transition[0][1] == seqElem:
                    validSeq = True
                    currentState = transition[1]
                    break
            if not validSeq:
                break
            else:
                lenSeq -= 1
        if currentState not in self.finalStates or lenSeq != 0:
            print('Check failed')
        else:
            print('Check success')
    
    
if __name__ == '__main__':
    
    finiteAutomata = FiniteAutomata()
    finiteAutomata.initFromFile('FA.in')
    while True:
        print('1. Display states')
        print('2. Display alphabet')
        print('3. Display initial state')
        print('4. Display final states')
        print('5. Display transitions')
        print('6. Verify sequence is valid')
        print('7. Exit')
        choice = input('Select number of choice ').strip()
        if choice == '1':
            print(finiteAutomata.getStates())
        elif choice == '2':
            print(finiteAutomata.getAlphabet())
        elif choice == '3':
            print(finiteAutomata.getInitialState())
        elif choice == '4':
            print(finiteAutomata.getFinalStates())
        elif choice == '5':
            for transition in finiteAutomata.getTransitions():
                print(transition)
        elif choice == '6':
            sequence = input('Sequence:').strip()
            finiteAutomata.isValidSequence(sequence)
        elif choice == '7':
            print('Goodbye!')
            exit(0)
        else:
            print('Unknown option')