from django.shortcuts import render

# Create your views here.
def test_view(request):
    return HttpResponse("Test page")