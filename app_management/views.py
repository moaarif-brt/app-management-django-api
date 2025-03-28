from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import App

@csrf_exempt
def add_app(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            app = App.objects.create(
                app_name=data['app_name'],
                version=data['version'],
                description=data.get('description', '')
            )
            return JsonResponse({
                'id': app.id, 
                'message': 'App added successfully'
            }, status=201)
        except KeyError:
            return JsonResponse({
                'error': 'Missing required fields'
            }, status=400)

def get_app(request, id):
    if request.method == 'GET':
        app = get_object_or_404(App, id=id)
        return JsonResponse({
            'id': app.id,
            'app_name': app.app_name,
            'version': app.version,
            'description': app.description
        })

@csrf_exempt
def delete_app(request, id):
    if request.method == 'DELETE':
        app = get_object_or_404(App, id=id)
        app.delete()
        return JsonResponse({
            'message': 'App deleted successfully'
        }, status=200)
