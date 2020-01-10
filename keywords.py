import spacy
import pandas as pd
import os
import ast
DATA_DIR="old/"

def get_aspects(x):

    nlp = spacy.load("en_core_web_sm")  # en_core_web_sm en_core_web_lg

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                  "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                  "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                  "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    doc = nlp(x)
    doc = [i.text for i in doc if i.text not in stop_words and i.pos_=="NOUN"] ## Remove common words and retain only nouns
    doc = list(map(lambda i: i.lower(),doc)) ## Normalize text to lower case
    doc = pd.Series(doc)
    doc = doc.value_counts().head().index.tolist() ## Get 5 most frequent nouns

    return doc

list_nouns = []
list_nouns_first = []
df = pd.read_csv('results/combined.csv', encoding='windows-1252') # put the csv here
list_reviews = df["reviewer_text"].tolist() # refer to column that contains reviews here

for review in list_reviews:
    nouns = get_aspects(review)
    list_nouns.append(nouns)

    if len(nouns) == 0:
        list_nouns_first.append('')
    else:
        list_nouns_first.append(nouns[0])

df["keywords"] = list_nouns
df["keywords_first"] = list_nouns_first



def countKeywords(df):
    list_main = []
    for index, row in df.iterrows():
        list_keywords = ast.literal_eval(row['keywords'])
        for keyword in list_keywords:
            row['single_keyword'] = keyword
            df = pd.DataFrame(row).transpose()
            list_main.append(df)

    df = pd.concat(list_main)

    return df

countKeywords(df)
df.to_csv("results/reviews/combined_keywords.csv") # set where the results will go here