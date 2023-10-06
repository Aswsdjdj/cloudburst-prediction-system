import tkinter
import customtkinter 
from PIL import Image, ImageTk

def predict():


    humidity_variable_value=int(humidity_variable.get())
    Air_pressure_variable_value=int(Air_pressure_variable.get())
    min_temp_variable_value=int(min_temp_variable.get())
    max_temp_variable_value=int(max_temp_variable.get())
    wind_speed_variable_value=int(wind_speed_variable.get())
    cloud_coverage_variable_value=int(cloud_coverage_variable.get())
    raining=radio_var.get()

    if wind_speed_variable_value>=13 and humidity_variable_value>=60 and cloud_coverage_variable_value>=65 :
        
        result_label=customtkinter.CTkLabel(master=login_credential_frame,text="There can be a cloud burst",font=("Century Gothic",50))
        result_label.place(x=375,y=800)

    else:
        result_label=customtkinter.CTkLabel(master=login_credential_frame,text="NO Chance of Cloud Burst   ",font=("Century Gothic",50))
        result_label.place(x=375,y=800)


customtkinter.set_appearance_mode("system")
login_window=customtkinter.CTk()
login_window.geometry("1920x1080")
login_window.title("Login Page")
image1=ImageTk.PhotoImage(Image.open("E:\\cloud burst\\background.jpg"))
background_frame1=customtkinter.CTkLabel(master=login_window,image=image1)
background_frame1.pack()
login_credential_frame=customtkinter.CTkFrame(master=background_frame1,width=1400,height=1000,corner_radius=10)
login_credential_frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

heading_label=customtkinter.CTkLabel(master=login_credential_frame,text="Cloud Burst Predictor",font=("Arial",50))
heading_label.place(x=500,y=45)

heading_label=customtkinter.CTkLabel(master=login_credential_frame,text="---------------------------------------------------------------------------------------------------------------------------------------------",font=("Arial",40))
heading_label.place(x=00,y=100)

location_label=customtkinter.CTkLabel(master=login_credential_frame,text="Location",font=("Century Gothic",30))
location_label.place(x=50,y=200)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=230,y=200)

optionmenu_var = customtkinter.StringVar(value="Select Location")
optionmenu = customtkinter.CTkOptionMenu(master=login_credential_frame, values=["Leh (Ladakh)", "UttarKashi (Uttarakhand)","Kedarnath (Uttarakhand)","Manali (Himachal Pradesh)","Dharm Shala (Himachal Pradesh)","Srinagar (Jammu and kashmir)","Chamba (Himachal Pradesh)","Baderwah (Jammu and kashmir)"],variable=optionmenu_var,width=1000,font=("Century Gothic",30))
optionmenu.place(x=250,y=200)

humidity_label=customtkinter.CTkLabel(master=login_credential_frame,text="Humidity",font=("Century Gothic",30))
humidity_label.place(x=50,y=300)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=230,y=300)

global humidity_variable
humidity_variable=customtkinter.StringVar()
humidity_entry=customtkinter.CTkEntry(master=login_credential_frame,width=300,textvariable=humidity_variable,font=("Century Gothic",30))
humidity_entry.place(x=250,y=300)
humidity_entry.focus()

Air_pressure_label=customtkinter.CTkLabel(master=login_credential_frame,text="Air pressure",font=("Century Gothic",30))
Air_pressure_label.place(x=750,y=300)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=930,y=300)

global Air_pressure_variable
Air_pressure_variable=customtkinter.StringVar()
Air_pressure_entry=customtkinter.CTkEntry(master=login_credential_frame,width=300,textvariable=Air_pressure_variable,font=("Century Gothic",30))
Air_pressure_entry.place(x=950,y=300)


min_temp_label=customtkinter.CTkLabel(master=login_credential_frame,text="Min Temp",font=("Century Gothic",30))
min_temp_label.place(x=50,y=400)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=230,y=400)

global min_temp_variable
min_temp_variable=customtkinter.StringVar()
min_temp_entry=customtkinter.CTkEntry(master=login_credential_frame,width=300,textvariable=min_temp_variable,font=("Century Gothic",30))
min_temp_entry.place(x=250,y=400)

max_temp_label=customtkinter.CTkLabel(master=login_credential_frame,text="Max Temp",font=("Century Gothic",30))
max_temp_label.place(x=750,y=400)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=930,y=400)

global max_temp_variable
max_temp_variable=customtkinter.StringVar()
max_temp_entry=customtkinter.CTkEntry(master=login_credential_frame,width=300,textvariable=max_temp_variable,font=("Century Gothic",30))
max_temp_entry.place(x=950,y=400)



wind_speed_label=customtkinter.CTkLabel(master=login_credential_frame,text="Wind Speed",font=("Century Gothic",30))
wind_speed_label.place(x=50,y=500)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=230,y=500)

global wind_speed_variable
wind_speed_variable=customtkinter.StringVar()
wind_speed_entry=customtkinter.CTkEntry(master=login_credential_frame,width=300,textvariable=wind_speed_variable,font=("Century Gothic",30))
wind_speed_entry.place(x=250,y=500)

cloud_coverage_label=customtkinter.CTkLabel(master=login_credential_frame,text="Cloud \n Coverage",font=("Century Gothic",30))
cloud_coverage_label.place(x=750,y=475)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=930,y=500)

global cloud_coverage_variable
cloud_coverage_variable=customtkinter.StringVar()
cloud_coverage_entry=customtkinter.CTkEntry(master=login_credential_frame,width=300,textvariable=cloud_coverage_variable,font=("Century Gothic",30))
cloud_coverage_entry.place(x=950,y=500)



rain_label=customtkinter.CTkLabel(master=login_credential_frame,text="Is it Raining currently or before 3 hours",font=("Century Gothic",30))
rain_label.place(x=50,y=600)

dot_label=customtkinter.CTkLabel(master=login_credential_frame,text=":",font=("Century Gothic",30))
dot_label.place(x=650,y=600)

radio_var = tkinter.IntVar(value=1)
radiobutton_1 = customtkinter.CTkRadioButton(master=login_credential_frame, text="Yes",variable= radio_var, value=1)
radiobutton_1.place(x=725,y=610)
radiobutton_2 = customtkinter.CTkRadioButton(master=login_credential_frame, text="No",variable= radio_var, value=0)
radiobutton_2.place(x=875,y=610)


predict_button=customtkinter.CTkButton(master=login_credential_frame,width=800,text="Predict",corner_radius=6,font=("Century Gothic",30),command=predict)
predict_button.place(x=300,y=700)


login_window.mainloop()