def return_10():
  return 10
 
def add(num_1, num_2):
  return num_1 + num_2

def subtract(num_1, num_2):
  return num_1 - num_2
  
def multiply(num_1, num_2): 
  return num_1 * num_2

def divide(num_1, num_2):
  return num_1 / num_2

def length_of_string(a_string):
  return len(a_string)

def join_string(string_1, string_2):
  return string_1 + string_2

def add_string_as_number(str_num1, str_num2):
  return int(str_num1) + int(str_num2)

import calendar
def number_to_full_month_name(month_num):
  return calendar.month_name[month_num]

def number_to_short_month_name(month_num):
  return calendar.month_abbr[month_num]