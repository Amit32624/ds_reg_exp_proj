import os.path
import pyexcel as pe
from docx import Document


def doc_analyse(doc):###read the data and append into dictonary
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    paragraph = '\n'.join(fullText)
    paragraph_smaller = paragraph.lower()
    raw_word = paragraph_smaller.split()
    unwanted_chars = '-,.,,,-,_,!,:,,*,?,—,(,),;,"'
    unwanted_chars1 = '"'
    for word in raw_word:
        words = word.strip(unwanted_chars)
        words = words.strip("'")
        if words not in wordfreq:
            wordfreq[words] = 0
        wordfreq[words] += 1
    a = dict(sorted(wordfreq.items(), key=lambda item: item[1], reverse=True))
    b = sum(a.values())
    a = {k: v / b for k, v in a.items()}
    return a
def excel_sheet(doc1):##based on wordfrequency and threshold value appended to excel sheet
    res = []
    word_threshold = 0.001
    for key, values in doc1.items():
        if (values > word_threshold):
            res.append([key, values])
    file_name = 'ulsyess'
    pe.save_as(array=res, dest_file_name=file_name + "_word_stats.xlsx")
    book = pe.get_book(file_name = file_name + "_word_stats.xlsx")
    sname = list(book.to_dict())[0]
    sheet = book[sname]
    sheet.name = "Word Frequency Stats"
    book.save_as(file_name + "_word_stats.xlsx")
    print(book)

if __name__ == '__main__':
     wordfreq={}
     rootdir = os.getcwd()
     doc = Document(os.path.join(rootdir, "ulysses.docx"))
     doc1=doc_analyse(doc)
     result=excel_sheet(doc1)