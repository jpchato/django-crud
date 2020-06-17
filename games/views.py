from django.shortcuts import render
# add this
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game
from django.urls import reverse_lazy

# Create your views here.
# list view, detail view, create view, update view, delete view

class GameListView(ListView):
    # don't forget the .html
    template_name = 'game_list.html'
    model = Game

class GameDetailView(DetailView):
    # don't forget the .html
    template_name = 'game_detail.html'
    model = Game

class GameCreateView(CreateView):
    template_name = 'game_create.html'
    model = Game
    fields = ['title', 'player', 'description']

class GameUpdateView(UpdateView):
    template_name = 'game_update.html'
    model = Game
    # fields don't have to match from create view, just the ones you want to allow to be updated
    fields = ['title', 'description']

class GameDeleteView(DeleteView):
    template_name = 'game_delete.html'
    model = Game
    success_url = reverse_lazy('game_list')