from django import forms
from users.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = []