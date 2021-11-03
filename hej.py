import datetime
date = str(input("Enter the date DD MM YYYY"))

day_name = ["måndag","tisdag","onsdag","torsdag","fredag","lördag","söndag"] 

day = datetime.datetime.strptime(date,"%d %m %Y").weekday()

svar = str((day_name[day]))

print (svar)

if svar == "måndag":
    print ("MA 08:30 till 09:30 SV 09:30 till 10:30 RAST 10:30 till 11:10 IDH 11:10 till 12:15 LUNCH 12:15 till 12:45 RAST 12:45 till 13:15 NO 13:15 till 14:30")
if svar == "tisdag":
    print ("MA 08:30 TILL 09:25 SO 09:25 TILL 10:30 RAST 10:30 TILL 11:05 SL 11:05 TILL 12:15 LUNCH 12:15 TILL 12:45 RAST 12:45 TILL 13:15 ENG 13:15 TILL 13:55") 
if svar == "onsdag":
    print ("SV 08:30 TILL 08:50 BL 08:50 TILL 09:90 ENG 09:30 TILL 10:30 RAST 10:30 TILL 11:00 SV 11:00 TILL 12:15 LUNCH 12:15 TILL 12:45 RAST 12:45 TILL 13:15 ENG 13:15 TILL 14:25")
if svar == "torsdag":
    print ("MA 08:40 TILL 09:40 MU 09:40 TILL 10:30 RAST 10:30 TILL 11:00 SV 11:00 TILL 12:15 LUNCH 12:15 TILL 12:45 RAST 12:45 TILL 13:15 SO 13:15 TILL 14:40 RAST 14:40 TILL 15:00 IDH 15:00 TILL 16:00 ")
if svar == "fredag":
    print ("")
if svar == "lördag":
    print ("Ledig")
if svar == "söndag":
    print ("Ledig")