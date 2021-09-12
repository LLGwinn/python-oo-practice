"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """ Prints random words from dictionary file

        >>> new_thing = WordFinder('example.txt')
        3 words read

        >>> new_thing.random() in new_thing.words
        True

        >>> new_thing.random() in new_thing.words
        True
    """
    
    def __init__(self, file):
        """ Reads file, prints number of items in file """

        dictionary = open(file, 'r')
        self.words = self.make_word_list(dictionary)
        print(f'{len(self.words)} words read')
        dictionary.close()

    def __repr__(self):
        """ Returns representation showing length of dictionary of WordFinder instance"""
        return f'<WordFinder with length {len(self.words)}>'

    def make_word_list(self, word_list):
        """ Creates list of words from given dictionary file """

        return [word.strip() for word in word_list]

    def random(self):
        """ Prints random word from dictionary file """

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """ Prints random words from dictionary files that contain blank lines or lines that start with '#'
    
        >>> new_thing = SpecialWordFinder('special_example.txt')
        4 words read

        >>> new_thing.random() in new_thing.words
        True

        >>> new_thing.random() in new_thing.words
        True
    
    """

    def __repr__(self):
        """ Returns representation showing length of dictionary of SpecialWordFinder instance"""

        return f'<SpecialWordFinder with length {len(self.words)}>'

    def make_word_list(self, word_list):
        """ Creates list of words from given dictionary file """

        return [word.strip() for word in word_list if word[0] != '#' and word.strip() != '']

   
