## Q2


### Algorithm

Problem: for input string `s`, if it satisfies the "prefix" property.

Sub-problem: for input string`s[i:]`, for an arbitrary `i`, whether `s[i:]` satisfies the prefix property.

Recurrence Relation:  
For input `s`, for all i within range 1 to l, if  `s[:i]` satisfies the "prefix" property for any `i`, we only need to know if `s[i:]` satisfies the property as well, and if so, the whole string satisfies the property.

Subproblem Ordering:   
Every subproblem comes from a problem that has a few more characters in front like a tree.

Code:
```python
S:str, symbol_to_bit:dict
bit_to_symbol:dict = symbol_to_bit.reverse_key_value() # now bit_to_symbol is a mapping from bit strings to symbols

# populate DP array
dp = [[False for j in range(l)] for i in range(len(S))] # each element specifies whether S[i:i+j] satisfies the prefix property
for i in range(len(S)):
    for j in range(l):
        # check if S[i:i+j] can be matched
        substr:str = S[i:i+j]
        if substr in bit_to_symbol: # can be matched
            # iterate over all mappings and check if substr can be made of other bits, continue if substr can be made of other bits(violating prefix property)
            if substr_can_be_made_of_other_bits:
                # this substr can be made of other shorter bits
                dp[i][j] = False
                # in addition, go back on the dp table to set substrs that can make up to this substr to false; they have been set to true in previous iterations with lower i and j values to interpret substrings.
                continue
            ...
            dp[i][j] = True

# perform backtracking DFS on the dp matrix that traverses nodes with `true` values as specified above, starting from dp[0][0], for dp[i][j], if it's true, go to dp[j][k] for k in range(l)
        
```

### Proof

The recurrent relation is valid because any interpretable and non-ambiguous substring has been already interpreted and will not affect later translation. By following the series of substrings we can get the final interpretation.

### Runtime
O(nkl), n and k for the double loop and l for the inner loop that checks whether the substr violates the prefix property.

### Space
`O(nl)` for the 2-dimensional dp table.