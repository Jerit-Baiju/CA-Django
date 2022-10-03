from django.shortcuts import render

# Create your views here.

def profile(request):
    context = {
        'nav': 'profile'
    }
    return render(request, 'accounts/profile.html', context)