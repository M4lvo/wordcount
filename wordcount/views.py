
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'blah':'ali.bhayani1@yahoo.com'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcount = len(wordlist)

    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'wordcount':wordcount,'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html',
                  {'abouttext':'Ali here. Just a word count app that counts the words in a given text'})