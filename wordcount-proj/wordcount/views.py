from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request , "home.html")

def aboutpage(request):
    return render(request, "about.html")

def counter(request):
    acttext = request.GET['acttext']
    textwords = acttext.split()
    wordcountdic = {}
    for a in textwords:
        if a in wordcountdic:
            wordcountdic[a] += 1
        else:
            wordcountdic[a] = 1
    
    
    print(wordcountdic)
    print(type(wordcountdic))    
    
    sortedwords = sorted(wordcountdic.items(), key=operator.itemgetter(1), reverse=True)
    
    print(type(sortedwords))
    print(sortedwords)
    # return render(request, "counter.html", {'acttext': acttext, 'wordcountdic':wordcountdic})
    return render(request, "counter.html", {'acttext': acttext, 'sortedwords':sortedwords})