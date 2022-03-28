my = ["a", 8, 19, "p", {1,2,3}]
for element in my:
    if type(element) == int:
        print("Element is numberic", element)
    elif  type(element) == str:
        print("Element is string", element)
    else:
        print("Element is something else", element)