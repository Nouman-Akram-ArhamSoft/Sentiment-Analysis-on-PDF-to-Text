import PyPDF2
import PyPDF2 as pdf
import re
from textblob import TextBlob
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

class PdfToText:
    """class used to convert pdf into text"""

    def __init__(self, file:str) -> None:
        """
        Constructor to initialize the file
        :param file: file path (str)
        """
        self.file = file

    def convert_pdf_to_text(self):
        """
        Convert PDF file to Text
        :return: Text Documents
        """
        output_string = StringIO()
        with open(self.file, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        x = output_string.getvalue()
        pdf_text = str(x)
        clean_text = re.sub(r'[^a-zA-Z\n\.]', " ", pdf_text)
        correction = TextBlob(clean_text)

        for item in correction.sentences:
            return item.correct()
