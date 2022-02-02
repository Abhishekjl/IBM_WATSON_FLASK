import json
import ibm_watson
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
api_key = 'LpSHy8YtJJmaIkh5MHwROU2U5h3F-u6DNlCPglV0ywqq'
api_url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/0ca47149-4943-4a5c-8f5d-81afe80463c6'
eng2fr = 'en-fr'
fr2eng = 'fr-en'
text_to_translate = 'Your content you want translate here'

# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(api_url )



def englishToFrench(englishText):
    translated = language_translator.translate(
    text=englishText,
    model_id=eng2fr).get_result()

    frenchText = translated['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    translated = language_translator.translate(
    text=frenchText,
    model_id=fr2eng).get_result()

    englishText = translated['translations'][0]['translation']
    return englishText


