#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

def load(event):
	try:
		f = open(filename.GetValue(), 'r')
		contents.SetValue(f.read())
	except:
		print 'file unexist, please click saveBtn to Creat it first'

def save(event):
	f = open(filename.GetValue(), 'w')
	f.write(contents.GetValue())
	f.close()

app = wx.App()
win = wx.Frame(None, title = "wxPython-zsy001", size = (410,335)) #窗口左上角pos为(0,0)

loadBtn = wx.Button(win, label = "Open", pos = (225,5), size = (80,25))
loadBtn.Bind(wx.EVT_BUTTON, load)
saveBtn = wx.Button(win, label = "Save", pos = (315,5), size = (80,25))
saveBtn.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(win, pos = (5,5), size = (215,25))
contents = wx.TextCtrl(win, pos = (5,35), size = (390,260), style=wx.TE_MULTILINE | wx.HSCROLL)

win.Show()
app.MainLoop()