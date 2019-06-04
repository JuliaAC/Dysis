from django import forms

from .models import Post, Picture

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        labels = {'title': 'Titel', 'text': 'Tekst'}


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ('document', 'description', 'post')
        labels = {'document': 'Afbeelding', 'description': 'Omschrijving', 'post': 'Op pagina/bij artikel'}