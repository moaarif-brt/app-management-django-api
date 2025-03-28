# App Management Django API
Repository

GitHub Repository: https://github.com/moaarif-brt/app-management-django-api.git
Clone the Repository:


```bash
git clone https://github.com/moaarif-brt/app-management-django-api.git
cd app-management-django-api
```

## Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)
- Android SDK (for Task 3 Android Emulation)

## Project Structure
```
project_root/
│
├── app_management/         # Django project directory
│   ├── settings.py
│   └── urls.py
│
├── apps/                   # Django app directory
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── manage_emulator.py      # Android emulator management script
├── networking.py           # Networking script
└── README.md
```

## Setup Instructions

1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up the database
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the development server
```bash
python manage.py runserver
```

## API Endpoints
- `POST /api/add-app`: Add a new app
- `GET /api/get-app/<id>`: Retrieve app details
- `DELETE /api/delete-app/<id>`: Delete an app

## Task 2: Database Management
### Schema
- See `app_management/models.py` for database model definition

### Sample Data Insertion
Using cURL:
```bash
curl -X POST http://localhost:8000/api/add-app -H "Content-Type: application/json" -d '{
    "app_name": "MyTestApp", 
    "version": "1.0.0", 
    "description": "A sample application"
}'
```

### Sample Payload
```json
{
    "app_name": "MyTestApp",
    "version": "1.0.0",
    "description": "A sample application"
}
```

## Task 3: Virtual Android System
### Preparation
1. Ensure Android SDK is installed
2. Update `AVD_NAME` and `APK_PATH` in `manage_emulator.py`

### Running the Emulator
```bash
python manage_emulator.py
```

### Expected Output
- Starts Android emulator
- Installs specified APK
- Logs OS version and device model

## Task 4: Networking
### Running the Networking Script
1. Start Django development server
2. Ensure emulator is running
3. Execute networking script:
```bash
python networking.py
```

### Expected Output
- Sends app data with system information to `/api/add-app`
- Logs server response

## Troubleshooting
- Verify all dependencies are installed
- Check that Django server is running on `localhost:8000`
- Ensure correct paths for APK and emulator
