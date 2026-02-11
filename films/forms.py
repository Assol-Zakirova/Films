from django import forms
from films.models import Category, Genre
list_of_bad_words = ['Assol']
class CreateFilmForm(forms.Form):
    name = forms.CharField()
    episodes = forms.CharField()
    image = forms.ImageField()
    def clean(self):
        data = self.cleaned_data
        name = data.get('name')
        if name in list_of_bad_words:
            raise forms.ValidationError('This word is forbidden ')
        return data
class SearchForm(forms.Form):
    for_test_list = [("1", "test1"), ("2", "test2")]
    choice_list = [('1', 'More than 100'), ('2', 'Less than 100')]
    search = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    episode_choice = forms.ChoiceField(choices=choice_list, required=False)
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), required=False)
    for_test = forms.MultipleChoiceField(choices=for_test_list, required=False)
