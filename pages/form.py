from django import forms
from pages.models import customers

class AddForm(forms.ModelForm):

    class Meta:
        model = customers
        fields = "__all__"
        # incase you dont want to inherit the whole field then you use the sytax below to identify what the field(column), you want to inherit.
        # fields = ('first_name', 'Last_name','email', 'phone')
