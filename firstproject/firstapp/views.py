from django.shortcuts import render
from django.http import HttpResponse

students = ['이태성', '김한길', '김명건', '양준']
# Create your views here.
def home(request):
    chat = 'hi'
    name = '이태성'
    
    # context = ['이태성', '김한길', '김명건', '양준']
    return render(request, 'home.html', {'mychat':chat, 'myname':name})

def signup(request):
    return render(request, 'signup.html')

def signin(request):

    return render(request, 'signin.html')

def result(request):
    name = request.POST['username']

    if name in students:
        is_exist = True
    else:
        is_exist = False


    return render(request, 'result.html', {'user_name':name, 'is_exist':is_exist})


def textlen(request):
    text = request.POST['usertext']
    count = len(text)
    # text_split = text.split()
    # count = len(text_split)
    # count = []
    # for i in text_split:
    #     count += len(i)

    return render(request, 'textlen.html', {'textcount':count})
