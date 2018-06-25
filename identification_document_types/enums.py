# -*- encoding: utf-8 -*-
from enum import Enum, unique


@unique
class IdentificationDocumentClass(Enum):
    ''' 
        This Enumeration: <IdentificationDocumentClass> is to identify the kind of the identification document.
        Esta Enumeración: <ClaseDocumentIdentificacion> es para identificar la clase del documento de identificación.
        Attributes - Atributos
            >Identity Document | Documento Identidad 
            >Tax Identificatión | Identificación Tributaria

    '''
    IDENTITY_DOCUMENT = 'Documento Identidad'
    TAX_IDENTIFICATION = 'Identificación Tributaria'