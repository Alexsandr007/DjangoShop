from django import forms



class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)