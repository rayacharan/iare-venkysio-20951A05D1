import time
r=time.time()
def reverse (string):
    if len(string) ==0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a= input("enter the string:")
print(reverse(a))
q=time.time()
print(q-r)
