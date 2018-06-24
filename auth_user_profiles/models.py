# -*- encoding: utf-8 -*-
from django.db import models
from persons.models import Person
from auth_users.models import AuthUser
from contact_information.models import ContactInformation
from extra_information.models import ExtraInformation


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
    contact_information = models.ManyToManyField(
        ContactInformation,
        blank=True, 
        help_text='Contact information | Informarción de contacto'
    )
    extra_information = models.ManyToManyField(
        ExtraInformation,
        blank=True, 
        help_text='Extra information | Informarción extra'
    )

    #Setter
    def set_auth_user(self, auth_user):
       self.auth_user = auth_user 
    
    def set_contact_information(self, contact_information):
        self.contact_information = contact_information 
    
    def set_extra_information(self, extra_information):
        self.extra_information = extra_information 
    
    #Getter
    def get_auth_user(self, auth_user):
        return self.auth_user 

    def get_contact_information(self):
        return self.contact_information

    def get_extra_information(self):
        return self.extra_information 

    class Meta:
        db_table = 'auth_user_profiles'
        verbose_name = 'Auth User Profile'
        verbose_name_plural = 'Auth User Profiles'