import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get() #getting city name from user
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=98c178f21b28af823ffb9282fb68eca9"
    json_data = requests.get(api).json() #getting the json data which we are recieving from api calling
    condition = json_data['weather'][0]['main'] #getting the weather json data
    temp = int(json_data['main']['temp'] - 273.15) 
    min_temp = int(json_data['main']['temp_min'] - 273.15) 
    max_temp = int(json_data['main']['temp_max'] - 273.15) 
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    #sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']))
    

    final_info = condition + "\n" +str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp:" +str(min_temp) + "\n" +"Pressure:" + str(pressure) +"\n" + "Humidity:" + str(humidity) + "\n" + "Wind Speed: " + str(wind) 
     
     #Attaching the data to the labels we have created
    label1.config(text= final_info)
    label2.config(text= final_data)
     





canvas = tk.Tk()
canvas.geometry("800x400") #defining the size of the block
canvas.title("My Weather App") #naming the app

f = ("poppins",15,"bold")
t = ("poppins",35,"bold") #adding fonts

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=50) #setting up the padding
textfield.focus() #when user enter the app, they can type city name directly without moving the cursor
textfield.bind('<Return>',getWeather)





label1 = tk.Label(canvas,font=t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()