#!/usr/bin/evn python
# -*- conding:utf-8 -*-
import os
from tkinter import *
from tkinter import messagebox

# class Main_windows:
# 	root = Tk()
# 	root.wm_title('查找文件')
# 	root.geometry("400x300+300+100")
# 	root.resizable(False,False)
# 	w = Label(root,text="输入查找文件大小:")
# 	w.pack()
# 	t = Entry(root)
# 	t.pack()
# 	b = Button(root,text="开始查找",command=Search_file)
# 	b.pack()
# 	text1 = Text(root)
# 	text1.pack()
# 	root.mainloop()

def is_number(s):
	if s=='':
		messagebox.showwarning("空","空")
		return False
	elif s.isdigit():
		messagebox.showwarning("数字","数字")
		return True
	else:
		messagebox.showwarning("非数字","非数字")
		return False

def Search_file():
	#search_size = t.get()
	#print(type(search_size))
	#print(search_size)
	file_size = int(t.get())
	search_path="e:/"
	#search_size=104857600
	for root,dirs,files in os.walk(search_path,topdown=False):
		for file in files:
			try:
				if os.path.getsize(os.path.join(root,file))>file_size:
					print (os.path.join(root,file))
					test1.insert(END,os.path.join(root,file))
			except OSError:
				print(OSError)
				continue



if __name__ == '__main__':
	root = Tk()
	root.wm_title('查找文件')
	root.geometry("400x300+300+100")
	root.resizable(False,False)
	w = Label(root,text="输入查找文件大小:")
	w.pack()
	t = Entry(root)
	t.pack()
	b = Button(root,text="开始查找",command=Search_file)
	b.pack()
	text1 = Text(root)
	text1.pack()
	root.mainloop()
	#print(search_size)
	#if is_number(search_size):
	#	Search_file(search_size)


