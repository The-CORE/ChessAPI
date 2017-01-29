import unittest


class TestChessAPI(unittest.TestCase):
    def setUp(self):
        '''
        The setup required for every test of ChessAPI
        '''
        self.assertTrue(self._can_import(), 'Cannot import ChessAPI')
        import ChessAPI
        self.ChessAPI = ChessAPI

    def _can_import(self):
        '''
        Returns true if you can import the package, and false otherwise.
        '''
        can_import = False
        try:
            import ChessAPI
        except ImportError:
            pass
        else:
            can_import = True
        return can_import


class TestPackage(TestChessAPI):
    def setUp(self):
        '''
        Sets up the tests on the module.
        '''
        self.attributes_to_check = [
            'Game',
            'DiscreteVector',
        ]
        return super(TestPackage, self).setUp()

    def test_attributes(self):
        '''
        Tests whether or not the package has all required attributes.
        '''
        for attribute in self.attributes_to_check:
            self.assertTrue(
                hasattr(self.ChessAPI, attribute),
                'ChessAPI does not have attribute "{}"'.format(attribute)
            )


class TestGame(TestChessAPI):
    pass


class TestDiscreteVector(TestChessAPI):
    def test_initiation(self):
        pass


unittest.main()
