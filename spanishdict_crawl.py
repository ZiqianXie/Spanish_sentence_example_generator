from requests_html import HTMLSession
import re


session = HTMLSession()
pattern = re.compile('<strong>(.+)</strong>')
def process_text(html):
    text = html.text
    word = re.findall(pattern, html.html)[0]
    text = text.replace(word, f'<b>{word}</b>')
    return text


def get_examples(word):
    r = session.get(f'https://www.spanishdict.com/examples/{word}?lang=es')
    r.html.render()
    ejemplos = r.html.find("._3t88e4lk")
    examples = []
    for ejemplo, traduccion in zip(ejemplos[::2], ejemplos[1::2]):
        t1 = process_text(ejemplo)
        t2 = process_text(traduccion)
        examples.append((t1, t2))
    return examples