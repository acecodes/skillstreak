from django import forms
from members.models import Member

class LoginForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ('email', 'password',)
		widgets = {'password':forms.PasswordInput}

