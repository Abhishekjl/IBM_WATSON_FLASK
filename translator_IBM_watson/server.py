from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
from machinetranslation import translator
app = Flask("Web Translator")

@app.route("/englishToFrench/<textToTranslate>")
def englishToFrench(textToTranslate):
    frenchText = translator.englishToFrench(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish/<textToTranslate>")
def frenchToEnglish(textToTranslate):
    englishText = translator.frenchToEnglish(textToTranslate)
    return englishText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    # host="0.0.0.0", port=8080
    app.run(debug = True)
