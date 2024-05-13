from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'title',
            'content',
            'feeling',
            'score',
            'date'
        ]
    # title = forms.CharField(max_length=100, label='제목')
    # content = forms.CharField(label='내용', widget=forms.Textarea)
    # feeling = forms.CharField(label='감정 상태', max_length=80)
    # score = forms.IntegerField(label='감정 점수')