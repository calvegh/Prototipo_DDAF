from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	return render(request, 'usuarios/index-login.html')

def loginView(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	request.session['user']=username
	print(request.session['user'])
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request,user)
	
	return render(request, 'usuarios/index-login.html')

def logoutView(request):
	logout(request)
	return redirect('/')