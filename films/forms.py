from django import forms
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
