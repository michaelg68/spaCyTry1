# https://realpython.com/natural-language-processing-spacy-python/
# https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
import spacy
import speech_recognition as sr

def my_func1():
    print("My func1")
    nlp = spacy.load('en_core_web_sm')
    introduction_text = ('This tutorial is about Natural Language Processing in Spacy')
    #introduction_text = ('Это проверка способностей аппликации')
    #introduction_text = ('שלום חברים')
    introduction_doc = nlp(introduction_text)
    print([token.text for token in introduction_doc])

    '''
    about_text = ('Gus Proto is a Python developer currently'
                  ' working for a London-based Fintech'
                  ' company. He is interested in learning'
                  ' Natural Language Processing.')
    '''
    about_text = ('שלום חברים.'
                  ' אני מעוניין לדבר איתכם.'
                  ' זה לא כזה חשבו, אבל עדיין!')

    about_doc = nlp(about_text)
    sentences = list(about_doc.sents)
    len(sentences)

    for sentence in sentences:
        print (sentence)


def set_custom_boundaries(doc):
    # Adds support to use `...` as the delimiter for sentence detection
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc

def my_func2():
    # ellipsis_text = ('Gus, can you, ... never mind, I forgot'
    #              ' what I was saying. So, do you think'
    #              ' we should ...')

    ellipsis_text = ('הי, מה נשמע...  לא משנה בעצם. צריך לקנות חלב.')
    # Load a new model instance
    custom_nlp = spacy.load('en_core_web_sm')
    custom_nlp.add_pipe(set_custom_boundaries, before='parser')
    custom_ellipsis_doc = custom_nlp(ellipsis_text)
    custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
    for sentence in custom_ellipsis_sentences:
        print(sentence)

def audio_file_to_text():
    print("Running audio_file_to_text function")
    filename = "resources/16-122828-0002.wav"
    #initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)

def audio_file_to_text_heb():
    print("Running audio_file_to_text_heb function")
    filename = "resources/heb_202126-231356.wav"
    #initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        #text = r.recognize_google(audio_data)
        text = r.recognize_google(audio_data, language="he-IL")
        print(text)


# Press the green button in the gutter to run the script.
def microphone_to_text():
    print("Running microphone_to_text function")
    #initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Speak now, please.")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)

def microphone_to_text_heb():
    print("Running microphone_to_text_heb function")
    #initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Speak now, please.")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data, language="he-IL")
        print(text)

if __name__ == '__main__':
    #my_func1()
    #my_func2()
    #audio_file_to_text()
    #microphone_to_text()
    #audio_file_to_text_heb()
    microphone_to_text_heb()
    
    