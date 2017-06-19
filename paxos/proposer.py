import math
import random

import mmh3


class Proposer:

    def __init__(self, acceptors):
        self.acceptors = acceptors


    def execute(self, value):
        choice = self.choose(value)
        responses = self.prepare(choice)
        # Majority accepted
        if len(responses) > (len(acceptors) / 2):
            self.propose(choice)

            
    def choose(self, key):
      highest_score, champion = -1, None
      for a in self.acceptors:
        score = a.compute_weighted_score(key)
        if score > highest_score:
          acceptor, highest_score = a, score
      return acceptor

  
    def prepare(self, choice):
        '''
        A proposer chooses a new proposal number n and sends a request to
        each member of some set of acceptors, asking it to respond with:
            (a) A promise never again to accept a proposal numbered less than n, and
            (b) The proposal with the highest number less than n that it has
        accepted, if any.

        example_response = {
            'promise': True,
            'previous_proposal': 41
            }

        '''
        responses = [a.prepare(choice) for a in acceptors]
        return [r for r in responses if r and r.is_accepted(choice.score)]


    def propose(self, chioce):
        '''
        example_proposal = {
            'number': 42,
            'value': 'SomeValue'
            }
        '''
        [a.accept(choice) for a in acceptors]



class Proposal:

    def __init__(self, value):
        self.value = value
        self.seed = random.randint(0, 100000)
        self.weight = random.randint(0, 100000)
        self.score = self._compute_score(self.value)

        
    def _compute_score(self, key):
        hash_1, hash_2 = mmh3.hash64(str(key), 0xFFFFFFFF & self.seed)
        hash_f = int_to_float(hash_2)
        score = 1.0 / -math.log(hash_f)
        return self.weight * score



class PrepareRequest:
    pass


class AcceptRequest:
    pass
    

def int_to_float(value):
  fifty_three_ones = (0xFFFFFFFFFFFFFFFF >> (64 - 53))
  fifty_three_zeros = float(1 << 53)
  return (value & fifty_three_ones) / fifty_three_zeros
