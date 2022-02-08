from django import forms


class WordForm(forms.Form):
    text=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        text=cleaned_data.get("text")
        # hello hai 123
        lst=[word.isnumeric() for word in text.split(" ")]
        if True in lst:
            msg="invalid"
            self.add_error("text",msg)