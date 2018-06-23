# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from entities.models import Entity
from contact_information.models import ContactInformation
from extra_information.models import ExtraInformation

# Create your models here.
class Headquarters(models.Model):
    '''   
        This Class: <Headquarters> contains the information of an headquarters.
        Esta Clase: <Sede> contiene la información de una sede.
    '''
    entity = models.ForeignKey(
        Entity, 
        db_index=True,
        on_delete=models.CASCADE, 
        help_text='Entity | Entidad'
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ], 
        help_text= 'Name | Nombre'
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
    active = models.BooleanField(
        default=True, 
        help_text='Active | Activo'
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )

    def __str__(self):
        return self.get_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(Headquarters, self).save(*args, **kwargs)

    #Setter
    def set_entity(self, entity):
        self.entity = entity 

    def set_name(self, name):
        self.name = name 
    
    def set_contact_information(self, contact_information):
        self.contact_information = contact_information
    
    def set_extra_information(self, extra_information):
        self.extra_information = extra_information
    
    def set_active(self, active):
        self.active = active 

    #Getter
    def get_entity(self):
        return self.entity 
    
    def get_name(self):
        return self.name 
    
    def get_contact_information(self):
        return self.contact_information
    
    def get_extra_information(self):
        return self.extra_information
    
    def is_active(self):
        return self.active

    def get_full_name(self):
        return '%s - %s'%(self.get_entity(), self.get_name())

    class Meta:
        db_table = 'headquarters'
        ordering = ['entity', 'name']
        verbose_name = 'Entity'
        verbose_name_plural = 'Headquarters'