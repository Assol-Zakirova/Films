from django import forms

class RegisterForms(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password_confirm = forms.CharField(required=True)

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
    
class LoginForms(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

class UpdateForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True) 
    password_confirm = forms.CharField(required=True)

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

class UpdateProfileForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    age = forms.IntegerField(required=True)
    image = forms.ImageField(required=False)
