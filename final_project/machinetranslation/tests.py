import unittest

from translator import frenchToEnglish,englishToFrench

class enfrtranslatortest(unittest.TestCase)
   def test_null():
       self.assertEqual(french_to_english(""), "")
       self.assertEqual(english_to_french(""), "")

   def test_greetings():
       self.assertEqual(french_to_English("Bonjour"), "Hello")
       self.assertEqual(english_to_french("Hello"), "Bonjour")
       self.assertEqual(french_to_english("Au revoir"), "Good bye")
       self.assertEqual(english_to_french("Good bye"), "Au revoir")
        