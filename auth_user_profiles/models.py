# -*- encoding: utf-8 -*-
from django.db import models
from persons.models import Person
from auth_users.models import AuthUser


# Create your models here.
class AuthUserProfile(Person):
    '''
        This class:<AuthUserProfile> inherits from the <Person> class.
        Esta class:<AuthPerfilUsuario> hereda de la clase persona.
    '''
    auth_user = models.OneToOneField(
        AuthUser, 
        unique=True,
        db_index=True,
        on_delete=models.CASCADE, 
        help_text='Auth user | Usuario'
    )

    #Setter
    def set_auth_user(self, auth_user):
       self.auth_user = auth_user 

    #Getter
    def get_auth_user(self, auth_user):
        return self.auth_user 

    class Meta:
        abstract = True