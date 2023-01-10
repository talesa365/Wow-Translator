from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views import View

from write_encode_app.forms import InputForm
from write_encode_app.models import Session, Input, Translation

from write_encode_app.translators import binary_translator, morse_translator

'''
Functions for creating & deleting sessions
'''
def delete_session(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    return HttpResponse("Session Data: Cleared")

def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password'

# Create your views here.
class TranslatorView(View):
    def get(self, request):
        create_session(request)
        
        try:
            Session.objects.get(session_key=request.session.session_key)
        except Session.DoesNotExist:
            print(request.session.session_key)
            # Session.objects.create(session_key=request.session.session_key)

        input_form =InputForm()
        
        context = {
            'form': input_form
        }
        
        return render (
            request=request,
            template_name='index.html',
            context=context,
        )
        
    def post(self, request):
        input_form = InputForm(request.POST)
        input_form.save()
        
        print(binary_translator(request.POST['content']))
        print(morse_translator(request.POST['content']))
        
        return redirect('translator')
        # html_data = {
        #     'input_form': input_form
        # }
        
        # if 'binary' in request.POST:
        #     print('BINARY')
        # elif 'morse' in request.POST:
        #     print('MORSE')
        # return render(
        #     request=request,
        #     template_name='index.html',
        #     context=html_data,
        # )

class HistoryView(View):
    def get(self, request):
        return render (
        request=request,
        template_name='history.html',
        context={}
        
        )
        