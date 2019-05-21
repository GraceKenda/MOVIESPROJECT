from django.shortcuts import render,get_object_or_404,redirect
from .models import Movie, Category
from . forms import MovieForm, UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movapp/index.html', {'movies': movies})


def detail(request, movie_id):
    movies = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movapp/index.html', {'movies': movies})


@login_required(login_url='movapp:login_user')
def create_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        movie = form.save(commit=False)
        movie.cover = request.FILES['cover']
        movie.user = request.user
        movie.save()
        movie = Movie.objects.all()
        context = {'movie':movie,
                   'message':'Movie Created!'
                   }
        return render(request, 'movapp/index.html',context)
    form = MovieForm()

    return render(request, 'movapp/create_movie.html',
                  {'form': form})

def delete_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    movie = Movie.objects.all()
    return render(request, 'movapp/index.html', {'movie':movie})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                movies = Movie.objects.filter(user=request.user)
                return render(request, 'movapp:index.html', {'movies': movies})
    return render(request, 'movapp/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        context = {'form':form,
                   'message':'Registered successfully!'
                   }
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                movies = Movie.objects.filter(user=request.user)
                return render(request, 'movapp/index.html', {'movies':movies})
    return render(request, 'movapp/register.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('movapp:login_user')

