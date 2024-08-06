from tokenizer import clean_text
import re

def test_clean_text():
    #Given: a string _text_ of text with words
    #When: the text is passed to function clean_text()
    #Then: should return a text with lower case without punctuation
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    for string in text:
        if re.search(' .|,|" ', string):
            assert clean_text(text) != text



if __name__=="__main__":

    data =  '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_ '''
    test_clean_text(data)
