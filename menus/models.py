# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from url_or_relative_url_field.fields import URLOrRelativeURLField
from django.core.validators import MinValueValidator, MaxValueValidator
from modules.models import Module 


# Create your models here.
class Menu(models.Model):
    '''
        This Class: <Menu> contains the menu of system.
        Esta clase: <Menu> contiene el menu del sistema.
    '''
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        help_text='Module | Módulo'
    )
    name = models.CharField(
        unique=True,
        db_index=True,
        max_length=100,
        help_text='Name | Nombre'
    )
    url = URLOrRelativeURLField(
        db_index=True,
        max_length=255,
        help_text='U.R.L. | U.R.L.'
    )
    order = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20),
        ], 
        default=0,
        help_text='Order | Orden'
    )
    image = models.ImageField(
        upload_to='images/menus/', 
        default='images/defaults/Default-1.png', 
        help_text='Image | Imagen'
    ) 
    main = models.BooleanField(
        default=False,
        help_text='Main | Principal',
    )
    active = models.BooleanField(
        default=True,
        help_text='Active | Activo',
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
        super(Menu, self).save(*args, **kwargs)

    #Setter
    def set_module(self, module):
        self.module =  module 

    def set_name(self, name):
        self.name = name
    
    def set_url(self, url):
        self.url = url

    def set_order(self, order):
        self.orden = order 

    def set_image(self, image):
        self.image = image 

    def set_active(self, active):
        self.active = active

    def set_main(self, main):
        self.main =  main

    #Getter
    def get_module(self):
        return self.module 

    def get_name(self):
        return self.name
   
    def get_url(self):
        return self.url
    
    def get_order(self):
        return self.order 

    def get_image(self):
        return self.image 

    def is_active(self):
        return self.active
    
    def is_main(self):
        return self.main

    class Meta:
        db_table = 'menus'
        ordering = ['order', 'module', 'name', 'url']
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'