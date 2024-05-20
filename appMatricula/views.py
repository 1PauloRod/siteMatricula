from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .form import EscolaForm, UserForm, EnderecoForm, AlunoForm
from .utils import generateRegisterNumberOfStudent
# Create your views here.

def welcome(request):
   return render(request, "pages/menuWelcome/welcome.html")

def service(request):
    return render(request, "pages/menuWelcome/service.html")

def about_us(request):
    return render(request, "pages/menuWelcome/about_us.html")

def support(request):
    return render(request, "pages/menuWelcome/support.html")

def contact(request):
    return render(request, "pages/menuWelcome/contact_us.html")
    
def register_user(request):
    if request.method == 'POST':
        escola = EscolaForm(request.POST)
        user_escola = UserForm(request.POST)
        endereco = EnderecoForm(request.POST)
        
        if escola.is_valid() and endereco.is_valid() and user_escola.is_valid():
            end = endereco.save()
            us = user_escola.save()
            esc = escola.save(commit=False)
            esc.endereco = end
            esc.userEscola = us
            esc.save()
            return redirect("login")   
        else:
            return render(request, "pages/register.html", {'escola_form': escola,
                                                       'user_form': user_escola, 
                                                       'endereco_form': endereco})
    else:
        escola_form = EscolaForm()
        user_form = UserForm()
        endereco_form = EnderecoForm()
        return render(request, "pages/register.html", {'escola_form': escola_form,
                                                       'user_form': user_form, 
                                                       'endereco_form': endereco_form})
           

        
def login_user(request):
    if request.method == "GET":
        return render(request, "pages/login.html")
    
    email = request.POST.get("email-escola")
    password = request.POST.get("senha-escola")
    
    user = authenticate(request, username=email, password=password)
    
    print(user)
    
    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        return redirect("login")
    
    
def logout_user(request):
    logout(request)
    return redirect('welcome')
    
    
@login_required(login_url="/login")
def home(request):
    return render(request, "pages/home.html")

@login_required(login_url="/login")
def school_data(request):
    userEmail = get_user(request)
    
    currentUser = CustomUser.objects.get(email=userEmail)
    escola = Escola.objects.get(userEscola=currentUser)
    
    
    return render(request, "pages/school_data.html", {"escola": escola})

@login_required(login_url="/login")
def student_area(request):
    
    userEscola = CustomUser.objects.get(email=get_user(request))
    escolaAluno = Escola.objects.get(userEscola=userEscola)
    alunos = Aluno.objects.filter(escola=escolaAluno)
        
    return render(request, "pages/student_area/student_area.html", {"alunos": alunos})

@login_required(login_url="/login")
def register_student(request):
    userEscolaEmail = get_user(request)
    currentUser = CustomUser.objects.get(email=userEscolaEmail)
    escola = Escola.objects.get(userEscola=currentUser)
    if request.method == "POST":
        alunoForm = AlunoForm(request.POST)
        alunoEnderecoForm = EnderecoForm(request.POST)
  
        if alunoForm.is_valid() and alunoEnderecoForm.is_valid():
            end = alunoEnderecoForm.save()
            al = alunoForm.save(commit=False)
            al.endereco = end
            al.escola = escola
            al.save()
            al.matricula = generateRegisterNumberOfStudent(al.id)
            al.save()
            return redirect("students")
        else:
            return render(request, "pages/student_area/register_student.html", {"alunoForm": alunoForm, 
                                                                                "alunoEnderecoForm": alunoEnderecoForm})
        
    else:
        aluno = AlunoForm()
        endereco = EnderecoForm()
        return render(request, "pages/student_area/register_student.html", {"alunoForm": aluno, 
                                                                            "alunoEnderecoForm": endereco})


@login_required(login_url="/login")
def search_student(request):
    query = request.GET.get('query')
    results = None
    if query:
        results = Aluno.objects.filter(matricula=query)
    
    return render(request, "pages/student_area/search_student.html", {"results": results})
    

@login_required(login_url="/login")
def edit_student(request, student_id):
    student = Aluno.objects.get(id=student_id)
    if request.method == "GET":
        return render(request, "pages/student_area/update_student.html", {"student": student})
    
    nomeAluno = request.POST.get("nome-aluno") 
    student.nome = nomeAluno
    student.save()
    return redirect("students")
    

    

     

        
    
    