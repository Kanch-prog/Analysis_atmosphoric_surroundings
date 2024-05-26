import pandas as pd

with open('weather_data.txt', 'r') as f:
    next(f)
    next(f)
    next(f)
    
    data = []
    for line in f:
        vars = line.strip().split(' ')
        data.append([float(var) for var in vars if var])
df = pd.DataFrame(data,columns=['PRES', 'HGHT', 'TEMP', 'DWPT', 'RELH', 'MIXR', 'DRCT', 'SKNT', 'THTA', 'THTE', 'THTV'])

#plot the temperature as a function of pressure 
import matplotlib.pyplot as plt

# Plot Temperature vs Height
plt.figure(figsize=(10, 5))
plt.plot(df['HGHT'], df['TEMP'], label="Increased Temperature", color="blue")
plt.xlabel("Height (m)")
plt.ylabel("Temperature (°C)")
plt.title("Effect of Temperature Increase on Atmospheric Temperature by Height")
plt.legend(loc="upper right")
plt.grid(True)
plt.show()

#temperature increases by 5 degrees Celsius at all altitudes
temp_increase = 5
df['TEMP'] += temp_increase


#pressure decreases by 10 millibars at all altitudes
pressure_decrease = 10
df['PRES'] -= pressure_decrease


#humidity increases by 2 percent at all altitudes   
humidity_increase = 2
df['RELH'] = df['RELH'] + humidity_increase
df['RELH'] = df['RELH'].apply(lambda x: min(x, 100))


#how the temperature change affetcs the pressure
import matplotlib.pyplot as plt
plt.plot(df['PRES'], df['TEMP'], label="Original Temperature", color="blue")
plt.plot(df['PRES'], df['TEMP'] - temp_increase, label="Increased Temperature", color="green")
plt.xlabel("Pressure (hPa)")
plt.ylabel("Temperature (°C)")
plt.title("Effect of Temperature Increase on Atmospheric Temperature")
plt.legend(loc="upper left")
plt.show()

# Plot Relative Humidity vs Pressure
plt.figure(figsize=(10, 5))
plt.plot(df['PRES'], df['RELH'], label="Increased Humidity", color="orange")
plt.xlabel("Pressure (hPa)")
plt.ylabel("Relative Humidity (%)")
plt.title("Effect of Humidity Increase on Atmospheric Humidity")
plt.legend(loc="upper left")
plt.gca().invert_xaxis()  # Invert x-axis to show decreasing pressure with height
plt.grid(True)
plt.show()