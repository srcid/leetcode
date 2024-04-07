from dataclasses import dataclass

@dataclass
class dfa:
    alphabet: str                         # set of symbols [Sigma]
    q_all: list[int]                      # set of all states [Q]
    q_initial: int                        # initial state [q_0]
    q_finals: list[int]                   # set of final states [F]
    transition: dict[tuple[int,str], int] # transition function [Delta] as dictionary
    
    def is_valid(self, word: str) -> bool:
        return all(map(lambda l: l in self.alphabet, word))

    def run(self, word: str) -> bool:
        if self.is_valid(word) is True:
            q = self.q_initial

            while word != "":
                q = self.transition[q, word[0]]
                word = word[1:] # remove first char

            return q in self.q_finals
       
        return False
    
automata = dfa(
    alphabet='ab',
    q_all=[0,1,2],
    q_initial=0,
    q_finals=[0,1],
    transition={
        (0,'a'): 0,
        (0,'b'): 1,
        (1,'a'): 2,
        (1,'b'): 1,
        (2,'a'): 2,
        (2,'b'): 2 
    }
)

s = input('word: ')

print(automata.run(s))