from django import forms


from movworldapp.models import MovieList


class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ['title', 'poster', 'desc', 'release_date', 'actors', 'category', 'link']
