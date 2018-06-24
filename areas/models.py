# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from headquarterses.models import Headquarters
from area_types.models import AreaType
from .enums import NominalOrganicStructureType

# Create your models here.
class Area(models.Model):
    '''   
        This Class: <Area> contains the information of an area.
        Esta Clase: <Área> contiene la información de una área.
    '''
    NOMINAL_ORGANIC_STRUCTURE_TYPE = [(nominal_organic_structure_type.value, nominal_organic_structure_type.value) for nominal_organic_structure_type in NominalOrganicStructureType]
    headquarters = models.ForeignKey(
        Headquarters, 
        db_index=True,
        on_delete=models.CASCADE, 
        help_text='Headquarters | Sede'
    )
    dependency = models.ForeignKey(
        'self', 
        db_index=True,
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text='Dependency | Dependencia'
    )
    area_type = models.ForeignKey(
        AreaType, 
        db_index=True,
        on_delete=models.CASCADE, 
        help_text='AreaType | Tipo área'
    )
    name = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ], 
        help_text= 'Name | Nombre'
    )
    initials = models.CharField(
        max_length=20,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20),
        ], 
        help_text= 'Initials | Iniciales'
    )
    nominal_organic_structure_type = models.CharField(
        choices = NOMINAL_ORGANIC_STRUCTURE_TYPE,
        max_length=15,
        help_text='Nominal organic structure Type | Tipo estructura orgánica nominal'
    )
    telephone_annex = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000),
        ], 
        blank=True,
        default=0,
        help_text='Telephone annex | Anexo telefónica'
    )
    fax = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000),
        ], 
        blank=True,
        default=0,
        help_text='Fax | Fax'
    )
    logo = models.ImageField(
        upload_to='images/areas/',
        null=True, 
        blank=True,
        default='images/defaults/Default-1.png', 
        help_text= 'Logo | logo'
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
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_full_name())
        else:
            slug = slugify(self.get_full_name())
            if self.slug != slug:
                self.slug = slug
        super(Area, self).save(*args, **kwargs)
    
    #Setter
    def set_dependency(self, dependency):
        self.dependency = dependency

    def set_headquarters(self, headquarters):
        self.headquarters = headquarters

    def set_name(self, name):
        self.name = name
    
    def set_initials(self, initials):
        self.initials = initials
    
    def set_telephone_annex(self, telephone_annex):
        self.telephone_annex = telephone_annex 
    
    def set_fax(self, fax):
        self.fax = fax
    
    def set_logo(self, logo):
        self.logo = logo 

    #Getter
    def get_headquarters(self):
        return self.headquarters 

    def get_name(self):
        return self.name 
    
    def get_initials(self):
        return self.initials 
    
    def get_telephone_annex(self):
        return self.telephone_annex  
    
    def get_fax(self):
        return self.fax 
    
    def get_logo(self):
        return self.logo
    
    def get_dependency(self):
        return self.dependency
    
    def get_full_name(self):
        return '%s - %s' %(self.get_headquarters().get_name(), self.get_name())

    class Meta:
        db_table = 'areas'
        ordering = ['headquarters', 'name', 'initials']
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'