from django.shortcuts import render, redirect
from .models import Songs
from .forms import SongForm
from django.contrib import messages

# Create your views here.

def home(request):
	songs = Songs.objects.all()
	context = {'songs':songs}
	return render(request, 'songs/home.html', context)

def agregar(request):
	if request.method == "POST":
		form = SongForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, '¡Song added!')
			return redirect('home')
	else:
		form = SongForm()
	context= {'form': form}
	return render(request, 'songs/agregar.html', context)

def eliminar(request, song_id):
	songs = Songs.objects.get(id=song_id)
	songs.delete()
	messages.success(request, '¡Song Deleted!')
	return redirect("home")

def editar(request, song_id):
	songs = Songs.objects.get(id=song_id)
	if request.method == "POST":
		form = SongForm(request.POST,instance=songs)
		if form.is_valid():
			form.save()
			messages.success(request, '¡Song updated!')
			return redirect("home")
	else:
		form= SongForm(instance=songs)
	context={"form": form}
	return render(request, "songs/editar.html", context) 