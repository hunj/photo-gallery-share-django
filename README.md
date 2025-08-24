# Photo Gallery Share - Django Application

A modern, feature-rich photo gallery application built with Django and django-allauth for user authentication.

## Features

### Core Functionality
- **User Authentication**: Complete user registration, login, and management using django-allauth
- **Album Management**: Create, edit, delete, and organize photo albums
- **Photo Management**: Upload, edit, delete, and organize photos
- **Privacy Control**: Public/private albums and photos
- **User Dashboard**: Personal dashboard showing user's albums and photos
- **Responsive Design**: Modern Bootstrap-based UI that works on all devices

### User Roles & Permissions
- **Regular Users**: Can create, edit, and delete their own albums and photos
- **Superusers/Admins**: Can manage all albums and photos in the system
- **Guest Users**: Can view public albums and photos

### Technical Features
- **Django 5.2+**: Built with the latest Django version
- **PostgreSQL Database**: Robust database backend
- **Image Processing**: Automatic image handling with Pillow
- **Docker Support**: Containerized deployment with Docker Compose
- **HTMX Integration**: Modern web interactions
- **Responsive Templates**: Bootstrap 5 UI framework

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd photo-gallery-share-django
   ```

2. **Build and start the containers**
   ```bash
   docker compose build
   docker compose up -d
   ```

3. **Create database migrations and apply them**
   ```bash
   docker compose exec app python manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   docker compose exec app python manage.py createsuperuser
   ```

5. **Access the application**
   - Main application: http://localhost:18001
   - Admin interface: http://localhost:18001/admin
   - Nginx proxy: http://localhost:18000

## Usage

### For Users

1. **Registration & Login**
   - Visit the signup page to create an account
   - Use your email for authentication
   - Verify your email address

2. **Creating Albums**
   - Click "Create Album" from the dashboard or albums page
   - Add a title, description, and set privacy settings
   - Albums can be public or private

3. **Uploading Photos**
   - Click "Upload Photo" from any page
   - Add title, description, and optionally assign to an album
   - Set privacy settings for individual photos

4. **Managing Content**
   - Edit or delete your albums and photos
   - Organize photos into albums
   - Control visibility with public/private settings

### For Administrators

1. **Admin Interface**
   - Access `/admin` with superuser credentials
   - Manage all users, albums, and photos
   - Monitor system usage and user activity

2. **User Management**
   - View and manage user accounts
   - Monitor user activity and content

## Project Structure

```
photo-gallery-share-django/
├── app/                          # Django application code
│   ├── core/                     # Main Django project
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py              # Main URL configuration
│   │   └── wsgi.py              # WSGI configuration
│   ├── gallery/                  # Photo gallery app
│   │   ├── models.py            # Album and Photo models
│   │   ├── views.py             # View logic
│   │   ├── forms.py             # Form definitions
│   │   ├── admin.py             # Admin interface
│   │   └── urls.py              # App URL patterns
│   ├── templates/                # HTML templates
│   │   ├── base.html            # Base template
│   │   └── gallery/             # Gallery-specific templates
│   └── manage.py                 # Django management script
├── nginx/                        # Nginx configuration
├── docker-compose.yml            # Docker services configuration
├── Dockerfile                    # App container definition
├── pyproject.toml               # Python dependencies
└── README.md                    # This file
```

## API Endpoints

### Authentication
- `/accounts/login/` - User login
- `/accounts/signup/` - User registration
- `/accounts/logout/` - User logout

### Albums
- `/` - List all albums (home page)
- `/album/new/` - Create new album
- `/album/<id>/` - View album details
- `/album/<id>/edit/` - Edit album
- `/album/<id>/delete/` - Delete album

### Photos
- `/photos/` - List all photos
- `/photo/new/` - Upload new photo
- `/photo/<id>/` - View photo details
- `/photo/<id>/edit/` - Edit photo
- `/photo/<id>/delete/` - Delete photo

### User Dashboard
- `/dashboard/` - User's personal dashboard

## Configuration

### Environment Variables
The application uses the following environment variables (with defaults):

```bash
# Django Settings
SECRET_KEY=deez_nuts
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Database
POSTGRES_DB=photo_gallery
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### Django Allauth Settings
- Email verification: Required
- Username: Not required (email-based authentication)
- Login method: Email
- Social accounts: Supported but not configured by default

## Development

### Running Tests
```bash
docker compose exec app python manage.py test
```

### Creating Migrations
```bash
docker compose exec app python manage.py makemigrations
```

### Applying Migrations
```bash
docker compose exec app python manage.py migrate
```

### Django Shell
```bash
docker compose exec app python manage.py shell
```

### Static Files
```bash
docker compose exec app python manage.py collectstatic
```

## Deployment

### Production Considerations
1. **Security**: Update SECRET_KEY and disable DEBUG
2. **Database**: Use production PostgreSQL instance
3. **Media Storage**: Configure cloud storage for media files
4. **HTTPS**: Enable SSL/TLS with proper certificates
5. **Environment**: Set appropriate environment variables

### Scaling
- Use multiple app containers behind a load balancer
- Implement Redis for session storage
- Use CDN for static and media files
- Consider database read replicas for high traffic

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Check the Django documentation
- Review django-allauth documentation

## Acknowledgments

- Django community for the excellent web framework
- django-allauth developers for authentication
- Bootstrap team for the UI framework
- All contributors to this project
