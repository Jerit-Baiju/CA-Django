from django.shortcuts import render
from accounts.models import User
# Create your views here.

def index(request):
    context = {
        'nav': 'chats'
    }
    return render(request, 'base/index.html', context)

def chat(request, pk):
    context = {
        'user': User.objects.get(id=pk)
    }
    return render(request, 'base/chat.html', context)