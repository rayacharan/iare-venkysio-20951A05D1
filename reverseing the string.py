def reverse (string):
    if len(string) ==0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a= input("enter the string:")
print(reverse(a))
