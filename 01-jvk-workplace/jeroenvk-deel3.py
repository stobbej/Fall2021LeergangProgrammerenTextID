# Fall 2021 - Leergang Programmeren TextID
# textmodel.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#
import copy
from hashlib import new

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
            input       =   file.read() 
            self.text   =   input
        
        return self.text

    def make_sentence_lengths(self):
        """
        method:     De methode bepaalt de lengte van zinnen en voert een count uit op identieke zinlengte
        argument:   self
        return:     sentence_lengths, as dictionary {lengte sentence: count}
        """

        gettext = copy.deepcopy(self.text)
        gettext = gettext.lower()
        replace_chars = ["...", "--"]            
        with_this = ""
        gettext = clean_the_mess(gettext, replace_chars, with_this)

        replace_chars = ["....", ",", "!", "?"]            
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
 
    def clean_string(self, s):
        """
        Method:     De methode verwijdert interpunctie en zet alle letters in lower-case
        argument:   self, s = string
        return:     clean_string, as string
        """
        from string import punctuation
        
        clean_string = ""                                               # init clean string als leeg     

        # print(punctuation)                                              # TEST-STAP
        
        for p in punctuation:                                           # voor elke interpunctie doorloop string
            # print(p)                                                    # TEST-STAP
            s = s.replace(p, "")                                        # vervang interpunctie door leeg
            # print(s)                                                    # TEST-STAP
        
        clean_string = s.lower()                                        # zet string in lower caps
        # print(clean_string)                                             # TEST-STAP
            
        return clean_string    

    def make_word_lengths(self):
        """
        method:     De methode maakt een dictionary om woordlengtes te herkennen
        argument:   self
        return:     make_word_lengths, as dictionary {lengte word: count}
        """

        self.word_lengths = {}  
        s = self.text
        tekst = self.clean_string(s)
        words = tekst.split()
        
        #print(words)

        for word in words:
            if len(word) not in self.word_lengths:
                self.word_lengths[len(word)] = 1
            else:
                self.word_lengths[len(word)] += 1

        #print(self.make_word_lengths)
        return self.word_lengths

    def make_words(self):
        """
        method:     De methode maakt een dictionary om woorden te herkennen
        argument:   self
        return:     make_words, as dictionary {word: count}
        """     

        self.words = {}  
        s = self.text
        tekst = self.clean_string(s)
        words = tekst.split()
        
        #print(words)

        for word in words:
            if word not in self.words:
                self.words[word] = 1
            else:
                self.words[word] += 1

        #print(self.make_words)
        return self.words  

    def make_stems(self):
        """
        method:     De methode...blabla
        argument:   
        retunr:     
        """
        
        clean_text = self.clean_string(self.text)
        list_of_words = clean_text.split() 

        import snowballstemmer
        # stemmer = snowballstemmer.stemmer('english');
        stemmer = snowballstemmer.stemmer('dutch')

        for word in list_of_words:
            if stemmer.stemWord(word) not in self.stems:
                self.stems[stemmer.stemWord(word)] = 1
            else:
                self.stems[stemmer.stemWord(word)] += 1
        return self.stems
    
    def normalize_dictionary(self, d):
        """
        method: Geeft genormaliseerde dictionary terug.
        argument: self en d (dictionary) die genormaliseerd moet worden.
        return: nieuwe dict met genormaliseerde waarde.
        """
        results = {}
        values = d.values()
        #print("values",values)
        sumofvalues = sum(values)
        #print("sum of values", sumofvalues)

        for k in d:
            #print("waarde", k)
            start = d[k]
            #print("start", start)
            new_value = start / sumofvalues
            #print("new value", new_value)
            #print("dit moet hem worden", k, new_value)
            results[k] = new_value

        return results

# Hier kan je dingen testen...

##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = ""
tekstbestand        = "test.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################

# Hier kan je dingen testen...
tm = TextModel()
tm.read_text_from_file(path_tekstbestanden+tekstbestand)
# Zet hier aanroepen neer die het model vullen met informatie
#print("TextModel:", tm)
#print("inhoud", tekstbestand.upper(), ": ",tm.text)
#tm.make_sentence_lengths()
tm.make_words()
#tm.make_word_lengths()
#tm.make_stems()

normalize = tm.normalize_dictionary(tm.words)
print(normalize)
print("Dit is de eindwaarde, moet gelijk zijn aan 1: ",sum(normalize.values()))