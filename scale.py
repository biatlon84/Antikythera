from tools import *

class Scale_C:
    def __init__(self,canvas) -> None:
        self.array_of_hands = []
        self.canvas=canvas
        self.mesde = [0, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 100]
        self.mes_2 = ["январь", " февраль", " март", "апрель", "май", "июнь", "июль", "август", "    сентябрь", "  октябрь",
                 "ноябрь", "December\n        12", "Ау что-то пошло не так"]
        self.mes = ["January\n     1", "February\n     2", "March\n    3", "April\n  4", "May\n  5", "June\n   6",
               "July\n   7", "August\n   8", "September\n        9", "October\n      10", "November\n      11",
               "December\n        12", "Ау что-то пошло не так"]
        canvas.create_oval([xc - r, yc - r], [xc + r, yc + r], fill="#000000")

        self.text = canvas.create_text(xc, yc + r / 2, text=5, font=('Arial', round(r / 8)), fill="#ff0000")
        self.text2 = canvas.create_text(xc, yc + r / 2, text=5, font=('Arial', round(r/ 8)), fill="#ff0000")

        self.arcy = []


    def line(self,s, i, gap, width, space, color, canvas):
        u = i / (space * 2)
        u = jan_to_equ(u)
        i = true_an(u)
        i = equ_to_jan(i)
        i = i * (space * 2)
        i = -i
        return canvas.create_line(xc + (r - s) * math.cos(i * math.pi / space + math.pi / 2),
                                  yc - (r - s) * math.sin(i * math.pi / space + math.pi / 2),
                                  xc + (r - gap) * math.cos(i * math.pi / space + math.pi / 2),
                                  yc - (r - gap) * math.sin(i * math.pi / space + math.pi / 2),
                                  width=width, fill=color)

    def line_tu(self,s, i, gap, width, space, color):
        i = -i
        return self.canvas.create_line(xc + (r - s) * math.cos(i * math.pi / space + math.pi / 2),
                                  yc - (r - s) * math.sin(i * math.pi / space + math.pi / 2),
                                  xc + (r - gap) * math.cos(i * math.pi / space + math.pi / 2),
                                  yc - (r - gap) * math.sin(i * math.pi / space + math.pi / 2),
                                  width=width, fill=color)

    def hand(self,i, width, color,enable):
        if(enable.get()):
            tempyy=self.canvas.create_line(xc, yc,
                                      xc + (r - 30) * math.sin(i * math.pi * 2 - math.pi * 2),
                                      yc - (r - 30) * math.cos(i * math.pi * 2 + math.pi * 2),
                                      width=width, fill=color)
            self.array_of_hands.append(tempyy)

    def equanox(self):
        i = 0
        while i < 360:
            if (i % 30) == 0:
                self.line(25, i, 45, 3, 360 / 2, '#ffffff', self.canvas)# if you want to add a shift to marks add 0.5 to i
            if (i % 30) == 0:
                self.line_tu(20, i + equinox * 360, 60, 3, 360 / 2, '#ff0202')
            i = i + 1

    def scal(self,leap_y, canvas):
        # arc = []
        i = 0
        scolko = 0
        current_ddd = 31
        yyy = 365
        leap_y -= 0.5
        while i < 365:
            self.arcy.append(self.line(0, i + leap_y, 30, 1, yyy / 2, '#00ffff', canvas))
            if ((i % current_ddd) == 0):
                current_ddd += self.mesde[scolko]
                self.arcy.append(self.line(0, current_ddd + leap_y, 30, 5, yyy / 2, '#00ffff', canvas))
                scolko += 1
            i = i + 1
        # return arc

    def names(self,canvas):
        i = 0
        while i < 12:
            canvas.create_text(xc + (r - 100) * math.cos((i+0.5) * PI / 6 - PI / 2),
                               yc + (r - 100) * math.sin((i+0.5) * PI / 6 - PI / 2),
                               text=self.mes[i], font=('Arial', 20), fill='#ffffff')
            i += 1

    # def ha_v(self):
    #     return self.ha

    def clear(self):
        self.canvas.delete(self.text, self.text2)

        for a in self.array_of_hands:
            self.canvas.delete(a)

        for a in self.arcy:
            self.canvas.delete(a)