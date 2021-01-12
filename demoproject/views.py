from django.http import JsonResponse

def home(request):
    return JsonResponse({"status":"Success","msg":"welcome to Zeet"})