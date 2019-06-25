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

    front = 'd'
    for end in text:
        if front != '.' and front != '!' and front != '?':
            if end == '.':
                sentence_cnt+=1
            elif end == '!':
                sentence_cnt+=1
            elif end == '?':
                sentence_cnt+=1
        front = end

    return render(request,'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items(), 'letter':len(text), 'sentence':sentence_cnt})
