from flask import Flask, request, render_template
from google.cloud import translate

credentials_json = ''
client = translate.Client.from_service_account_json(credentials_json)

def a_to_b(text, a, b):
    result = client.translate(text, source_language=a, target_language=b)
    return result['translatedText']

def de_to_sv(text):
    return a_to_b(text, 'de', 'sv')

def de_to_is(text):
    return a_to_b(text, 'de', 'is')

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def page():
    german = request.form.get('text')
    if german:
        sverige = de_to_sv(german).lower()
        icelandic = de_to_is(german).lower()
        return render_template('page.html', sverige=sverige, icelandic=icelandic)
    else:
        return render_template('page.html')

