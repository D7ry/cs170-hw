## Q3

### Algorithm

0. Initialize a solution map mapping all vertices to their ideal targets, initialize them as None.
1. Do a topological sort
2. starting from the right-most node(bottom-most)
3. For each vertex v, solution[v] = vertex that has the maximum value in : max(s[v], {s[u], s[solution[u]] for u in v.childs})

Subproblem: to calculate one vertex's childrens' maximum scores.

Recurrence: same algorithm applied to each parent.

Ordering: Child first, parent later so that children info can be used for parents.


### Runtime

Topoligical sort O(|V| + |E|) + iterating over each vertex O(|V|); O(|V| + |E|).