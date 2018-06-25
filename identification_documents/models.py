# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from persons.models import Person
from identification_document_types.models import IdentificationDocumentType


# Create your models here.
class IdentificationDocument(models.Model):
    '''
        This class:<IdentificationDocument>.
        Esta class:<DocumentoIdentificacion>.
    '''
    person = models.ForeignKey(
        Person,
        db_index=True,
        on_delete=models.CASCADE, 
        help_text='Person | Persona'
    )
    identification_document_type = models.ForeignKey(
        IdentificationDocumentType,
        on_delete=models.CASCADE, 
        help_text='Identification document type | Tipo Documento de identificación'    
    )
    number = models.CharField(
        max_length=25,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(25),
        ], 
        help_text= 'Number | Número'
    )
    
    def __str__(self):
        return self.get_identification_document()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_identification_document())
        else:
            slug = slugify(self.get_identification_document())
            if self.slug != slug:
                self.slug = slug
        super(IdentificationDocument, self).save(*args, **kwargs)
    
    #Setter
    def set_person(self, person):
        self.person =  person 

    def set_identification_document_type(self, identification_document_type):
        self.identification_document_type =  identification_document_type

    def set_number(self, number):
        self.number =  number 

    #Getter
    def get_person(self):
        return self.person

    def get_identification_document_type(self):
        return self.identification_document_type 

    def get_number(self):
        return self.number 
    
    def get_identification_document(self):
        return '%s - %s - %s' %(self.get_person().get_full_name(), self.get_identification_document_type().get_initials(), self.get_number())
    class Meta:
        db_table = 'identification_documents'
        ordering = ['number']
        verbose_name = 'Identification Document'
        verbose_name_plural = 'Identification Documents'