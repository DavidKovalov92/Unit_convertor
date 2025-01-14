from django import forms

class convertFormLength(forms.Form):
    params = [
        ('millimeter', 'millimeter'),
        ('centimeter', 'centimeter'),
        ('meter', 'meter'),
        ('kilometer', 'kilometer'),
        ('inch', 'inch'),
        ('foot', 'foot'),
        ('yard', 'yard'),
        ('mile', 'mile'),
    ]
    number = forms.IntegerField()
    first_unit = forms.ChoiceField(choices=params)
    second_unit = forms.ChoiceField(choices=params)

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if number < 0:
            raise forms.ValidationError("Number must be a non-negative value.")
        return number

class convertFormWeight(forms.Form):
    params = [
        ('miligram', 'miligram'),
        ('grams', 'grams'),
        ('kilogram', 'kilogram'),
        ('ounces', 'ounces'),
        ('pound', 'pound'),
    ]
    number = forms.IntegerField()
    first_unit = forms.ChoiceField(choices=params)
    second_unit = forms.ChoiceField(choices=params)

class convertFormTemperature(forms.Form):
    params = [
        ('celsius', 'celsius'),
        ('fahrenheit', 'fahrenheit'),
        ('kelvin', 'kelvin'),
    ]
    number = forms.IntegerField()
    first_unit = forms.ChoiceField(choices=params)
    second_unit = forms.ChoiceField(choices=params)