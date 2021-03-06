# -*- encoding: utf-8 -*-
from django.db import models
from persons.enums import Gender, MaritalStatus
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from contact_information.models import ContactInformation
from extra_information.models import ExtraInformation
from identification_document_types.models import IdentificationDocumentType

# Create your models here.
class Person(models.Model):
    '''
        This Class:<Person> is abstract and contains basic personal information.
        Esta Clase:<Persona> es abstracto y contiene la información personal básica.
    '''
    GENDER_CHOICES = [(gender.value, gender.value) for gender in Gender]
    MARITAL_STATUS_CHOICES = [(marital_status.value, marital_status.value) for marital_status in MaritalStatus]
    name = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        help_text='Name | Nombre'
    )
    last_name = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        help_text='Last name | Apellido paterno'
    )
    mother_last_name = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ], 
        help_text='Mother last name | Apellido materno'
    )   
    identification_document_type = models.ManyToManyField(
        IdentificationDocumentType,
        through='identification_documents.IdentificationDocument',
    )
    birthday = models.DateField(
        help_text='birthday | Fecha nacimiento'
    )
    gender = models.CharField(
        choices = GENDER_CHOICES,
        max_length=9,
        help_text='Gender | Género'
    )
    marital_status = models.CharField(
        choices = MARITAL_STATUS_CHOICES,
        max_length=9,
        help_text='Marital status | Estado marital o civil'
    )
    photography = models.ImageField(
        upload_to='images/persons/', 
        null=True, 
        blank=True,
        default='images/defaults/Default-1.png', 
        help_text='Photography | Fotografía'
    ) 
    contact_information = models.ManyToManyField(
        ContactInformation,
        blank=True,
        null=True, 
        help_text='Contact information | Informarción de contacto'
    )
    extra_information = models.ManyToManyField(
        ExtraInformation,
        blank=True, 
        null=True, 
        help_text='Extra information | Informarción extra'
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )
    
    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_full_name())
        else:
            slug = slugify(self.get_full_name())
            if self.slug != slug:
                self.slug = slug
        super(Person, self).save(*args, **kwargs)

    def get_full_name(self):
        return '%s %s, %s' % (self.get_last_name(), self.get_mother_last_name(), self.get_name())

    #Setter
    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_mother_last_name(self, mother_last_name):
        self.mother_last_name = mother_last_name

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_gender(self, gender):
        self.gender = gender

    def set_marital_status(self, marital_status):
        self.marital_status = marital_status
    
    def set_contact_information(self, contact_information):
        self.contact_information = contact_information 
    
    def set_extra_information(self, extra_information):
        self.extra_information = extra_information 
    
    #Getter 
    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_mother_last_name(self):
        return self.mother_last_name

    def get_birthday(self):
        return self.birthday 

    def get_gender(self):
        return self.gender

    def get_marital_status(self):
        return self.marital_status 
    
    def get_contact_information(self):
        return self.contact_information

    def get_extra_information(self):
        return self.extra_information 

    class Meta:
        db_table = 'person'
        ordering = ('last_name', 'mother_last_name', 'name')
        verbose_name = 'Person'
        verbose_name_plural = 'Persons - People'