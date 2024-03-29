# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    # Write your code here
    
    hours, minutes, seconds = s[:-2].split(':')
    period = s[-2:]
    
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    
    if period.upper() == 'PM' and hours < 12:
        hours += 12
    elif period.upper() == 'AM' and hours == 12:
        hours = 0
    
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    