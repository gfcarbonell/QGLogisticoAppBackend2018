# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from url_or_relative_url_field.fields import URLOrRelativeURLField
from django.core.validators import MinValueValidator, MaxValueValidator
from menus.models import Menu


# Create your models here.
class SubMenu(models.Model):
    '''
        This Class: <SubMenu> contains the submenu of system.
        Esta clase: <SubMenu> contiene el submenu del sistema.
    '''
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        help_text='Menu | Menú'
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
        upload_to='images/submenus/', 
        default='images/defaults/Default-1.png', 
        help_text='Image | Imagen'
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
        super(SubMenu, self).save(*args, **kwargs)

    #Setter
    def set_menu(self, menu):
        self.menu = menu

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

    #Getter
    def get_menu(self):
        return self.menu 

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

    class Meta:
        db_table = 'submenus'
        ordering = ['order', 'menu', 'name', 'url']
        verbose_name = 'Sub Menu'
        verbose_name_plural = 'Sub Menus'