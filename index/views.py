from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json
from .forms import registerForm,loginForm
from .models import foodItem

# Create your views here.
def loginPage(request):
	form = loginForm()
	if(request.user.is_authenticated()):
		return redirect(dash)
	else:
		context = {'form':form}
		return render(request, "login.html",context)

def dash(request):
	if(not request.user.is_authenticated()):
		return redirect(loginPage)
	else:
		foodList = foodItem.objects.all()
		paginator = Paginator(foodList, 8)

		page = request.GET.get("page")

		try:
			foodItems = paginator.page(page)
		except PageNotAnInteger:
			foodItems = paginator.page(1)
		except EmptyPage:
			foodItems = paginator.page(paginator.num_pages)

		context = {"username":request.user.username,"foodItems":foodItems}
		return render(request,"dashboard.html",context)

def register(request):
	if(request.user.is_authenticated()):
		return redirect(dash)
	else:
		form = registerForm()
		context = {'form':form}
		return render(request, "register.html", context)

def registerUser(request):
	form = registerForm(request.POST)
	username = request.POST.get("username")
	email = request.POST.get("email")
	password = request.POST.get("password")
	if form.is_valid():
		user = User.objects.create_user(username=username,email=email,password=password)
		user.save()
		return HttpResponse('{"status":"ok"}',content_type="application/json")
	else:
		return HttpResponse(json.dumps(form.errors),content_type="application/json")

def authUser(request):
	form = loginForm(request.POST)
	username = request.POST.get("username")
	password = request.POST.get("password")

	if form.is_valid():
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponse('{"status":"ok"}',content_type="application/json")
		else:
			return HttpResponse('{"status":"invalid"}',content_type="application/json")
	else:
		return HttpResponse(json.dumps(form.errors),content_type="application/json")

def logoutUser(request):
	logout(request)
	return redirect(loginPage)

def test(request):
	form = registerForm()
	context = {'form':form}
	return render(request, "test.html",context)