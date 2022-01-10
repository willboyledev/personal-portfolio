from django.shortcuts import render

# Create your views here.
def coding(request):
    return render(request, 'coding/coding.html')