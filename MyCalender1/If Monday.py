# this first part of the program will tell if I have a monday in my calender.

Mycalender1 = (" Day       Time             Subject\n"
               "--------------------------------------\n"
               "Monday   9:10-10:15         P.E.\n"
               "Monday   10:15-10:35        Break\n"
               "Monday   10:35-11:40        Exploratory wheel\n"
               "Monday   11:40-12:10        Lunch\n"
               "Monday   12:10-1:15         Science\n"
               "Monday   1:15-3:00          Independent work time\n"
               "Tuesday  9:10-10:15         Math\n"
               "Tuesday  10:15-10:35        Break\n"
               "Tuesday  10:35-11:40        Language arts\n"
               "Tuesday  11:40-12:10        Lunch\n"
               "Tuesday  12:10-1:15         Social Studies\n"
               "Tuesday  1:15-3:00          Independent work")

if "Monday" in Mycalender1:
    print("There is a Monday in my calender")
else:
    print("There is not a Monday in my calender")
# this is where my calender will be uppercase
print(Mycalender1.upper())