#list of stops on a route
route_stops = ("Station A", "Station B", "Station C", "Station D", "Station E")

#function to view all stops
def view_stops():
  """Display all stops on the route."""
  print("Stops on the route:")
  for index, stop in enumerate(route_stops):    # enumarate gives us index as well as the values of the tuple item
      print(f"{index + 1}. {stop}")

def check_stop_exits (stop_name):
    if stop_name in route_stops:
        print (f"{stop_name} is on the route!")
    else:
        print (f"{stop_name} is not on the route.")

def find_distance_from_start(stop_name):
    try:
        stop_index = route_stops.index(stop_name)
        print(f"{stop_name} is {stop_index} stop(s) away from the starting point.")
    except ValueError:
        print(f"{stop_name} does not exit on the route")
def main():
    view_stops()
    stop_name = input("Enter the name of the stop to check: ").strip()
    check_stop_exits(stop_name)
    stop_name = input("Enter the name of the stop to find distance: ").strip()
    find_distance_from_start(stop_name)

main()