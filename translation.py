import requests
import uuid


def translate_text(text, to_lang):
    key = "0b5be4f9a9f24f4da3fe8dd673219a66"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "centralindia"
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': "en",
        'to': to_lang
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    lines = text.splitlines()
    translated_lines = []

    for line in lines:
        body = [{
            'text': line
        }]
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        translated_text = response[0]['translations'][0]['text']
        translated_lines.append(translated_text)

    translated_text = '\n'.join(translated_lines)
    return translated_text
