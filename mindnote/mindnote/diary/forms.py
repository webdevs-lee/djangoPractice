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
        widgets = {
            # 날짜를 Calendar로 고를 수 있게 하기 위해서 사용한 코드
            # 참고사이트: https://pythonassets.com/posts/date-field-with-calendar-widget-in-django-forms/
            'date': forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})
        }
    # title = forms.CharField(max_length=100, label='제목')
    # content = forms.CharField(label='내용', widget=forms.Textarea)
    # feeling = forms.CharField(label='감정 상태', max_length=80)
    # score = forms.IntegerField(label='감정 점수')