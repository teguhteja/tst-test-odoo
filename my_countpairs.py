# %%
def countPairs(array, total):
    list_count = []
    for a in array:
        b = total - a
        if not b in array :
            continue
            
        new_list = [min(a,b), max(a,b)]
        if new_list in list_count :
            continue
        
        list_count.append(new_list)
    return len(list_count)    

print(countPairs([1, 3, 2, 2, 3, 4], 5))

# %%
print(countPairs([1, 3, 2, 2, 3, 4], 5))
print(countPairs([1, 1, 1, 1], 2))
print(countPairs([1, 2, 3, 4, 5], 7))

# %%


# %%



