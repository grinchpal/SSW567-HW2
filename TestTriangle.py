# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        print(classifyTriangle(3,4,5))

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')

    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,2,1),'Isoceles','2,2,1 should be isoceles')

    def testNotTriangles(self): 
        self.assertEqual(classifyTriangle(1,3,1),'NotATriangle','1,3,1 should be not a triangle')

    def testValidInput1(self): 
        self.assertEqual(classifyTriangle("a","x","b"),'InvalidInput','"a","x","b" should be invalid input')

    def testValidInput2(self): 
        self.assertEqual(classifyTriangle(201,2,1),'InvalidInput','201,2,1 should be invalid input')

    def testValidInput3(self): 
        self.assertEqual(classifyTriangle(2,201,1),'InvalidInput','2,201,1 should be invalid input')

    def testValidInput4(self): 
        self.assertEqual(classifyTriangle(2,2,1000),'InvalidInput','2,2,1000 should be invalid input')

    def testValidInput5(self): 
        self.assertEqual(classifyTriangle(0,2,1),'InvalidInput','0,2,1 should be invalid input')

    def testValidInput6(self): 
        self.assertEqual(classifyTriangle(2,-1,1),'InvalidInput','2,-1,1 should be invalid input')

    def testValidInput7(self): 
        self.assertEqual(classifyTriangle(2,1,-1),'InvalidInput','2,1,-1 should be invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

