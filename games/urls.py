from django.urls import path
from .views import GameDetailView, GameListView, GameCreateView, GameUpdateView, GameDeleteView

urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('game/new/', GameCreateView.as_view(), name='game_create'),
    path('game/<int:pk>/edit', GameUpdateView.as_view(), name='game_update'),
    path('game/<int:pk>/delete', GameDeleteView.as_view(), name='game_delete'),
]