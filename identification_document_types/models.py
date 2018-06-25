# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from .enums import IdentificationDocumentClass 


# Create your models here.
class IdentificationDocumentType(models.Model):
    '''
        This class: <IdentificationDocumentType> contains the information of the types of identification documents.
        Esta clase: <TipoDocumentIdentificacion> contiene la información de los tipos de documentos de identificación.
    '''
    IDENTIFICATION_DOCUMENT_CLASS_CHOICES = [(identification_document_class.value, identification_document_class.value) for identification_document_class in IdentificationDocumentClass]
    identification_document_class = models.CharField(
        choices = IDENTIFICATION_DOCUMENT_CLASS_CHOICES,
        max_length=25,
        help_text='Identification document type | Tipo documento de identificación'
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text='Name | Nombre'
    )
    initials = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        help_text='Initials | Iniciales'
    )
    digits = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(30),
        ], 
        default=0,
        help_text='Digits | Dígitos'
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )
    
    def __str__(self):
        return self.get_initials()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(IdentificationDocumentType, self).save(*args, **kwargs)

    #Setter
    def set_identification_document_class(self, identification_document_class):
        self.identification_document_class = identification_document_class

    def set_name(self, name):
        self.name = name
    
    def set_initials(self, initials):
        self.initials = initials
    
    def set_digits(self, digits):
        self.digits = digits

    #Getter
    def get_name(self):
        return self.name
   
    def get_initials(self):
        return self.initials
    
    def get_digits(self):
        return self.digits

    def get_identification_document_class(self):
        return self.identification_document_class

    class Meta:
        db_table = 'identification_document_types'
        ordering = ['identification_document_class', 'name', 'initials', 'digits']
        verbose_name = 'Identification Document Type'
        verbose_name_plural = 'Identification Document Types'