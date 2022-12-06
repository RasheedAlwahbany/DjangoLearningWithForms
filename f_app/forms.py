from django import forms
import datetime
class examForms(forms.Form):
    question=forms.CharField(label="Question",max_length=300)
    answer=forms.CharField(label="Answer",max_length=400)
    # date=forms.CharField(help_text="date",label="Date",max_length=200,empty_value=datetime.datetime.now(),)