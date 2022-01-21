from django import forms
from mysite.models import Marks, MaxStudentScore, Users


class CreateMarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'


class CreateMaxScoreForm(forms.ModelForm):
    class Meta:
        model = MaxStudentScore
        fields = '__all__'

