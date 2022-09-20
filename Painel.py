from tkinter import *
from Save import *
from start import *
import re

ponto = [float(save_open()[2])]

def interface ():
    root = Tk()
    root.geometry("400x600")
    root.title("DTS_LV")

    ###########################################

    frame1 = Frame(root, bg="white", height=30, width=350)
    frame1.grid(column=0, row=0, padx=0, pady=0, columnspan=3)

    frame2 = Frame(root, bg="grey", height=200, width=400)
    frame2.grid(column=0, row=2, padx=0, pady=0, columnspan=3, rowspan=3)

    frame3 = Frame(root, bg="white", height=140, width=400)
    frame3.grid(column=0, row=6, padx=0, pady=0, columnspan=3, rowspan=3)

    #############################################

    titulo = Label(root, text="MENU -  LabView DTS")
    titulo.grid(column=0, row=0, padx=0, pady=20, columnspan=3)

    #############################################
    # Fibra entry box
    R1 = 1

    def temp_text_fibra(e):
        textbox.delete(0, "end")

    def save_values_fibra():
        if textbox.get() == '':
            pass
        else:
            save_write(15, textbox.get())

    txt1 = Label(root, text="Comprimento da Fibra Atual:")
    txt1.grid(column=0, row=R1, padx=0, pady=0, sticky='E')

    textbox = Entry(root, bg="white", width=24, borderwidth=2)
    textbox.grid(column=1, row=R1, padx=0, pady=30)

    textbox.insert(0, save_open()[7])
    #textbox.bind("<FocusIn>", temp_text_fibra)

    #############################################
    # Posição na fibra entry box
    R2 = 2

    def temp_text_point(e):
        textbox.delete(0, "end")

    def save_values_point():
        if textbox.get() == '':
            pass
        else:
            save_write(5, textbox2.get())

    txt2 = Label(root, text="Ponto especifico da fibra: ")
    txt2.grid(column=0, row=R2, padx=0, pady=0,sticky='E')

    textbox2 = Entry(root, bg="white", width=24, borderwidth=2)
    textbox2.insert(0, save_open()[2])
    textbox2.grid(column=1, row=R2, padx=0, pady=0)
   #textbox2.bind("<FocusIn>", temp_text_point)

    #############################################
    # Bara da posição inicial
    R3 = 3

    def save_values_ini():
        save_write(1, ini.get())

    txt3 = Label(root, text="Ponto inicial:   ")
    txt3.grid(column=0, row=R3, padx=0, pady=0, sticky='E')

    ini = Scale(root, from_=0, to=(save_open()[7]), tickinterval=10,length=150,orient=HORIZONTAL)
    ini.grid(column=1, row=R3, padx=0, pady=0)

    ini.set(float(save_open()[0]))

    #############################################
    # Bara da posição final
    R4 = 4

    def save_values_fim():
        get_pref = (fim.get())
        save_write(3,get_pref)

    txt4 = Label(root, text="Ponto final:   ")
    txt4.grid(column=0, row=R4, padx=0, pady=0, sticky='E')

    fim = Scale(root, from_=0, to=(save_open()[7]), tickinterval=10,length=150,orient=HORIZONTAL)
    fim.grid(column=1, row=R4, padx=0, pady=0)

    fim.set(float(save_open()[1]))

    #############################################
    # Bara do passo eixo X
    R5 = 5

    def save_values_step():
        get_pref = (step.get())
        save_write(7,get_pref)

    txt5 = Label(root, text="Step temporal do grafico (min):")
    txt5.grid(column=0, row=R5, padx=0, pady=0,sticky='W')

    step = Scale(root, from_=0, to=10, tickinterval=10,length=150,orient=HORIZONTAL)
    step.grid(column=1, row=R5, padx=0, pady=0)
    step.set(float(save_open()[3]))


    #############################################
    def button_dts(preference,R,C):

        txt = Label(root, text="Grafico DTS")
        txt.grid(column=1, row=R, padx=0, pady=0,sticky='W')

        def toggle():
            position = ((preference * 2) + 1)
            if var.get() == "ON":
                save_write(position, "ON")

            else:
                save_write(position, "OFF")

        status = re.sub("\n", "", (save_open()[preference]))
        print(status)

        var = StringVar()
        var.set(str(status))


        buton = Checkbutton(root, onvalue="ON", offvalue="OFF", width=4, indicatoron=False,
                                variable=var, textvariable=var,
                                selectcolor="green", background="red",
                                command=toggle)

        status = re.sub("\n", "", (save_open()[preference]))
        var.set(status)

        buton.grid(column=C, row=R, padx=0, pady=10)

    #############################################
    def button_lv(preference,R,C):

        txt = Label(root, text="Grafico Temperatura LabView")
        txt.grid(column=1, row=R, padx=0, pady=0,sticky='W')

        def toggle():
            position = ((preference * 2) + 1)
            if var.get() == "ON":
                save_write(position, "ON")

            else:
                save_write(position, "OFF")

        status = re.sub("\n", "", (save_open()[preference]))
        print(status)

        var = StringVar()
        var.set(str(status))


        buton = Checkbutton(root, onvalue="ON", offvalue="OFF", width=4, indicatoron=False,
                                variable=var, textvariable=var,
                                selectcolor="green", background="red",
                                command=toggle)

        status = re.sub("\n", "", (save_open()[preference]))
        var.set(status)

        buton.grid(column=C, row=R, padx=0, pady=10)

    #############################################
    def button_vasao(preference,R,C):

        txt = Label(root, text="Grafico Vasão de Vazamento")
        txt.grid(column=1, row=R, padx=0, pady=0,sticky='W')

        def toggle():
            position = ((preference * 2) + 1)
            if var.get() == "ON":
                save_write(position, "ON")
            else:
                save_write(position, "OFF")

        status = re.sub("\n", "", (save_open()[preference]))
        print(status)

        var = StringVar()
        var.set(str(status))


        buton = Checkbutton(root, onvalue="ON", offvalue="OFF", width=4, indicatoron=False,
                                variable=var, textvariable=var,
                                selectcolor="green", background="red",
                                command=toggle)

        status = re.sub("\n", "", (save_open()[preference]))
        var.set(status)

        buton.grid(column=C, row=R, padx=0, pady=10)

    #############################################
    if save_open()[8] == '0':
        print(save_open()[8])
        switch_variable = StringVar()
        switch_variable.set("point")

    if save_open()[8] == '1':
        print(save_open()[8])
        switch_variable = StringVar()
        switch_variable.set("range")

    def switch_button():

        def point_switch():
            print('point')
            del ponto[:]
            ponto.append(0)
            save_write(17, 0)

        def range_switch():
            print('range')
            del ponto[:]
            ponto.append(float(save_open()[2]))
            save_write(17, 1)

        point = Radiobutton(root, text="", variable=switch_variable,
                            indicatoron=False, value="point", width=4,
                            selectcolor="green", background="light gray", command=point_switch)
        point.grid(column=2, row=2, padx=0, pady=0)

        range = Radiobutton(root, text="", variable=switch_variable,
                            indicatoron=False, value="range", width=4,
                            selectcolor="green", background="light gray", command=range_switch)
        range.grid(column=2, row=3, padx=0, pady=0, rowspan=2)

    #############################################
    def Save_button(R):
        def DATA():
            save_values_fibra()
            save_values_point()
            save_values_ini()
            save_values_fim()
            save_values_step()
            print('save')

        save = Button(root, text='  SAVE  ', command=DATA)
        save.grid(column=0, row=R, padx=0, pady=20)

    #############################################
    def Start_button(R):
        pref_save = Button(root, text='  START ', command=lambda:start_dts_lv(float(ponto[0])))
        pref_save.grid(column=1, row=R, padx=0, pady=20)

    #################################################################
    button_dts(4,6,0)
    button_lv(5,7,0)
    button_vasao(6,8,0)
    switch_button()

    Save_button(9)
    Start_button(9)

    #############################################
    root.mainloop()