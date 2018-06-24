# -*- encoding: utf-8 -*-
from enum import Enum, unique


@unique
class PersonType(Enum):
    NATURAL = 'Natural'
    LEGAL = 'Jurídica'

@unique
class Gender(Enum):
    MALE = 'Masculino'
    FEMALE = 'Femenino'
    OTHERS = 'Otros'

@unique
class MaritalStatus(Enum):
    SINGLE = 'Soltero'
    MARRIED = 'Casado'
    DIVORCED = 'Divorciado'
    SEPARATED = 'Separado'
    WIDOWER = 'Viudo'