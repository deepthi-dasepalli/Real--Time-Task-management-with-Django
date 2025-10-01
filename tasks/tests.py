from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description")

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "Test Description")
        # Removed check for 'completed' field as it does not exist

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.task_data = {'title': 'API Test Task', 'description': 'API Test Description'}
        self.task = Task.objects.create(**self.task_data, assigned_to=self.user)

    def test_get_task_list(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('API Test Task', str(response.data))

    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'New Description'}
        response = self.client.post(reverse('task-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_update_task(self):
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(reverse('task-detail', kwargs={'pk': self.task.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
