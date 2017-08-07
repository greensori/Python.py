import TKinter
import datetime as dtime

def caldate():
    #calculating between entry1() and entry2() date
    if len(Entry1.get()) == 8 and len(Entry2.get()) == 8:
        print "cal date module"
        sdate = Entry1.get()
        edate = Entry2.get()
        sdate = dtime.date(int(sdate[:4]), int(sdate[4:6]), int(sdate[6:8]))
        edate = dtime.date(int(edate[:4]), int(edate[4:6]), int(edate[6:8]))
        delta = edate - sdate
        delta = delta + dtime.timedelta(1)
        print delta.days
    #calculating after entry2() date
    if len(Entry1.get()) == 8 and len(Entry2.get()) < 8:
        sdate = Entry1.get()
        sdate = dtime.date(int(sdate[:4]), int(sdate[4:6]), int(sdate[6:8]))
        afterday = sdate + dtime.timedelta(int(Entry2.get()) - 1)
        print afterday
    return
  
        
App = Tkinter.Tk()
App.title("Testsample")

Entry1 = Tkinter.Entry(App, width = 22)
Entry1.grid(row = 0, column = 0)
Entry2 = Tkinter.Entry(App, width = 22)
Entry2.grid(row = 1, column = 0)
Button1 = Tkinter.Button(App, text = 'date', width = 22, command = caldate)
Button1.grid(row=0,column=0)
