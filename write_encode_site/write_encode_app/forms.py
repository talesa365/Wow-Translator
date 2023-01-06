from django.forms import ModelForm

from write_encode_app.models import Input, Session, Translation

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['content']

# class SessionForm(ModelForm):
#     class Meta:
#         model = Session
#         fields = ['']

# class TranslationForm(ModelForm):
#     class Meta:
#         model = Translation
#         fields = ['']