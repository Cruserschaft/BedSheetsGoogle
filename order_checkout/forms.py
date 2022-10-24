from django import forms


class SearchOrder(forms.Form):
    search = forms.CharField(
        min_length=20,
        max_length=50,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "id": "search",
            "name": "search",
            "placeholder": "Замовлення",
        })
    )