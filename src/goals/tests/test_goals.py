from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import User
from goals.models import Board, BoardParticipant, Goal, GoalCategory


class GoalsListTestCase(APITestCase):

    def test_auth_required(self):
        response = self.client.get(reverse('list-goals'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_success(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        response = self.client.get(reverse('list-goals'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        goals_list = response.json()
        self.assertTrue(isinstance(goals_list, list))


class GoalCreateTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('create-goal')

    def test_auth_required(self):
        response = self.client.post(self.url, {
            'title': 'goal title',
            'description': 'anything description',
            'due_date': datetime.now(),
            'priority': Goal.Priority.medium,
            'status': Goal.Status.in_progress,
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
            title='cat_title',
            board=board
        )
        self.assertTrue(GoalCategory.objects.exists())

        self.assertFalse(Goal.objects.exists())
        goal = Goal.objects.create(
            user_id=user.id,
            category=category,
            title='goal X',
            description='anything description',
            status=Goal.Status.to_do,
            priority=Goal.Priority.medium,
            due_date=datetime.now(),
        )
        self.assertTrue(Goal.objects.exists())

        response = self.client.get(reverse('retrieve-update-destroy-goal', kwargs={'pk': goal.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GoalRetrievedTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test_user', password='test_password')

        self.board = Board.objects.create(title='board_title')
        BoardParticipant.objects.create(board=self.board, user=self.user, role=BoardParticipant.Role.owner)
        self.category = GoalCategory.objects.create(user_id=self.user.id, title='cat_title', board=self.board)
        self.goal = Goal.objects.create(
            user_id=self.user.id,
            category=self.category,
            title='goal X',
            description='anything description',
            status=Goal.Status.to_do,
            priority=Goal.Priority.medium,
            due_date=datetime.now(),
        )

    def test_auth_required(self):
        response = self.client.get(reverse('retrieve-update-destroy-goal', kwargs={'pk': self.goal.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('retrieve-update-destroy-goal', kwargs={'pk': self.goal.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
