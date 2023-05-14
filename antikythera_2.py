from tkinter import *
from tkinter import ttk
import time
from tkcalendar import Calendar
from planets import *
from moon import *
from scale import *
import calendar
window = Tk()
window.title("system")
window.configure(bg="#675481")
xc = 400
yc = 400
canvas = Canvas(window,width=800,height=800,bg="#554433",cursor="pencil")
canvas_moon = Canvas(window,width=250,height=250,bg="#212121",cursor="pencil")
canvas_leap_year = Canvas(window,width=250,height=250,bg="#212121",cursor="pencil")

#scale object ini
scale=Scale_C(canvas)
scale.equanox()
scale.names(canvas)

#calendar ini
now = datetime.datetime.now()
cal = Calendar(window, selectmode='day',
               year=now.year, month=now.month,
               day=now.day)
#slider ini
scale1 = DoubleVar()
w = Scale(window, from_=0, to=240, orient=HORIZONTAL,length=240,label="UTC Time",variable=scale1)

#packs
canvas.pack(side = LEFT)
canvas_moon.pack(side = LEFT)
canvas_leap_year.pack(side = LEFT)
cal.pack(side = TOP)
canvas_moon.pack(side=BOTTOM)
w.pack()
canvas_leap_year.pack(side=BOTTOM)

def rad_to_frac(ang1):
    return ang1/(PI*2)

def sun_anm(days_j2000a):
    days_j2000a-=(equinox * year)
    fraction_of_year = (days_j2000a % year) / year
    return fraction_of_year

def line2(i,gap,width,space,color):
    i= -i
    canvas_leap_year.create_line(125+100 * math.cos(i * math.pi/space + math.pi/2),
                        125-100 * math.sin(i * math.pi/space + math.pi/2),
                        125+(100-gap) * math.cos(i * math.pi/space + math.pi/2),
                        125-(100-gap) * math.sin(i * math.pi/space + math.pi/2),
                        width = width,fill=color)


mars_check = IntVar()
mars_check.set(1)

jupiter_check = IntVar()
jupiter_check.set(1)

mercury_check = IntVar()
mercury_check.set(1)

sun_check = IntVar()
sun_check.set(1)

moon_check = IntVar()
moon_check.set(1)

venus_check = IntVar()
venus_check.set(1)

neptune_check = IntVar()
neptune_check.set(1)

uranus_check =IntVar()
uranus_check.set(1)

saturn_check =IntVar()
saturn_check.set(1)

enabled_checkbutton = ttk.Checkbutton(text="Mercury", variable=mercury_check)
enabled_checkbutton.pack(anchor=S)

enabled_checkbutton = ttk.Checkbutton(text="Venus", variable=venus_check)
enabled_checkbutton.pack(side=TOP)

enabled_checkbutton = ttk.Checkbutton(text="Mars", variable=mars_check)
enabled_checkbutton.pack(side=TOP)

enabled_checkbutton = ttk.Checkbutton(text="Jupiter", variable=jupiter_check)
enabled_checkbutton.pack(side=TOP)

enabled_checkbutton = ttk.Checkbutton(text="Saturn", variable=saturn_check)
enabled_checkbutton.pack(side=TOP)

enabled_checkbutton = ttk.Checkbutton(text="Uranus", variable=uranus_check)
enabled_checkbutton.pack(side=TOP)

enabled_checkbutton = ttk.Checkbutton(text="Neptune", variable=neptune_check)
enabled_checkbutton.pack(side=TOP)

i=0
while i < 96:
    line2(i, 12, 1,48 , '#660000')
    if((i%24)==0):
        line2(i, 13, 3, 48, '#22aa77')
    i = i + 1
    h=(time.time()%86400)/86400
    w.set(math.floor(240 * h))

leap = canvas_leap_year.create_line(125, 125,
                                    125 + (100) * math.cos(math.pi * 2 - math.pi * 2),
                                    125 - (100) * math.sin(math.pi * 2 + math.pi * 2),
                                    width=5, fill="#00ff00")

arr1 = circle(False, 0,canvas_moon)
arr2 = circle(False, 1,canvas_moon)
arr3 = []

