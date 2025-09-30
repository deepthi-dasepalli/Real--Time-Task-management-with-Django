# Real-Time Task Management Dashboard with Django

This project is a real-time task management dashboard built using Django, Django Channels, Django REST Framework, and Bootstrap 5. It features a Kanban-style board with drag-and-drop functionality and real-time updates via WebSockets.

## Features

- User authentication (login, logout)
- Task CRUD operations via REST API
- Real-time task updates using Django Channels and WebSockets
- Responsive Kanban dashboard with drag-and-drop support
- Role-based task filtering

## Technologies Used

- Django 5.x
- Django REST Framework
- Django Channels 4.x
- Bootstrap 5
- SortableJS for drag-and-drop
- SQLite (default) database

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```
7. Access the app at `http://127.0.0.1:8000/`

## Testing

Manual testing is recommended for:

- User authentication flows
- Task CRUD API endpoints
- Real-time WebSocket updates
- Frontend Kanban board functionality

## Deployment

For production deployment, configure ASGI server (e.g., Daphne), Redis as the channel layer backend, and secure settings accordingly.

## License

MIT License
