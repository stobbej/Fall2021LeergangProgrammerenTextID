# Fall 2021 - Leergang Programmeren TextID
# textmodel.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#
import copy
from string import punctuation
from math import log2

def clean_the_mess(text, replace_chars, with_this):
        """
        method: Replaces items in the source text to clean up strings.
        argument: text: string - source material, replace: list of characters to be replaced, with_this: list of characters to substitute with 'replace'.
        return: cleaned string.
        """
        for replace in range(len(replace_chars)):
            text = text.replace(replace_chars[replace], with_this) 

        print(text)
        
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
        self.punctuation = {}       # Interpunctie tellen
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
        s += 'Leestekens:\n' + str(self.punctuation) + '\n\n'
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

        replace_chars = ["....", "!", "?"]            
        with_this = "."            
        gettext = clean_the_mess(gettext, replace_chars, with_this) 

        replace_chars = ["\n"]            
        with_this = " "            
        gettext = clean_the_mess(gettext, replace_chars, with_this) 
      
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
    
    def make_punctuation(self):
        """     
        make_punctuation geeft de interpunctie en het voorkomen ervan weer.
        """   
        words = self.text.split() 
        for word in words:
            for letter in word:
                    if letter in punctuation:
                        if letter not in self.punctuation:
                            self.punctuation[letter] = 1
                        else:
                            self.punctuation[letter] += 1       
        return self.punctuation
    
    def normalize_dictionary(self,d):
        """
        
        """
        totaal = sum(d.values())                        # Sum van alle entries in een dictionary
        
        for key, value in d.items():                    # Doorloop alle entries en pak waarde
            d[key] = value / totaal                     # Normaliseer 
        return d                                        # Geef genormaliseerde dict terug
    
    
    def smallest_value(self, nd1, nd2):
        """
        
        """
        min_nd1 = min(nd1.values(), default=0)          # bepaal de kleinste waarde van dict1
        min_nd2 = min(nd2.values(), default=0)          # bepaal de kleinste waarde van dict2
        
        if min_nd1 == min_nd2:
            return min_nd1                              # indien gelijk geef een waarde terug
        else:
            return min(min_nd1, min_nd2)                # bepaal de kleinste tussen dict1 en dict2
     
        
    def compare_dictionaries(self, d, nd1, nd2):
        """
        
        """
        totaal_nd1 = 0.0
        totaal_nd2 = 0.0
        epsilon = self.smallest_value(nd1, nd2) / 2

        for key, value in d.items():
            if key == 0:
                totaal_nd1 = 0.01
            elif key not in nd1.keys():
                totaal_nd1 += 1 * log2(epsilon)   
            else:
                for key1, value1 in nd1.items():
                    if key == key1:
                        totaal_nd1 += value * log2(value1)
            
        for key, value in d.items():
            if key == 0:
                totaal_nd2 = 0.01
            elif key not in nd2.keys():
                totaal_nd2 += 1 * log2(epsilon)           
            else:
                for key1, value1 in nd2.items():
                    if key == key1:
                        totaal_nd2 += value * log2(value1)   
            
        self.list_of_log_probs = [totaal_nd1, totaal_nd2]

        return self.list_of_log_probs
    
    
    def create_all_dictionaries(self):
        """
        
        """
        self.make_sentence_lengths()
        self.make_word_lengths()
        self.make_words()
        self.make_stems()
        self.make_punctuation()
     
    
    def compare_text_with_two_models(self, model1, model2):
        """
        
        """      
        score_tm1   = 0
        score_tm2   = 0
        
        ### Words ###
        nd1_word    =   self.normalize_dictionary(model1.words)
        nd2_word    =   self.normalize_dictionary(model2.words)
        
        wordsscore = self.compare_dictionaries(self.words, nd1_word, nd2_word)
        if wordsscore[0] > wordsscore[1]:
            score_tm1 += 1
        else:
            score_tm2 += 1
       
        ### Word lenghts ###
        nd1_wordlength  = self.normalize_dictionary(model1.word_lengths)
        nd2_wordlength  = self.normalize_dictionary(model2.word_lengths)

        wordlengthscore = self.compare_dictionaries(self.word_lengths, nd1_wordlength, nd2_wordlength)
        if wordlengthscore[0] > wordlengthscore[1]:
            score_tm1 += 1
        else:
            score_tm2 += 1
  
        ### Zinslengte ###
        nd1_sentence_len = self.normalize_dictionary(model1.sentence_lengths)
        nd2_sentence_len = self.normalize_dictionary(model2.sentence_lengths)

        sent_len_score   = self.compare_dictionaries(self.sentence_lengths, nd1_sentence_len, nd2_sentence_len)
        if sent_len_score[0] > sent_len_score[1]:
            score_tm1 += 1
        else:
            score_tm2 += 1
        
        ### Stems ###
        nd1_stems = self.normalize_dictionary(model1.stems)
        nd2_stems = self.normalize_dictionary(model2.stems)

        stem_score = self.compare_dictionaries(self.stems, nd1_stems, nd2_stems)
        if stem_score[0] > stem_score[1]:
            score_tm1 += 1
        else:
            score_tm2 += 1

        ### Interpunctie ###
        nd1_punc = self.normalize_dictionary(model1.punctuation)
        nd2_punc = self.normalize_dictionary(model2.punctuation)
        
        punc_score = self.compare_dictionaries(self.punctuation, nd1_punc, nd2_punc)
        if punc_score[0] > punc_score[1]:
            score_tm1 += 1
        else:
            score_tm2 += 1
     
        ### Winnaar ###
        print("Vergelijkingsresultaten:\n")
        print(f"     {'naam':>20s}   {'model1':>10s}   {'model2':>10s} ")
        print(f"     {'----':>20s}   {'------':>10s}   {'------':>10s} ")       
        print(f"     {'words':>20s}   {wordsscore[0]:>10.2f}   {wordsscore[1]:>10.2f} ") 
        print(f"     {'word_lengths':>20s}   {wordlengthscore[0]:>10.2f}   {wordlengthscore[1]:>10.2f} ") 
        print(f"     {'sentence_lengths':>20s}   {sent_len_score[0]:>10.2f}   {sent_len_score[1]:>10.2f} ")
        print(f"     {'stems':>20s}   {stem_score[0]:>10.2f}   {stem_score[1]:>10.2f} ") 
        print(f"     {'punctuation':>20s}   {punc_score[0]:>10.2f}   {punc_score[1]:>10.2f} ") 
        print("\n")
        print(f"--> Model 1 wint op {score_tm1} features")
        print(f"--> Model 2 wint op {score_tm2} features")
        print("\n")

        if score_tm1 > score_tm2:
            print("+++++ Model 1 komt beter overeen ! +++++")
        else:
            print("+++++ Model 2 komt beter overeen ! +++++")


    
    
# Hier kan je dingen testen...

##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = """C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\"""
tekstbestand        = "test.txt"
#
##################### Initialiseren naar persoonlijke DEV-environment #####################

print(' +++++++++++ Model 1 +++++++++++ ')
tm1 = TextModel()
tm1.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\train1.txt')
tm1.create_all_dictionaries()  # deze is hierboven gegeven
print(tm1)

print(' +++++++++++ Model 2+++++++++++ ')
tm2 = TextModel()
tm2.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\train2.txt')
tm2.create_all_dictionaries()  # deze is hierboven gegeven
print(tm2)

print(' +++++++++++ Onbekende tekst +++++++++++ ')
tm_unknown = TextModel()
tm_unknown.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\unknown.txt')
tm_unknown.create_all_dictionaries()  # deze is hierboven gegeven
print(tm_unknown)