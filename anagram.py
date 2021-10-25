import math
import sys
import re
import copy


class Anagram:

    def __init__(self, word, numb=0):
        self.letters = list()
        self.word = word
        self.numb = numb
        self.matches = list()
        self.counter = {}

        self.regex = "["+self.word+"]{"+str(len(self.word))+"}"
        for letter in self.word:
            self.letters.append(letter)
            if self.word.count(letter) > 1:
                self.counter = {letter: self.word.count(letter)}
        # print(self.counter)

        with open("anagram-master-dictionnaire.txt", "r") as file:
            my_list = file.readlines()

        temp_list = list()
        for k, line in enumerate(my_list):
            if re.search(self.regex, line[0:-1]) and len(self.word) == len(line[0:-1]) and line[0:-1] != self.word:
                # print(line[0:-1])
                temp_list.append(line[0:-1])
        # print(temp_list)

        temp_list2 = list()
        if self.counter:
            for word in temp_list:
                for letter_repete, number in self.counter.items():
                    # print(letter_repete, number)
                    if word.count(letter_repete) == number:
                        temp_list2.append(word)
        else:
            temp_list2 = copy.copy(temp_list)
        # print(temp_list2)
        
        
        for word in temp_list2:
            flag = 0
            # print(word, word.find('g'), word.find('a'), word.find('r'), word.find('d'), word.find('e'), word.find('r'))
            for letter in self.letters:
                # counter = word.count(letter)
                # if counter == 2:

                if word.find(letter) >= 0:
                    flag += 1
                else:
                    flag = 0
                    continue
                if int(flag) == int(len(self.word)):
                    print(word)
                    flag = 0


init = Anagram(sys.argv[1])
