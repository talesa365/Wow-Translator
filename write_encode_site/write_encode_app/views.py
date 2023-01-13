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
            Session.objects.create(session_key=request.session.session_key)

        input_form =InputForm()
        
        context = {
            'session_key': request.session.session_key,
            'form': input_form,
            'translation': '',
        }
        
        return render (
            request=request,
            template_name='index.html',
            context=context,
        )
        
    def post(self, request):
        
        session = Session.objects.get(session_key=request.session.session_key)
        
        input_form = InputForm(request.POST)
        input_form.save(session)
        
        input = Input.objects.get(content=request.POST['content'])
        
        input_form = InputForm()
        
        translation = Translation.objects.get(input_id=input.id)
        
        context = {
            'session_key': request.session.session_key,
            'form': input_form,
            'translation': translation,
        }
        
        return render (
            request=request,
            template_name='index.html',
            context=context,
        )

class HistoryView(View):
    def get(self, request, session_key):

        session = Session.objects.get(session_key=session_key)
        
        translations = Translation.objects.all()

        context = {
            'session_key': session_key,
            'session': session.id,
            'translations': translations,
        }

        return render (
        request=request,
        template_name='history.html',
        context=context,
        )
    
    def post(self, request, session_key):
        print(request.POST)
        
        session = Session.objects.get(session_key=session_key)
        
        if 'delete' in request.POST:
        
            translation = Translation.objects.get(id=request.POST['delete'])
            translation.delete()
        
        elif 'morse' in request.POST:
            translation = Translation.objects.get(id=request.POST['morse'])
            translation.output = morse_translator(translation.input_content)
            translation.language = 'morse'
            translation.save()
        elif 'binary' in request.POST:
            translation = Translation.objects.get(id=request.POST['binary'])
            translation.output = binary_translator(translation.input_content)
            translation.language = 'binary'
            translation.save()
            
        
        translations = Translation.objects.all()

        context = {
            'session_key': session_key,
            'session': session.id,
            'translations': translations,
        }

        return render (
        request=request,
        template_name='history.html',
        context=context,
        )
        