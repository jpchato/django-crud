from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Game


class GameTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='jpchato',
            email='jpchato@gmail.com',
            password='pass'
        )

        self.game = Game.objects.create(
            title='tekken',
            description='steve b1',
            player=self.user,
        )

    def test_string_representation(self):
        game = Game(title='tekken')
        self.assertEqual(str(game), game.title)

    def test_game_content(self):
        self.assertEqual(f'{self.game.title}', 'tekken')
        self.assertEqual(f'{self.game.player}', 'jpchato')
        self.assertEqual(f'{self.game.description}', 'steve b1')

    def test_game_list_view(self):
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tekken')
        self.assertTemplateUsed(response, 'game_list.html')

    def test_game_detail_view(self):
        response = self.client.get('/game/1/')
        no_response = self.client.get('/game/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'steve b1')
        self.assertTemplateUsed(response, 'game_detail.html')


    def test_game_create_view(self):
        response = self.client.post(reverse('game_create'), {
            'title': 'sf5',
            'description': 'sagat',
            'player': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'sf5')
        self.assertContains(response, 'sagat')
        self.assertTemplateUsed(response, 'game_create.html')


    def test_game_update_view(self):
        response = self.client.post(reverse('game_update',args='1'), {
            'title': 'changed title',
            'description': 'changed description',
        })
        self.assertEqual(response.status_code, 302)

    def test_game_delete_view(self):
        response = self.client.get(reverse('game_delete',args='1'))
        self.assertEqual(response.status_code, 200)