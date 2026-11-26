import time

class Stats:
    def __init__(self):
        self.kills = 0
        self.mushrooms = 0
        self._start_time = None
        self._elapsed = 0.0

    def start_timer(self):
        self._start_time = time.time()
        self._elapsed = 0.0

    def add_kill(self):
        self.kills += 1

    def add_mushroom(self):
        self.mushrooms += 1

    def all_enemies_dead(self, total):
        return self.kills >= total

    def elapsed_seconds(self):
        if self._start_time is None:
            return self._elapsed
        return time.time() - self._start_time