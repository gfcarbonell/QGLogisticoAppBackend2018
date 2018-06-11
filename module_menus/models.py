from django.db import models
from modules.models import Module
from menus.models import Menu 
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify

class ModuleMenu(models.Model):
    '''
        This Class: <ModuleMenu> contains all items of menu and submenu of system.
        Esta clase: <MóduloMenu> contiene todos los items del módulo y menús del sistema.
    '''
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        help_text= 'Module | Módule'
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        help_text= 'Menu | Menús'
    )
    order = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20),
        ], 
        help_text='Order | Orden'
    )
    image = models.ImageField(
        upload_to='images/module-menus/', 
        default=None, 
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
        return self.get_module_menu_info()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_module_menu_info())
        else:
            slug = slugify(self.get_module_menu_info())
            if self.slug != slug:
                self.slug = slug
        super(ModuleMenu, self).save(*args, **kwargs)

    #Setter
    def set_module(self, module):
        self.module = module

    def set_menu(self, menu):
        self.menu = menu
    
    def set_order(self, order):
        self.order = order

    def set_image(self, order):
        self.image = image

    def set_active(self, active):
        self.active = active

    #Getter
    def get_module(self):
        return self.module 

    def get_menu(self):
        return self.menu
   
    def get_submenu(self):
        return self.submenu
    
    def get_order(self):
        return self.order 

    def get_image(self):
        return self.image 

    def is_active(self):
        return self.active

    def get_module_menu_info(self):
        return '%s | %s ' %(self.get_module().get_name(), self.get_menu().get_name())

    class Meta:
        db_table = 'module_menus'
        ordering = ['order', 'module', 'menu']
        verbose_name = 'Module Menu'
        verbose_name_plural = 'Module Menus'