from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    sentence_cnt = 0

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    for dot in text:
        if dot == '.':
            sentence_cnt+=1

    return render(request,'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items(), 'letter':len(text), 'sentence':sentence_cnt})
