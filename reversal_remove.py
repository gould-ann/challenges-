def reverse_remove(input):
    a = []
    for i in input:
        if i not in a:
            a.append(i)
    for count in range(len(a)-1, -1, -1):
        a.append(a.pop(count))
        print a
reverse_remove(input("reverse and remove duplicate entries: "))
