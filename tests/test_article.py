import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviour of the Article class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.news_article= Article("All eyes on Biden's response to COVID variants, Afghanistan, border crisis, inflation", "Fox News", " 2021-08-14T15:37:22.0946428Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.news_article,Article))

if __name__ == '__main__':
    unittest.main()