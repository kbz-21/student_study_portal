from django import forms
from models import *

class NotesForm(forms.ModelForm):
    class Meta:
        # mapping model class note section so we didn't need to write those 3 line again(note section).
        models=Notes
        fields=['tittle','description']  
