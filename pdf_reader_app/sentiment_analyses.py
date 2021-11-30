from textblob import TextBlob
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import re

class SentimentAnalysis:
    """Class used to sentiment analysis of pdf paragraph"""

    def __init__(self, file):
        """Add file"""
        self.file = file

    def paragraph_sentence(self):
        output_string = StringIO()
        parser = PDFParser(self.file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        x = output_string.getvalue()
        pdf_text = str(x).strip()
        clean_text = re.sub(r'[^a-zA-Z\.]', " ", pdf_text)
        return clean_text

    def sentiment_polarity(self, paragraph):
        if paragraph.sentiment.polarity > 0:
            return "Positive Behaviour of Sentence"
        elif paragraph.sentiment.polarity < 0:
            return "Negative Behaviour of Sentence"
        elif paragraph.sentiment.polarity == 0:
            return "No negative and positive behaviour found"

    def sentiment_analysis(self):
        sentence_data = self.paragraph_sentence()
        correction = TextBlob(sentence_data)
        sentence_list = []
        for item in correction.sentences:
            item = item.replace(".", "")
            if len(item) > 0:
                sentence_list.append((item, self.sentiment_polarity(item)))
        return sentence_list



