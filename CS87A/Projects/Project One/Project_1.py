#Name: Alfonso Del Rosario
#Assignment # 1
#Submission Date: 06/27/2021

user = input("Enter your name: ")

hourlyRate = float(input("%s kindly enter your hourly rate? " % (user)))

totalHours = float(input("%s kindly enter the total hours you have worked this week "% (user)))

print("%s your salary for this week should be %.2f" % (user, hourlyRate * totalHours))