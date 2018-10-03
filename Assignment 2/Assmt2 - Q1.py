'''
Many times, I have to make a decision to travel by local train or take the bus - examples:
    Coming to the Department of Computer Science on weekends.
    Coming back from shopping during evenings
    Going to the airport to pick up friends
Events which can change my choices drastically:
    Waking up late or early
    Window-shopping
    Change in flight timings
Let's hope this algorithm helps me out!
'''


def check_time(bus_time, train_time):
'''
Function to check which mode of travel is quicker
:param bus_time: Time taken by bus
:param train_time: Time taken by train
:returns: Either Quicker mode of travel or any if both are equal
'''
  if bus_time < train_time:
    mode = 'bus'
  elif bus_time == train_time:
    mode = 'any'
  else:
    mode = 'train'
  return mode

def check_fare(bus_fare, train_fare):
'''
Function to check which mode of travel is cheaper
:param bus_fare: Fare taken by bus
:param train_fare: Fare taken by train
:returns: Either cheaper mode of travel or any if both are equal
'''
  if bus_fare < train_fare:
    mode = 'bus'
  elif bus_fare == train_fare:
    mode = 'any'
  else:
    mode = 'train'
  return mode

def check_crowd(bus_crowd, train_crowd):
'''
Function to check which mode of travel is less crowded
:param bus_crowd: Crowd for bus
:param train_crowd: Crowd for Train
:returns: Either less crowded mode of travel or any if both are equal
'''
  if bus_crowd < train_crowd:
    mode = 'bus'
  elif bus_crowd == train_crowd:
    mode = 'any'
  else:
    mode = 'train'
  return mode

total_dist = float(input("Enter distance you want to travel in kms"))

choice = input("Do you want to travel quicker or cheaper or can't decide?")
bus_fare = float(input("Enter the bus fare in rupees"))
bus_time = float(input("Enter time taken to travel by bus in hours"))

train_fare = float(input("Enter the train fare in rupees"))
train_time = float(input("Enter time taken by train in hours"))

if choice == 'quicker':
  mode_t = check_time(bus_time, train_time)
  if mode_t != 'any':
    print("Travel by ", mode_t)
  else:
    mode_f = check_fare(bus_fare, train_fare)
    if mode_f != 'any':
      print("Any mode is fine, but " + mode_f + " is cheaper")
    else:
      print("Both ways take the same time and money")

elif choice == 'cheaper':
  mode_f = check_fare(bus_fare, train_fare)
  if mode_f != 'any':
    print("Travel by ", mode_f)
  else:
    mode_t = check_time(bus_time, train_time)
    if mode_t != 'any':
      print("Any mode is fine, but " + mode_t + " is quicker")
    else:
      print("Both ways take the same time and money")

else:
  bus_crowd = int(input("Enter the bus crowd"))
  train_crowd = int(input('Enter the train crowd'))
  mode_c = check_crowd(bus_crowd, train_crowd)
  if mode_c != 'any':
    print(mode_c + " is less crowded")
  else:
    print("Both are similarly crowded. Take any mode of travel")
