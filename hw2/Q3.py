class ProblemState:
    def __init__(self):
        self.even_m3_r0:int = 0
        self.even_m3_r1:int = 0
        self.even_m3_r2:int = 0
        
        self.odd_m3_r0:int = 0
        self.odd_m3_r1:int = 0
        self.odd_m3_r2:int = 0
    
def solution(array:'list[int]') -> int:
    state:ProblemState = ProblemState()
    while len(array) != 0:
        elem = array.pop() # get one element from array
        remainder = elem % 3
        # size of all sets *= 2 + 1(from the number alone)
        new_odd_m3_r0:int = 0
        new_even_m3_r0:int = 0 
        new_odd_m3_r1:int =0 
        new_even_m3_r1:int =0 
        new_odd_m3_r2:int = 0 
        new_even_m3_r2:int = 0
        if remainder == 0:
            new_odd_m3_r0 = state.odd_m3_r0 + state.even_m3_r0 + 1
            new_even_m3_r0 = state.even_m3_r0 + state.odd_m3_r0
            new_odd_m3_r1 = state.odd_m3_r1 + state.even_m3_r1
            new_even_m3_r1 = state.even_m3_r1 + state.odd_m3_r1
            new_odd_m3_r2 = state.odd_m3_r2 + state.even_m3_r2
            new_even_m3_r2 = state.even_m3_r2 + state.odd_m3_r2
        elif remainder == 1:
            new_odd_m3_r0 = state.odd_m3_r0 + state.even_m3_r2
            new_even_m3_r0 = state.even_m3_r0 + state.odd_m3_r2
            new_odd_m3_r1 = state.odd_m3_r1 + state.even_m3_r0 + 1
            new_even_m3_r1 = state.even_m3_r1 + state.odd_m3_r0
            new_odd_m3_r2 = state.odd_m3_r2 + state.even_m3_r1
            new_even_m3_r2 = state.even_m3_r2 + state.odd_m3_r1
        elif remainder == 2:
            new_odd_m3_r0 = state.odd_m3_r0 + state.even_m3_r1
            new_even_m3_r0 = state.even_m3_r0 + state.odd_m3_r1
            new_odd_m3_r1 = state.odd_m3_r1 + state.even_m3_r2
            new_even_m3_r1 = state.even_m3_r1 + state.odd_m3_r2
            new_odd_m3_r2 = state.odd_m3_r2 + state.even_m3_r0 + 1
            new_even_m3_r2 = state.even_m3_r2 + state.odd_m3_r0
        state.odd_m3_r0 = new_odd_m3_r0
        state.even_m3_r0 = new_even_m3_r0
        state.odd_m3_r1 = new_odd_m3_r1
        state.even_m3_r1 = new_even_m3_r1
        state.odd_m3_r2 = new_odd_m3_r2
        state.even_m3_r2 = new_even_m3_r2
    
    return state.odd_m3_r0
            
            
        
from itertools  import combinations
def brute_force(A):
    n = len(A)
    count = 0
    res = []
    for k in range(1, n + 1, 2):  # Consider only odd-sized subsets
        for subset in combinations(A, k):
            if sum(subset) % 3 == 0:
                count += 1
                res.append(subset)
    
    print(res)
    return count
    
def one_test(input:'list[int]', solutionFunc, referenceFunc) -> bool:
    from copy import deepcopy
    solution_res = solutionFunc(deepcopy(input))
    reference_res = referenceFunc(deepcopy(input))
    return solution_res == reference_res

def run_tests():
    from random import randint
    for i in range(3): # do 3 tests
        input = []
        for j in range(randint(0, 10)): # each tests contains in between 0 -30 elements
            num = randint(0, 1000) # each number can be between 0 - 1000:
            if num not in input:
                input.append(num)
        print("testing {}".format(input))
        if not one_test(input=input,  solutionFunc=solution, referenceFunc=brute_force):
            print("test failed with input: {}".format(input))
            
run_tests()