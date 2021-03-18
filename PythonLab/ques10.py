''''Write a program to convert seconds to day, hour, minutes and seconds.'''

second = int(input("enter the time:"))
minutes = second // 60
hour = ((second // 60) // 60)
day = (((second // 60) //60) // 24)
remain_second = second % 60
print(f"time in minutes is {minutes}")
print(f"time in hour is {hour}")
print(f"time in day is {day}")
print(f"Remaining second is {remain_second}")