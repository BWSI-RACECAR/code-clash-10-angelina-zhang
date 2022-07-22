"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #10 - Song Analyzer (songanalyzer.py)


Author: Carter Berlind

Difficulty Level: 5/10

Prompt: Freddy is trying to write a song to impress his friends but needs help 
checking his lines. He decides to enlist you, a python programmer, to create a 
program to see if his lines are good. He tells you that he wants his lines to 
be judged off of whether they rhyme and how much alliteration is there.

Create a program in which the user can input a sentence and the program will 
report back how many words start with the same letters and what those letters 
are and how many words end in the same last three letters (If a word is less 
than three letters we do not consider its rhymes). 

Constraints: Words must be separated by a space. Only report if letters occur at the 
beginning of words multiple times. Don’t worry about commas and punctuation.

Test Cases:
Input: “carter is cool and not a fool”;                     Output: ”c=2,a=2, 2 rhyming words”
Input: “running jumping and swimming are really fun”;       Output: ”r=2, a=2, 3 rhyming words"
Input: “a ban on that book”;                                Output: ”b=2, 0 rhyming words”
Input: “good food for nice mice”;                           Output: ”f=2, 4 rhyming words”
Input: “howdy rowdy hikers hope you have a great time”;     Output: "h=4, 2 rhyming words”
"""

class Solution:
    def song_analyze(self,lyric):
        # type lyric: string
        # return: string 
        
        # TODO: Write code below to return a string with the solution to the prompt
        words = lyric.split(" ")
        first = []
        alit = []
        letter_count = []
        word_endings = []
        filtered_endings = []
        rhyme_amount = []
        rhyme_counte = 0
        for i in range (len(words)):
            if(words[i][0] in first):
                if(words[i][0] in alit):
                    letter_count[alit.index(words[i][0])]+=1
                else:
                    alit.append(words[i][0])
                    letter_count.append(2)
            else:
                first.append(words[i][0])
        for j in range(len(words)):
            if (words[j][-3:] in word_endings):
                if(words[j][-3:] in filtered_endings):
                    rhyme_amount[filtered_endings.index(words[j][-3:])]+=1
                else:
                    filtered_endings.append(words[j][-3:])
                    rhyme_amount.append(2)
            else:
                word_endings.append(words[j][-3:])
        for k in range (len(rhyme_amount)):
            rhyme_counte += rhyme_amount[k]
        final_string = ""
        for i in range(len(alit)):
            final_string = final_string + "{letter}={number}, ". format(letter= alit[l],number=letter_count[l])
        return final_string + "{rhymes} rhyming words". format(rhymes=rhyme_counte)


        # list = lyric.split()
        # new_list= []
        # for char in list:
        #     new_list.append(char[0])
        # my_dict = {i:new_list.count(i) for i in new_list}
        # new_dict = {}
        # for key in my_dict:
        #     if my_dict[key] != 1:
        #         new_dict[key]= my_dict[key]
        # # for i in range (0, len(new_list)):
        # #     if char[i]
        # count_rhyme = 0
        # count_letters = ""
        # return new_dict, ", rhyming words", count_rhyme

def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.song_analyze(string1)
    print(ans)

if __name__ == "__main__":
    main()