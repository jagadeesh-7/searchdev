from django.forms import ModelForm
from django import forms

from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description','featured_image', 'demo_link', 'source_link']

        widgets= {
            'tags':forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args, **kwargs)

        # ineffiecient to hardcode
        # self.fields['title'].widget.attrs.update({'class':'input'})

        # looping logic
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value' : 'Place Your Vote',
            'body' : 'Add a Comment With Your Vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm,self).__init__(*args, **kwargs)

        # ineffiecient to hardcode
        # self.fields['title'].widget.attrs.update({'class':'input'})

        # looping logic
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})