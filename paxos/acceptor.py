import math
import mmh3
import random



class Acceptor:
    '''
    Hash generated using Rendevous Hashing:
    
    http://www.eecs.umich.edu/techreports/cse/96/CSE-TR-316-96.pdf
    '''
    def __init__(self, name):
        self.name = name
        self.highest_proposal = None
        self.proposals = set()

    def prepare(self, request):
        '''
        There is then no reason for the acceptor to respond to the new prepare request,
        since it will not accept the proposal numbered n that the proposer wants to issue. So
        we have the acceptor ignore such a prepare request. We also have it ignore a prepare
        request for a proposal it has already accepted.
        '''
        self.proposals.add(request)
        
        if request.score > self.highest_proposal:
            self.highest = request.score
            
            return AcceptPrepare(request.score, True)

    
    def accept(self, request):
        '''
        An acceptor can accept a proposal numbered n iff it has not responded
        to a prepare request having a number greater than n.
        '''
        pass




class AcceptPrepare:

    def __init__(self, score, promise):
        self.promise = promise
        self.score = score


    def is_accepted(self, score):
        return self.promise and self.score == self.score


class AcceptProposal:
    pass
