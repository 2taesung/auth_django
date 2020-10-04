from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AiClass, Students

# Create your views here.

#auth
def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return redirect('home')



def home(request):
    class_object = AiClass.objects.all()
    # class_object = AiClass.objects.filter(class_num=2)
    # context = {'class_object':class_object}
    return render(request, 'home.html', {'class_object':class_object})


def detail(request, class_pk):
    
    Class_obj = AiClass.objects.get(pk=class_pk)
    Students_q = Students.objects.filter(class_num=class_pk)

    context = {'Class_obj':Class_obj, 'Students_q':Students_q, 'class_pk': class_pk}

    return render(request, 'detail.html', context)


def add(request, class_pk):

    if request.method == 'POST':
        Students.objects.create(
            class_num=class_pk,
            name=request.POST['name'],
            phon_num=request.POST['phon_num'],
            intro_text=request.POST['intro_text'],           
        )

        return redirect('detail', class_pk)

    # Class_obj = AiClass.objects.get(pk=class_pk)

    context = {
        'class_pk':class_pk
    }
    return render(request, 'add.html', context)

def deditt(request, students_pk):

    student = Students.objects.get(pk=students_pk)

    context = {
        'student':student
    }
    return render(request, 'edit.html', context)

def edit(request, students_pk):

    if request.method == "POST":
        target_student = Students.objects.filter(pk=students_pk)
        print(target_student)
    
        target_student.update(
            name=request.POST['name'],
            phon_num=request.POST['phon_num'],
            intro_text=request.POST['intro_text'],
        )

        return redirect('students_detail', students_pk)

    student = Students.objects.get(pk=students_pk)

    context = {
        'student':student
    }

    return render(request, 'edit.html', context)

def students_detail(request, students_pk):

    student_obj = Students.objects.get(pk=students_pk)
    
    context = {
        'student_obj':student_obj
    }


    return render(request, 'students_detail.html', context)
