import atexit
import tempfile
import unittest

import rcore.sqlitecache

test_values = [
    ('key1', 'text', None),
    ('key2', 2, None),
    (3, 'val4', None),
    (5, 6, None),
    (7, None, None),
    (None, 8, None),
    ]


class Test_SQLiteCache(unittest.TestCase):

    def setUp(self):
        if True:
            self._fn = '/tmp/test.db'
        else:
            self._fn = tempfile.mkstemp(suffix='.db')
            atexit.register(lambda: os.remove(self._fn))

        self.cache = rcore.sqlitecache.SQLiteCache(self._fn)

    def test_tvs(self):
        for tv in test_values:
            self.assertEqual( self.cache[tv[0]], tv[1] )

if __name__ == '__main__':
    unittest.main()
