from django import forms
from .models import ModelInline
from dal import autocomplete, forward


class ModelInlineForm(forms.ModelForm):
    class Meta:
        model = ModelInline
        fields = "__all__"
        widgets = {
            'text': autocomplete.ModelSelect2Multiple(url='error:error-autocomplete',
                                             forward=[forward.Self()]),
        }
