lst = ['Apple', 'Pineapple' , 'Banana', 'Grapes']

print("Length Of List:" , len(lst))
print("First Element: " , lst[0])
print("Last Element: " , lst[-1])

lst.append('Papaya')
print("Updated List: " , lst)

lst.sort()
print("Updated Sorted List: " , lst)

lst.remove('Grapes')
print("Updated List: " , lst)

lst.reverse()
print("Updated Reversed List: " , lst)
