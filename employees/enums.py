# -*- encoding: utf-8 -*-
from enum import Enum, unique


@unique
class InstructionLevel(Enum):
    NO_LEVEL = 'Sin nivel'
    PRESCHOOL = 'Pre escolar'
    PRIMARY = 'Primaria'
    HIGH_SCHOOL = 'Secundaria'
    HIGHER = 'Superior'

@unique
class BloodGroup(Enum):
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'