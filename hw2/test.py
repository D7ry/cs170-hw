
def solution_recursive(arr1:list[int], arr2:list[int], k:int) -> int:
    if k == 1:
        return min(arr1[0] if arr1 else float('inf'), arr2[0] if arr2 else float('inf'))
    if not arr1:
        return arr2[k-1]
    if not arr2:
        return arr1[k-1]
    arr1_mid_point = len(arr1) // 2
    arr2_mid_point = len(arr2) // 2
    arr1_median:int = arr1[arr1_mid_point]
    arr2_median:int = arr2[arr2_mid_point]
    if arr1_median < arr2_median:
        return solution_recursive(arr1[arr1_mid_point+1:], arr2[:arr2_mid_point], k - (arr1_mid_point + 1))
    else:
        return solution_recursive(arr2[arr2_mid_point+1:], arr1[:arr1_mid_point], k - (arr2_mid_point + 1))

    
print(solution_recursive([1,3,5,7,9], [2,4,6,8,10], 5))

# def solution_checker(arr1, arr2, k):
#     arr3 = arr1 + arr2
#     arr3.sort()
#     return arr3[k - 1]

# print(solution_checker([1,3,5,7,9], [2,4,6,8,10], 5))