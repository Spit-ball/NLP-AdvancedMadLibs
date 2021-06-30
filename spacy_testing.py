# import required modules
import spacy


def languageProcessing(userInput):
    nlp = spacy.load("en_core_web_sm")

    # returns a document of object
    doc = nlp(userInput)

    # checking if it is a noun or not
    if doc[0].tag_ == 'NNP':
        print(userInput, "is a noun.")
    else:
        print(userInput, "is not a noun.")

    if doc[0].tag_ == 'VBG':
        print(userInput, "is a verb.")
    else:
        print(userInput, "is not a verb.")
# def return_variable():
#    return
