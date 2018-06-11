from django.db import models
from menus.models import Menu 
from submenus.models import SubMenu
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify

class MenuSubMenu(models.Model):
    '''
        This Class: <MenuSubMenu> contains all items of menu and submenu of system.
        Esta clase: <MenuSubMenu> contiene todos los items del menús y sub menús del sistema.
    '''
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        help_text= 'Menu | Menús'
    )
    submenu = models.ForeignKey(
        SubMenu,
        on_delete=models.CASCADE,
        help_text= 'Sub Menu | Sub Menú'
    )
    order = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20),
        ], 
        help_text='Order | Orden'
    )
    image = models.ImageField(
        upload_to='images/menu-submenus/', 
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
        return self.get_menu_submenu_info()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_menu_submenu_info())
        else:
            slug = slugify(self.get_menu_submenu_info())
            if self.slug != slug:
                self.slug = slug
        super(MenuSubMenu, self).save(*args, **kwargs)

    #Setter
    def set_menu(self, menu):
        self.menu = menu
    
    def set_submenu(self, submenu):
        self.submenu = submenu
    
    def set_order(self, order):
        self.order = order

    def set_image(self, order):
        self.image = image

    def set_active(self, active):
        self.active = active

    #Getter
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

    def get_menu_submenu_info(self):
        return '%s | %s ' %(self.get_menu().get_name(), self.get_submenu().get_name())

    class Meta:
        db_table = 'menu_submenus'
        ordering = ['order', 'menu', 'submenu']
        verbose_name = 'Menu Sub Menu'
        verbose_name_plural = 'Menu Sub Menus'