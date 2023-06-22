from django import forms
from datetime import date

ACTIVITY_CHOICES = (
    ("Magic The Gathering", "Magic The Gathering"),
    ("Pokemon", "Pokemon"),
    ("Yu-Gi-Oh", "Yu-Gi-Oh"),
    ("DnD", "DnD"),
)

LOCATION_CHOICES = (
    ("Any", "Any"),
    ("Portland, OR", "Portland, OR"),
    ("Seattle, WA", "Seattle, WA")
)

PRICE_CHOICES = (
    ("Any", "Any"),
    ("0", "Free"),
    ("5", "$5"),
    ("10", "$10"),
    ("20", "$20"),
    ("50", "$50"),
)

CATEGORY_CHOICES = (
    ("Local", "Local"),
    ("Regional", "Regional"),
    ("Major", "Major"),
    ("Convention", "Convention"),
)

class DateInput(forms.DateInput):
    input_type = 'date'

class EventSearchForm(forms.Form):
    activity = forms.MultipleChoiceField(label='Activity', choices=ACTIVITY_CHOICES, widget=forms.CheckboxSelectMultiple)
    location = forms.ChoiceField(label='Location', choices=LOCATION_CHOICES, required=False)
    start_date = forms.DateField(label='After Date', widget=DateInput(), required=False)
    end_date = forms.DateField(label='Before Date', widget=DateInput(), required=False)
    price = forms.ChoiceField(label='Price', choices=PRICE_CHOICES)
    category = forms.MultipleChoiceField(label='Category', choices=CATEGORY_CHOICES, widget=forms.CheckboxSelectMultiple)
