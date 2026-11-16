set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_result = set1 |set2
print(" Union (set1|set2) :",union_result)

inter_result = set1 & set2
print(" intersection (set1&set2) :",inter_result)

diff_result = set1 - set2 
print(" difference (set1-set2) :",diff_result)

diff_sym_result = set1 ^ set2
print(" difference symetrique (set1^set2) :",diff_sym_result)