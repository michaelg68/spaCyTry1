# https://realpython.com/natural-language-processing-spacy-python/

import spacy

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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #my_func1()
    my_func2()

