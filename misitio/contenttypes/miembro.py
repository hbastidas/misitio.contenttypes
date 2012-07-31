# -*- coding:  utf-8 -*-
from five import grok
from zope import schema
from plone.directives import form
from Products.CMFCore.utils import getToolByName

class Imiembro(form.Schema):
    nombre = schema.TextLine(
        title = u"nombre",
        description = u"nombre de la persona",
        required = False,
    )

    apellido = schema.TextLine(
        title = u"apellido",
        description = u"apellido de la persona",
        required = False,
    )

    ci = schema.TextLine(
        title = u"C.I",
        description = u"Identificacion nacional",
        required = False,
    )

    direcci_n_f_sica = schema.TextLine(
        title = u"direccion fisica",
        description = u"ubicacion de habitacion",
        required = False,
    )

    direccion_electronica = schema.TextLine(
        title = u"correo",
        description = u"correo de los miembros",
        required = False,
    )

    twitter = schema.TextLine(
        title = u"Telefono",
        description = u"telefono de contacto",
        required = False,
    )

grok.templatedir('miembro_templates')

class View(grok.View):
    """
    registrando una vista basada en grok para conectarse al esquema concejo comunal.
    """
    grok.context(Imiembro)
    grok.require("zope2.View")
    grok.template("view")

