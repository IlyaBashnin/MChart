from django import forms


class YMusiChartForm(forms.Form):
    author_name = forms.CharField(max_length=50, label='Author', required=True)
    field_order = [author_name]
