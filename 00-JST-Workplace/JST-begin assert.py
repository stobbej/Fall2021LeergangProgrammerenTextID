# Fall 2021 - Leergang Programmeren TextID
# file          :   JST-begin/py
# date          :   2022-01-21
# author        :   StobbeJ
#
# Opdracht: Tekstidentificatie
#
# Naam: Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#
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
        method:     De methode...blabla

        """
        pass

# Hier kan je dingen testen...

##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = """C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\"""
tekstbestand        = "test.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################

# Hier kan je dingen testen...
tm = TextModel()
tm.read_text_from_file(path_tekstbestanden+tekstbestand)
# Zet hier aanroepen neer die het model vullen met informatie
print("TextModel:\n\n", tm)
print("inhoud", tekstbestand.upper(), ": ",tm.text)

#################### Assert ###############################################################
# 
test_text = """Dit is een korte zin. Dit is geen korte zin, omdat
deze zin meer dan 10 woorden en een getal bevat! Dit is
geen vraag, of wel?

Dat klopt helemaal! :-)"""

assert tm.text == test_text