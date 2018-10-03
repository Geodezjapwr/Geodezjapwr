from django import forms

from .models import Opinia

class OpiniaForm(forms.ModelForm):

    class Meta:
        model = Opinia
        fields = ('autor', 'text',)


