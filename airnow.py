from tkinter import *
import requests
import json

root=Tk()
root.title("Weather GUI")
pinCode="60640"
data=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+pinCode+"&distance=25&API_KEY=E2BDE2A9-B6E8-4B75-8219-5CA31048834D")
pythondata=json.loads(data.content)
try:
    AQIvalue = pythondata[0]['AQI']
    reportingArea = pythondata[0]['ReportingArea']
    Feedback = pythondata[0]['Category']['Name']
    if AQIvalue < 20:
        color = "green"
    elif AQIvalue < 40:
        color = "yellow"
    else:
        color = "red"
    canvas = Canvas(root, width=300, height=300,bg=color)
    canvas.pack()
except:
    AQIvalue="error"
    reportingArea="error"
    Feedback="error"
    if AQIvalue:
        color="maroon"
    canvas = Canvas(root, width=300, height=300, bg=color)
    canvas.pack()



d_label=Label(root,text="Here is the Data!!",font="Arial",fg="blue")
canvas.create_window(150,60,window=d_label)

output_label=Label(root,text=f"Air Quality:{AQIvalue}\nArea:{reportingArea}\nFeedback:{Feedback}",font="Arial",bg="violet")
canvas.create_window(150,150,window=output_label)


root.mainloop()

