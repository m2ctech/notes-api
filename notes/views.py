from django.shortcuts import render
from .models import Note
from rest_framework import viewsets
from .serializers import NoteSerializer

# Create your views here.

class NotesViewsets(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

