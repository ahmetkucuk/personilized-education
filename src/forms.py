from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from models import *

'''

class ContextForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-responseForm'
        self.helper.form_class = 'form-vertical'
        self.helper.add_input(Submit('submit', 'Save'))
    class Meta:
        model = Context
        fields = ['text', 'confidence']
        labels = dict(text=_('Your answer'))
'''

class SampleForm(forms.Form):
    item = forms.CharField()