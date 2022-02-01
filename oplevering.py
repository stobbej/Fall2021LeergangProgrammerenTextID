# Fall 2021 - Leergang Programmeren TextID
# 
# Bestandsnaam      : oplevering.py
# Opdracht          : Tekstidentificatie
#
# Naam              : Marlies Wanders, Jeroen van Kleef, Jeroen Stobbe
#
import copy
import snowballstemmer
from string import punctuation
from math import log2

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
        self.articles = {}          # Om lidwoorden te tellen
        self.quotes = {}     # Om spreektaal vast te stellen 
        self.relative_pronouns = {} # Om gebruik betrekkelijk voornaamwoorden vast te stellen
        self.adjectives = {}        # Om gebruik bijvoeglijk naamwoorden vast te stellen																							 																				

    def __repr__(self):
        """
        Display the contents of a TextModel.
        """
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'Leestekens:\n' + str(self.punctuation) + '\n\n'
        s += 'Lidwoorden:\n' + str(self.articles) + '\n\n'
        s += 'Spreektaal:\n' + str(self.quotes) + '\n\n'
        s += 'Betrekkelijk voornaamwoorden:\n' + str(self.relative_pronouns) + '\n\n'
        s += 'Bijvoeglijk naamwoorden:\n' + str(self.adjectives) + '\n\n'																				 																	 
     
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
      
        sentences = gettext.split(".")                                           
        self.sentence_lengths = {}                                                 
        sentence = 0                                                            
               
        for sentence in sentences:                                                
            just_words = sentence.split()                                           
            length = len(just_words)                                                
          
            if length == 0:                                                         
                    continue                                                        
            elif length not in self.sentence_lengths:                               
                self.sentence_lengths[length] = 1                                   
            else:                                                                   
                self.sentence_lengths[length] += 1                                 
        
        return self.sentence_lengths
 
    def clean_string(self, s):
        """
        method:         the method removes interpunction and set words in lower-case
        argument:       self, s = string
        return:         clean_string, as string
        """
       
        clean_string = ""   
                
        for p in punctuation:                                        
            s = s.replace(p, "")                                   
        
        clean_string = s.lower()                                   
                    
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
        
        for word in words:
            if len(word) not in self.word_lengths:
                self.word_lengths[len(word)] = 1
            else:
                self.word_lengths[len(word)] += 1

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
        
        for word in words:
            if word not in self.words:
                self.words[word] = 1
            else:
                self.words[word] += 1

        return self.words  

    def make_stems(self):
        """
        method:         the method creates a dictionary with stems and counts the number of equal stems
        argument:       self
        return:         make_stems, as dictionary {stem: count}     
        """
        
        clean_text = self.clean_string(self.text)
        list_of_words = clean_text.split() 

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
    
    def make_articles(self):
        """
        method:         the method creates a dictionary with articles and counts the number of equal articles
        argument:       self
        return:         make_articles, as dictionary {arcticles: count}
        """
        
        list_of_words = self.clean_string(self.text).split()
        list_of_articles = ["a", "an", "the"]
        # list_of_articles = ["de", "het", "een"]

        for word in list_of_words:
            if word in list_of_articles:
                if word not in self.articles:
                    self.articles[word] = 1
                else:
                    self.articles[word] += 1
        return self.articles
    
    def make_quotes(self):
        """
        method:         the method determines if a sentences is quotes and counts the number of sentences with quotes
        argument:       self
        return:         make_quotes, as dictionary {quotes}
        """
    
        gettext = copy.deepcopy(self.text)
        
        replace_chars = [".\"", "!\"", "?\""]          
        with_this = "-ENDCOL"
        gettext = clean_the_mess(gettext, replace_chars, with_this)
        
        replace_chars = ["\""]
        with_this = "STARTCOL-"
        gettext = clean_the_mess(gettext, replace_chars, with_this)
        
        replace_chars = [".", "!", "?"]          
        with_this = "-ENDSEN"
        gettext = clean_the_mess(gettext, replace_chars, with_this)
        
        words = gettext.split()
             
        self.quotes["non_quotes"] = 0
        self.quotes["quotes"]     = 0
     
        for word in words:
            if word.find("STARTCOL-") != -1 or word.find("-ENDCOL") != -1 or word.find("-ENDSEN") != -1:
                if word.find("-ENDSEN") != -1:
                    self.quotes["non_quotes"] += 1
                if word.find("STARTCOL-") != -1:
                    self.quotes["quotes"] += 1
                        
        return self.quotes

    def make_relative_pronouns(self):
        """
        method:         the method creates a dictionary of the use of relative pronouns
        argument:       self
        return:         self.relative_pronouns, as dictionary {pronoun: count}
        """

        self.relative_pronouns = {}  
        s = self.text.lower()
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
    
    def make_adjectives(self):
        """
        method:         the method creates a dictionary of the use of adjectives that express tone or emotion
        argument:       self
        return:         self.adjectives, as dictionary {adjective: count}
        """
        
        self.adjectives = {}
        s = self.text.lower()
        tekst = self.clean_string(s)
        words = tekst.split()    
                 
        emotion_adjectives = ["amazed","aggravated","anxious","attractive","awful","awestruck","bold","chilly","bashful","brave","dejected","cautious","bubbly","dirty","composed”,”cheerful","dreadful","easygoing","comfortable","heavy","horrified","delightful","irritated","intelligent","excited","pessimistic","numb","festive","tearful","puzzled","free","tense","quizzical","jolly","terrible","ravenous","optimistic","tired","reluctant","proud","ugly","settled","wonderful","weak","shy","appreciative","angry","accepting","blissful","disenchanted","calm","contented","distressed","confident","ecstatic","glum","cool","elated","gloomy","earnest","glad","grumpy","easy","happy","grouchy","evenhanded","joyful","miserable","indifferent","jubilant","mad","neutral","merry","moody","nostalgic","respectful","nervous","passive","sweet","sad","reserved","serene","sadistic","satisfied","upbeat","selfish","sentimental","vivacious","sour","surprised","agreeable","annoyed","acerbic","animated","bitter","ambivalent","bright","disgruntled","ardent","clever","disgusted","candid","encouraging","evil","cautionary","fresh","guilt","conciliatory","gentle","hostile","knowledgeable","hopeful","hurtful","mysterious","kind","nasty","pragmatic","loving","obnoxious","regretful","open","oppressive","resigned","pleased","overbearing","satirical","supportive","resentful","secretive","sympathetic","sarcastic","solemn","warm","sardonic","strong"]
            
        for word in words:
            if word in emotion_adjectives:
                if word not in self.adjectives:
                    self.adjectives[word] = 1
                else:
                    self.adjectives[word] += 1   
        
        return self.adjectives
	
    def normalize_dictionary(self,d):
        """
        method:         the method creates from a dictionary a normalized dictionary
        argumnent:      self
                        d: as dictionary
        return:         normalized dictionary
        """
        totaal = sum(d.values())    
        
        for key, value in d.items():
            d[key] = value / totaal 
        return d                    
    
    def smallest_value(self, nd1, nd2):
        """
        method:         the method returns the smalles_value of two normalized dictionaries 
        argument:       self
                        nd1: normalized dictionary 1
                        nd2: normalized dictionary 2
        return          smallest_value of a dictionary 1 or 2
        """
        min_nd1 = min(nd1.values(), default=0)                          # geef 0 terug wanneer dict leeg is 
        min_nd2 = min(nd2.values(), default=0)                          # geef 0 terug wanneer dict leeg is 
      
        return min(min_nd1, min_nd2)    
        
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
            if d[k] != 0 and norm_dict1 != 0:                           # de testbestanden leveren een waarde 0 voor spreektaal
                if k in norm_dict1:
                    totaal_nd1 += d[k]*log2(norm_dict1[k])
                else:
                    totaal_nd1 += d[k]*log2(epsilon)
                
        for k in d:
            if d[k] != 0 and norm_dict2 != 0:                           # de testbestanden leveren een waarde 0 voor spreektaal
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
        self.make_articles()
        self.make_quotes()
        self.make_relative_pronouns()
        self.make_adjectives()							  
    
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
     
        ### Articles ###      
        articles_score = self.compare_dictionaries(self.articles, model1.articles, model2.articles)
        if articles_score[0] > articles_score[1]:
            score_tm1 += 1
        elif articles_score[0] < articles_score[1]:
            score_tm2 += 1
     
        ### quotes ###
        quotes_score = self.compare_dictionaries(self.quotes, model1.quotes, model2.quotes)
        if quotes_score[0] > quotes_score[1]:
            score_tm1 += 1
        elif quotes_score[0] < quotes_score[1]:
            score_tm2 += 1
            
        ### Relative pronouns ###
        pronouns_score = self.compare_dictionaries(self.relative_pronouns, model1.relative_pronouns, model2.relative_pronouns)
        if pronouns_score[0] > pronouns_score[1]:
            score_tm1 += 1
        elif pronouns_score[0] < pronouns_score[1]:
            score_tm2 += 1
            
        ### Adjectives ###
        adjectives_score = self.compare_dictionaries(self.adjectives, model1.adjectives, model2.adjectives)
        if adjectives_score[0] > adjectives_score[1]:
            score_tm1 += 1
        elif adjectives_score[0] < adjectives_score[1]:						  
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
        print(f"     {'articles':>20s}   {articles_score[0]:>10.2f}   {articles_score[1]:>10.2f} ")
        print(f"     {'quotes':>20s}   {quotes_score[0]:>10.2f}   {quotes_score[1]:>10.2f} ")
        print(f"     {'relative_pronouns':>20s}   {pronouns_score[0]:>10.2f}   {pronouns_score[1]:>10.2f} ")
        print(f"     {'adjectives':>20s}   {adjectives_score[0]:>10.2f}   {adjectives_score[1]:>10.2f} ")																											
        print("\n")
        print(f"--> Model 1 wint op {score_tm1} features")
        print(f"--> Model 2 wint op {score_tm2} features")
        print("\n")

        if score_tm1 > score_tm2:
            print("+++++ Model 1 komt beter overeen ! +++++")
        elif score_tm1 < score_tm2:
            print("+++++ Model 2 komt beter overeen ! +++++")
        else:
            print("+++++ Geen winnaar +++++")

