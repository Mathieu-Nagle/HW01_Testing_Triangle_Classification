import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    if(a == b == c):
        return 'Equilateral'

    elif(a == b or a == c or b == c):
        if(a**2 + b**2 == c**2):
            return 'Right'
        return 'Isoceles'

    else:
        if(a**2 + b**2 == c**2):
            return 'Right'
        return 'Scalene'
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    def testSet1(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertNotEqual(classifyTriangle(1,2,3),'Right','1,2,3 is not a Right triangle')
        
    def testMyTestSet2(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')
        self.assertNotEqual(classifyTriangle(1,3,5),'Equilateral','Should be Scalene')
        self.assertEqual(classifyTriangle(1,3,3),'Isoceles','1,3,3 should be Isoceles')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        self.assertNotEqual(classifyTriangle(10,10,10),'Scalene','Should be Equilateral')

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(1,2,1)
    runClassifyTriangle(3,4,5)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       
