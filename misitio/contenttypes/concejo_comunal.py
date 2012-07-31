# -*- coding:  utf-8 -*-
from Acquisition import aq_inner
from five import grok
from zope import schema
from plone.directives import form
from Products.CMFCore.utils import getToolByName
from misitio.contenttypes.miembro import Imiembro

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

grok.templatedir('concejo_comunal_templates')

class View(grok.View):
    """
    registrando una vista basada en grok para conectarse al esquema concejo comunal.
    """
    grok.context(Iconcejocomunal)
    grok.require("zope2.View")
    grok.template("view")

    def miembros_concejo_comunal(self):
        """
            retorna un resultado de busqueda en el catalogo de los miembros de un concejo_comunal
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context,"portal_catalog")
        return catalog(object_provides=Imiembro.__identifier__, path='/'.join(context.getPhysicalPath()), sort_on = 'sortable_title')
