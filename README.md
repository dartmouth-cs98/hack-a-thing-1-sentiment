## Hack-a-Thing 1: Sentiment and Entity Analysis
## Emily Lin and Helen He

### Files

- `hacktivity.py`: contains functions to start the application, analyze files, and display the results through a GUI interface  
- `util.py`: contains helper functions to convert .pdf and .doc(x) files into text files. This code is derived from David Burke's code available on GitHub.
-  `My Project-18f01ab781d8.json`: used for authentication of Google API account
-  `api_examples.py`: contains examples of Google API calls. This file is from a Google API tutorial.

### Usage

1. Start the application by running `python hacktivity.py`.
2. Select a PDF, Word, or text file that you wish to analyze. 
3. The application will display the results of running sentiment and entity analyses using Google's Natural Language API.

### What we built

We used the Google Cloud Natural Language API tutorial to build a application that performs sentiment and entity analysis on a PDF, Word, or text file. 

The sentiment analysis consists of giving the file both a score and a magnitude. The score, which ranges from -1.0 to 1.0, gives an indication of the pverall tone of the file. Score below 0 are negative, while scores above 0 are positive. The magnitude, which is always greater than 0, gives an indication of how much negative/positive content is present within the document. It is calculated as the sum of the absolute values of the scores given to each sentence in the document.

The entity analysis provides to the user information about the entities in the text. An entity can be thought of as a "noun." The application that we built returns 10 most important entities in a file, ranked based on entity salience, the relevance of the entity to the entire document text.

The immediate relevant use that we came up for this application was for students to get a quick sense of the content of their readings prior to starting on them. 

### Who did what

Emily set up Google API calls for sentiment and entity analysis.
    
Helen implemented the simple GUI interface and wrote the README.

### What we learned

We learned:

- that even seemingly simple instructions are not simple - setting up and authenticating APIs can be frustrating.
- how to set up Google Cloud accounts, and the fact that Google has a number of cool APIs that can be used during your free 12 month trial.
- some PyQt commands.
- useful text conversion functions.

### What didn't work
- The application crashed when it analyzed files with special characters (accent marks on German characters, for example). We fixed this by encoding and decoding the text file.
- The application wasn't able to analyze a PDF document that we provided that was comprised of scanned images instead of text. We realized that we would have to implement image-to-text capabilities for this to work.




