"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
<<<<<<< HEAD
import json
import sys
=======
>>>>>>> 590ca1c... sent analysis tutorial

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

<<<<<<< HEAD
import googleapiclient.discovery


def print_sentiment_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

=======

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

>>>>>>> 590ca1c... sent analysis tutorial
    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


<<<<<<< HEAD
<<<<<<< HEAD
def analyze_entities(text, encoding='UTF32'):
    entities = client.analyze_entities(document=document)
    entity_dict = dict()

    for entity in entities.entities:
        if entity_dict.get(entity, -1) == -1:
            entity_dict[entity] = 1
        else:
            entity_dict[entity] = entity_dict.get(entity) + 1
    
    


def analyze_sentiment(filename):
    annotations = client.analyze_sentiment(document=document)
    # Print the results
    print_result(annotations)


def analyze_syntax(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding
    }

    service = googleapiclient.discovery.build('language', 'v1')

    request = service.documents().analyzeSyntax(body=body)
    response = request.execute()

    return response


def analyze(filename):
    client = language.LanguageServiceClient()

    with open(filename, 'r') as review_file:
=======
def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(movie_review_filename, 'r') as review_file:
>>>>>>> 590ca1c... sent analysis tutorial
=======
def analyze(filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(filename, 'r') as review_file:
>>>>>>> b2fac4f... entity analysis
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
<<<<<<< HEAD

    analyze_sentiment(filename, client)
    analyze_entities(filename, client
    
=======
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)
>>>>>>> 590ca1c... sent analysis tutorial


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
<<<<<<< HEAD
<<<<<<< HEAD
        'filename',
        help='The filename of the text you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.filename)
=======
        'movie_review_filename',
        help='The filename of the movie review you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.movie_review_filename)
>>>>>>> 590ca1c... sent analysis tutorial
=======
        'filename',
        help='The filename of the text you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.filename)
>>>>>>> b2fac4f... entity analysis
