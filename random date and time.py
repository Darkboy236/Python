import random #importing module
import time

def getRandomDate(startDate, endDate ): #defining function#
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.Random
    dateformat = "%m/%d/%Y"
    startTime = time.mktime(time.strptime(startDate, dateformat))
    endTime = time.mktime(time.strptime(endDate, dateformat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateformat, time.localtime(randomTime))
    return randomDate
#display result
print("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))