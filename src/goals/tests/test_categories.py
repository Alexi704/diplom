from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import User
from goals.models import Board, BoardParticipant, GoalCategory


class CategoryListTestCase(APITestCase):

    def test_auth_required(self):
        response = self.client.get(reverse('list-categories'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_success(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        response = self.client.get(reverse('list-categories'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        categories_list = response.json()
        self.assertTrue(isinstance(categories_list, list))


class CategoryCreateTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('create-category')

    def test_auth_required(self):
        response = self.client.post(self.url, {
            'title': 'category title',
            'board': Board.objects.create(title='board_title'),
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_success(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        self.assertFalse(BoardParticipant.objects.exists())
        board = Board.objects.create(title='board_title')
        BoardParticipant.objects.create(board=board, user=user, role=BoardParticipant.Role.owner)
        self.assertTrue(BoardParticipant.objects.exists())

        self.assertFalse(GoalCategory.objects.exists())
        category = GoalCategory.objects.create(
            user_id=user.id,
            title='category title X',
            board=board,
        )
        self.assertTrue(GoalCategory.objects.exists())

        response = self.client.get(reverse('list-categories'), kwargs={'id': category.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_goal_user_role(self):
        # создаем пользователей
        user_1 = User.objects.create_user(username='user_1', password='test_password')
        user_2 = User.objects.create_user(username='user_2', password='test_password')
        user_3 = User.objects.create_user(username='user_3', password='test_password')

        # создаем доску от имени 1-го пользователя
        board = Board.objects.create(title='board_title')
        BoardParticipant.objects.create(board=board, user=user_1, role=BoardParticipant.Role.owner)

        # добавляем на доску пользователей
        BoardParticipant.objects.create(board=board, user=user_2, role=BoardParticipant.Role.writer)
        BoardParticipant.objects.create(board=board, user=user_3, role=BoardParticipant.Role.reader)

        # логинимся под 1-м пользователем и создаем на доске категорию
        self.client.force_login(user_1)
        response = self.client.post(self.url, {'title': 'cat_title_user_1', 'is_deleted': False, 'board': board.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # логинимся под 2-м пользователем и создаем на доске категорию
        self.client.force_login(user_2)
        response = self.client.post(self.url, {'title': 'cat_title_user_2', 'is_deleted': False, 'board': board.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # логинимся под 3-м пользователем и пробуем создать на доске категорию
        self.client.force_login(user_3)
        response = self.client.post(self.url, {'title': 'cat_title_user_3', 'is_deleted': False, 'board': board.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
