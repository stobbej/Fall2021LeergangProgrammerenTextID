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

    def clean_the_mess(self, vervang, hierdoor):
        """
        
        """
        pass

    def make_sentence_lengths(self):
        """
        method: Maakt een dictionary van de zinslengtes in het bestand.

        """

        # Replace leestekens die op einde van zin duiden.
        # We gaan nog kijken naar een cleanere methode om dit te doen, maar voor nu werkt dit.
        # Let op: er zijn 'onvolkomenheden' in de telling: 
        # mrs. (telt als zin van 1 woord)
        # nalopen van de zin met lengte 181
        clean_text_exclamation = self.text.replace("!",".")
        clean_text_question = clean_text_exclamation.replace("?",".")
        clean_text_dashes = clean_text_question.replace("--","")
        clean_text_quotes = clean_text_dashes.replace('"',"")
        clean_text_4dots = clean_text_quotes.replace("....",".")
        clean_text_3dots = clean_text_4dots.replace("...","")
        clean_text = clean_text_3dots.replace("\n", " ")

        print(clean_text)

        sentences = clean_text.split(".")                                   # Splits de tekst in zinnen (bij punt)
        sentence_length_dict = {}
        sentence = 0                                                        # Initialiseer dictionary en teller
        
        print(sentences)
        
        for sentence in sentences:
            print(sentence)                      
            just_words = sentence.split()
            print(just_words)   
            length = len(just_words)
            print(length)

            # Condities voor telling.
            # 0 is niets, dus hou buiten de dictionary (komt voor bij het gebruik van bijvoorbeeld !!)
            if length == 0:
                    continue
            # Waarde nog niet aanwezig in dict? Voeg dan toe.
            elif length not in sentence_length_dict:
                sentence_length_dict[length] = 1
                print(sentence_length_dict)
            # Waarde wel aanwezig in dict? Voeg dan 1 extra toe bovenop wat je al had.
            else:
                sentence_length_dict[length] += 1
                print(sentence_length_dict)

        # Zet self.sentence_lengths met de dictionary
        self.sentence_lengths=sentence_length_dict
        return

#testcode voor uitvoer
b = TextModel()
b.read_text_from_file("""C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\HP1.txt""")
dict = b.make_sentence_lengths()
print(b.sentence_lengths)
