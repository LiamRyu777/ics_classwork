import time


swimmer1 = "GALLANT"
swimmer2 = "GOOFUS "

minimum_temperature = 79.0
current_temperature = 0.0
saved_temperature = 0.0
swim_time = 0

current_temperature = float(input("What is the current water temperature? "))
saved_temperature = current_temperature  # saves a copy of this value so we can get it back later.

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer1} approaches the lake....")

swim_time = 0
while current_temperature >= minimum_temperature:
    print(f"\t{swimmer1} swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)  # pauses for 600 milliseconds
    current_temperature -= 0.5  # subtracts 1/2 a degree from the water temperature
    print(f"\tThe current water temperature is now {current_temperature} F.")


print(f"{swimmer1} stops swimming. Total swim time: {swim_time} min.")

current_temperature = saved_temperature  # restores original water temperature

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer2} approaches the lake....")

swim_time = 0
while True:
    print("\t" + swimmer2 + " swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)
    current_temperature -= 0.5
    print(f"\tThe current water temperature is now {current_temperature} F.")
    
    if current_temperature < minimum_temperature:
        break

print(f"{swimmer2} stops swimming. Total swim time: {swim_time} min.")

# Q1. Yes, for 4 minutes
# Q2.Gallant does not swim at all because he checks the temperature first and sees that it is below 79°F. 
# Goofus swims for 1 minute before stopping because he checks the temperature after swimming.
# Q3.Gallant checks the water temperature first. If the temperature is below 79°F, he does not swim.
# Q4.Goofus dives right in without checking the temperature first. He checks the temperature after swimming.
# Q5.The first while loop checks the condition before executing the loop. 
# The second loop uses while True, so it starts running immediately and checks the temperature inside the loop. 
# The break keyword immediately stops the loop when the condition for stopping is met.
# Q6.The first loop (Gallant's) is the pre-test loop because it checks the condition before running. 
# The second loop (Goofus's) is the post-test loop because he swims before checking the temperature.