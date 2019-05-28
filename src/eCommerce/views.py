# aafai  aafai banako file tara convention chai views.py nai ho. 
# this file takes Web request and returns a Web response
# This response can be the HTML contents of a Web page, or a redirect, or a 404 error
# or an XML document, or an image . . . or anything, really. 

#from django.http import HttpResponse  
#we imported the class HttpResponse from the django.http module.


from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect  # render is used to render html files.
from .forms import ContactForm, LoginForm, RegisterForm

def HomePage(request):
	content = {
	"title":"Home page",
	"name":"Rupesh"
	}
	content['check'] = "yess"

	return render(request, "homepage.html", content)

def AboutPage(request):
	return render(request, "homepage.html", {})

def ContactPage(request):
	#newform = ContactForm()  creating new object of ContactFrom
	newform = ContactForm(request.POST or None) #passing data from post
	content = {
									# "title":"Homepage",
									# "name":"Rupesh",
	"form":newform
	}
	# if newform.is_valid():
	# 	print(newform.cleaned_data)
	return render(request, "contactpage.html", content)



def LoginPage(request):
	form = LoginForm(request.POST or None)
	if form.is_valid(): 
		# print(form.cleaned_data) #form takes cleaned_data attribute only after is_valid

		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate( request, username=username, password=password)

		# print(user)

		if user is not None:
			login(request, user)
			return redirect("/homepage")
		else:
			return render(request, "auth/errorpage.html",content)
	   
	# print(request.user.is_authenticated())   shows if user is logged in
	content= {
	"FormToBeCalledInView":form
	}
	return render(request, "auth/login.html", content)

def RegisterPage(request):
	form = RegisterForm(request.POST or None)
	content = {
	"form" : form
	}
	return render(request, "auth/register.html", content)

def CreateUser(request):
	form = RegisterForm(request.POST or None)





