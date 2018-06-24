# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class AreaType(models.Model):
    '''
        This Class: <AreaType> is for to identify the type that an area belongs.
        Esta Clase: <TipoArea> es para identificar el tipo que pertenece una área.
        For example:
            Management | Gerencia
    '''
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
    abbreviation = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20),
        ], 
        help_text= 'Abbreviation | Abreviatura'
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
        super(AreaType, self).save(*args, **kwargs)

    #Setter
    def set_name(self, name):
        self.name = name
    
    def set_abbreviation(self, abbreviation):
        self.abbreviation = abbreviation
    
    #Getter
    def get_name(self):
        return self.name
   
    def get_abbreviation(self):
        return self.abbreviation

    def get_full_name(self):
        return '%s - %s' %(self.get_name(), self.get_abbreviation())

    class Meta:
        db_table = 'area_types'
        ordering = ['name', 'abbreviation']
        verbose_name = 'Area Type'
        verbose_name_plural = 'Areas Types'