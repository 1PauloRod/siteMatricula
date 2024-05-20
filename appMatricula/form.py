from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from .models import Escola, Endereco, CustomUser, Aluno
#from django.contrib.auth.models import User

class EscolaForm(forms.ModelForm):
    
    class Meta:
        model = Escola
        fields = ['nome', 'cnpj', 'telefone', 'dataFundacao']
        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Nome Escola', 'required': True}),  
            
            'dataFundacao': forms.TextInput(attrs={'id': 'mask-bday', 
                                          'placeholder': 'Data da Fundação'}),
        }
        
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if Escola.objects.filter(telefone=telefone).exists():
            #self.fields['telefone'].error_messages['unique'] = "Telefone já existe."
            raise forms.ValidationError("Telefone já existe.")

        if len(telefone) < 14:
            raise forms.ValidationError("Insira o telefone no formato válido.")
        return telefone
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if Escola.objects.filter(cnpj=cnpj).exists():
            raise forms.ValidationError("CNPJ já existe.")
        
        if len(cnpj) < 18:
            raise forms.ValidationError("Insira o CNPJ no formato válido")
        return cnpj
  
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['endereco', 'numero', 'bairro', 'cep', 'cidade', 'complemento']
        widgets = {
            'endereco':forms.TextInput(attrs={'placeholder':'Endereço', 'required': True}), 
            'numero':forms.TextInput(attrs={'placeholder':'Número', 'required': True}),
            'bairro':forms.TextInput(attrs={'placeholder':'Bairro', 'required': True}),
            'cidade':forms.TextInput(attrs={'placeholder':'Cidade', 'required': True}), 
            'complemento':forms.TextInput(attrs={'placeholder':'Complemento'})
        }
        
    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if len(cep) < 9:
            raise forms.ValidationError("Insira um CEP no formato válido.")

        return cep

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirmar Senha'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].error_messages['unique'] = "Email já cadastrado."
        self.fields['email'].error_messages['invalid'] = "Insira um email válido."
    
    class Meta:
        model = CustomUser
        fields = ['password', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Email', 'required': True}),
            'password': forms.PasswordInput(attrs={'placeholder':'Senha', 'required': True}) 
            }
        
    def clean_password(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        confirm_password = self.data.get('confirm_password')
    
        if len(password) < 6 or len(password) > 20:
            raise forms.ValidationError("Senha deve conter entre 7 e 19 caracteres.")
        
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Senha deve conter pelo menos um digito.")
        
        if not any(char.isalnum() for char in password):
            raise forms.ValidationError("Senha deve conter pelo menos uma letra.")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        
        password_validation.validate_password(password, self.instance)
        
        return password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        

class AlunoForm(forms.ModelForm):
    
    class Meta:
        
        model = Aluno
        fields = ['nome', 'sexo', 'aniversario', 'telefone', 'cpf', 'rg', 'orgao_emissor', 'email', 'mae', 'pai']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}), 
            'telefone': forms.TextInput(attrs={'id': 'mask-telefone', 
                                               'placeholder': 'telefone'}),
           
            #'aniversario': forms.DateInput(attrs={'type': 'date'}), se eu usar o DateInput na minha model
            'aniversario': forms.TextInput(attrs={'id': 'mask-bday', 
                                                  'placeholder': 'Aniversário'}), 
            'cpf': forms.TextInput(attrs={'id': 'mask-cpf', 
                                          'placeholder': 'CPF'}),
            'rg': forms.TextInput(attrs={'id': 'mask-rg', 
                                         'placeholder': 'Número RG'}),
            'orgao_emissor': forms.TextInput(attrs={'placeholder': 'Órgão Emissor'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email', 
                                             'required': False}),
            'mae': forms.TextInput(attrs={'placeholder': 'Nome mãe'}),
            'pai': forms.TextInput(attrs={'placeholder': 'Nome Pai', 
                                          'required': False}),
        }
