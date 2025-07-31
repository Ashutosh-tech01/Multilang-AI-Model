from transformers import pipeline

# Load translation model (English to Hindi)
translator = pipeline("translation_en_to_hi")

def translate_text(text):
    result = translator(text, max_length=100)[0]['translation_text']
    return result

if __name__ == "__main__":
    print("Multi-language Content Translator")
    user_input = input("Enter content to translate: ")
    print("Translated Output:")
    print(translate_text(user_input))
