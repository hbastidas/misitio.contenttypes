# -*- coding:  utf-8 -*-

from zope import schema
from plone.directives import form

class Iconcejocomunal(form.Schema):
    ubicacion = schema.TextLine(
        title = u"ubicacion",
        description = u"DESCRIPCION DE LA UBICACION",
        required = False,
    )

    persona_de_contacto = schema.TextLine(
        title = u"persona de contacto",
        description = u"DESCRIPCION DE LA UBICACION",
        required = False,
    )

    correo = schema.TextLine(
        title = u"Correo",
        description = u"DESCRIPCION DE LA UBICACION",
        required = False,
    )

    Telefono = schema.TextLine(
        title = u"Telefono",
        description = u"DESCRIPCION DE LA UBICACION",
        required = False,
    )



