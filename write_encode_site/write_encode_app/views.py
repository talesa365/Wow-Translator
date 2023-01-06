from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from write_encode_app.forms import InputForm

# Create your views here.

def index(request):
    return HttpResponse

class TranslatorView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='index.html'
            context={}
        )
        
    def post(self, request):
        input_form = InputForm()
        html_data = {
            'input_form': input_form
        }
        return render(
            request=request,
            template_name='index.html',
            context=html_data,
        )

class HistoryView(View):
    def get(self, request):
        return render (
        request=request,
        template_name='history.html',
        context={}
        
        )