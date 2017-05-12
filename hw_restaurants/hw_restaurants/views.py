from django.shortcuts import redirect

def index(request):
    return redirect('restaurants_index')