##################### Initialiseren naar persoonlijke DEV-environment #####################
# Set path naar de locatie van tekst-bestanden
path_tekstbestanden = """C:\\Users\\jeroe\\GIT\\Fall2021LeergangProgrammerenTextID\\Tekst-bestanden\\"""
##################### Initialiseren naar persoonlijke DEV-environment #####################

print(' +++++++++++ Model 1 +++++++++++ ')
tm1 = TextModel()
# tm1.read_text_from_file(path_tekstbestanden+"train1.txt")
tm1.read_text_from_file(path_tekstbestanden+"HP1.txt")
tm1.create_all_dictionaries()  # deze is hierboven gegeven
print(tm1)

print(' +++++++++++ Model 2 +++++++++++ ')
tm2 = TextModel()
# tm2.read_text_from_file(path_tekstbestanden+"train2.txt")
# tm2.read_text_from_file(path_tekstbestanden+"Holmes.txt")
tm2.read_text_from_file(path_tekstbestanden+"HP2.txt")
# tm2.read_text_from_file(path_tekstbestanden+"HP1.txt")
tm2.create_all_dictionaries()  # deze is hierboven gegeven
print(tm2)

print(' +++++++++++ Onbekende tekst +++++++++++ ')
tm_unknown = TextModel()
# tm_unknown.read_text_from_file(path_tekstbestanden+"unknown.txt")
# tm_unknown.read_text_from_file(path_tekstbestanden+"HP2.txt")
tm_unknown.read_text_from_file(path_tekstbestanden+"HP1.txt")
# tm_unknown.read_text_from_file(path_tekstbestanden+"Holmes.txt")
tm_unknown.create_all_dictionaries()  # deze is hierboven gegeven
print(tm_unknown)

print(tm_unknown.compare_text_with_two_models(tm1,tm2))