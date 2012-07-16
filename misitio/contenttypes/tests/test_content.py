import unittest2 as unittest

from AccessControl import Unauthorized

from plone.i18n.normalizer import idnormalizer
from Products.ATContentTypes.lib import constraintypes

from Products.CMFCore.utils import getToolByName

from misitio.contenttypes.testing import\
    MISITIO_CONTENTTYPES_INTEGRATION_TESTING

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class TestContent(unittest.TestCase):

    layer = MISITIO_CONTENTTYPES_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.types = getToolByName(self.portal, 'portal_types')
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'misitio.contenttypes'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_contenttypes_is_registred(self):
        existing = self.types.objectIds()
        self.assertTrue('misitio.contenttypes.concejo_comunal' in existing)
        self.assertTrue('misitio.contenttypes.miembro' in existing)

    def test_consejo_comunal_allowed_content_types(self):

        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        oid = idnormalizer.normalize("consejos comunales", 'es')
        self.portal.invokeFactory('misitio.contenttypes.concejo_comunal', id=oid, title='prueba consejo comunal')
        self.folder = self.portal[oid]
        types = ['misitio.contenttypes.miembro',]
        allowed_types = [t.getId() for t in self.folder.allowedContentTypes()]
        for t in types:
            self.assertTrue(t in allowed_types)
        
		# trying to add any other content type raises an error
        self.assertRaises(ValueError,
                          self.folder.invokeFactory, 'Document', 'Registro legal')
        try:
            self.folder.invokeFactory('misitio.contenttypes.miembro', 'leonardo caballero')
        except Unauthorized:
            self.fail()

