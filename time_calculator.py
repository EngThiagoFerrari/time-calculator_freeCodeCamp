def add_time(start, duration, day_week=""):

  o_time = start[0:5].split(":")
  delta = duration.split(":")

  #converting strings to integers
  o_time = list(map(int, o_time))
  delta = list(map(int, delta))

  # Calculating and adjusting the minutes and the hour
  sum_minutes = o_time[1] + delta[1]
  if sum_minutes >= 60:
    sum_minutes -= 60
    delta[0] += 1
  sum_minutes = "{:02d}".format(sum_minutes)
  sum_hours = o_time[0] + delta[0]

  # Checking the hour and AM/ PM
  hours = list(range(0, 12))
  n = ["AM", "PM"]

  # Start indexes
  current_sign = start[-2:]
  n_i = n.index(current_sign)
  t_i = hours.index(o_time[0])

  h = 0
  while h < delta[0]:
    h += 1
    t_i += 1
    if t_i > 11:
      t_i = 0
      if n_i == 0:
        n_i = 1
      elif n_i == 1:
        n_i = 0

  am_pm = n[n_i]
  hh = hours[t_i]
  if hh == 0:
    hh = 12

  #number of days
  if "PM" in start and o_time[0] >= 1:
    sum_hours += 12
  int_days = sum_hours // 24

  # Resulting time to be displayed
  resulting_time = [hh, sum_minutes]
  time_display = ":".join(map(str, resulting_time)) + f" {am_pm}"

  # Setting the Days of the Week
  if day_week:
    days_week = [
        'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday'
    ]

    day_week = day_week.lower()
    i_days = days_week.index(day_week)

    s_index = i_days + int_days
    s = i_days
    while s < s_index:
      s += 1
      i_days += 1
      if i_days > 6:
        i_days = 0

    # Getting the resulting day of the week to be displayed
    day_week_display = days_week[i_days]

  # Formatting the resulting time display
  if int_days < 1:
    if day_week:
      result_display = f"{time_display}, {day_week_display.title()}"
    else:
      result_display = f"{time_display}"
  elif int_days == 1:
    if day_week:
      result_display = f"{time_display}, {day_week_display.title()} (next day)"
    else:
      result_display = f"{time_display} (next day)"
  elif int_days >= 2:
    if day_week:
      result_display = f"{time_display}, {day_week_display.title()} ({str(int_days)} days later)"
    else:
      result_display = f"{time_display} ({str(int_days)} days later)"

  new_time = result_display

  return new_time
