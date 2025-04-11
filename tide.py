class Tide:
    def __init__(self, threshold=1.5):
        self.threshold = threshold

    def is_high_tide(self, level):
        return level > self.threshold

    def is_low_tide(self, level):
        return level < self.threshold

