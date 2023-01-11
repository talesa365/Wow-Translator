from django.forms import ModelForm

from write_encode_app.models import Input, Session, Translation
from write_encode_app.translators import binary_translator, morse_translator

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['content']
        labels = {
            'content': '',
        }
        
    def save(self, session, *args, **kwargs):
        
        content = self.data['content']
        char_length = len(self.data['content'])
        
        try:
            Input.objects.get(content=content)
        except Input.DoesNotExist:
            input = Input.objects.create(content=content, character_length=char_length)
        
        session.inputs.add(input)
        
        if 'binary' in self.data:
            Translation.objects.create(input_id=input.id, output=binary_translator(content), language='binary')
        elif 'morse' in self.data:
            Translation.objects.create(input_id=input.id, output=morse_translator(content), language='morse')
            

# class SessionForm(ModelForm):
#     class Meta:
#         model = Session
#         fields = ['']

# class TranslationForm(ModelForm):
#     class Meta:
#         model = Translation
#         fields = ['']
