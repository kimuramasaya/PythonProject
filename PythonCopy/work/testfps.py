import time, sys
import Queue
import numpy as np

class fpsCalculator(object):
    def __init__(self, length=5):
        self.times = Queue.LifoQueue()
        self.length = length
        self.fpsHist = []

    def tick_tack(self):
        if self.times.qsize() < self.length:
            self.times.put(time.time())

        elif self.times.qsize() == self.length:
            begin = self.times.get()
            end = time.time()
            self.times.put(end)
            fps = self.length / (end - begin)
            sys.stdout.write("\r FPS: %2.2f " % fps)
            sys.stdout.flush()

            self.fpsHist.append(fps)

    def getFPS(self):
        return np.average(np.array(self.fpsHist[1:]))

fps = fpsCalculator()

while True:
    try:
        fps.tick_tack()
        time.sleep(0.1)
    except KeyboardInterrupt:
        break

print 'average of fps = ', fps.getFPS()
