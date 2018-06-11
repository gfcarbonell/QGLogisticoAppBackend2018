# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from url_or_relative_url_field.fields import URLOrRelativeURLField
from submenus.models import SubMenu


# Create your models here.
class Menu(models.Model):
    '''
        This Class: <Menu> contains the menu of system.
        Esta clase: <Menu> contiene el menu del sistema.
    '''
    sub_menu = models.ManyToManyField(SubMenu, through='menu_submenus.MenuSubMenu')
    name = models.CharField(
        unique=True,
        db_index=True,
        max_length=100,
        help_text='Name | Nombre'
    )
    url = URLOrRelativeURLField(
        unique=True,
        db_index=True,
        max_length=255,
        help_text='U.R.L. | U.R.L.'
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
    def set_name(self, name):
        self.name = name
    
    def set_url(self, url):
        self.url = url
    
    #Getter
    def get_name(self):
        return self.name
   
    def get_url(self):
        return self.url

    class Meta:
        db_table = 'menus'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'