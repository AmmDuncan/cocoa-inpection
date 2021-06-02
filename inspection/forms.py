from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Fieldset, HTML

from .models import Report

class ReportForm(forms.ModelForm):
    insurance_starting_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    insurance_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    road_worthiness_starting_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    road_worthiness_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    driving_license_starting_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    driving_license_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = Report
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tags = False
        self.helper.layout = Layout (
            Fieldset(
                'Car Details',
                Row(
                    Column('name', css_class='col-md-12 mt-2')
                ),
                Row(
                    Column('loan_for', css_class='col-md-6 mt-2'),
                    Column('item_inspected', css_class='col-md-6 mt-2'),
                    css_class='row mt-3'
                ),
                Row(
                    Column('make', css_class='col-md-6 mt-2'),
                    Column('registration', css_class='col-md-6 mt-2'),
                    Column('chasis_number', css_class='col-md-6 mt-2'),
                    Column('cubic_capacity', css_class='col-md-6 mt-2'),

                    css_class='row mt-3'
                )
            ),
            Fieldset(
                'Insurance',
                Row(
                Column('insurance_policy_number', css_class='col-md-12 mt-2'),
                Column('insurance_starting_date', css_class='col-md-6 mt-2'),
                Column('insurance_expiry_date', css_class='col-md-6 mt-2'),
                css_class='row'
                ),
                
                css_class='mt-5',

            ),
            Fieldset(
                'Road Worthiness Certificate',
                Row(
                Column('road_worthiness_starting_date', css_class='col-md-6 mt-2'),
                Column('road_worthiness_expiry_date', css_class='col-md-6 mt-2'),
                css_class='row'
                ),
                
                css_class='mt-5',

            ),
            Fieldset(
                'License Details',
                Row(
                Column('driving_license_number', css_class='col-md-6 mt-2'),
                Column('driving_license_starting_date', css_class='col-md-6 mt-2'),
                Column('driving_license_expiry_date', css_class='col-md-6 mt-2'),
                css_class='row'
                ),
                
                css_class='mt-5',

            ),
            Fieldset(
                'Deed of Assignment',
                Row(
                Column('deed_status', css_class='col-md-4 mt-2'),
                
                ),
                css_class='mt-5',
            ),
            Fieldset(
                'Allowance Status',
                Row(
                Column('currently_receiving', css_class='col-md-4 mt-2'),
                
                ),
                css_class='mt-5',
            ),
            Fieldset(
                'Manager',
                Row(
                    Column('manager', css_class='col-md-4 mt-2'),
                ),  
                css_class='mt-5',
            ),           
            # Row(
            #     Submit('submit', 'Save', css_class='mt-3 mt-2'),
            #     css_class="create-report"
            # ) 
        )
    