from datetime import date, timedelta

startdate = '20180727'
enddate = '20210927'

startdateyear = startdate[:4]
startdateyear = int(startdateyear)
startdatemonth = startdate[4:6]
startdatemonth = int(startdatemonth)
startdateday = startdate[6:]
startdateday = int(startdateday)

enddateyear = enddate[:4]
enddateyear = int(enddateyear)
enddatemonth = enddate[4:6]
enddatemonth = int(enddatemonth)
enddateday = enddate[6:]
enddateday = int(enddateday)

startdate = date(startdateyear, startdatemonth, startdateday)
enddate = date(enddateyear, enddatemonth, enddateday)

difference = enddate - startdate
print(difference)
count = 0
for i in range(difference.days+1):
    day = startdate + timedelta(days=i)
    if str(day.ctime())[:3] == "Sat" and int(str(day)[-2:])%5 ==0:
        print(day)