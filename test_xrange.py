import unittest
from xrange import xrange

def getitem(obj, index):
    return obj[index]

class XrangeTests(unittest.TestCase):

    def test_init(self):
        r = xrange(0)
        self.assertEqual(0, r._start)
        self.assertEqual(0, r._stop)
        self.assertEqual(1, r._step)

        r = xrange(1)
        self.assertEqual(0, r._start)
        self.assertEqual(1, r._stop)
        self.assertEqual(1, r._step)

        r = xrange(2)
        self.assertEqual(0, r._start)
        self.assertEqual(2, r._stop)
        self.assertEqual(1, r._step)

        r = xrange(1, 2)
        self.assertEqual(1, r._start)
        self.assertEqual(2, r._stop)
        self.assertEqual(1, r._step)

        r = xrange(1, 2, 1)
        self.assertEqual(1, r._start)
        self.assertEqual(2, r._stop)
        self.assertEqual(1, r._step)

        r = xrange(2, 2, 1)
        self.assertEqual(2, r._start)
        self.assertEqual(2, r._stop)
        self.assertEqual(1, r._step)

        r = xrange(1, 2, -1)
        self.assertEqual(1, r._start)
        self.assertEqual(1, r._stop)
        self.assertEqual(-1, r._step)

        r = xrange(2, 1, -1)
        self.assertEqual(2, r._start)
        self.assertEqual(1, r._stop)
        self.assertEqual(-1, r._step)

        self.assertRaises(TypeError, xrange, 1, 2, 3, 4)
        self.assertRaises(TypeError, xrange, 'abc')
        self.assertRaises(ValueError, xrange, 1, 2, 0)

    def test_repr(self):
        self.assertEqual(repr(xrange(1)), 'xrange(1)')
        self.assertEqual(repr(xrange(1, 2)), 'xrange(1, 2)')
        self.assertEqual(repr(xrange(1, 3, 2)), 'xrange(1, 3, 2)')

    def test_index(self):
        r = xrange(1)
        self.assertEqual(0, r.index(0))
        self.assertRaises(ValueError, r.index, -1)
        self.assertRaises(ValueError, r.index, 1)

        r = xrange(10)
        self.assertEqual(4, r.index(4))
        self.assertEqual(9, r.index(9))
        self.assertRaises(ValueError, r.index, -1)
        self.assertRaises(ValueError, r.index, 10)

        r = xrange(3, 6)
        self.assertEqual(0, r.index(3))
        self.assertEqual(2, r.index(5))
        self.assertRaises(ValueError, r.index, 2)
        self.assertRaises(ValueError, r.index, 6)

        r = xrange(3, 6, 2)
        self.assertEqual(0, r.index(3))
        self.assertEqual(1, r.index(5))
        self.assertRaises(ValueError, r.index, 2)
        self.assertRaises(ValueError, r.index, 6)

        r = xrange(5, 2, -1)
        self.assertEqual(2, r.index(3))
        self.assertEqual(0, r.index(5))
        self.assertRaises(ValueError, r.index, 2)
        self.assertRaises(ValueError, r.index, 6)

        r = xrange(5, 2, -2)
        self.assertEqual(1, r.index(3))
        self.assertEqual(0, r.index(5))
        self.assertRaises(ValueError, r.index, 2)
        self.assertRaises(ValueError, r.index, 6)

    def test_count(self):
        r = xrange(1)
        self.assertEqual(0, r.count(-1))
        self.assertEqual(1, r.count(0))
        self.assertEqual(0, r.count(1))

        r = xrange(0, 5, 2)
        self.assertEqual(0, r.count(-1))
        self.assertEqual(1, r.count(0))
        self.assertEqual(0, r.count(1))
        self.assertEqual(1, r.count(2))
        self.assertEqual(0, r.count(3))
        self.assertEqual(1, r.count(4))
        self.assertEqual(0, r.count(5))

        r = xrange(5, 0, -1)
        self.assertEqual(0, r.count(-1))
        self.assertEqual(0, r.count(0))
        self.assertEqual(1, r.count(1))
        self.assertEqual(1, r.count(2))
        self.assertEqual(1, r.count(3))
        self.assertEqual(1, r.count(4))
        self.assertEqual(1, r.count(5))
        self.assertEqual(0, r.count(6))

    def test_contains(self):
        r = xrange(5)
        self.assertFalse(-1 in r)
        self.assertTrue(1 in r)
        self.assertTrue(4 in r)
        self.assertFalse(5 in r)

        r = xrange(0, 5, 2)
        self.assertFalse(-1 in r)
        self.assertTrue(0 in r)
        self.assertFalse(1 in r)
        self.assertTrue(2 in r)
        self.assertFalse(3 in r)
        self.assertTrue(4 in r)
        self.assertFalse(5 in r)

        r = xrange(5, 0, -1)
        self.assertFalse(-1 in r)
        self.assertFalse(0 in r)
        self.assertTrue(1 in r)
        self.assertTrue(2 in r)
        self.assertTrue(3 in r)
        self.assertTrue(4 in r)
        self.assertTrue(5 in r)
        self.assertFalse(6 in r)

    def test_iter_basic(self):
        self.assertEqual(
            [],
            [x for x in xrange(0)])

        self.assertEqual(
            [0],
            [x for x in xrange(1)])

        self.assertEqual(
            [0, 1, 2],
            [x for x in xrange(3)])

        self.assertEqual(
            [0, 2, 4],
            [x for x in xrange(0, 5, 2)])

        self.assertEqual(
            [5, 3, 1],
            [x for x in xrange(5, 0, -2)])

        iterator = iter(xrange(5))
        self.assertTrue(iterator is iter(iterator))

    def test_reversed(self):
        self.assertEqual(reversed(xrange(1)), xrange(0, -1, -1))
        self.assertEqual(reversed(xrange(5)), xrange(4, -1, -1))
        self.assertEqual(reversed(xrange(1, 5)), xrange(4, 0, -1))
        self.assertEqual(reversed(xrange(5, 1, -1)), xrange(2, 6, 1))

    def test_getitem(self):
        r = xrange(0)
        self.assertRaises(IndexError, getitem, r, -1)
        self.assertRaises(IndexError, getitem, r, 0)
        self.assertRaises(IndexError, getitem, r, 1)

        r = xrange(1)
        self.assertRaises(IndexError, getitem, r, -2)
        self.assertEqual(0, r[-1])
        self.assertEqual(0, r[0])
        self.assertRaises(IndexError, getitem, r, 1)

        r = xrange(3)
        self.assertRaises(IndexError, getitem, r, -4)
        self.assertEqual(0, r[-3])
        self.assertEqual(2, r[-1])
        self.assertEqual(0, r[0])
        self.assertEqual(2, r[2])
        self.assertRaises(IndexError, getitem, r, 3)

        r = xrange(1, 4)
        self.assertRaises(IndexError, getitem, r, -4)
        self.assertEqual(1, r[-3])
        self.assertEqual(3, r[-1])
        self.assertEqual(1, r[0])
        self.assertEqual(3, r[2])
        self.assertRaises(IndexError, getitem, r, 3)

        r = xrange(3, 0, -1)
        self.assertRaises(IndexError, getitem, r, -4)
        self.assertEqual(3, r[-3])
        self.assertEqual(1, r[-1])
        self.assertEqual(3, r[0])
        self.assertEqual(1, r[2])
        self.assertRaises(IndexError, getitem, r, 3)

    def test_getitem_slice(self):
        r = xrange(10)

        self.assertRaises(ValueError, getitem, r, slice(1, 2, 0))

        self.assertEqual(r[:], xrange(10))
        self.assertEqual(r[::], xrange(10))
        self.assertEqual(r[::1], xrange(10))
        self.assertEqual(r[::2], xrange(0, 10, 2))

        self.assertEqual(r[::-1], xrange(9, -1, -1))
        self.assertEqual(r[::-2], xrange(9, -1, -2))

        self.assertEqual(r[1:2], xrange(1, 2))
        self.assertEqual(r[1:9], xrange(1, 9))
        self.assertEqual(r[1:-1], xrange(1, 9))

        self.assertEqual(r[-20:-1], xrange(0, 9))
        self.assertEqual(r[-20:-19], xrange(0, 0))

    def test_len(self):
        r = xrange(0)
        self.assertEqual(0, len(r))

        r = xrange(1)
        self.assertEqual(1, len(r))

        r = xrange(10)
        self.assertEqual(10, len(r))

        r = xrange(3, 5)
        self.assertEqual(2, len(r))

        r = xrange(3, 5, 2)
        self.assertEqual(1, len(r))

        r = xrange(5, 3, -1)
        self.assertEqual(2, len(r))

        r = xrange(5, 3, -2)
        self.assertEqual(1, len(r))

    def test_large_nums(self):
        r = xrange(2**64 + 1)
        self.assertEqual(r._len, 2**64 + 1)
        # note, however, that you can't use len() on
        # such an xrange, as the return value of len()
        # must be expressable as a C (unsigned?) long

        self.assertEqual(r[0], 0)
        self.assertEqual(r[-1], 2**64)

if __name__ == '__main__':
    unittest.main()

