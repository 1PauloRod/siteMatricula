from django.urls import path
from .views import welcome, register_user, login_user, home, school_data, student_area, logout_user, register_student, search_student, edit_student, service, about_us, support, contact, delete_student
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', welcome, name="welcome"),
    path('servicos/', service, name="service"), 
    path('sobre_nos/', about_us, name="about_us"), 
    path('suporte/', support, name="support"),
    path('contato/', contact, name="contact_us"),
    path('cadastrar/', register_user, name="register"), 
    path('login/', login_user, name="login"), 
    path('principal/', home, name='home'), 
    path('dados_escola/', school_data, name="school_data"), 
    path('alunos/', student_area, name="students"), 
    path('alunos/cadastra_aluno', register_student, name="register_student"),
    path('alunos/busca_aluno', search_student, name="search_student"),
    path('edita_aluno/<int:student_id>/', edit_student, name="edit_student"),
    path('deleta_aluno/<int:student_id>/', delete_student, name="delete_student"),
    path('logout/', logout_user, name="logout")
]
