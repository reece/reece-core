import atexit
import collections
import tempfile
import unittest

import rcore.sqlitecache


tests = [
    ('str_str',  'key1', 'text'),
    ('str_int',  'key2',      2),
    ('int_str',      3,  'val4'),
    ('int_int',      5,       6),
    ('int_None',     7,    None),
    ('None_int',  None,       8),
    ]


class Test_SQLiteCache(unittest.TestCase):

    def setUp(self):
        if True:
            self._fn = '/tmp/test.db'
        else:
            self._fn = tempfile.mkstemp(suffix='.db')
            atexit.register(lambda: os.remove(self._fn))

        self.cache = rcore.sqlitecache.SQLiteCache(self._fn)

        for n,k,v in tests:
            self.cache[k] = v

    def test(self):
        for n,k,v in tests:
            self.assertEqual(v, self.cache[k])

if __name__ == '__main__':
    unittest.main()
