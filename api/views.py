from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageOps
import io
import base64
import json

@csrf_exempt
def get_resolution(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            img_data = base64.b64decode(data['image_b64'])
            img = Image.open(io.BytesIO(img_data))
            
            return JsonResponse({'width': img.width, 'height': img.height})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)

@csrf_exempt
def convert_grayscale(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            img_data = base64.b64decode(data['image_b64'])
            img = Image.open(io.BytesIO(img_data))
            
            # Resmi gri tonlamaya çevir
            gray_img = ImageOps.grayscale(img)
            
            buffered = io.BytesIO()
            gray_img.save(buffered, format="JPEG")
            gray_b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
            
            return JsonResponse({'image_b64': gray_b64})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)