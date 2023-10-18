## Q5

### a  

For the 2 results of the cut each represented by a sliced(horizontally or vertically) version of A, the minimum number of cuts needed to separate 1 elements from 0.

### b

parent's minimum cut equals: 1 + for all possible ways to cut the paper, the minimum value of the sum of the cut children's required cut to achieve result. This is when we assume the parent contains non-homogeneous values.
base case: every element of the cut are of the same value(0/1), in this case we need 0 cut.

### c

Let the dp table be a 4-dimentional matrix with dimentions representing starting index of i, end index of i, start index of j, end index of j, respectively. The 4D table captures all possibilities of subsets of the grid. 

To build the base table, for all elements where `i_start` == `i_end` and `j_start` == `j_end`, fill in 0.

The above two populates subgrids that are only of size 1 and therefore guaranteed to be homogeneous, giving a cut cost of 0.

Then we can iteratively increase the delta between `i_start` and `i_end` and `j_start` and `j_end` by 1 for each iteration, as the iteration has the costs of cutting the sub-grids ready from previous iterations, inductively.

### d

O(m^2n^2) same as space complexity, because we perform calculation once for each element in the dp matrix.

### e

O(m^2n^2) for the dp matrix.