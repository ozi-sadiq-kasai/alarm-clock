from datetime import datetime
from playsound import playsound

AlarmHour = int(input('Enter Hour: '))
AlarmMinute = int(input('Enter Minute: '))
Am_Pm = input("Enter 'am' or 'pm': ").lower()

if Am_Pm == 'pm':
    AlarmHour += 12

print('initializing alarm')

while True:
    if AlarmHour == datetime.now().hour and AlarmMinute == datetime.now().minute:
        print('Wake up')
        playsound(r"C:\Users\user\Downloads\Kizz_Daniel_Ft_Tekno_-_Buga.mp3")