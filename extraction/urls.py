# extraction/urls.py
from django.urls import path

from extraction.api.views import PDFExtractView

urlpatterns = [
    path('extract/', PDFExtractView.as_view(), name='pdf-extract'),
]
