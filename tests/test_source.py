import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test behaviour of the source class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.new_source= Source( "ars-technica","Ars Technica","The PC enthusiast's resource. Power users and the tools they love, without computing religion.","http://arstechnica.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()