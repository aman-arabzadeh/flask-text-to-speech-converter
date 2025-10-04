from gtts.lang import tts_langs
# this script lists all supported languages by gTTS
AVAILABLE_LANGUAGES = tts_langs()
for code, name in AVAILABLE_LANGUAGES.items():
    print(f"Language: {name}, language code: {code}")
