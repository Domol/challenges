from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    return open(DICTIONARY, 'r').read().split('\n')[:-1]

WORD_LIST = load_words()
def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[x.upper()] for x in word if x not in ['.','-']])


def max_word_value(word_list=WORD_LIST):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    values = [calc_word_value(x) for x in word_list]
    index = max(xrange(len(values)), key=values.__getitem__)

    return word_list[index]

if __name__ == "__main__":
    a = load_words()
    print len(a)
