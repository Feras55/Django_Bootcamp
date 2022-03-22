from django import forms
from django.core import validators


# Custom clean method
def check_for_z(value):
    if value[0].lower() != 'z':
        return forms.ValidationError("Z REQUIRED FIRST LETTER")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter email again")
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email!=vemail:
            raise forms.ValidationError("Emails not matching")

    # Native validator
    # def clean_botCatcher(self):
    #     botcatcher = self.cleaned_data['botCatcher']
    #     if len(botcatcher):
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher
