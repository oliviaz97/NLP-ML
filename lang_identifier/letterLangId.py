# letter bigram model for language identification with no smoothing - Olivia Zhang
import os
import sys
from math import log
from decimal import Decimal
import string

# preprocess English text
f = open(os.getcwd() + "/training/LangId.train(1).English", "r")
english_sentences = f.readlines() # store the input text as a list of individual sentences
f.close()

# process the English text, remove punctuations and spaces, add start and end chars for better calculation
for sen in english_sentences:
    sen = list(sen)
    # get rid of all punctuations in the list of words
    for s in sen:
        if s in string.punctuation:
            sen.remove(s)
    sen = ['<s>'] + sen + ['<s>'] + [None] # concatenate start and end chars for better calculation

# preprocess French text
f = open(os.getcwd() + "/training/LangId.train(1).French", "r")
french_sentences = f.readlines() # store the input text as a list of individual sentences
f.close()
# process the text, remove punctuations and spaces, add start and end chars for better calculation
for sen in french_sentences:
    sen = list(sen)
    # get rid of all punctuations in the list of words
    for s in sen:
        if s in string.punctuation:
            sen.remove(s)
    sen = ['<s>'] + sen + ['<s>'] + [None] # concatenate start and end chars for better calculation

# preprocess Italian text
f = open(os.getcwd() + "/training/LangId.train(1).Italian", "r")
italian_sentences = f.readlines() # store the input text as a list of individual sentences
f.close()
# process the text, remove punctuations and spaces, add start and end chars for better calculation
for sen in italian_sentences:
    sen = list(sen)
    # get rid of all punctuations in the list of words
    for s in sen:
        if s in string.punctuation:
            sen.remove(s)
    sen = ['<s>'] + sen + ['<s>'] + [None] # concatenate start and end chars for better calculation

# preprocess test data
f = open(os.getcwd() + "/testing/LangId(1).test", "r")
test_sentences = f.readlines() # store the input text as a list of individual sentences
f.close()
# process the text, remove punctuations and spaces, add start and end chars for better calculation
for sen in test_sentences:
    words = list(sen.split()) # split the input by space, store into a list
    # get rid of all punctuations in the list of words
    for word in words:
        if word in string.punctuation:
            words.remove(word)
    sen = list(sen)
    sen = ['<s>'] + sen + ['<s>'] + [None] # concatenate start and end chars for better calculation

# creates a dictionary of bigram
def create_bg(sentences):
    bg = {}
    # sen is a string of words
    for sen in sentences:
        for word in range(0, len(sen) - 1):
            # create entry if current word is not in the bigram
            # set occurance to 1
            if sen[word] not in bg.keys():
                bg[sen[word]] = {}
                bg[sen[word]][sen[word + 1]] = 1
            # cur word is already in the bigram
            # move on if next word is already in the colums
            else:
                if sen[word + 1] in bg[sen[word]].keys():
                    bg[sen[word]][sen[word + 1]] += 1
                # set occurance to 1 if next word isn't in the bigram
                else:
                    bg[sen[word]][sen[word + 1]] = 1
    return bg

# calculate the probability
def test(bg, word, prev):
    prob = 0
    tol = 0
    # if previous word is not in the bigram, return nothing
    if prev in bg.keys():
        if word in bg[prev].keys():
            prob = bg[prev][word]
        # word not in the bigram, occur = 0
        else:
            return 0
        for i in bg[prev].keys():
            tol = tol + bg[prev][i]
    else:
        return 0 # previous word not in the bigram, occur = 0
    return (log(prob/float(tol)))

def result_lang(sen):
    # idx: 0 - eng, 1 - fr, 2 - it
    result_prob = [0, 0, 0]

    for word in range(0, len(sen) - 1):
        result_prob[0] = result_prob[0] + test(eng_bg, sen[word + 1], sen[word])
        result_prob[1] = result_prob[1] + test(fr_bg, sen[word + 1], sen[word])
        result_prob[2] = result_prob[2] + test(it_bg, sen[word + 1], sen[word])

    max_prob = max(result_prob)

    if(result_prob.index(max_prob) == 0):
        return "English\n"
    elif(result_prob.index(max_prob) == 1):
        return "French\n"
    else:
        return "Italian\n"


# main
if __name__ == "__main__":
    eng_bg = create_bg(english_sentences)
    fr_bg = create_bg(french_sentences)
    it_bg = create_bg(italian_sentences)

    output_list = [] # list to store the output languages
    count = 0
    for sen in test_sentences:
        count += 1
        output_list.append(str(count) + " " + result_lang(sen))

    # writting to output
    output = "".join(output_list)
    op = open("letterLangId.out", "w")
    op.write(output)
    op.close()
