# -*- encoding: utf-8 -*-
from enum import Enum, unique

@unique
class NominalOrganicStructureType(Enum):
    ''' 
        This Enumeration: <NominalOrganicStructureType> is to identify the type of nominal organic structure.
        Esta Enumeración: <TipoEstructuraOrgánicaNominal> es para identificar el tipo de estructura orgánica nominal.
        
        Attributes - Atributos
            >Not Assigned | No Asigando
            >High Direction | Alta Dirección
            >Direction | Dirección
            >Consultancy | Consultoría
            >Advice | Consejo
            >Control | Control
            >Line | Línea
            >Decentralized | Descentralizado

    '''
    NOT_ASSIGNED = 'No Asigando'
    HIGH_DIRECTION = 'Alta Dirección'
    DIRECTION = 'Dirección'
    CONSULTANCY = 'Consultoría'
    ADVICE = 'Consejo'
    CONTROL = 'Control'
    LINE = 'Línea'
    DESCENTRALIZED = 'Descentralizado'