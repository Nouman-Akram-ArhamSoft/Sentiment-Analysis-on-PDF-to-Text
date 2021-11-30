from django.shortcuts import render
from django.shortcuts import render
from .sentiment_analyses import SentimentAnalysis

# Create your views here.
class PdfUploader:
    pass



def simple_upload(request):
    if request.method == 'POST' and request.FILES['my_file']:
        my_file = request.FILES['my_file']
        sentiment = SentimentAnalysis(my_file)
        sentence_list = sentiment.sentiment_analysis()
        # print(sentence_list)
        return render(request, 'pdf_reader_app/sentiment-analysis.html', {'pdf_text_list' : sentence_list})
    return render(request, 'pdf_reader_app/main.html')