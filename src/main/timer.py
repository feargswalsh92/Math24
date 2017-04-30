
from tkinter import *
import time

totalTime = 5

class Timer(Frame):
    """ implements a stopwatch frame widget """
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        """ Make th time label. """
        l = Label(self, textvariable=self.timestr, fg='green', bg='black', width=10, height=2)
        l.config(font=('Courier', 32))
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        """ Update label with elapsed time """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elapsed):
        """ Set time string to Minutes:Seconds.Tenths """
        seconds = int(totalTime - elapsed)
        hundredths = int((totalTime-elapsed-seconds)*10)
        if (seconds<0 or hundredths < 0):
            self.after_cancel(self._timer)
            self._running = 0
            seconds = 0
            hundredths = 0
            self.timestr.set('%02d.%01d' % (seconds, hundredths))
        self.timestr.set('%02d.%01d' % (seconds, hundredths))


    def Start(self):
        """ Start stopwatch only if not already running """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        """ stop the stopwatch if not already stopped """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        """ Reset the stopwatch """
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

        
def main():
    root = Tk()
    root.configure(background='black')
    sw = Timer(root)
    sw.pack(side=TOP)

    Button(root, text='Start', command=sw.Start).pack(side=LEFT)
    Button(root, text='Stop', command=sw.Stop).pack(side=LEFT)
    Button(root, text='Reset', command=sw.Reset).pack(side=LEFT)
    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)

    root.mainloop()

    
if __name__ == '__main__':
    main()


