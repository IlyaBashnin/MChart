from django import forms


class YMusiChartForm(forms.Form):
    author_name = forms.CharField(max_length=50, label='Author', help_text='Input looking author name', required=False)
    field_order = [author_name]
