from docx import Document

document = Document('C://Users//91720//Documents//ds_reg_exp_proj//assignment2//ulysses.docx')
for para in document.paragraphs:
    print(para.text)