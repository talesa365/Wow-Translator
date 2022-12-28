from django.urls import path
from . import views
from write_encode_app.views import TranslatorView, HistoryView

urlpatterns = [
    path('', views.index, name='index'),
    path('', TranslatorView.as_view(), name='translator'),
    path('<str:translator', HistoryView.as_view(), name='history')
]