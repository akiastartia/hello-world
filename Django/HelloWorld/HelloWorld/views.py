# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

# def runoob(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)

def runoob(request):
    views_name = "美少女战士之家"
    views_list = ["美少女战士之家","咸蛋超人之家","R301 Dream House"]
    views_dict = {"name1": "美少女",
                  "name2": "咸蛋超人",
                  "name3": "Chamber of weapon"}
    # return render(request, "runoob.html", {"views_list":views_list})
    return render(request, "runoob.html", {"views_dict":views_dict})