from django.shortcuts import render

# Create your views here.
def index(request):
  html = "dice_web.html"
  return render(request, html)
