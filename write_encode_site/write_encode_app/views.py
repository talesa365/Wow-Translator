from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class TranslatorView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='index.html',
            # context=

        )

class HistoryView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='history.html',
            # context=
        )