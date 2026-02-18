from django import forms
from films.models import Film
from films.models import Category, Genre
class CreateFilmForm(forms.ModelForm):
    name = forms.CharField()
    episodes = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Film
        fields = ["name", "episodes", "image"] 
    
class SearchForm(forms.Form):
    for_test_list = [("1", "test1"), ("2", "test2")]
    choice_list = [('1', 'More than 100'), ('2', 'Less than 100')]
    search = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    episode_choice = forms.ChoiceField(choices=choice_list, required=False)
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), required=False)
    for_test = forms.MultipleChoiceField(choices=for_test_list, required=False)
