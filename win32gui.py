import win32gui

#getting mouse position
flags, hcursor, (x, y) = win32gui.GetCursorInfo()
