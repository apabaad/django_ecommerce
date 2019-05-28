# aafai banako file

from django import forms

class ContactForm(forms.Form):   #parent class of forms is forms.Form
	
	fullname= forms.CharField(
		label = 'Your Name', 
		max_length=100
		# widget=forms.TextInput(
		# 	attrs={
		# 		"class":"form-control", 
		# 		"placeholder":"Fullname"
		# })
		) 
	
	
	email= forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				"class":"form-control", 
				"placeholder":"E-mail"
		}))


	content= forms.CharField(
		widget=forms.Textarea(
			attrs={
			"class":"form-control",
			"placeholder":"Write your content..."
			}))

	
	#additional validation: if email is gmail.com or not

	def clean_email(self):
		EmailVar = self.cleaned_data.get("email")
		if not "gmail.com" in EmailVar:
			raise forms.ValidationError("Email has to be gmail.com")
		return EmailVar


class LoginForm(forms.Form):
	
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control",
			"placeholder":"username"
			}))

	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control",
			"placeholder":"password"
			}))


class RegisterForm(forms.Form):
	
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control",
			"placeholder":"username"
			}))

	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				"class":"form-control", 
				"placeholder":"E-mail"
		}))

	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control",
			"placeholder":"password"
			}))

	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control",
			"placeholder":"conform password"
			}))

	def clean(self):
		# data = self.cleaned_data
		password = self.cleaned_data.get('password') 
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError("Passwords don't match")
		# return data
