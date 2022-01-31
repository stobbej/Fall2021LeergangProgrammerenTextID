# Fall 2021 - Leergang Programmeren TextID
# 
# Bestandsnaam      : oplevering.py
# Opdracht          : Tekstidentificatie
#
# Naam              : Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#
import copy
from string import punctuation
from math import log2
from time import sleep

def clean_the_mess(text, replace_chars, with_this):
        """
        function:       replaces items in the source text to clean up strings.
        argument:       text:           string - source material;
                        replace_chars:  list of characters to be replaced;
                        with_this:      list of characters to substitute with 'replace'.
        return:         cleaned string.
        """
        for replace in range(len(replace_chars)):
            text = text.replace(replace_chars[replace], with_this) 
       
        return text

class TextModel:
    """
    A class supporting complex models of text.
    """

    def __init__(self):
        """
        Create an empty TextModel.
        """
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
        """
        Display the contents of a TextModel.
        """
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'Leestekens:\n' + str(self.punctuation) + '\n\n'
     
        return s
    
    def read_text_from_file(self, filename):
        """
        method:         the method reads the content of a file in the variable self.text as string
        argument:       filename:       string - the filename of the file
        return:         read string
        """

        with open(filename, encoding='utf-8') as file:
            input       =   file.read() 
            self.text   =   input
        
        return self.text

    def make_sentence_lengths(self):
        """
        method:         the method calculates the lenght of sentences and counts the number of sentences with equal lenght
        argument:       self
        return:         sentence_lengths, as dictionary {lengte sentence: count}
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
        method:         the method removes interpunction and set words in lower-case
        argument:       self, s = string
        return:         clean_string, as string
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
        method:         the method creates a dictionary with wordslenghts and counts the number of words with equal lenght
        argument:       self
        return:         make_word_lengths, as dictionary {lengte word: count}
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
        method:         the method creates a dictionary with words and counts the number of equal words
        argument:       self
        return:         make_words, as dictionary {word: count}
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
        method:         the method creates a dictionary with stems and counts the number of equal stems
        argument:       self
        return:         make_stems, as dictionary {stem: count}     
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
        method:         the method creates a dictionary with punctuation and counts the number of equal punctuation
        argument:       self
        return:         make_punctuation, as dictionary {punctuation: count }
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
        method:         the method creates from a dictionary a normalized dictionary
        argumnent:      self
                        d: as dictionary
        return:         normalized dictionary
        """
        totaal = sum(d.values())                        # Sum van alle entries in een dictionary
        
        for key, value in d.items():                    # Doorloop alle entries en pak waarde
            d[key] = value / totaal                     # Normaliseer 
        return d                                        # Geef genormaliseerde dict terug
    
    
    def smallest_value(self, nd1, nd2):
        """
        method:         the method returns the smalles_value of two normalized dictionaries 
        argument:       self
                        nd1: normalized dictionary 1
                        nd2: normalized dictionary 2
        return          smallest_value of a dictionary 1 or 2
        """
        min_nd1 = min(nd1.values(), default=0)          # bepaal de kleinste waarde van dict1, geef 0 terug wanneer dict leeg is 
        min_nd2 = min(nd2.values(), default=0)          # bepaal de kleinste waarde van dict2, geef 0 terug wanneer dict leeg is 
      
        return min(min_nd1, min_nd2)                    # bepaal de kleinste tussen dict1 en dict2
     
        
    def compare_dictionaries(self, d, nd1, nd2):
        """
        method:         the method calculates the probability that the dictionary d arises from the distribution of the data in the 
                        normalized dictionary nd1, and the same probability, but for nd2.
        argument:       self
                        d: dictionary
                        nd1: normalized dictionary 1
                        nd2: normalized dictionary 2
        return:         probability
        """
        norm_dict1 = self.normalize_dictionary(nd1)
        norm_dict2 = self.normalize_dictionary(nd2)
        
        totaal_nd1 = 0                                             
        totaal_nd2 = 0                            
        epsilon = self.smallest_value(norm_dict1, norm_dict2) / 2           
            
        for k in d:
            if k in norm_dict1:
                totaal_nd1 += d[k]*log2(norm_dict1[k])
            else:
                totaal_nd1 += d[k]*log2(epsilon)
                
        for k in d:
            if k in norm_dict2:
                totaal_nd2 += d[k]*log2(norm_dict2[k])
            else:
                totaal_nd2 += d[k]*log2(epsilon)
    
        return [totaal_nd1, totaal_nd2]    
    
    def create_all_dictionaries(self):
        """
        method:         the method creates all required dictionaries
        argument:       self
        return:         created dictionaries
        """
        self.make_sentence_lengths()
        self.make_word_lengths()
        self.make_words()
        self.make_stems()
        self.make_punctuation()
     
    
    def compare_text_with_two_models(self, model1, model2):
        """
        method:         the method compares the text with two other models
        argument:       self
                        model1, an object with dictionaries
                        model2, an object with dictionaries
        return:         printed result
        """      
        score_tm1   = 0
        score_tm2   = 0
        
        ### Words ###      
        wordsscore = self.compare_dictionaries(self.words, model1.words, model2.words)
        if wordsscore[0] > wordsscore[1]:
            score_tm1 += 1
        elif wordsscore[0] < wordsscore[1]:
            score_tm2 += 1
       
        ### Word lenghts ###
        wordlengthscore = self.compare_dictionaries(self.word_lengths, model1.word_lengths, model2.word_lengths)
        if wordlengthscore[0] > wordlengthscore[1]:
            score_tm1 += 1
        elif wordlengthscore[0] < wordlengthscore[1]:
            score_tm2 += 1
  
        ### Zinslengte ###
        sent_len_score   = self.compare_dictionaries(self.sentence_lengths, model1.sentence_lengths, model2.sentence_lengths)
        if sent_len_score[0] > sent_len_score[1]:
            score_tm1 += 1
        elif sent_len_score[0] < sent_len_score[1]:
            score_tm2 += 1
        
        ### Stems ###
        stem_score = self.compare_dictionaries(self.stems, model1.stems, model2.stems)
        if stem_score[0] > stem_score[1]:
            score_tm1 += 1
        elif stem_score[0] < stem_score[1]:
            score_tm2 += 1

        ### Interpunctie ###      
        punc_score = self.compare_dictionaries(self.punctuation, model1.punctuation, model2.punctuation)
        if punc_score[0] > punc_score[1]:
            score_tm1 += 1
        elif punc_score[0] < punc_score[1]:
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
        elif score_tm1 < score_tm2:
            print("+++++ Model 2 komt beter overeen ! +++++")
        else:
            print('+++++ Geen winnaar +++++')


print(' +++++++++++ Model 1 +++++++++++ ')
tm1 = TextModel()
# tm1.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\train1.txt')
tm1.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\HP1.txt')
tm1.create_all_dictionaries()  # deze is hierboven gegeven
print(tm1)

print(' +++++++++++ Model 2 +++++++++++ ')
tm2 = TextModel()
# tm2.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\train2.txt')
# tm2.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\Holmes.txt')
tm2.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\HP2.txt')
# tm2.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\HP1.txt')
tm2.create_all_dictionaries()  # deze is hierboven gegeven
print(tm2)

print(' +++++++++++ Onbekende tekst +++++++++++ ')
tm_unknown = TextModel()
# tm_unknown.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\unknown.txt')
# tm_unknown.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\HP3.txt')
tm_unknown.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\HP1.txt')
# tm_unknown.read_text_from_file('C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\Holmes.txt')
tm_unknown.create_all_dictionaries()  # deze is hierboven gegeven
print(tm_unknown)

print(tm_unknown.compare_text_with_two_models(tm1,tm2))