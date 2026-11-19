from deep_translator import GoogleTranslator

print("===== LANGUAGE TRANSLATION TOOL =====")

text = input("Enter your text: ")

source = input("Enter source language (en, ta, hi): ")
target = input("Enter target language (en, ta, hi): ")

try:
    translator = GoogleTranslator(source=source, target=target)
    result = translator.translate(text)

    print("\nTranslated Text:")
    print(result)

except Exception as e:
    print("Translation error:", e)
