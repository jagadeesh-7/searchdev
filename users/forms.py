from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Message, Profile, Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)

        # ineffiecient to hardcode
        # self.fields['title'].widget.attrs.update({'class':'input'})

        # looping logic
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        exclude = ['user']

    
    def __init__(self, *args, **kwargs):
        super(ProfileForm,self).__init__(*args, **kwargs)

        # ineffiecient to hardcode
        # self.fields['title'].widget.attrs.update({'class':'input'})

        # looping logic
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm,self).__init__(*args, **kwargs)

        # ineffiecient to hardcode
        # self.fields['title'].widget.attrs.update({'class':'input'})

        # looping logic
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
    
    def __init__(self, *args, **kwargs):
        super(MessageForm,self).__init__(*args, **kwargs)

        # ineffiecient to hardcode
        # self.fields['title'].widget.attrs.update({'class':'input'})

        # looping logic
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


