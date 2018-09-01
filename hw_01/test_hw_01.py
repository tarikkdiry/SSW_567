import unittest
from hw_01 import classify_triangle

class Test(unittest.TestCase):
    # ================= EQUILATERAL TRIANGLES ==================
    def test01(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')
    
    def test02(self):
        self.assertEqual(classify_triangle(2, 2, 2), 'equilateral')

    def test03(self):
        self.assertEqual(classify_triangle(100, 100, 100), 'equilateral')

    # ================= ISOSCELES TRIANGLES ==================

    def test04(self):
        self.assertEqual(classify_triangle(1, 2, 2), 'isosceles')
    
    def test05(self):
        self.assertEqual(classify_triangle(2, 3, 3), 'isosceles')

    def test06(self):
        self.assertEqual(classify_triangle(100, 200, 200), 'isosceles')

    # ================= SCALENE TRIANGLES ==================

    def test07(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'scalene')
    
    def test08(self):
        self.assertEqual(classify_triangle(2, 3, 4), 'scalene')

    def test09(self):
        self.assertEqual(classify_triangle(100, 200, 300), 'scalene')

    # ================= RIGHT TRIANGLES ==================

    def test10(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'right')
    
    def test11(self):
        self.assertEqual(classify_triangle(6, 8, 10), 'right')

    def test12(self):
        self.assertEqual(classify_triangle(9, 12, 15), 'right')

    # ================= INVALID TRIANGLES ==================

    def test13(self):
        self.assertEqual(classify_triangle(-1, 1, 1), 'NotATriangle')

    def test14(self):
        self.assertEqual(classify_triangle(0, 12, 15), 'NotATriangle')
    
    def test15(self):
        self.assertEqual(classify_triangle(0, 1, 0), 'NotATriangle')




if __name__ == "__main__":
    unittest.main()