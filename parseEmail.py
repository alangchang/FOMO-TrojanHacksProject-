import os
import six
import argparse
import sys
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\Alan Chang\\Downloads\\FOMO-2b64149f8e8e.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"

def entities_text(text):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens
    entities = client.analyze_entities(document).entities

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    naturalParse = []
    Ndict = {}
    for token in tokens:
        if pos_tag[token.part_of_speech.tag] == 'NOUN':
            if token.text.content == 'Monday' or token.text.content == 'Tuesday' or token.text.content == 'Wednesday' or token.text.content == 'Thursday' or token.text.content == 'Friday' or token.text.content == 'Saturday'or token.text.content == 'Sunday':
                Ndict['weekday']=token.text.content.title()
                # nouns.append(token.text.content)
            if token.text.content == 'January' or token.text.content == 'February' or token.text.content == 'March' or token.text.content == 'April' or token.text.content == 'May' or token.text.content == 'June' or token.text.content == 'July' or token.text.content == 'August' or token.text.content == 'September' or token.text.content == 'October' or token.text.content == 'November' or token.text.content == 'December':
                Ndict['month']=token.text.content.title()
                # months.append(token.text.content)

    return Ndict
