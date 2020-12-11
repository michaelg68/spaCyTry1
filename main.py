# https://realpython.com/natural-language-processing-spacy-python/

import spacy

def my_func():
    print("My func")
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





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    my_func()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
