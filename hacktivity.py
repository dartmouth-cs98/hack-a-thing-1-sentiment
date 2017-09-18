"""Demonstrates how to make a simple call to the Natural Language API."""

import operator

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import util
import sys
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog, QLineEdit, QDialog, QMessageBox


def display_result(sentiment_result, entities_result):
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
    entity_type = ('unknown', 'person', 'location', 'organization',
                   'event', 'work of art', 'consumer good', 'other')
    for entity_result in entities_result:
        entity_dict[entity_result.name] = (entity_result.salience, entity_type[entity_result.type])

    complete = QMessageBox()
    complete.setWindowTitle("Sentiment and Entity Analyzer")
    complete.setText('\nAnalysis is complete! Here are the results for your file.\n')
    complete.exec_()

    sent_string = "********* SENTIMENT ANALYSIS *********\n" + \
        "Your document has a overall sentiment score of {:.4f} with a magnitude of {:.4f}. This means that this document is {} in tone.\n".format(score, magnitude, sentiment)
    sent_window = QMessageBox()
    sent_window.setWindowTitle("Sentiment and Entity Analyzer")
    sent_window.setText(sent_string)
    sent_window.exec_()

    ent_string = "********** ENTITY ANALYSIS **********\n" + \
        "These are the 10 most important key words in your document, ordered from most important to least important:"
    sorted_entities = sorted(entity_dict.items(), key=operator.itemgetter(1), reverse=True)

    counter = 1
    for entity in sorted_entities:
        if counter > 10:
            break
        word = entity[0].encode('utf-8')
        type = entity[1][1]
        importance = entity[1][0]
        ent_string += "\n----------\n"
        ent_string += "Word: {}\nType: {}\nImportance: {:.4f}".format(word, type, importance)
        counter += 1
    ent_window = QMessageBox()
    ent_window.setWindowTitle("Sentiment and Entity Analyzer")
    ent_window.setText(ent_string)
    ent_window.exec_()


def analyze(filename):
    # Run analysis request on text within a passed filename.
    client = language.LanguageServiceClient()
    content = util.document_to_text(filename).decode('utf-8')

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment_result = client.analyze_sentiment(document=document)
    entities_result = client.analyze_entities(document=document).entities

    display_result(sentiment_result, entities_result)

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
                    "Please choose a pdf or doc file.")
    welcome.exec_()

    files = QFileDialog.getOpenFileName(gui, "Sentiment and Entity Analyzer")
    filename = files[0]
    analyze(filename)
    sys.exit()


