import unittest

from translator import french_to_english,english_to_french

class enfrtranslatortest(unittest.TestCase):
   def test_null(self):
       self.assertEqual(french_to_english(" "), " ")
       self.assertEqual(english_to_french(" "), " ")

   def test_greetings(self):
       self.assertEqual(french_to_english("Bonjour"), "Hello")
       self.assertEqual(english_to_french("Hello"), "Bonjour")
       self.assertEqual(french_to_english("Au revoir"), "Goodbye")
       self.assertEqual(english_to_french("Goodbye"), "Au revoir")
        
if __name__ == '__main__':
    unittest.main()