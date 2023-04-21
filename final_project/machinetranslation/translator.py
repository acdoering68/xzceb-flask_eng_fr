""" Example python code for using translator service in the IBM cloud"""

import os
import json # pylint: disable=unused-import

from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ Translate given English text to French using watson cloud service""" 
    return language_translator.translate(text=english_text,model_id='en-fr').get_result()

def french_to_english(french_text):
    """ Translate given French text to English using watson cloud service"""
    return language_translator.translate(text=french_text,model_id='fr-en').get_result()
