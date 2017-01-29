import unittest


class TestChessAPIModule(unittest.TestCase):
    def test_import(self):
        can_import = False
        try:
            import ChessAPI
            print("Got here.")
        except Exception as e:
            print(e)
        except ImportError:
            pass
        else:
            can_import = True
        self.assertTrue(can_import)

unittest.main()
