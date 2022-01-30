# Fall 2021 - Leergang Programmeren TextID
# file          :   begin.py
# date          :   2022-01-21
# projectgroep  :   Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#
# Opdracht: Tekstidentificatie
#
#

from cgitb import text
from string import punctuation

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
            # input       =   file.read().replace("\n", " ").rstrip()             # vervang EndOfLine met een spatie
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
        # print("Lijst van woorden :", list_of_words)                     # TEST-STAP
        word_count                  = 0                                 # init een teller word_count
        sentence_count              = []                                # init een list sentence_count
        endPunc                     = ".?!" 	                        # init einde zin

        for new_word in list_of_words:                                  # doorloop de woorden
            if new_word not in endPunc:                                 # nog steeds in dezelfde zin
                word_count          +=1                                 # verhoog de teller met een woord
                # print(word_count, new_word)                             # TEST-STAP
            if new_word[-1] in endPunc:                                 # einde zin
                sentence_count     += [word_count]                      # voeg zin-lengte toe aan list
                # print(sentence_count)                                   # TEST-STAP
                word_count          = 0                                 # zet teller word_count op nul voor nieuwe zin
                       
        for teller in sentence_count:                                   # doorloop de word_counts
            if teller in self.sentence_lengths:                         # als word_count reeds in dict
                self.sentence_lengths[teller] += 1                      # tel 1 op
            else:                                                       # als word_count niet in dict
                self.sentence_lengths[teller] = 1                       # start met 1

        return self.sentence_lengths 

    def clean_string(self, s):
        """
        Method:     De methode verwijdert interpunctie en zet alle letters in lower-case
        argument:   self, s = string
        return:     clean_string, as string
        """
        clean_string = ""                                               # init clean string als leeg     

        print(punctuation)                                              # TEST-STAP
        
        for p in punctuation:                                           # voor elke interpunctie doorloop string
            print(p)                                                    # TEST-STAP
            s = s.replace(p, "")                                        # vervang interpunctie door leeg
            print(s)                                                    # TEST-STAP
        
        clean_string = s.lower()                                        # zet string in lower caps
        print(clean_string)                                             # TEST-STAP
            
        return clean_string
            
##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = """C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\"""
tekstbestand        = "test.txt"
# tekstbestand        = "train1.txt"
# tekstbestand        = "HP1.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################
# Hier kan je dingen testen...
tm = TextModel()
tm.read_text_from_file(path_tekstbestanden+tekstbestand)
print("Orginele tekst: \n", tm.text)

clean_text = """dit is een korte zin dit is geen korte zin omdat
deze zin meer dan 10 woorden en een getal bevat dit is
geen vraag of wel

dat klopt helemaal"""
clean_s = tm.clean_string(tm.text)
print("\nSchone tekst: \n",clean_s)
assert clean_s == clean_text