# Fall 2021 - Leergang Programmeren TextID
# file          :   begin.py
# date          :   2022-01-23
# projectgroep  :   Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#
# Opdracht      :   Tekstidentificatie
#

import copy

def clean_the_mess(text, replace_chars, with_this):
        """
        method: Replaces items in the source text to clean up strings.
        argument: text: string - source material, replace: list of characters to be replaced, with_this: list of characters to substitute with 'replace'.
        return: cleaned string.
        """
        for replace in range(len(replace_chars)):
            text = text.replace(replace_chars[replace], with_this) 

        return text

class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        #
        # Maak dictionary's voor elke eigenschap
        #
        self.words = {}             # Om woorden te tellen
        self.modals = {}            # Om modals te tellen -> de dict van modals met counts
        self.modals_diversity = {}  # Om modals te tellen -> verschillende modals
        self.modals_count = {}      # Om modals te tellen -> full count
        self.woordenschat = {}      # Om woordenschat te tellen
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
        s = 'Woordschat:\n' + str(self.woordenschat) + '\n\n'
        s = 'Hulpwerkwoorden:\n' + str(self.modals) + '\n\n'
        s = 'Aantal verschillende hulpwerkwoorden:\n' + str(self.modals_diversity) + '\n\n'
        s = 'Totaal aantal hulpwerkwoorden:\n' + str(self.modals_count) + '\n\n'
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

        # Replace leestekens die op einde van zin duiden.
        # We gaan nog kijken naar een cleanere methode om dit te doen, maar voor nu werkt dit.
        # Let op: er zijn 'onvolkomenheden' in de telling: 
        # mrs. (telt als zin van 1 woord)
        # nalopen van de zin met lengte 181
        #clean_text_exclamation = self.text.replace("!",".")                         # zet ! om naar zinseinde .
        #clean_text_question = clean_text_exclamation.replace("?",".")               # zet ? om naar zinseinde .
        #clean_text_dashes = clean_text_question.replace("--","")                    # verwijder --
        #clean_text_quotes = clean_text_dashes.replace('"',"")                       # verwijder "
        #clean_text_4dots = clean_text_quotes.replace("....",".")                    # zet .... om naar zinseinde .
        #clean_text_3dots = clean_text_4dots.replace("...","")                       # verwijder ...
        #clean_text = clean_text_3dots.replace("\n", " ")                            # verwijder End of Line

        gettext = copy.deepcopy(self.text)
        gettext = gettext.lower()
        replace_chars = ["....", "...", "--"]            
        with_this = ""
        gettext = clean_the_mess(gettext, replace_chars, with_this)

        replace_chars = [",", "!", "?"]            
        with_this = "."            
        gettext = clean_the_mess(gettext, replace_chars, with_this) 

        replace_chars = ["\n"]            
        with_this = " "            
        gettext = clean_the_mess(gettext, replace_chars, with_this) 
        # print(clean_text)                                                           # TEST-STAP

        sentences = gettext.split(".")                                           # splits de tekst in zinnen (bij punt)
        self.sentence_lengths = {}                                                  # init dictionary
        sentence = 0                                                                # init teller
        
        # print(sentences)                                                            # TEST-STAP
        
        for sentence in sentences:                                                  # doorloop elke zin in zinnen
            # print(sentence)                                                         # TEST-STAP
            just_words = sentence.split()                                           # splits zin op in woorden
            # print(just_words)                                                       # TEST-STAP
            length = len(just_words)                                                # tel aantal woorden in just_words
            # print(length)                                                           # TEST-STAP

            if length == 0:                                                         # als aantal woorden = 0
                    continue                                                        # ga verder
            elif length not in self.sentence_lengths:                               # als aantal woorden NIET in dict
                self.sentence_lengths[length] = 1                                   # maak key aan met waarde 1
                # print(self.sentence_lengths)                                        # TEST-STAP
            else:                                                                   # aantal woorden WEL in dict
                self.sentence_lengths[length] += 1                                  # verhoog key met waarde 1
                # print(self.sentence_lengths)                                        # TEST-STAP
        
        return self.sentence_lengths
 

    def make_words(self):
        """
        Method: Makes a dictionary of the read text file that contains all words and their count.
        Argument: self.
        Return: dictionary in self.words.
        """
        # Deel 1: maak deep copy zodat origineel behouden blijft.
        # Zet daarna alles op lower case, vervang leestekens en vervang enters.
        gettext = copy.deepcopy(self.text)
        gettext = gettext.lower()
        replace_chars = ["\"", ".", ",", "\'", "....", "...", "--", "?", "!"]            
        with_this = ""
        gettext = clean_the_mess(gettext, replace_chars, with_this)

        replace_chars = ["\n"]            
        with_this = " "            
        gettext = clean_the_mess(gettext, replace_chars, with_this) 

        # Deel 2: Splits het in woorden op en tel woord voor woord wat het aantal is. Schrijf die weg naar self.words.
        sourcematerial = gettext.split()

        for word in sourcematerial:
            if word == "":
                #print(word)
                continue
            elif word not in self.words:
                #print(word)
                self.words[word] = 1
            else:
                #print(word)
                self.words[word] += 1
        
        # De woordenschat kan ook direct worden toegevoegd.
        self.woordenschat = len(self.words)         
        return

    def detect_modals(self):
        """
        Method: Detect commonly used modals in text.
        Argument: self.
        Return: number of modals used in the source material (int) and a dict of the modals itself.
        """
        # Deel 1: maak deep copy zodat origineel behouden blijft.
        # Zet daarna alles op lower case, vervang leestekens en vervang enters.
        gettext = copy.deepcopy(self.text)
        gettext = gettext.lower()
        replace_chars = ["\"", ".", ",", "\'", "....", "...", "--", "?", "!"]            
        with_this = ""
        gettext = clean_the_mess(gettext, replace_chars, with_this)

        replace_chars = ["\n"]            
        with_this = " "            
        gettext = clean_the_mess(gettext, replace_chars, with_this) 

        # Deel 2: Splits het in woorden op en tel woord voor woord wat het aantal is. Schrijf die weg naar self.modals.
        sourcematerial = gettext.split()

        # Modals / Hulpwerkwoorden
        modals = ["can", "may", "might", "could", "should", "would", "will", "must"]

        for word in sourcematerial:
            if word == "":
                #print(word)
                continue
            if word in modals:                 
                if word not in self.modals:
                    #print(word)
                    self.modals[word] = 1
                else:
                    #print(word)
                    self.modals[word] += 1
        
        # De modalstatistieken kan ook direct worden toegevoegd.
        self.modals_diversity = len(self.modals) 
        
        self.modals_count = sum(self.modals.values())
        
        return

    def make_word_lengths(self):
        """
        Method: Makes a dictionary of the read text file that contains all word lengths and their counts.
        Argument: self.
        Return: dictionary in self.word_lengths.
        """
        # Deel 1: maak deep copy zodat origineel behouden blijft.
        # Zet daarna alles op lower case, vervang leestekens en vervang enters.
        gettext = copy.deepcopy(self.text)
        gettext = gettext.lower()
        replace_chars = ["\"", ".", ",", "\'", "....", "...", "--", "?", "!"]            
        with_this = ""        
        gettext = clean_the_mess(gettext, replace_chars, with_this)

        replace_chars = ["\n"]            
        with_this = " "            
        gettext = clean_the_mess(gettext, replace_chars, with_this)

        # Deel 2: Splits het in woorden op en tel woord voor woord wat het aantal is. Schrijf die weg naar self.word_lengths.
        sourcematerial = gettext.split()

        for word in sourcematerial:
            length = len(word)
            if length == 0:
                #print("0",word)
                continue
            elif length not in self.word_lengths:
                #print("uit", word)
                self.word_lengths[length] = 1
            else:
                #print("in", word)
                self.word_lengths[length] += 1            
        return



##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = ""
tekstbestand        = "test.txt"
# tekstbestand        = "train1.txt"
# tekstbestand        = "HP1.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################
# Hier kan je dingen testen...
tm = TextModel()
tm.read_text_from_file(path_tekstbestanden+tekstbestand)

tm.make_words()
print("woorden: ", tm.words)
print("woordenscha: ", tm.woordenschat)

tm.make_sentence_lengths()
print("Zinslengte: ", tm.sentence_lengths)

tm.make_word_lengths()
print("Woordlengte: ", tm.word_lengths)

tm.detect_modals()
print("Hulpwerkwoorden: ", tm.modals)
print("Diversiteit aan hulpwerkwoorden: ", tm.modals_diversity)
print("Totaal aantal hulpwerkwoorden: ", tm.modals_count)

#assert dict == {5: 1, 16: 1, 6: 1, 3: 1}                                          # test.txt
# assert dict == {5: 1, 16: 1, 6: 1}                                                  # train1.txt