def whi_main():
    global leap
    global arr2
    global arr1 , arr3
    scale.clear()
    canvas_leap_year.delete(leap)
    for a in arr1:
        canvas_moon.delete(a)
    for a in arr3:
        canvas_leap_year.delete(a)
    for b in arr2:
        canvas_moon.delete(b)

    day_s = scale1.get() * 86400 / 240

    date = cal.get_date()

    time_tuple = time.strptime(date, "%m/%d/%y")
    seconds_since_epoch=calendar.timegm(time_tuple)
    seconds_since_epoch += day_s

    j2000_day = (seconds_since_epoch-j2000_start)/86400
    moon_d2 = angle_moon(j2000_day)

    #leap day correction calculation
    day_l = leap_corr(j2000_day)
    #update scale marks position acording to leap day value
    scale.scal(day_l,canvas)

    #sun calculation
    sun_pos_e = sun_anm(j2000_day)
    sun_pos_e = true_an(sun_pos_e)
    sun_pos_j= equ_to_jan(sun_pos_e)

    #moon calculation
    phase = moon_d2 - sun_pos_e
    phase += 1
    phase=(phase * 2 * math.pi)+math.pi/2

    #planets hands calculation

    mercury_pos = rad_to_frac(mercury_87(j2000_day)[0])
    mercury_pos = equ_to_jan(mercury_pos)

    venus_pos = rad_to_frac(venus_87(j2000_day)[0])
    venus_pos = equ_to_jan(venus_pos)

    mars_pos = rad_to_frac(mars_87(j2000_day)[0])
    mars_pos = equ_to_jan(mars_pos)

    jupiter_pos = rad_to_frac(jupiter_87(j2000_day)[0])
    jupiter_pos = equ_to_jan(jupiter_pos)

    saturn_pos = rad_to_frac(saturn_87(j2000_day)[0])
    saturn_pos = equ_to_jan(saturn_pos)

    uranus_pos = rad_to_frac(uranus_87(j2000_day)[0])
    uranus_pos = equ_to_jan(uranus_pos)

    neptune_pos = rad_to_frac(neptune_87(j2000_day)[0])
    neptune_pos = equ_to_jan(neptune_pos)

    #updating hands
    scale.hand(mercury_pos, 3, "#ff00ff", mercury_check)
    scale.hand(venus_pos,3,"#b87838",venus_check)
    scale.hand(mars_pos, 5, "#ff0000",mars_check)
    scale.hand(jupiter_pos,5,"#c29f8d",jupiter_check)
    scale.hand(saturn_pos, 5, "#d8b47c", saturn_check)
    scale.hand(uranus_pos, 5, "#88adb3", uranus_check)
    scale.hand(neptune_pos,5,"#3858e8",neptune_check)
    scale.hand(equ_to_jan(moon_d2), 5, "#ffffff",moon_check)
    scale.hand(sun_pos_j,5,"#ffff00",sun_check)

    day_l=(-day_l/2)+0.5
    leap = canvas_leap_year.create_line(125, 125,
                                  125 + (100) * math.cos(day_l * math.pi),
                                  125 - (100) * math.sin(day_l * math.pi),
                                  width=3, fill="#00ff00")

    arr3.append(canvas_leap_year.create_text(100, 150, text=j2000_day, font=('Arial', 12), fill="#ff78dd"))
    arr3.append(canvas_leap_year.create_text(100, 180, text=days_to_yday(j2000_day), font=('Arial', 12), fill="#ff78dd"))

    scale.text2 = canvas.create_text(xc,
                               yc + r / 2.5,
                               text=moon_d2 * 360,
                               font=('Arial', round(r / 32)),
                               fill="#99ffff")
    scale.text = canvas.create_text(xc,
                              yc + r / 2,
                              text=sun_pos_e * 360,
                              font=('Arial', round(r / 32)),
                              fill="#ffff00")


    arr1,arr2 = phase_m(phase,canvas_moon)
    window.after(30,whi_main)
window.after(1,whi_main)
window.mainloop()
