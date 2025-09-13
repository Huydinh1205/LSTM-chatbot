print("hello conda")
lst=['a','b']
lst1=list(set(lst))
lst1.extend(['\t','\n'])
chars = sorted(lst1)
print(chars)