# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


from entity_activities.models import EntityActivity
from entity_classes.models import EntityClass
from entity_types.models import EntityType


# Create your models here.
class Entity(models.Model):
    '''   
        This Class: <Entity> contains the information of an entity.
        Esta Clase: <Entidad> contiene la información de una entidad.
    '''
    entity_class = models.ForeignKey(
        EntityClass,
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        help_text= 'Entity class | Clase de la entidad'
    )
    entity_type = models.ForeignKey(
        EntityType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        help_text= 'Entity type | Tipo de la entidad'
    )
    entity_activity = models.ForeignKey(
        EntityActivity, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        help_text= 'Entity activity | Actividad de la entidad'
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
    slogan = models.CharField(
        max_length=100,
        unique=True,
        null=True, 
        blank=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ], 
        help_text= 'Slogan | Slogan'
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
    logo = models.ImageField(
        upload_to='images/entities/',
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
        return self.get_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(Entity, self).save(*args, **kwargs)
    
    def set_entity_class(self, entity_class):
        self.entity_class = entity_class
    
    def set_entity_type(self, entity_type):
        self.entity_type = entity_type
    
    def set_entity_activity(self, entity_activity):
        self.entity_activity = entity_activity
    
    def set_name(self, name):
        self.name = name 

    def set_slogan(self, slogan):
        self.slogan = slogan

    def set_initials(self, initials):
        self.initials = initials
    
    def set_logo(self, logo):
        self.logo = logo 

    def set_active(self, active):
        self.active = active 

    def get_entity_class(self):
        return self.entity_class 
    
    def get_entity_type(self):
        return self.entity_type 
    
    def get_entity_activity(self):
        return self.entity_activity 

    def get_name(self):
        return self.name
    
    def get_slogan(self):
        return self.slogan 

    def get_initials(self):
        return self.initials 
    
    def get_logo(self):
        return self.logo 

    def is_active(self):
        return self.active
    
    def get_full_name(self):
        return '%s - %s' %(self.get_name(), self.get_initials())
        
    class Meta:
        db_table = 'entities'
        ordering = ['entity_class', 'entity_type', 'entity_activity', 'name']
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'