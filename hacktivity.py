"""Demonstrates how to make a simple call to the Natural Language API."""

import operator

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog, QLineEdit, QDialog, QMessageBox

def display_result(sentiment_result, entities_result, filename):
    score = sentiment_result.document_sentiment.score
    magnitude = sentiment_result.document_sentiment.magnitude

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

    entity_dict = dict()
    for entity_result in entities_result:
        entity_dict[entity_result.name] = (entity_result.salience, entity_type[entity_result.type])
    sorted_entities = sorted(entity_dict.items(), key=operator.itemgetter(1), reverse=True)
    entity_type = ('unknown', 'person', 'location', 'organization',
                   'event', 'work of art', 'consumer good', 'other')

    complete = QMessageBox()
    complete.setWindowTitle("Sentiment and Entity Analyzer")
    complete.setText('\nAnalysis is complete! Here are the results for your file.\n')
    return_value = complete.exec()

    sent_string = "********* SENTIMENT ANALYSIS *********\n" + 
        "Your document has a overall sentiment score of {} with a magnitude of {}. This means that this document is {} in tone.\n".format(score, magnitude, sentiment)
    sent_window = QMessageBox()
    sent_window.setWindowTitle("Sentiment and Entity Analyzer")
    sent_window.setText(sent_string)
    return_value = sent_window.exec()

    ent_string = "********** ENTITY ANALYSIS **********\n" + 
        "These are the most important key words in your document, ordered from most important to least important:"
    for entity in sorted_entities:
        ent_string += "----------"
        ent_string += "Word: {}\nType: {}\nImportance: {}".format(entity[0], entity[1][1], entity[1][0])
    ent_window = QMessageBox()
    ent_window.setWindowTitle("Sentiment and Entity Analyzer")
    ent_window.setText(sent_string)
    return_value = ent_window.exec()

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
    entity_type = ('unknown', 'person', 'location', 'organization',
                   'event', 'work of art', 'consumer good', 'other')

    entity_dict = dict()

    for entity_result in entities_result:
        entity_dict[entity_result.name] = (entity_result.salience, entity_type[entity_result.type])

    sorted_entities = sorted(entity_dict.items(), key=operator.itemgetter(1), reverse=True)

    print('These are the most important key words in your document, ordered from most important to least important:')

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

    display_result(sentiment_result, entities_result, filename)


if __name__ == '__main__':


    # print("*************************************************")
    # print("* Welcome to the Sentiment and Entity Analyzer! *")
    # print("************************************************* \n")

    # filename = raw_input("Which file would you like to analyze? ")
    
    app = QApplication(sys.argv)
    gui = QWidget()
    welcome = QMessageBox()
    welcome.setWindowTitle("Sentiment and Entity Analyzer")
    welcome.setText("*************************************************\n"
                    "* Welcome to the Sentiment and Entity Analyzer! *\n"
                    "*************************************************\n"
                    "Please choose a text file.")
    return_value = welcome.exec()

    files = QFileDialog.getOpenFileName(gui, "Sentiment and Entity Analyzer")
    filename = files[0]
    #analyze(filename)
    print(filename)

    sys.exit()


