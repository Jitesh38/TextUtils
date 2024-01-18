puntuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result="" 
 
def remove(djtext):
    result="" 
    for i in djtext:
        if i not in puntuation:
             result+=i
    return result
def upcase(djtext):
    return djtext.upper()

def newlnrmv(djtext):
    result="" 
    for char in djtext:
        if char != "\n" and char != "\r":
            result+=char
    return result

def charcount(djtext):
    count=0
    for i in djtext:
        count+=1
    return count

import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

def capfirst(djtext):
    return c.hump(djtext)