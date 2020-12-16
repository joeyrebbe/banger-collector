from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Banger, Playlist
from .forms import ListeningForm


# Create your views here.

class BangerCreate(CreateView):
    model = Banger
    fields = ['name', 'genre', 'artist', 'hypeness']
    success_url = '/bangers/'

class BangerUpdate(UpdateView):
    model = Banger
    fields = ['genre', 'artist', 'hypeness']

class BangerDelete(DeleteView):
    model = Banger
    success_url = '/bangers/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bangers_index(request):
    bangers = Banger.objects.all()
    return render(request, 'bangers/index.html', { 'bangers': bangers })

def bangers_detail(request, banger_id):
    banger = Banger.objects.get(id=banger_id)
    playlists_banger_isnt_in = Playlist.objects.exclude(id__in = banger.playlists.all().values_list('id'))
    listening_form = ListeningForm()
    return render(request, 'bangers/detail.html', { 
        'banger': banger, 'listening_form': listening_form, 
        'playlists': playlists_banger_isnt_in
    })

def add_listen(request, banger_id):
    form = ListeningForm(request.POST)
    if form.is_valid():
        new_listen = form.save(commit=False)
        new_listen.banger_id = banger_id
        new_listen.save()
    return redirect('detail', banger_id=banger_id)

def assoc_playlist(request, banger_id, playlist_id):
    Banger.objects.get(id=banger_id).playlists.add(banger_id)
    return redirect('detail', banger_id=banger_id)

class PlaylistList(ListView):
    model = Playlist

class PlaylistDetail(DetailView):
    model = Playlist

class PlaylistCreate(CreateView):
  model = Playlist
  fields = ['name', 'vibe']

class PlaylistUpdate(UpdateView):
  model = Playlist
  fields = ['name', 'vibe']

class PlaylistDelete(DeleteView):
  model = Playlist
  success_url = '/playlists/'







