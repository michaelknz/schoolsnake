import time

class Timersm:
    def __init__(self,timecol):
        self.timecol=timecol
        self.last_t=time.clock()

    def Update(self):
        cur_t=time.clock()
        self.timecol-=(cur_t-self.last_t)
        self.last_t=cur_t