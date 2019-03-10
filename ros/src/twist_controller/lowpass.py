
class LowPassFilter(object):
    def __init__(self, tau, ts):
        self.alpha = 1.0 / (tau / ts + 1.0)
        self.beta = tau / ts / (tau / ts + 1.0)

        self.last_val = 0.0
        self.ready = False

    def get(self):
        return self.last_val

    def filter(self, val):
        if self.ready:
            val = self.alpha * val + self.beta * self.last_val
        else:
            self.ready = True

        self.last_val = val
        return val
