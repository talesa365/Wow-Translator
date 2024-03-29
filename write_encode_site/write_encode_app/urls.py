from django.urls import path
from write_encode_app.views import TranslatorView, HistoryView

urlpatterns = [
    path('', TranslatorView.as_view(), name='translator'),
    path('<str:session_key>/', HistoryView.as_view(), name='history'),
]