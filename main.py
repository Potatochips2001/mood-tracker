#!/usr/bin/env python3
from datetime import date, datetime
import json

def resetLogs():
  resetOption = input("Are you sure you want to reset logs?[Y/n]")
  if resetOption.upper() != 'Y': exit("Your logs were not deleted")
  resetOption = input("Type 'delete' to confirm: ")
  if resetOption.lower() != 'delete': exit("Your logs were not deleted");
  f = open("logs.json", 'w')
  f.truncate(0)
  f.close()
  del(f)
  exit("Your logs have been reset")

def viewLogs():
  f = open("logs.json", 'r')
  for line in f.readlines():
    lineDate = json.loads(line)['mood-tracker']['date']
    lineMood = json.loads(line)['mood-tracker']['mood']
    lineDescription = json.loads(line)['mood-tracker']['description']
    lineGoals = json.loads(line)['mood-tracker']['goals']
    print(f"Date: {lineDate}, Mood: {lineMood}, Description: {lineDescription}, Goals: {lineGoals}\n")
  del(f)
  exit()

_option = input('''
Options:
1) Add new log
2) View logs
\u001b[31;1m3) Reset logs\u001b[0m
''')

if _option == '2': viewLogs()
elif _option == '3': resetLogs()

moodRating = input('''
How are you feeling?
1) Suicidal
2) Bad
3) Normal
4) Good
5) Euphoric
''')
if moodRating == '1':
  moodRating = 'Suicidal'
elif moodRating == '2':
  moodRating = 'Bad'
elif moodRating == '3':
  moodRating = 'Normal'
elif moodRating == '4':
  moodRating = 'Good'
elif moodRating == '5':
  moodRating = 'Euphoric'

describeMood = input("Describe your mood: ")

goals = input("What are your goals, how can you accomplish them: ")

logToAdd = {
  "mood-tracker": {
    "date": f"{datetime.today().month}/{datetime.today().day}/{datetime.today().year} {datetime.today().hour}:{datetime.today().minute}",
    "mood": moodRating,
    "description": describeMood,
    "goals": goals
  }
}

f = open("logs.json", 'a')
f.write(json.dumps(logToAdd) + '\n')
f.close()
