from django.forms import ModelForm

from write_encode_app.models import Input, Session, Translation

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['content']
        labels = {
            'content': '',
        }
        
    def save(self, *args, **kwargs):
        content = self.data['content']
        char_length = len(self.data['content'])
        
        print(content, char_length)
        # Input.objects.create(content=self.data['content'],)

# class SessionForm(ModelForm):
#     class Meta:
#         model = Session
#         fields = ['']

# class TranslationForm(ModelForm):
#     class Meta:
#         model = Translation
#         fields = ['']