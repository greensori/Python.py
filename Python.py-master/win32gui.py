import win32gui

#getting mouse position
flags, hcursor, (x, y) = win32gui.GetCursorInfo()

#getting foreground window title name
wname = win32gui
wname.GetWindowText (wname.GetForegroundWindow())
