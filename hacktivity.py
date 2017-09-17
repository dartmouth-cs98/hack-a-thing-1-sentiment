"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
<<<<<<< HEAD:hacktivity2.py
<<<<<<< HEAD
import operator
=======
>>>>>>> 30bc927... Added print statements and consolidated sentiment and entity analyses
=======
import operator
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

<<<<<<< HEAD:hacktivity2.py
<<<<<<< HEAD

def print_result(sentiment_result, entities_result, filename):
    score = sentiment_result.document_sentiment.score
    magnitude = sentiment_result.document_sentiment.magnitude
    print('\nHere are the results for your file {}!\n'.format(filename))

    print('********* SENTIMENT ANALYSIS *********\n')
=======
import easygui


def print_result(sentiment_result, entities_result, filename):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    print('Here are the results for your file {}!'.format(filename))

    print('********* SENTIMENT ANALYSIS *********')
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))
    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
>>>>>>> 30bc927... Added print statements and consolidated sentiment and entity analyses
=======

def print_result(sentiment_result, entities_result, filename):
    score = sentiment_result.document_sentiment.score
    magnitude = sentiment_result.document_sentiment.magnitude
    print('\nHere are the results for your file {}!\n'.format(filename))

    print('********* SENTIMENT ANALYSIS *********\n')
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py

    if score >= 0.5:
        sentiment = "clearly positive"
    elif score >= 0.2:
        sentiment = "positive"
    elif score > -0.2 and magnitude < 2:
        sentiment = "neutral"
    elif score > -0.2 and magnitude >= 2:
        sentiment = "mixed"
    elif score > -0.5:
        sentiment = "negative"
    else:
        sentiment = "clearly negative"

<<<<<<< HEAD:hacktivity2.py
<<<<<<< HEAD
=======
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py
    print('Your document has a overall sentiment score of {} with a magnitude of {}. This means that this document is {} in tone.\n'.format(
        score, magnitude, sentiment))

    print('********** ENTITY ANALYSIS **********\n')
<<<<<<< HEAD:hacktivity2.py
=======
    print('********** ENTITY ANALYSIS **********')
>>>>>>> 30bc927... Added print statements and consolidated sentiment and entity analyses
=======
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py

     # Entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

<<<<<<< HEAD:hacktivity2.py
<<<<<<< HEAD
=======
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py
    entity_dict = dict()

    for entity_result in entities_result:
        entity_dict[entity_result.name] = (entity_result.salience, entity_result.type)

    sorted_entities = sorted(entity_dict.items(), key=operator.itemgetter(1), reverse=True)

    print('These are the most important key words in your document, ordered from most important to least important:')

    for entity in sorted_entities:
        print('----------')
        print('Word: {}\nType: {}\nImportance: {}'.format(entity[0], entity[1][1], entity[1][0]))

<<<<<<< HEAD:hacktivity2.py
=======
    for entity in entities:
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
        print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
    return 0
>>>>>>> 30bc927... Added print statements and consolidated sentiment and entity analyses
=======
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py

def analyze(filename):
    """Run analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()
    with open(filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment_result = client.analyze_sentiment(document=document)
    entities_result = client.analyze_entities(document=document).entities

    # Print the results
<<<<<<< HEAD:hacktivity2.py
<<<<<<< HEAD
    print_result(sentiment_result, entities_result, filename)


if __name__ == '__main__':
=======
    print_result(sentiment_result, enities_result, filename)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     description=__doc__,
    #     formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument(
    #     'filename',
    #     help='The filename of the text you\'d like to analyze.')
    # args = parser.parse_args()
>>>>>>> 30bc927... Added print statements and consolidated sentiment and entity analyses
=======
    print_result(sentiment_result, entities_result, filename)


if __name__ == '__main__':
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py

    print("*************************************************")
    print("* Welcome to the Sentiment and Entity Analyzer! *")
    print("************************************************* \n")

<<<<<<< HEAD:hacktivity2.py
<<<<<<< HEAD
    filename = raw_input("Which file would you like to analyze? ")
=======
    filename = raw_input("Which file would you like to analyze?")
>>>>>>> 30bc927... Added print statements and consolidated sentiment and entity analyses
=======
    filename = raw_input("Which file would you like to analyze? ")
>>>>>>> 2721624... using both sentiment and text analysis:hacktivity.py

    analyze(filename)
    