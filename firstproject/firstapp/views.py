from django.shortcuts import render
from django.http import HttpResponse
from .models import AiClass, Students

# Create your views here.
def home(request):
    class_object = AiClass.objects.all()
    # class_object = AiClass.objects.filter(class_num=2)
    # context = {'class_object':class_object}
    return render(request, 'home.html', {'class_object':class_object})

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

def detail(request, class_pk):
    # print(class_pk)

    Class_obj = AiClass.objects.get(pk=class_pk)
    Students_obj = Students.objects.filter(class_num=class_pk)

    context = {'Class_obj':Class_obj, 'Students_obj':Students_obj, 'class_pk': class_pk}

    return render(request, 'detail.html', context)

def add(request, class_pk):

    Class_obj = AiClass.objects.get(pk=class_pk)

    if request.method == 'POST':
        Studnets.objects.create(
            name=request.POST['name'],
            class_num=class_pk,
            phon_num=request.POST['phon_num'],
            intro_text=request.POST['intro_text'],
            
        )

        return redirect('detail', class_pk)

    context = {
        'Class_obj':Class_obj
    }
    return render(request, 'add.html', context)
