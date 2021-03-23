from docx import Document
import re
import os
import pyexcel as pe


def analyze(docfile):
    frequency ={}
    document = docfile
    dicts ={}
    for file in os.listdir(os.getcwd()):
        if file.endswith(".docx"):
            file_name_ = (os.path.join(file))

    file_name =(file_name_.rsplit('.', 1)[0]) 


    file =''
    for para in document.paragraphs:
        file +=para.text.lower()

    match_pattern = re.findall(r'\b[a-zA-Z]{1,40}\b', file)
    len_words = len(match_pattern)

    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        frequency_list = frequency.keys()
    for words in frequency_list:
        threshold = 0.001
        if  (frequency[words]/len(match_pattern)) >= threshold:
            dicts[words] =((frequency[words]/len(match_pattern)))
        else:
            pass

    dictionary_items = dicts.items()
    sorted_items = sorted(dictionary_items)
    sorted_items = dict(sorted_items)
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
        docfile = Document('ulysses.docx')
        analyze(docfile) #Calling main function 
