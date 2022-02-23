from cpf_field.models import CPFField
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
class  UserManager(BaseUserManager):

    def create_user(self,email,username=None,cpf=None,nome=None,data_nascimento=None, password=None):
        if not email:
            raise ValueError("O usuário precisa de um email")
        usuario = self.model(

            username=username,
            nome=nome,
            email=self.normalize_email(email),
            cpf=cpf,
            data_nascimento = data_nascimento,
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username,nome, email,cpf,data_nascimento,password=None):
        usuario = self.create_user(
            username=username,
            nome=nome,
            email=email,
            cpf=cpf,
            data_nascimento=data_nascimento
        )
        usuario.is_superuser = True
        usuario.is_staff=True
        usuario.set_password(password)
        usuario.save()
        return usuario


class User(AbstractBaseUser,PermissionsMixin):
    objects = UserManager()

    username = models.CharField('Usuário', max_length=50, unique=True)
    nome = models.CharField('Nome',max_length=100, null=True, blank=False)
    email = models.EmailField('E-mail',unique=True, null=False, blank=False)
    cpf = CPFField('CPF',max_length=11,unique=True,null=True,blank=False)
    telefone = models.CharField('Telefone',max_length=14, blank=False, null=False)
    data_nascimento = models.DateField('Data de Nascimento',blank=False, null=True)
    foto = models.ImageField(blank=True, upload_to='user_foto', verbose_name='Foto', null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome', 'cpf', 'data_nascimento']


    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = 'Usuario'