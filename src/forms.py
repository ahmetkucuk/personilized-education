from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import InlineRadios
from models import *


class ContextForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-responseForm'
        self.helper.form_class = 'form-vertical'
        self.helper.add_input(Submit('submit', 'Save'))
    class Meta:
        model = Context
        fields = ['age', 'english_level', 'native_language']


class SampleForm(forms.Form):
    item = forms.CharField()

class LessonForm(forms.Form):
    def __init__(self, lesson, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-responseForm'
        self.helper.form_class = 'form-vertical'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['answer'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            label="Question text ",
            choices=(('1',lesson.choice1),('2',lesson.choice2),('3',lesson.choice3),),
            )

    answer=forms.ChoiceField()



class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-responseForm'
        self.helper.form_class = 'form-vertical'
        self.helper.add_input(Submit('submit', 'Save'))