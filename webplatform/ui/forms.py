from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, SetPasswordForm,
                                       PasswordChangeForm, PasswordResetForm)
from product_minisite.models import MiniSite

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.novalidate = True
        self.helper.form_action = 'login'

        self.helper.add_input(Submit('submit', 'Submit'))


class AccountForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salva'))



class MiniSiteForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = MiniSite
        fields = ['organization', 'name', 'site_template']

    def __init__(self, *args, **kwargs):
        super(MiniSiteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salva'))
        self.helper.novalidate = True
        self.helper.form_action = 'minisite-create'

    def clean(self):
        cleaned_data = super(MiniSiteForm, self).clean()
        return cleaned_data

class MiniSiteUpdateForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = MiniSite
        fields = ['organization', 'site_template']

    def __init__(self, *args, **kwargs):
        super(MiniSiteUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salva'))
        self.helper.novalidate = True
        self.helper.form_action = ' '

    def clean(self):
        cleaned_data = super(MiniSiteUpdateForm, self).clean()
        return cleaned_data
