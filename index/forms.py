from django import forms

class registerForm(forms.Form):
	username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Username','class':'text'}))
	email = forms.EmailField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Email','class':'text'}))
	password = forms.CharField(max_length=30,
		widget = forms.PasswordInput(attrs={'placeholder':'Password','class':'text'}))


class loginForm(forms.Form):
	username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Username','class':'text'}))
	password = forms.CharField(max_length=30,
		widget = forms.PasswordInput(attrs={'placeholder':'Password','class':'text'}))
