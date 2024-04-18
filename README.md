# Mini-Drf-Project

An example Django REST framework project.
## About

I'm working on creating an real-time chat for this project.

## Test Case Scenarios

- Authentication(jwt) with gmail verification
- File managing
- User customization
- PostgreSQL
- CRUD api
  
## API Endpoints

### Users

- `/account/register/`: User registration endpoint
- `/api/login/`: User login endpoint
- `/api/token/blacklist/`: User logout endpoint(Not working yet)

### Profiles

- `/Profile/profile/`: Get Profiles endpoint
- `//Profile/profile/create/`: Create Profiles endpoint
- `/profile/<int:pk>/`: Update Profiles endpoint
- `/profile/<int:pk>/delete/`: Delete Profiles endpoint

  
### Profiles

- `/Camera_Files/files`: Get Camera_files endpoint
- `/Camera_Files/files/create/`: Create Camera_files endpoint
- `/Camera_Files/files/<int:pk>/`: Update Camera_files endpoint
- `/Camera_Files/files/<int:pk>/delete/`: Delete Camera_files endpoint

### Google token(this is for mobile app)

- `/Camera_Files/getgtoken/`: Create Google token endpoint

## Install

```bash
pip install -r requirements.txt
```
## RUN

```bash
python manage.py runserver
```
