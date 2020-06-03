from django.contrib.auth.models import  User
from django import forms


class  UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	conpassword = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email' , 'password']

	def clean(self):
		cleaned_data = super(UserForm,self).clean()
		password = cleaned_data.get("password")
		conpassword = cleaned_data.get("conpassword")
		msg = "did not match"
		if password != confirm_password:
			self.add_error('conpassword', msg)
            