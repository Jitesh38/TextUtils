# I have created this file - jitesh
from django.http import HttpResponse
from django.shortcuts import render
from . import fun

# video 6
# def index(request):
#     return HttpResponse('''<a href="https://www.youtube.com/">youtube</a> <h1>Jitesh</h1>''')
# def about(request):
#     return HttpResponse(" about  hello")
# def w3school(request):
#     return HttpResponse('''<a href="https://www.w3schools.com/python/default.asp">w3school</a>''')


# # video 7
# def index(request):
#     return HttpResponse('''<a href="http://127.0.0.1:8000/removepunc">next</a>''')
# def removepunc(request):
#     return HttpResponse('''<a href="http://127.0.0.1:8000/">back</a> 
#                         <a href="http://127.0.0.1:8000/capfirst">next</a>''')
# def capfirst(request):
#     return HttpResponse("cap first")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spaceremove(request):
#     return HttpResponse("helloo")
# def charcount(request):
#     pass


# video 8
# def index(request):
#     return render(request,'index.html')
# def removepunc(request):
#     # get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     # analyaze the text
#     return HttpResponse()
# def capfirst(request):
#     return HttpResponse("cap first")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spaceremove(request):
#     return HttpResponse("helloo")
# def charcount(request):
#     pass


# video 10
def login(request):
    return render(request,'login.html')

def index(request):
    email=request.POST.get('email')
    pass1=request.POST.get('pass')
    print(email)
    print(pass1)
    return render(request,'index.html')

def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcapse=request.POST.get('fullcapse','off')
    newlineremove=request.POST.get('newlineremove','off')
    charcount=request.POST.get('charcount','off')
    capfirst=request.POST.get('capfirst','off')

    if removepunc == "on":
        analyzed=fun.remove(djtext)            
        params={'purpose': 'Removed punctuations','analyzed_text':analyzed}
        djtext=analyzed
    if fullcapse == "on":
        analyzed=fun.upcase(djtext)
        params={'purpose': 'Upper Case transformation','analyzed_text':analyzed}
        djtext=analyzed
    if newlineremove == "on":
        analyzed=fun.newlnrmv(djtext)
        params={'purpose': 'Remove New Line','analyzed_text':analyzed}
        djtext=analyzed
    if charcount == "on":
        analyzed=fun.charcount(djtext)
        params={'purpose': 'Character Count','analyzed_text':analyzed}
    if capfirst == "on":
        analyzed=fun.capfirst(djtext)
        params={'purpose': 'Camle case','analyzed_text':analyzed}
        djtext=analyzed
    if removepunc!="on" and fullcapse!="on" and newlineremove!="on" and charcount != "on" and capfirst != "on":
        return HttpResponse("ERROR")

    return render(request,'analyze.html',params)

