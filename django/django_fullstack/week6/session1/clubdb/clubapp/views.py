from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User,Club

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        return redirect('/clubs')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/clubs')

def logout(request):
    # clear session
    request.session.clear()
    return redirect('/')

def new(request):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return render(request,"addclub.html",context)

def create(request):
    if request.method == "POST":
        errors = Club.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print(errors)
            return redirect("/clubs/new")
        Club.objects.create(
            name =request.POST['name'],
            desc=request.POST['desc'],
            date_start = request.POST['date_start'],
		    date_end = request.POST['date_end'],
            owner=User.objects.get(id=request.session['user_id'])
        )
    return redirect("/clubs")

def clubs(request):
    if 'user_id' not in request.session:
        return redirect("/")
    user = User.objects.get(id = request.session['user_id'])
    print(user)
    context = {
        # "clubs": Club.objects.all(),
		"user": user,
		"user_clubs":Club.objects.filter(owner = user),
        "member_clubs" : Club.objects.filter(joined=user),
		"other_clubs": Club.objects.all().exclude(owner=user).exclude(joined=user),
	}
    return render(request,"clubs.html",context)

def join(request,c_id):
    # Get user id from session
    user = User.objects.get(id = request.session['user_id'])
    # Get club from c_id
    club=Club.objects.get(id=c_id)
    # Add club to user
    user.joined_clubs.add(club)
    return redirect("/clubs")

def cancel(request,c_id):
    # Get user id from session
    user = User.objects.get(id = request.session['user_id'])

    # Get club from c_id
    club=Club.objects.get(id=c_id)

    # Remove club from user
    user.joined_clubs.remove(club)

    return redirect("/clubs")

def delete(request,id):
    club=Club.objects.get(id=id)
    club.delete()
    return redirect("/clubs")
    
def edit(request,id):
    context={
        'club':Club.objects.get(id=id)
    }
    return render(request,"edit.html",context)

def update(request,id):
    if request.method == "POST":
        errors = Club.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/clubs/edit/{id}")
        else:
            club=Club.objects.get(id=id)
            club.name=request.POST['name']
            club.desc=request.POST['desc']
            club.save()
    return redirect('/clubs')
    
def show(request, id):
    context={
        'club':Club.objects.get(id=id)
    }
    return render(request,"display.html",context)

    
    

