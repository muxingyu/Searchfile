#!/usr/bin/evn python
# -*- conding:utf-8 -*-
import os
from tkinter import *

def Search_file():
	search_size = t.get()
	print(type(search_size))
	print(search_size)
	if search_size.isdigit():
		tkMessageBox.showwarning("非数字","非数字")
	else:
		tkMessageBox.showwarning("数字","数字")

	search_path="e:/"
	search_size=104857600
	for root,dirs,files in os.walk(search_path,topdown=False):
		for file in files:
			try:
				if os.path.getsize(os.path.join(root,file))>search_size:
					print (os.path.join(root,file))
			except OSError:
				print(OSError)
				continue

if __name__ == '__main__':
	root = Tk()
	w = Label(root,text="输入查找文件大小:")
	w.pack()
	t = Entry(root)
	t.pack()
	b = Button(root,text="开始查找",command=Search_file)
	b.pack()
	root.mainloop()

