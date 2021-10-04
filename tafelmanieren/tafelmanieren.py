for tafel in range(1,11):   #eerste
    print(tafel)            

print("-----------------------------------------")

for lancering in reversed(range(1,31)):         #tweede, reversed zorgt voor het 'reversen' van de range
    print(lancering)
print("We zijn gelanceerd!")

print("-----------------------------------------")

for time in range(0,24):                    #derde
    if time < (10):
        print("0"+ (str(time) + ":00 AM"))
    elif time >(10):
        print(str(time) + ":00 AM")
    elif time >= (13):
        print(str(time) + ":00 PM")

print("-----------------------------------------")

for EvenGetallen in range(20,50,2):             #vierde was ez
    print(EvenGetallen)
