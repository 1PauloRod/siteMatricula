from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        blank=True, 
        related_name='customuser_user_premissions'
    )
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_groups',
        related_query_name='user'
    )
    
    def __str__(self):
        return self.email

class Endereco(models.Model):
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.endereco}, {self.numero}, {self.bairro}, {self.cep}, {self.complemento}"

class Escola(models.Model):
    userEscola = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)
    telefone = models.CharField(max_length=14, unique=True, null=True)
    dataFundacao = models.CharField(max_length=10, null=True)
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.lower()
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.nome}"

class Aluno(models.Model):
    SEX_CHOICES = (
        ('M', 'Masculino'), 
        ('F', 'Feminino')
    )
    
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=7, unique=True, null=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES)
    aniversario = models.CharField(max_length=10, null=True)
    telefone = models.CharField(max_length=14, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=12, unique=True)
    orgao_emissor = models.CharField(max_length=10)
    email = models.CharField(max_length=100, blank=True, null=True)
    mae = models.CharField(max_length=100)
    pai = models.CharField(max_length=100, blank=True, null=True) 
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.nome}, {self.cpf}"
    


