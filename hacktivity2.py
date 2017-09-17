"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
import operator

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def print_result(sentiment_result, entities_result, filename):
    score = sentiment_result.document_sentiment.score
    magnitude = sentiment_result.document_sentiment.magnitude
    print('\nHere are the results for your file {}!\n'.format(filename))

    print('********* SENTIMENT ANALYSIS *********\n')

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

    print('Your document has a overall sentiment score of {} with a magnitude of {}. This means that this document is {} in tone.\n'.format(
        score, magnitude, sentiment))

    print('********** ENTITY ANALYSIS **********\n')

     # Entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    entity_dict = dict()

    for entity_result in entities_result:
        entity_dict[entity_result.name] = (entity_result.salience, entity_result.type)

    sorted_entities = sorted(entity_dict.items(), key=operator.itemgetter(1), reverse=True)

    print('These are the most important key words in your document, ordered from most important to least important')

    for entity in sorted_entities:
        print('----------')
        print('Word: {}\nType: {}\nImportance: {}'.format(entity[0], entity[1][1], entity[1][0]))


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
    print_result(sentiment_result, entities_result, filename)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     description=__doc__,
    #     formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument(
    #     'filename',
    #     help='The filename of the text you\'d like to analyze.')
    # args = parser.parse_args()

    print("*************************************************")
    print("* Welcome to the Sentiment and Entity Analyzer! *")
    print("************************************************* \n")

    filename = raw_input("Which file would you like to analyze? ")

    analyze(filename)
    