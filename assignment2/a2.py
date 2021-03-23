# Course: CS6507
# Laboratory: Assignment 2
# Date of creation: 2021/03/15
# Author: Amit Somnath Sambrekar
# Number: 120220153
# Description: Write a Python program named a2.py that includes a function analyze(docfile) that reads
#the text contained in the file named docfile (presumed to be a .docx file) and calculates the
#frequency of occurence of each word appearing therein.

from docx import Document
import re
import os
import pyexcel as pe

#Main function to retrieve word frequency from docx file.
def analyze(docfile):
    frequency ={}
    document = docfile
    dicts ={}

    #Retriving docx file name.
    for file in os.listdir(os.getcwd()):
        if file.endswith(".docx"):
            file_name_ = (os.path.join(file))

    #Removing the extension of the filename.
    file_name =(file_name_.rsplit('.', 1)[0]) 
    file=[]
    for para in document.paragraphs:

        file.append(para.text.lower())
    paragraph = '\n'.join(file)

    #Extracting words from the document
    match_pattern = re.findall(r'(\b[^\s]+\b)', paragraph)
    len_words = len(match_pattern) #counting the number of words

    #Calculating the word frequency for each word.
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        frequency_list = frequency.keys()
    for words in frequency_list:
        threshold = 0.001
        if  (frequency[words]/len(match_pattern)) >= threshold:
            dicts[words] =((frequency[words]/len_words))
        else:
            pass

    #Sorting the frequency values in descending order
    sorted_items = sorted(dicts.items(), key=lambda x:x[1],reverse=True)
    sorted_items = dict(sorted_items)

    #Writing the values into the xlsx file
    res = [] 
    for key, val in sorted_items.items(): 
        temp = [key,val]
        res.append(temp) 
    pe.save_as(array=res, dest_file_name=file_name+"_word_stats.xlsx")
    FILE_NAME = file_name+"_word_stats.xlsx"
    book = pe.get_book(file_name = FILE_NAME)
    sname = list(book.to_dict())[0]
    sheet = book[sname]
    sheet.name = "Word Frequency Stats"
    book.save_as(file_name+"_word_stats.xlsx")


if __name__ == '__main__':
        for file in os.listdir(os.getcwd()):
            if file.endswith("ses.docx"):
                file_name_ = (os.path.join(file))
        docfile = Document(file_name_)
        analyze(docfile) #Calling main function 

