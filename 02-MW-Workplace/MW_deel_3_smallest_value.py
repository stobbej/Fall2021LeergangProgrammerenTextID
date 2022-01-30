# Fall 2021 - Leergang Programmeren TextID
# textmodel.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#

from multiprocessing.sharedctypes import Value
import string
import math

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

        # feature marlies
        self.relative_pronouns = {}        # Om ... te tellen

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'Betrekkelijk vornaamwoorden:\n' + str(self.relative_pronouns) + '\n\n'
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

    def clean_the_mess(self):
        """
        verwijdert niet-alfabetische karakters en niet-cijfers die NIET kunnen duiden op het einde van een zin
        
        .?! blijven dus bestaan
        """          
        # verwijderen van gekke tekens:
        cleaner = ""
        
        for char in self.text:
            if char in string.ascii_letters or char in string.digits or char in "?!. \n" :
                cleaner += char
        
        #print(cleaner)
        return cleaner
        

    def make_sentence_lengths(self):
        """
        method:     De methode bepaalt de lengte van zinnen en voert een count uit op identieke zinlengte
        argument:   self
        return:     sentence_lengths, as dictionary {lengte sentence: count}
        """

        clean_text = self.clean_the_mess()
        
        l1 = ["!", "?", "....", "...", "\n"]
        l2 = [".", ".", ".", "", " "]    
        
        for i in range(len(l1)):
            new = clean_text.replace(l1[i],l2[i])
            clean_text = new
            
        # print(clean_text)

        sentences = clean_text.split(".")                                           # splits de tekst in zinnen (bij punt)
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

    def clean_string(self,s):
        """krijgt een string s mee en geeft een opgeschoonde versie ervan terug zonder leestekens en zonder hoofdletters.

        Args:
            s (string): de ingegeven tekst
        """
        
        s = s.lower()
        
        for p in string.punctuation:
            s = s.replace(p,'')
            
        # print(s)
        return s
    
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
        method:     De methode maakt een dictionary van stammen 
        argument:   self
        return:     make_stems, as dictionary {stem: count}
        """

        clean_text = self.clean_string(self.text)
        list_of_words = clean_text.split() 

        import snowballstemmer
        stemmer = snowballstemmer.stemmer('english')
        # stemmer = snowballstemmer.stemmer('dutch')

        for word in list_of_words:
            if stemmer.stemWord(word) not in self.stems:
                self.stems[stemmer.stemWord(word)] = 1
            else:
                self.stems[stemmer.stemWord(word)] += 1
        return self.stems
    
    
    def make_relative_pronouns(self):
        """
        method:     De methode maakt een dictionary om het gebruik van betrekkelijk voornaamwoorden te herkennen
        argument:   self
        return:     make_relative_pronouns, as dictionary {pronoun: count}
        """

        self.relative_pronouns = {}  
        s = self.text
        tekst = self.clean_string(s)
        words = tekst.split()       
        
        pronouns = ["which", "that", "who", "what", "whose", "whom"]
        
        for word in words:
            if word in pronouns:
                if word not in self.relative_pronouns:
                    self.relative_pronouns[word] = 1
                else:
                    self.relative_pronouns[word] += 1

        #print(self.relative_pronouns)
        return self.relative_pronouns            

    def normalize_dictionary(self, d):
        """
        method: Geeft genormaliseerde dictionary terug.
        argument: self en d (dictionary) die genormaliseerd moet worden.
        return: nieuwe dict met genormaliseerde waarde.
        """
        results = {}
        
        #Eerste deel: haal de waardes uit de dictionary.
        #Tel die waardes bij elkaar op om de som te krijgen van de waardes.
        values = d.values()       
        #print("values",values)
        sumofvalues = sum(values)
        #print("sum of values", sumofvalues)

        #Deel twee: Loop door alle sleutels in d heen, haal daar de waarde uit en deel die door de som van alle waarden.
        #Zet vervolgens de uitkomst als nieuwe genormaliseerde waarde in de dictionary results.
        for k in d:
            #print("waarde", k)
            start = d[k]
            #print("start", start)
            new_value = start / sumofvalues
            #print("new value", new_value)
            #print("dit moet hem worden", k, new_value)
            results[k] = new_value

        return results

    def smallest_value(self, nd1, nd2):
        """
        method: krijgt twee dictionary’s nd1 en nd2 mee uit het model en geeft de kleinste positieve waarde terug die in de dictionary’s samen voorkomt.
        arguments: normalized dicionanry 1 (nd1) en 2 (nd2).
        return: de kleinste waarde uit beide dictionary's.
        """

        if sum(nd1.values()) > 1:
            nd1 = self.normalize_dictionary(nd1)
        
        if sum(nd2.values()) > 1:
            nd2 = self.normalize_dictionary(nd2)       
        
        data = []
        
        for x in nd1.values():
            if x != 0:
                data.append(x)
        
        for x in nd2.values():
            if x != 0:
                data.append(x)         
        
        lowest = min(data)
              
        return lowest
    
        
            

#testcode voor uitvoer
tm = TextModel()
tm.read_text_from_file("""C:\\Users\\marli\\SynologyDrive\\Marlies Werk\\Studies en opleidingen\\IT Academy - Leergang Programmeren\\TextID\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\test.txt""")

# maak alle dictionary's
tm.make_sentence_lengths()
tm.make_words()
tm.make_word_lengths()
tm.make_stems()
d = tm.make_relative_pronouns()
tm.normalize_dictionary(d)

# alle dictionary's bekijken!
print('Het model bevat deze dictionary\'s:')
print(tm)
