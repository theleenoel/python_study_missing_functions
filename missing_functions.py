def is_on_list(days=[],a=""):
  return a in days

def get_x(days=[],a=0):
  return days[a]

def add_x(days=[],a=""):
  return days.append(a)

def remove_x(days=[],a=""):
  return days.remove(a)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #