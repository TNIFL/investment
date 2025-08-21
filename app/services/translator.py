"""
from googletrans import Translator
#영어 : en
#한국어 : ko
#일본어 : ja
#중국어 : zh-cn

def translate():
    translator = Translator()

    text = 'can you translate this sentence'

    translated = translator.translate(text, src='en', dest='ko')

    print('원문 :', text)
    print('번역 :', translated.text)
    """