import os
import sys

f1 = open(os.getcwd() + "/LangId.sol")
sol = f1.readlines()
f1.close()

f2 = open(os.getcwd() + "/letterLangId.out")
out = f2.readlines()
f2.close()

f3 = open(os.getcwd() + "/wordLangId.out")
word_out = f3.readlines()
f3.close()

f4 = open(os.getcwd() + "/wordLangId2.out")
word_out2 = f4.readlines()
f4.close()

fit = 0
for i in range(0, len(sol)):
    if(sol[i] == out[i]):
        fit += 1
print(fit)
print(fit/float(len(out)))

word_fit = 0
for i in range(0, len(sol)):
    if(sol[i] == word_out[i]):
        word_fit += 1
print(word_fit)
print(word_fit/float(len(word_out)))

word_fit2 = 0
for i in range(0, len(sol)):
    if(sol[i] == word_out2[i]):
        word_fit2 += 1
print(word_fit2)
print(word_fit2/float(len(word_out2)))
