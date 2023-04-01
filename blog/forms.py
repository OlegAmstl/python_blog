from django import forms


class PostSearchForm(forms.Form):
    """
    Строка поиска постов.
    """
    q = forms.CharField()

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].widget.attrs.update({'class': 'form-control'})