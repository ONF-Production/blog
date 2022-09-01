from django.shortcuts import render


# Create your views here.
def indexAdmin(request):
    return render(request, 'index_admin.html')