from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .my_python_project.run_program import nearest_similarity_cosmul

@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def getanswer(request):
    if request.method == 'POST':
        # Accepting POST request from the user
        
        str1 = request.POST.get("str1", "")
        str2 = request.POST.get("str2", "")
        str3 = request.POST.get("str3", "")

        answer = nearest_similarity_cosmul(str1, str2, str3)

        
        return HttpResponse("<html><head><title>Relations in Harry Potter</title></head><body><br><br><center><h1>Relations in Harry Potter</h1></center><br><br><center>"+str1+ " is related to "+str2+", as "+answer+" is related to "+str3+"</center></body></html>")
    else:
        return HttpResponse("Something went wrong!")


