import unittest
from translator import frenchToEnglish,englishToFrench



class french2english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("je t'aime"),'i love you' ) # test when 2 is given as input the output is 4.
        self.assertEqual(french2english('qui es-tu'),'who are you')  # test when 3.0 is given as input the output is 9.0.

class english2french(unittest.TestCase):
    def test2(self):
        self.assertEqual(english2french('My name is abhishek'),"Je m'appelle Abhishek") # test when 2 is 
        self.assertEqual(english2french('this is french'),"c'est français")
   

unittest.main()
