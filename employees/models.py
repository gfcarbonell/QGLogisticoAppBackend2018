# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from areas.models import Area
from auth_user_profiles.models import AuthUserProfile
from .enums import InstructionLevel, BloodGroup
from employee_types.models import EmployeeType
from employee_positions.models import EmployeePosition



# Create your models here.
class Employee(models.Model):
    '''
        This class:<Employee> inherits from the employee class.
        Esta class:<Empleado> hereda de la clase empleado.
    '''
    INSTRUCTION_LEVEL_CHOICES = [(instruction_level.value, instruction_level.value) for instruction_level in InstructionLevel]
    GROUP_CHOICES_BLOOD = [(blood_group.value, blood_group.value) for blood_group in BloodGroup]
    area = models.ForeignKey(
        Area, 
        db_index=True,
        on_delete=models.CASCADE, 
        help_text='Area | Área'
    )
    employee_type = models.ForeignKey(
        EmployeeType,
        db_index=True,
        on_delete=models.CASCADE,
        help_text= 'Employee type | Tipo de empleado'
    )
    employee_position = models.ForeignKey(
        EmployeePosition,
        db_index=True,
        on_delete=models.CASCADE,
        help_text= 'Employee position | Cargo de empleado'
    )
    auth_user_profile = models.OneToOneField(
        AuthUserProfile, 
        unique=True,
        db_index=True,
        on_delete=models.CASCADE, 
        help_text='Auth user profile | Perfil de usuario'
    )
    start_date_contract = models.DateField(
        help_text='Start date contract | Inicio fecha contrato'
    )
    end_date_contract = models.DateField(
        help_text='End date contract | Fin fecha contrato'
    )
    instruction_level = models.CharField(
        choices = INSTRUCTION_LEVEL_CHOICES,
        max_length=12,
        help_text='Instruction level | Nivel de instrucción'
    )
    blood_group = models.CharField(
        choices = GROUP_CHOICES_BLOOD,
        max_length=9,
        null=True,
        blank=True,
        help_text='Blood group | Grupo sanguíneo'
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
        return self.get_auth_user_profile().get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_auth_user_profile().get_full_name())
        else:
            slug = slugify(self.get_auth_user_profile().get_full_name())
            if self.slug != slug:
                self.slug = slug
        super(Employee, self).save(*args, **kwargs)

    #Setter 
    def set_area(self, area):
        self.area = area 
    
    def set_employee_type(self, employee_type):
        self.employee_type = employee_type

    def set_entity_position(self, entity_position):
        self.entity_position = entity_position

    def set_auth_user_profile(self, auth_user_profile):
        self.auth_user_profile = auth_user_profile

    def set_start_date_contract(self, start_date_contract):
        self.start_date_contract = start_date_contract

    def set_end_date_contract(self, end_date_contract):
        self.end_date_contract = end_date_contract 

    def set_instruction_level(self, instruction_level):
        self.instruction_level =  instruction_level

    def set_blood_group(self, blood_group):
        self.blood_group = blood_group   

    #Getter 
    def get_area(self):
        return self.area 

    def get_employee_type(self):
        return self.employee_type 

    def get_entity_position(self):
        return self.entity_position 

    def get_auth_user_profile(self):
        return self.auth_user_profile 

    def get_start_date_contract(self):
        return self.start_date_contract 

    def get_end_date_contract(self):
        return self.end_date_contract 

    def get_instruction_level(self):
        return self.instruction_level

    def get_blood_group(self):
        return self.blood_group    

    class Meta:
        db_table = 'emplooyes'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'