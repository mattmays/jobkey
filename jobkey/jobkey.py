from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder, TrigramAssocMeasures, TrigramCollocationFinder
from nltk.corpus import stopwords
import json
import argparse

common_stop_words=stopwords.words("english")
my_stop_words=['in','a','just','its','them','ways','what','most','years','re','is','we','product','products','you','the','s','ll','cross','manager','1','2','3','4','5','6','7','8','9','0','or','day','be','are']

def parse_args():    
    parser = argparse.ArgumentParser(description='Uses some basic Natural Language Processing to identify keywords in job descriptions than can then be used on a resume.')
    parser.add_argument('--data', type=str,
                        help='name of data file', default='data/jobs.json')
    parser.add_argument('--bigrams', type=int,
                        help='number of bigrams', default='30')
    parser.add_argument('--trigrams', type=int,
                        help='number of trigrams', default='30')
    parser.add_argument('--words', type=int,
                        help='number of words', default='30')
    return parser.parse_args()

def print_results(results,title):
    print("\n====== ",title,"====== \n")
    for result in results:
         if isinstance(result,tuple): 
              result = ' '.join(result)
         print(result)

def import_jobs():
    text = ''
    companies = []
    with open(args.data,encoding='utf-8') as f:
        data = json.load(f)

    for job in data:
        text += job["description"].lower()
        companies.append(job["company"].lower())

    return text,companies

def tokenize(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized = tokenizer.tokenize(text)
    return tokenized

def filter_text(text, words):
    filtered_text = []
    for w in text:
        if w not in words:
            filtered_text.append(w)
    return filtered_text

def top_ngram(text,measures,finder,num):

    finder = finder.from_words(text)

    # only bigrams that appear 3+ times
    finder.apply_freq_filter(3)

    # return the n-grams with the highest PMI
    return finder.nbest(measures, num)

def top_words(text,num):
    fdist = FreqDist(text)
    return fdist.most_common(num)

if __name__ == "__main__":
    args = parse_args()
    text, companies = import_jobs()
    text = tokenize(text)
    text = filter_text(text,my_stop_words+companies+common_stop_words)
    results = top_ngram(text,BigramAssocMeasures.pmi,BigramCollocationFinder, args.bigrams)
    print_results(results,"Top bigrams (PMI)")

    results = top_ngram(text,TrigramAssocMeasures.pmi,TrigramCollocationFinder, args.trigrams)
    print_results(results,"Top trigrams (PMI)")

    results = top_words(text,30)
    results = [result[0] for result in results]
    print_results(results,"Top Words")