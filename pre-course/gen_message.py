import random

class WordGen:
    """
    The class holds some messages and will return a random one on call
    """   
    def __init__(self, possible_messages: str):
        """
        Initialize the word generator with a given word.

        :param word: The word to be stored.
        """
        # The word to be stored
        self.m_messages = possible_messages

      
    def select_word(self):
        """
        Return a random word from the stored word list.
        :return: A random word from the stored word list.
        """
        return random.choice(self.m_messages)
    
    def get_word(self):
        """
        Retrieve the stored word.
        :return: The stored word.
        """
        # Return the stored word
        return self.select_word()
        
        
