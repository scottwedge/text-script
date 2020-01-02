from pynput.keyboard import Listener
from Logger import Logger


# Class catches individual words as they are typed
class WordCatcher:

    def __init__(self, log):

        # Creates instance wide log variable
        self.log = log.log

        # Temporary word variable
        self.word_in_progress = False
        self.current_word = ""

        # Current key and KeyData
        self.key = None
        self.keydata = None

        # Delimiter
        self.delimiter = "#"

        self.log.debug("WordCatcher has been initialized.")

    def word_builder(self, key):
        """
        word_test should listen for the delimiter. If delimiter is pressed, this method should:
        - append following letters to word
        - keep a count of appended letters
        - remove letters when Key.backspace is pressed, and reduce count
        - print word when tab, space, or backspace is pressed
        - delete word after it is printed

        :param key:
        :return:
        """

        # Sets keypress to instance key value
        self.key = key

        # Converts to raw value string
        self.keycode_to_keydata()

        # Checks delimiter
        self.delimiter_check()

        # Checks if word has ended
        self.word_end_check()

        # Checks for backspace
        self.backspace_check()

        # Appends letter if word is in progress
        self.letter_append()

    def keycode_to_keydata(self):
        """
        Converts KeyCode to raw key value.
        """

        # Converts KeyData to string, strips ' from result
        self.keydata = str(self.key)
        self.keydata = self.keydata.strip("'")

        print(self.keydata)

    def delimiter_check(self):
        """
        Checks if delimiter has been entered
        """

        if self.keydata == self.delimiter and self.word_in_progress is True:
            # If delimiter is entered but there is a word in progress, clear the word and start anew
            self.clear_current_word()
            self.word_in_progress = True

            self.log.debug("Delimiter detected while word in progress.")

        elif self.keydata == self.delimiter and self.word_in_progress is False:
            # If delimiter is entered, start a new word
            self.word_in_progress = True

            self.log.debug("Delimiter detected. Starting new word.")

    def word_end_check(self):
        """
        Checks if Key.tab, Key.space, or Key.enter is pressed. Prints word if pressed.
        """

        if self.keydata == "Key.tab" or self.keydata == "Key.space" or self.keydata == "Key.enter":

            self.log.debug(f"Word has ended: {self.current_word}\n")

            # Clears current word
            self.clear_current_word()

    def backspace_check(self):

        if self.keydata == "Key.backspace":

            # Removes last letter from word
            self.current_word = self.current_word[:-1]

    def letter_append(self):
        """
        Appends the letter to self.current_word if self.word_in_progress is true
        """

        if self.word_in_progress is True and len(self.keydata) == 1:

            # Adds letter to the word
            self.current_word += self.keydata

            self.log.debug(f"Appended {self.keydata} to self.current_word.")

    def clear_current_word(self):

        self.current_word = ""
        self.word_in_progress = False

        self.log.debug("self.current_word changed to False.")


class TextTyper:
    pass


if __name__ == "__main__":

    # Creates instance of Logger
    l = Logger()
    l.log.debug("Program started from TextController.py. Debugging.")

    # Creates instance of WordCatcher
    w = WordCatcher(l)

    # Starting listener
    with Listener(on_press=w.word_builder) as listener:
        listener.join()