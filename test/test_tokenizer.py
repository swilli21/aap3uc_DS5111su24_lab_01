from tokenizer import tokenize
# - test_bash_tokenize(): test 'tokenize' using bash
# - test_tokenize_skipper(): test function to show pytest mark and skipping
# - test_all_tokenize(): test 'tokenize on all the English texts'
# - test_corbeau_tokenize(): test 'tokenize' against snippet from Le Corbeau
#!pip install pytest


def test_tokenize():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list as return representing the words as elements in the list

    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'

    assert isinstance(tokenize(text), list), f"Tokenizer failed on sample text: {text}"


if __name__=="__main__":

    data =  '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    test_tokenize(data)
