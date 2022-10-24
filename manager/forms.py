from django import forms


class OrderSearch(forms.Form):
    search = forms.CharField(
        min_length=20,
        max_length=50,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "placeholder": "Шукати замовлення",
        })
    )