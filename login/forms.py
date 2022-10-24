from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control",
        "id": "username",
        "name": "username",
        "placeholder": "Логін"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "class": "form-control",
        "id": "password",
        "name": "password",
        "placeholder": "Пароль"
    }))

    def clean(self):
        username = self.cleaned_data["username"].strip()
        password = self.cleaned_data["password"].strip()

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or user.check_password(password):
                return forms.ValidationError("Невірні дані")

        return super().clean()


class RegistrationUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control",
        "id": "username",
        "name": "usermane",
        "placeholder": "Логін",
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "class": "form-control",
        "id": "password",
        "name": "password",
        "placeholder": "Пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "class": "form-control",
        "id": "password2",
        "name": "password2",
        "placeholder": "Підтвердження пароля"
    }))

    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] == data["password2"]:
            return data["password2"]
        raise forms.ValidationError("Паролі мають співпадати")

    class Meta:
        model = User
        fields = ("username", "password", "password2")