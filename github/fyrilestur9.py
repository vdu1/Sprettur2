# =============================================================================
# 47 Prufa. Abstract class og erfðir frh.
# Abstract base methods/Interface
# Overriding
# =============================================================================

from abc import ABC, abstractmethod

#Abstract Interface class cannot be instantiated
class Shape(object):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
#Concreate class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width= 8
        self.height= 5
        super(Rectangle, self).__init__()
    def area(self):
        print('Using Rectangle area method')
        return (self.width*self.height)*10
    def perimeter(self):
        return self.width*2 + self.height*2

#Concreate class
class Sqaure(Rectangle):
    def __init__(self, side_lenght):
        self.side_lenght= side_lenght
        super(Sqaure, self).__init__(side_lenght, side_lenght)

    #Override Ractangle area method
    def area(self):
        print('Using Square area method')
        print (self.width*self.height*10)
        return self.side_lenght*self.side_lenght

def main():
    s1= Rectangle(6, 6)
    s2= Sqaure(5)
    print(s1.area())
    print(s2.area())

if __name__ == '__main__':
    main()
#print(s2.perimeter())

# =============================================================================
# 48 Prufa.Unittest
# =============================================================================
import unittest
from bankareikningur import Bankareikningur
from subprocess import call

class Testbankareikningur(unittest.TestCase):
    call(['clear'])
    a= Bankareikningur()
    def setUp(self):
        self.func= Bankareikningur()
        self.b= 0

    def test_1(self):
        self.assertTrue(True)
    def test_2(self):
        self.assertEqual(self.func.inneign, 0)
    def test_3(self):
        self.assertEqual(self.func.inneign, 0)
    def test_4(self):
        self.func.inneign += 4*10**(-8)     #0.00000004
        self.assertAlmostEqual(self.func.inneign, 0)
    def test_5(self):
        self.b= int(self.func.inneign)
    def test_6_leggja_inn(self):
        self.assertEqual(self.func.leggja_inn(100000),False)
        self.assertEqual(self.func.str1,' ')
    def test_7_taka_ut(self):
        self.assertEqual(self.func.taka_ut(1000), False)
    #    self.assertRaises(ValueError, self.func.saekja_stodu())

if __name__ == '__main__':
    unittest.main()
