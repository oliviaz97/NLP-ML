# -*- coding: utf-8 -*-
'''
Program that extracts two types of dates from an input txt file
two types of dates include:
 1. Fixed dates (e.g. “January 15, 2014”, “the 21st of December”,
    “01/15/2014” (only the American notation), “Monday”, “Monday the 23rd”,
    “Monday, 2pm”, “Monday afternoon” )
 2. Holidays
'''
import re
import sys

file = sys.argv[1]
f = open(file, "r") # store lines from input.txt as elements in a list
input = f.read()
f.close()

result = []

month = "(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|(Nov|Dec)(ember)?)" # specify whitespace?
day_of_week = "(Mon(day)?|Tue(sday)?|Wed(nesday)?|Thur(sday)?|Fri(day)?|Sat(urday)?|Sun(day))"
holidays = "(New Year's Day|New Year's Eve|Martin Luther King(\s)?(Jr.)? Day|George Washington's Birthday|Veteran(')?s Day|Groundhog Day|Labor Day|Valentine's Day|Presidents' Day|St. Patrick's Day|Easter(\s)?(Sunday)?|Cinco de Mayo|Memorial Day|Independence Day|Columbus Day|Presidents' Day|Christmas(\s)?(Day)?|Thanksgiving(\s)?(Day)?|Inauguration Day)"
date = "(yesterday|today|tomorrow|tonight)" # ambiguous dates?
time = "(morning|noon|afternoon|evening)"
counting = "(st|nd|rd|th)?"
m_a = "(a(.)?m(.)?|p(.)?m(.)?)"

# month roots
month_roots = "(" + "(" + "(" + day_of_week + "?(,?)" + month + ".?,?\s" + "\d{1,2}" + counting + ",?)" + "\s(\d{4})?)" + "\s?" + holidays + "?)"

# day roots
day_roots = "(" + "(" + day_of_week + "(.?)(,?|(,?\s?)|\s?)" + ")?" + "(the\s\d{1,2}" + counting + "\sof\s" + month + ",?" + "(\s?\d{4})?" + "\s?" + ")" + "(" + "at\s\d{1,2}" + m_a + ")?" +")"

# morning/evenings
mo_ev = "(" + day_of_week + "(" + "\s" + time + ")?(" + ",?\s" + month + ".?,?\s" + "\d{1,2}" + counting + ",?(\s?(\d{4}))?" + ")?" + "((,?)\s(at\s)?\d{1,2}" + m_a + "?" + counting + ")?)"

# formatted dates
slash_format = "(\d{1,2}[-/]\d{1,2}([-/]\d{4})?)"

#find dates with month roots
find_month_roots = re.compile(month_roots, re.IGNORECASE)
mds = find_month_roots.findall(input) # match
mds = [x[0] for x in mds if x != " "] # get rid of spaces
for date in mds:
    result.append(date)
    result.append("\n")

#find dates with day roots
find_day_roots = re.compile(day_roots, re.IGNORECASE)
drs = find_day_roots.findall(input) # match
drs = [x[0] for x in drs if len(x) > 1] # get rid of spaces
for date in drs:
    result.append(date)
    result.append("\n")

#find afternoon/evenings
find_day = re.compile(mo_ev)
me = find_day.findall(input)
me = [x[0] for x in me if len(x) > 1]
for day in me:
    result.append(day)
    result.append("\n")

#find slashed dates
find_slashes = re.compile(slash_format, re.IGNORECASE)
sf = find_slashes.findall(input) # match
sf = [x[0] for x in sf if len(x) > 1] # get rid of spaces
for date in sf:
    result.append(date)
    result.append("\n")

# find holidays
find_holidays = re.compile(holidays, re.IGNORECASE)
holidays = find_holidays.findall(input)
holidays = [x[0] for x in holidays if len(x) > 1]
for holiday in holidays:
    result.append(holiday)
    result.append("\n")

for i in result:
    print(i)

output = "".join(result)
op = open("output.txt", "w")
op.write(output)
op.close()
