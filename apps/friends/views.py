from django.shortcuts import render, HttpResponse, redirect
from .models import User, Interest

def index(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, 'friends/index.html', context)

def newUser(request):
	# interet
	name = request.POST['interest'].lower()
	interest_list = Interest.objects.filter(name = name)
	if not interest_list:
		interest = Interest.objects.create(name = name)
	else:
		interest = interest_list[0]

	# user
	first_name = request.POST['first_name'].lower()
	last_name = request.POST['last_name'].lower()
	user_list = User.objects.filter(first_name = first_name, last_name = last_name)
	if not user_list:
		user = User.objects.create(first_name = first_name, last_name = last_name)
	else:
		user = user_list[0]

	# add the interest to the user
	user.interests.add(interest)
	return redirect('/')

def viewUser(request, id):
	user_list = User.objects.filter(id=id)
	if user_list:
		user = user_list[0]
		interests = user.interests.all()
		context = {'user': user, 'interests': interests}
		return render(request, 'friends/view.html', context)
	return redirect('/')
