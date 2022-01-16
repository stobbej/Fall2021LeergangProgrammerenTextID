# Fall 2021 - Leergang Programmeren TextID
# textmodel.py
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
            input       =   file.read() 
            self.text   =   input
        
        return self.text

    def make_sentence_lengths(self):
        """
        method:     De methode...blabla

        """
        pass

    def clean_string(self, s):
        """
        method:     De methode...blabla
        argument:   s, as string

        """
        pass

    def make_word_lengths(self):
        """
        method:     De methode...blabla

        """
        pass

    def make_words(self):
        """
        method:     De methode...blabla
        """
        pass

    def make_stems(self):
        """
        method:     De methode...blabla
        """
        pass

    def JSTopenJST(self):
        """
        method:     De methode...blabla
        """
        pass

    def normalize_dictionary(self, d):
        """
        method:     De methode...blabla
        argument:   d, as dictionary
        """
        pass
    
    def smallest_value(self, nd1, nd2):
        """
        method:     De methode...blabla
        argument:   nd1, as dictionary
        argument:   nd2, as dictionary
        """
        pass

    def compare_dictionaries(self, d, nd1, nd2):
        """
        method:     De methode...blabla
        argument:   d, as dictionary
        argument:   nd1, as dictionary
        argument:   nd2, as dictionary
        """
        pass

    def create_all_dictionaries(self):
        """
        method:     De methode...blabla
        """
        pass

    def compare_text_with_two_models(self, model1, model2):
        """
        method:     De methode...blabla
        argument:   model1, as object
        argument:   model2, as object
        """
        pass

# Hier kan je dingen testen...

##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = """C:\\Users\\jeroe\\GIT\\LeergangP\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\"""
tekstbestand        = "test.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################

# Hier kan je dingen testen...
tm = TextModel()
tm.read_text_from_file(path_tekstbestanden+tekstbestand)
# Zet hier aanroepen neer die het model vullen met informatie
print("TextModel:", tm)
print("inhoud", tekstbestand.upper(), ": ",tm.text)