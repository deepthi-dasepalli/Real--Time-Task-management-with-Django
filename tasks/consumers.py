import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Task
from .serializers import TaskSerializer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'tasks'

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'update_task':
            task_data = data.get('task')
            task_id = task_data.get('id')
            updated_task = await self.update_task(task_id, task_data)
            if updated_task:
                # Broadcast the update to all connected clients
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type': 'task_update',
                        'task': updated_task
                    }
                )

    @database_sync_to_async
    def update_task(self, task_id, task_data):
        try:
            task = Task.objects.get(id=task_id)
            for field, value in task_data.items():
                if field != 'id':
                    setattr(task, field, value)
            task.save()
            # Serialize the updated task
            serializer = TaskSerializer(task)
            return serializer.data
        except Task.DoesNotExist:
            return None

    # Send message to group
    async def task_update(self, event):
        task = event['task']
        await self.send(text_data=json.dumps({
            'action': 'task_update',
            'task': task
        }))
