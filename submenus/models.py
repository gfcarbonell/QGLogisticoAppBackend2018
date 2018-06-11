# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from url_or_relative_url_field.fields import URLOrRelativeURLField


# Create your models here.
class SubMenu(models.Model):
    '''
        This Class: <SubMenu> contains the submenu of system.
        Esta clase: <SubMenu> contiene el submenu del sistema.
    '''
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
        super(SubMenu, self).save(*args, **kwargs)

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
        db_table = 'submenus'
        verbose_name = 'Sub Menu'
        verbose_name_plural = 'Sub Menus'