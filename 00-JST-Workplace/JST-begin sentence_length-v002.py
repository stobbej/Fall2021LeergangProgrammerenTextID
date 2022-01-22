# Fall 2021 - Leergang Programmeren TextID
# file          :   JST-begin/py
# date          :   2022-01-21
# author        :   StobbeJ
#
# Opdracht: Tekstidentificatie
#
# Naam: Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#

from typing import OrderedDict

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

        with open(filename, encoding='utf-8') as file:
            input       = file.read().replace("\n"," ").rstrip("")              # vervang EndOfLine met een spatie
            # moeten we op termijn de inhoud van een tekstbestand schonen van vreemde technische karakters?
            # input       =   file.read() 
            input       = input.replace("\"", " ")                              # vervang " met een spatie
            self.text   = input
            
        return self.text
        
    def make_sentence_lengths(self):
        """
        method:     De methode bepaalt de lengte van zinnen en voert een count uit op identieke zinlengte
        argument:   self
        return:     sentence_lengths, as dictionary {lengte sentence: count}
        """
        
        from nltk.tokenize import sent_tokenize, word_tokenize          # import natural language processing
        from collections import Counter                                 # import Counter voor tellen
        
        end_interpunctie = [".", "!", "?"]                              # definitie van zinseinde
                                                                        # definitie van overige interpunctie
        nonend_interpunctie = [";", ":", ",", "-", "&", "-", "(", ")", "{", "}", "[", "]", "<", ">", '"', "'", "....", "...", "..", "`", "”", "“", "''", "``", "--"]
        lenght_zinnen = []                                              # init dict length_zinnen

        sentences       = sent_tokenize(self.text)                      # knip tekst op in zinnen

        for sentence in sentences:                                      # doorloop alle zinnnen
            print("Zin:            ", sentence)                         # TEST-STAP
            word_count  = 0                                             # init woorden teller
            words       = word_tokenize(sentence)                       # knip zin op in woorden, interpuntie wordt woord
            print("Woorden:        ", words)                            # TEST-STAP
            for word in words:                                          # doorloop alle woorden
                if word not in end_interpunctie and word not in nonend_interpunctie:          # als woord niet interpunctie is dan
                    word_count += 1                                     # verhoog woorden teller met 1
            print("Woorden teller: ", word_count)                       # TEST-STAP
            lenght_zinnen   += [word_count]                             # plaats woorden teller dict
                       
        self.sentence_lengths = dict(Counter(lenght_zinnen))            # score zinnen met zelfde lengte
        
        return self.sentence_lengths  
            
##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = """C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\"""
tekstbestand        = "test.txt"
# tekstbestand        = "HP1.txt"
# tekstbestand        = "HP2.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################
# Hier kan je dingen testen...
tm = TextModel()
tm.read_text_from_file(path_tekstbestanden+tekstbestand)

dict = tm.make_sentence_lengths()
sorted_dict = OrderedDict(sorted(dict.items()))
print(sorted_dict)

assert tm.sentence_lengths == {5: 1, 16: 1, 6: 1, 3: 1}