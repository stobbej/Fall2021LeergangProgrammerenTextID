# Fall 2021 - Leergang Programmeren TextID
# file          :   JST-begin/py
# date          :   2022-01-21
# author        :   StobbeJ
#
# Opdracht: Tekstidentificatie
#
# Naam: Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#

import nltk
nltk.download()

class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        #
        # Maak dictionary's voor elke eigenschap
        #
        self.words = {}             # Om woorden te tellen
        self.word_lengths = {}      # Om woordlengtes te tellen
        self.stems = {}             # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen
        #
        # Maak een eigen dictionary
        #
        self.my_feature = {}        # Om ... te tellen

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'MIJN EIGENSCHAP:\n' + str(self.my_feature)
        return s
    
    # Voeg hier andere methodes toe.
    # Je hebt in het bijzonder methodes nodig die het model vullen.

    def read_text_from_file(self, filename):
        """
        method:     De methode plaatst de inhoud van 'filename' in de variabele 'self.text' as string
        argument:   filename, as string
        return:     self.text, as string
        """

        with open(filename) as file:
            # input       =   file.read().replace("\n", " ")            # vervang EndOfLine met een spatie
            # moeten we op termijn de inhoud van een tekstbestand schonen van vreemde technische karakters?
            input       =   file.read() 
            self.text   =   input
        
        return self.text

    def make_sentence_lengths(self):
        """
        method:     De methode bepaalt de lengte van zinnen en voert een count uit op identieke zinlengte
        argument:   self
        return:     sentence_lengths, as dictionary {lengte sentence: count}

        """
        
        list_of_words               = self.text.split()                 # zet alle woorden in een lijst
        word_count                  = 0                                 # init een teller word_count
        sentence                    = []                                # init een list sentence

        for new_word in list_of_words:                                  # doorloop de woorden
            if new_word not in ".?!":                                   # nog steeds in dezelfde zin
                word_count          +=1                                 # verhoog de teller met een woord 
            if new_word[-1] in ".?!":                                   # einde zin
                sentence            += [word_count]                     # voeg zin-lengte toe aan list
                word_count          = 0                                 # zet teller word_count op nul voor nieuwe zin
                       
        for teller in sentence:                                         # doorloop de word_counts
            if teller in self.sentence_lengths:                         # als word_count reeds in dict
                self.sentence_lengths[teller] += 1                      # tel 1 op
            else:                                                       # als word_count niet in dict
                self.sentence_lengths[teller] = 1                       # start met 1

        return self.sentence_lengths  


##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = """C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\"""
tekstbestand        = "test.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################
# Hier kan je dingen testen...
tm = TextModel()
tm.read_text_from_file(path_tekstbestanden+tekstbestand)
print(tm.make_sentence_lengths())

assert tm.sentence_lengths == {5: 1, 16: 1, 6: 1, 3: 1}