from tkinter import*
from random import randint

#main window
mainw = Tk()
mainw.title('Password Generator')
mainw.iconbitmap()
mainw.geometry("500x600")
mainw.configure(bg = '#fff')
mainw.resizable(False,False)

def gen_pass():
	out_box.delete(0, END)

	pass_len = int(in_box1.get())
	pass_format = int(p_form.get())

	g_pass = ''

	#
	if pass_format == 0:
		for x in range(pass_len):
			g_pass += chr(randint(33,126))
	elif pass_format == 1:
		for x in range(pass_len):
			stock = randint(1,2)
			if stock == 1:
				g_pass += chr(randint(48,57))
			elif stock == 2:
				g_pass += chr(randint(65,90))
			elif stock == 2:
				g_pass += chr(randint(97,122))
	elif pass_format == 2:
		for x in range(pass_len):
			stock = randint(1,2)
			if stock == 1:
				g_pass += chr(randint(65,90))
			elif stock == 2:
				g_pass += chr(randint(97,122))

	out_box.insert(0, g_pass)

#copy to clipboard
def copy_pass():
	mainw.clipboard_clear()
	mainw.clipboard_append(out_box.get())

#reset data
def clear_everything():
	in_box1.delete(0, END)
	out_box.delete(0, END)

#password generator image
title_img = PhotoImage(file = './Assets/PG.png')
Label(mainw, image = title_img, bg = 'white', width = 480).pack(pady = 20)
Label(mainw, text = "BY: PEROCHE, JOHN MARK P. (BSCS 1-3)", font = ("Roboto", 7), bg = 'white', width = 480).pack(pady = 1)
Frame(mainw, width = 200, height = 1, bg = 'black').place(x = 150, y = 108)

#password size label
num_char = LabelFrame(mainw, text="Enter the number of characters", font = ("Montserrat", 13, 'bold'), fg = '#57a1f8', bg = 'white')
num_char.pack(pady = 50)

#password size container
in_box1 = Entry(num_char,font = ("Roboto", 13), bd = 2, bg = 'white')
in_box1.pack(pady = 20, padx = 20)

#format radiobuttons
p_form = IntVar()
first_c = Radiobutton(mainw,text = 'Letters Only', font = ("Montserrat", 10), variable = p_form, value = 2, command = format, bg = '#fff').pack(anchor = CENTER)
second_c = Radiobutton(mainw,text = 'Combination of Letters and Numbers', font = ("Montserrat", 10), variable = p_form, value = 1, command = format, bg = '#fff').pack(anchor = CENTER)
third_c = Radiobutton(mainw,text = 'Recommended (Letters, Numbers & Characters)', font = ("Montserrat", 10), variable = p_form, value = 0, command = format, bg = '#fff').pack(anchor = CENTER)

choice_box = Label(mainw)
choice_box.pack(pady = 1)

#passwords output container
out_box = Entry(mainw, text='', font = ("Roboto", 24), bd = 0, bg = 'white')
out_box.pack(pady = 20)
Frame(mainw,width = 380, height = 2, bg = 'black').place(x = 60, y = 462)

#button container
b_frame = Frame(mainw, bg = 'white')
b_frame.pack(pady = 20)

#generate password container
button1 = Button(b_frame, text = 'Generate Password', width = '15', height = '2', cursor = 'hand2' , border = 0, bg = '#57a1f8', fg = 'white', command = gen_pass)
button1.grid(row = 0, column = 0, padx = 10)

#copy to clipboard button
button2 = Button(b_frame, text = 'Copy to Clipboard', width = '15', height = '2', cursor = 'hand2' , border = 0, bg = '#57a1f8', fg = 'white', command = copy_pass)
button2.grid(row = 0, column = 1, padx = 10)

#clear button
button2 = Button(b_frame, text = 'Clear', width = '15', height = '2', cursor = 'hand2' ,border = 0, bg = '#57a1f8', fg = 'white', command = clear_everything)
button2.grid(row = 0, column = 2, padx = 10)


mainw.mainloop()