class ProblemState:
    def __init__(self):
        self.even_r0:int = 0
        self.even_r1:int = 0
        self.even_r2:int = 0
        
        self.odd_r0:int = 0
        self.odd_r1:int = 0
        self.odd_r2:int = 0
        
def sum(numbers:'list[int]') -> int:
    ret = 0
    for number in numbers:
        ret += number
    return ret

def solution_divide_conquer_wrapper(array:'list[int]') -> int:
    return solution_divide_conquer(array).odd_r0

def solution_divide_conquer(array:'list[int]') -> ProblemState:
    ret:ProblemState = ProblemState()
    if len(array) == 0:
        return ret
    if len(array) == 1:
        remainder = array[0] % 3
        if remainder == 0:
            ret.odd_r0 = 1
        elif remainder == 1:
            ret.odd_r1 = 1
        else:
            ret.odd_r2 = 1
        return ret
    split_point:int = len(array) // 2
    res_1:ProblemState = solution_divide_conquer(array[:split_point])
    res_2:ProblemState = solution_divide_conquer(array[split_point:])
    
    ret.even_r0 = sum([res_1.even_r0 + res_2.even_r0,
                        res_1.even_r0 * res_2.even_r0,
                          res_1.even_r1 * res_2.even_r2,
                          res_1.even_r2 * res_2.even_r1,
                          res_1.odd_r0 * res_2.odd_r0,
                          res_1.odd_r1 * res_2.odd_r2,
                          res_1.odd_r2 * res_2.odd_r1,
                         ])
    
    ret.odd_r0 = sum([res_1.odd_r0 +  res_2.odd_r0,
                      res_1.even_r0 * res_2.odd_r0,
                      res_1.even_r1 * res_2.odd_r2,
                      res_1.even_r2 * res_2.odd_r1,
                      res_1.odd_r0 * res_2.even_r0,
                      res_1.odd_r1 * res_2.even_r2,
                      res_1.odd_r2 * res_2.even_r1
    ])
    
    ret.even_r1 = sum([res_1.even_r1 +  res_2.even_r1,
                       res_1.even_r0 * res_2.even_r1,
                       res_1.even_r1 * res_2.even_r0,
                       res_1.even_r2 * res_2.even_r2,
                       res_1.odd_r0 * res_2.odd_r1,
                       res_1.odd_r1 * res_2.odd_r0,
                       res_1.odd_r2 * res_2.odd_r2
                         ])
    
    ret.odd_r1 = sum([res_1.odd_r1 + res_2.odd_r1,
                        res_1.even_r0 * res_2.odd_r1,
                       res_1.even_r1 * res_2.odd_r0,
                       res_1.even_r2 * res_2.odd_r2,
                       res_1.odd_r0 * res_2.even_r1,
                       res_1.odd_r1 * res_2.even_r0,
                       res_1.odd_r2 * res_2.even_r2
    ])
    
    ret.even_r2 = sum([res_1.even_r2 + res_2.even_r2,
                        res_1.even_r0 * res_2.even_r2,
                       res_1.even_r1 * res_2.even_r1,
                       res_1.even_r2 * res_2.even_r0,
                       res_1.odd_r0 * res_2.odd_r2,
                       res_1.odd_r1 * res_2.odd_r1,
                       res_1.odd_r2 * res_2.odd_r0
                         ])
    
    ret.odd_r2 = sum([res_1.odd_r2 + res_2.odd_r2,
                        res_1.even_r0 * res_2.odd_r2,
                       res_1.even_r1 * res_2.odd_r1,
                       res_1.even_r2 * res_2.odd_r0,
                       res_1.odd_r0 * res_2.even_r2,
                       res_1.odd_r1 * res_2.even_r1,
                       res_1.odd_r2 * res_2.even_r0
    ])
    
    return ret
    

def solution(array:'list[int]') -> int:
    state:ProblemState = ProblemState()
    while len(array) != 0:
        elem = array.pop() # get one element from array
        remainder = elem % 3
        # size of all sets *= 2 + 1(from the number alone)
        new_odd_r0:int = 0
        new_even_r0:int = 0 
        new_odd_r1:int =0 
        new_even_r1:int =0 
        new_odd_r2:int = 0 
        new_even_r2:int = 0
        if remainder == 0:
            new_odd_r0 = state.odd_r0 + state.even_r0 + 1
            new_even_r0 = state.even_r0 + state.odd_r0
            new_odd_r1 = state.odd_r1 + state.even_r1
            new_even_r1 = state.even_r1 + state.odd_r1
            new_odd_r2 = state.odd_r2 + state.even_r2
            new_even_r2 = state.even_r2 + state.odd_r2
        elif remainder == 1:
            new_odd_r0 = state.odd_r0 + state.even_r2
            new_even_r0 = state.even_r0 + state.odd_r2
            new_odd_r1 = state.odd_r1 + state.even_r0 + 1
            new_even_r1 = state.even_r1 + state.odd_r0
            new_odd_r2 = state.odd_r2 + state.even_r1
            new_even_r2 = state.even_r2 + state.odd_r1
        elif remainder == 2:
            new_odd_r0 = state.odd_r0 + state.even_r1
            new_even_r0 = state.even_r0 + state.odd_r1
            new_odd_r1 = state.odd_r1 + state.even_r2
            new_even_r1 = state.even_r1 + state.odd_r2
            new_odd_r2 = state.odd_r2 + state.even_r0 + 1
            new_even_r2 = state.even_r2 + state.odd_r0
        state.odd_r0 = new_odd_r0
        state.even_r0 = new_even_r0
        state.odd_r1 = new_odd_r1
        state.even_r1 = new_even_r1
        state.odd_r2 = new_odd_r2
        state.even_r2 = new_even_r2
    
    return state.odd_r0
            
            
        
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
    
    return count
    
def one_test(input:'list[int]', solutionFunc, referenceFunc) -> bool:
    from copy import deepcopy
    solution_res = solutionFunc(deepcopy(input))
    reference_res = referenceFunc(deepcopy(input))
    result_string =  "success" if solution_res == reference_res else "failed"
    print("solution {}  on {}. Expected: {}, actual: {}".format(result_string, input, reference_res, solution_res))
    return solution_res == reference_res

def run_tests():
    from random import randint
    for i in range(5): # do 5 tests
        input = []
        for j in range(randint(0, 10)): # each tests contains in between 0 -30 elements
            num = randint(0, 1000) # each number can be between 0 - 1000:
            if num not in input:
                input.append(num)
       # print("testing {}".format(input))

        one_test(input=input,  solutionFunc=solution_divide_conquer_wrapper, referenceFunc=solution)

            
run_tests()