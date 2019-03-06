from django.forms.widgets import DateInput, Select
from django.core.validators import MinValueValidator
from django import forms
from django_registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.db import models
from .models import User, Product_Unit, Product, Location, Room, Reserve
from django.forms.widgets import DateInput, TextInput, Select
from captcha.fields import ReCaptchaField


class SignUpForm(RegistrationForm):
    captcha = ReCaptchaField()
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AdvancedSearch(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-12 searchfield'}), label=False)
    CHOICES=[
             ('unit', 'Unit'),
             ('location','Location'),
             ('item_type','Item type'),
             ('finished', 'Finished')
             ]
    advanced_search = forms.ChoiceField(choices=CHOICES, label=False)
    advanced_search.widget.attrs.update({'class': 'col-md-6'})
    advanced_search.widget.attrs.update({'name': 'advanced_search'})
    advanced_search.widget.attrs.update({'id': 'advanced_search'})
    #search.widget.attrs.update({'action': '/search/'})
    search.widget.attrs.update({'name': 'description'})
    search.widget.attrs.update({'type': 'search'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        #self.helper.form_method = "post='/search/'"

        self.helper.layout = Layout(
            "search",
            "advanced_search",
            Submit("submit", "Search", css_class="btn")
        )

class Product_UnitForm(forms.ModelForm):
    number = forms.IntegerField(label='How many items with exactly those properies do you want to add to the database?',
    initial=1, validators=[MinValueValidator(1)])



    class Meta:
        UNIT_CHOICES = (
        ('kg', 'kg'),
        ('l', 'l'),
        ('g', 'g'),
        ('ml', 'ml'),
        ('mg', 'mg'),
        ('µl', 'µl'),
        ('µg', 'µg')
        )
        model = Product_Unit
        exclude = ['reservation', 'is_inactive', 'curr_amount']
        widgets = {
            "del_date":DateInput(attrs = {"type":"date"}),
            "open_date":DateInput(attrs = {"type":"date"}),
            "exp_date":DateInput(attrs = {"type":"date"}),
            "ret_date":DateInput(attrs = {"type":"date"}),
            "m_unit":Select(choices=UNIT_CHOICES),
        }
        #m_unit = forms.MultipleChoiceField

class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class Location_Form(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

class Room_Form(forms.ModelForm):
    class Meta:
        model = Room
        fields="__all__"

class Reserve_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Reserve_Form, self).__init__(*args, **kwargs)
    class Meta:
        model=Reserve
        #exclude = ['is_complete',]

        widgets = {
            "date_res":DateInput(attrs = {"type":"date"}),
            #'user': TextInput(),
        }
        exclude = ['user',]
        #fields="__all__"

class Update_item_Form(forms.ModelForm):

    used_amount = forms.IntegerField(label='Used amount', required=False)
    prod_units = forms.ModelChoiceField(queryset=Product_Unit.objects.all(), label="Select a unit")


    class Meta:
        model = Product_Unit
        fields = ("prod_units","used_amount", "open_date","ret_date", "exp_date", "location",)

        widgets = {
            "open_date":DateInput(attrs = {"type":"date"}),
            "ret_date":DateInput(attrs = {"type":"date"}),
            "exp_date":DateInput(attrs = {"type":"date"}),
        }
    def __init__(self, *args, **kwargs):
        super(Update_item_Form, self).__init__(*args, **kwargs)
        self.fields['location'].required = False
