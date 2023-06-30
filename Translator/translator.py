import googletrans 
from googletrans import Translator
# print(googletrans.LANGUAGES)

text1 = "My name is Moses"
text2 = "Benim adım Omo"
text3 = "اسمي أومو"

translator = Translator()

print(translator.detect(text1))
print(translator.detect(text2))
print(translator.detect(text3))

#print("Translated From Lingala to English: ",translator.translate(text2))
#print("Translated From Lingala to English: ",translator.translate(text3))

# Translating from English to Any other language
print("Translating from English to Arabic: ",translator.translate(text1,src='en',dest='ar'))
print("Translating from English to Turkish: ",translator.translate(text1,src='en',dest='tr'))

print("Translating from Arabic to English: ",translator.translate(text3,src='ar',dest='en'))