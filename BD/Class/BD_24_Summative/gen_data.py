import random, numpy, math

devices = [x for x in range(11)]
offsets = [random.randint(25, 60) for d in devices]
offsets[1] = 90 # Fudge the numbers a little
offsets[0] = 70

eyes = [0 for d in devices]

sensors = ['Temp1', 'Temp2', 'Temp3', 'Temp_Ambient']
sensor_numbers = [0 for d in devices] # Which sensor will be reported next\

def gen_readings(d, i):
    t = 0 # The core temperature
    t1, t2, t3 = 0, 0, 0 # Three sensor readings
    if d in [3, 10]:t3 += 200 # These two are malfuctioning
    t += numpy.random.normal(offsets[d], 5) # Some random noise around the 'true' temo from offsets
    # Adding trends to the temps
    if d in [1, 2, 4]:
        t += -10 * math.sin(i/(200*d))
    if d in [8,9]:
        t += (i*(d%3))/100
        
    # Deriving the three readings
    t1 = t
    t2 = t*1.1+10
    t3 += t/2
    t4 = numpy.random.normal(22.0, 0.2) + 5*math.sin(i/100) # Room temperature
    
    return [t1, t2, t3, t4]

def getReading():
    d = random.choice(devices) # pick a random device
    i = eyes[d]
    
    t1, t2, t3, t4 = gen_readings(d, i)
    
    report = {'Device_ID':d, 'Temp1':t1, 'Temp2':t2, 'Temp3':t3, 'Temp_Ambient':t4}
    
    sensor_numbers[d] += 1 # Next one next time
    if sensor_numbers[d] == 4: # We've done all three sensors
        sensor_numbers[d] = 0
        eyes[d] += 1
        
    
    return i, report
