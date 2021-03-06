import random
from django.http import JsonResponse
from .models import Dice

def roll(request):
  response = {}
  mode = request.GET.get("mode", "realistic")
  if (mode == "realistic" or mode == ""):
    response["dice"] = getRealisticDice()
  elif (mode == "independent"):
    response["dice"] = getIndependentDice()
  else:
    response["error"] = "Invalid mode"
  return JsonResponse(response)

def getRealisticDice():
  dices = [
    {"face" : "1", "color" : "red"},
    {"face" : "2", "color" : "blue"},
    {"face" : "3", "color" : "green"},
    {"face" : "4", "color" : "yellow"},
    {"face" : "reverse", "color" : "white"},
    {"face" : "double", "color" : "white"}
  ]
  dice = random.choice(dices)
  Dice(mode="realistic", face=dice["face"], color=dice["color"]).save()
  return dice

def getIndependentDice():
  faces = [ "1", "2", "3", "4", "reverse", "double" ]
  colors = [ "red", "blue", "green", "yellow" ]
  dice = {
    "face" : random.choice(faces),
    "color" : random.choice(colors)
  }
  Dice(mode="independent", face=dice["face"], color=dice["color"]).save()
  return dice
