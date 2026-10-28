from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'description', 'release_year', 'rating', 'image_url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'rating': forms.NumberInput(attrs={'step': '0.1'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/poster.jpg'}),
        }
        labels = {
            'image_url': 'Image URL',
        }
        error_messages = {
            'title': {'required': 'Title cannot be empty.'},
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if not title:
            raise forms.ValidationError('Title cannot be empty.')
        return title
