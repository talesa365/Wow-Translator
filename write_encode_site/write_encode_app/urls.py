from django.urls import path
from . import views
from write_encode_app.views import TranslatorView, HistoryView

urlpatterns = [
    path('', TranslatorView.as_view(), name='index'),
    path('history/', HistoryView.as_view(), name='history')
]