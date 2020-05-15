from django import forms

class CityNameForm(forms.Form):
    postale_code = forms.CharField(max_length=200,label = "Code Postale")

class ChangeDurationForm(forms.Form):
    duration_type = forms.ChoiceField(choices = [
                (365,'Year'),
                (30,'Month'),
                (7,'Week'),
                (1,'Day'),
                ], label = "",initial = 1)
    quantity = forms.IntegerField(label="",initial = 1)

