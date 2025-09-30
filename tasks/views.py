from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all().order_by('-created_at')
        return Task.objects.filter(assigned_to=user).order_by('-created_at')
