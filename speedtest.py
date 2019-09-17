import unittest
from speed import speed_penality

class Penality(unittest.TestCase):
    
    def test_speed_by45(self):
        result= speed_penality(45)
        self.assertEquals(result, "ok")
    def test_speed_by65(self):
        result= speed_penality(65)
        self.assertEquals(result, "€30")
    def test_speed_by90(self):
        result= speed_penality(90)
        self.assertEquals(result, "license taken")
    def test_speed_by50(self):
        result = speed_penality(50)
        self.assertEquals(result, "ok")
        
    
if __name__ == "__main__":
    unittest.main()


    




