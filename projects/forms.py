from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total','vote_ratio', 'owner', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})