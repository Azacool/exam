from django.shortcuts import render
from .models import Content

def main(request):
    contents = Content.objects.all()
    for content in contents:
        print(content.image)
    return render(request,'index.html',{'contents':contents})

def contact(request,pk):
    contact = Content.objects.get(id=pk)
    return 