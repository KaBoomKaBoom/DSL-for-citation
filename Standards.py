from docx import Document
from docx.shared import Pt
class Standards:
    def generate_apa_citation(qouote, source_type, author, year, title, book_title, publisher):
    #print(qouote, source_type, author, year, title, book_title, publisher)
        doc = Document("test.docx")
            # For in-text citation
        citation_text = qouote + "(" + author + ", " + str(year) + ")"
        p = doc.add_paragraph(citation_text)
        p.style.font.name = 'Times New Roman'
        p.style.font.size = Pt(12)
            # For bibliography/reference list
        citation_bib = author + " (" + str(year) + "). " + title + ". "
        p = doc.add_paragraph(citation_bib)

        if source_type == "book":
            citation_bib += book_title  + ' ' + publisher + "."
            p.add_run(book_title + ' ')
            p.add_run(publisher + ".").italic = True   
        elif source_type == "journal":
            citation_bib += book_title  + ' ' + publisher + "."
            p.add_run(book_title + ' ')
            p.add_run(publisher + ".").italic = True 
        elif source_type == "website":
            citation_bib += book_title  + ' ' + publisher + "."
        doc.save('test.docx')
        return citation_text, citation_bib

    def generate_mla_citation(qouote, source_type, author, year, title, book_title, publisher):
        #print(qouote, source_type, author, year, title, book_title, publisher)
        doc = Document("test.docx")
            # For in-text citation
        citation_text = qouote + " (" + author + ")."
        p = doc.add_paragraph(citation_text)
        p.style.font.name = 'Times New Roman'
        p.style.font.size = Pt(12)
            # For bibliography/reference list
        citation_bib = author + '"' + title + '."'
        p = doc.add_paragraph(citation_bib)

        if source_type == "book":
            citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
            p.add_run(book_title + ', ').italic = True
            p.add_run(publisher + ", ")
            p.add_run(str(year) + ".") 
        elif source_type == "journal":
            citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
            p.add_run(book_title + ', ').italic = True
            p.add_run(publisher + ", ")
            p.add_run(str(year) + ".")
            
        elif source_type == "website":
            citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
            p.add_run(book_title + ', ').italic = True
            p.add_run(publisher + ", ")
            p.add_run(str(year) + ".")
        doc.save('test.docx')
        return citation_text, citation_bib

    def generate_cms_citation(qouote, source_type, author, year, title='', book_title='', publisher='', link=''):
        #print(qouote, source_type, author, year, title, book_title, publisher)
        doc = Document("test.docx")
            # For in-text citation
        citation_text = qouote + " (" + author + " " + str(year) + ")."
        p = doc.add_paragraph(citation_text)
        p.style.font.name = 'Times New Roman'
        p.style.font.size = Pt(12)
            # For bibliography/reference list
        citation_bib = author + ". "

        if source_type == "book":
            p = doc.add_paragraph(citation_bib)
            citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
            p.add_run(book_title + '. ').italic = True
            p.add_run(publisher + ", ")
            p.add_run(str(year) + ".") 
        elif source_type == "journal":
            p = doc.add_paragraph(citation_bib)
            citation_bib += '"' + book_title  + '," ' + publisher + ', ' + str(year) +  "."
            p.add_run('"' + book_title + '," ')
            p.add_run(publisher + ", ")
            p.add_run(str(year) + ".")
            
        elif source_type == "website":
            date = datetime.datetime.now()
            p = doc.add_paragraph(citation_bib)
            citation_bib += title  + ', ' + publisher + ', ' + 'accessed ' + date.strftime("%d %b %Y") + ", " +  link + "."
            p.add_run(title + ', ')
            p.add_run(publisher + ", ")
            p.add_run( 'accessed ' + date.strftime("%d %b %Y") + ", ")
            p.add_run(link + ".")
        doc.save('test.docx')
        return citation_text, citation_bib

    def generate_cse_citation(qouote, source_type, author, year,  book_title='', title='', publisher='', link='', index = None):
        #print(qouote, source_type, author, year, title, book_title, publisher)
        doc = Document("test.docx")
            # For in-text citation superscript the number of the citation
        citation_text = qouote + ' ' + str(index) + "."
        p = doc.add_paragraph(qouote )
        index_run = p.add_run(str(index))
        index_run.superscript = True
        p.add_run('.')
        p.style.font.name = 'Times New Roman'
        p.style.font.size = Pt(12)
            # For bibliography/reference list
        citation_bib = author  

        if source_type == "book":
            citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
            p = doc.add_paragraph(citation_bib)
            p.add_run(book_title + '. ')
            p.add_run(publisher + "; ")
            p.add_run(str(year) + ".") 
        elif source_type == "journal":
            citation_bib += '"' + book_title  + '," ' + publisher + ', ' + str(year) +  "."
            p.add_run(book_title + '. ')
            p.add_run(publisher + ", ")
            p.add_run(str(year) + ".")
            
        elif source_type == "website":
            date = datetime.datetime.now()
            citation_bib += title  + ', ' + publisher + '. ' + str(year) +', ' + '[accessed ' + date.strftime("%d %b %Y") + "]; " +  link + "."
            p = doc.add_paragraph(author)
            p.add_run(title + '. ')
            p.add_run(publisher + ". " + str(year))
            p.add_run( '[accessed ' + date.strftime("%d %b %Y") + "]; ")
            p.add_run(link + ".")
        doc.save('test.docx')
        return citation_text, citation_bib