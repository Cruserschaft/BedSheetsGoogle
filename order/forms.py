from django import forms
from captcha.fields import *
from .models import *
import re


def errors_dict(value: str):
    tmp = {'required': f"""Поле "{value}" порожнє""",
           'min_length': f"""В полі "{value}" недостатньо символів""",
           'max_length': f"""В полі "{value}" недостатньо символів"""}
    return tmp


class OrderForm(forms.ModelForm):

    captcha = CaptchaField()

    first_name = forms.CharField(
        error_messages=errors_dict("Ім'я"),
        max_length=50,
        min_length=2,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "first",
            "name": "name",
            "placeholder": "Ім'я*"
        })
    )

    last_name = forms.CharField(
        error_messages=errors_dict("Прізвище"),
        max_length=50,
        min_length=2,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "last",
            "name": "name",
            "placeholder": "Прізвище*"
        })
    )

    phone = forms.CharField(
        error_messages=errors_dict("Телефон"),
        max_length=13,
        min_length=10,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "number",
            "name": "number",
            "placeholder": "Номер телефону*"
        })
    )

    email = forms.CharField(
        error_messages=errors_dict("Email"),
        max_length=50,
        min_length=5,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "email",
            "name": "compemailany",
            "placeholder": "Email адреса*"
        })
    )

    city = forms.CharField(
        error_messages=errors_dict("Місто"),
        max_length=50,
        min_length=5,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "add1",
            "name": "add1",
            "placeholder": "Місто*"
        })
    )

    address = forms.CharField(
        error_messages=errors_dict("Адреса"),
        max_length=50,
        min_length=5,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "add2",
            "name": "add2",
            "placeholder": "Адреса*"
        })
    )

    post = forms.ModelChoiceField(
        error_messages={'required': """Оберіть тип доставки"""},
        queryset=PostType.objects.all(),
        label="Тип доставки",
        empty_label="Не обрано*",
    )

    post_number = forms.CharField(
        max_length=5,
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "post_code",
            "name": "post_code",
            "placeholder": "Поштове відділення"
        })
    )

    post_code = forms.CharField(
        error_messages=errors_dict("Поштовий індекс"),
        max_length=5,
        min_length=5,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "post_code",
            "name": "post_code",
            "placeholder": "Поштовий код*"
        })
    )

    commentary = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(attrs={
            "type": "text",
            "class": "form-control",
            "id": "commentary",
            "name": "commentary",
            "placeholder": "Додаткова інформація (Номер відділення пошти)"
        })
    )



    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        if len(re.findall(r"[A-Za-zА-Яа-яІіЄєЇї\s]{2,30}", data)) == 1:
            return data
        raise forms.ValidationError("Правильно введіть ім'я")

    def clean_last_name(self):
        data = self.cleaned_data["last_name"]
        if len(re.findall(r"[A-Za-zА-Яа-яІіЄєЇї\s]{2,30}", data)) == 1:
            return data
        raise forms.ValidationError("Правильно введіть прізвище")

    def clean_phone(self):
        data = self.cleaned_data["phone"]
        if len(re.findall(r"(\+380?|380?|0)[0-9]{9}$", data)) == 1:
            return data
        raise forms.ValidationError("Правильно введіть телефон")

    def clean_email(self):
        data = self.cleaned_data["email"]
        if len(re.findall(r"[A-Za-z.-]{3,10}@[A-Za-z0-9]{4,}.[a-z]{2,3}$", data)) == 1:
            return data
        raise forms.ValidationError("Правильно введіть email пошту")

    def clean_city(self):
        data = self.cleaned_data["city"]
        if len(re.findall(r"[A-Za-zА-Яа-яІіЄєЇї\s]{2,30}$", data)) == 1:
            return data
        raise forms.ValidationError("Правильно введіть назву міста")

    def clean_address(self):
        data = self.cleaned_data["address"]
        if len(re.findall(r"[A-Za-zА-Яа-яІіЄєЇї\s0-9]{2,30}$", data)) == 1:
            return data
        raise forms.ValidationError("Правильно введіть адресу")

    def clean_post(self):
        data = self.cleaned_data["post"]
        if data:
            return data
        raise forms.ValidationError("Оберіть тип доставки")

    def clean_post_code(self):
        data = self.cleaned_data["post_code"]
        if len(re.findall(r"^[0-9]{5}$", data)) == 1:
            return data
        raise forms.ValidationError("Правильно введіть поштовий індекс")

    class Meta:
        model = Order
        fields = "__all__"
