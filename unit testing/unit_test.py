# import package unittest
import unittest


class TestStringMethod(unittest.TestCase):
    # test case pertama
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    # test case kedua
    def test_isalnum(self):
        self.assertTrue('coding'. isalnum())
        self.assertFalse('coding'.isalnum())

    # test case ketiga
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)

        # cek s.index gagal jika tidak ditemukan
        s.index('decode')


if __name__ == '__main__':
    # run test
    unittest.main()
