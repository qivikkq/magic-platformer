import time


class Stats:
    """Статистика прохождения уровня."""

    def __init__(self):
        self.kills = 0
        self.mushrooms = 0
        self.start_time = None

    def start_timer(self):
        """Запускает таймер прохождения уровня."""
        self.start_time = time.time()

    def add_kill(self):
        """Увеличивает количество убитых врагов."""
        self.kills += 1

    def add_mushroom(self):
        """Увеличивает количество собранных грибов."""
        self.mushrooms += 1

    def all_enemies_dead(self, total):
        """Проверяет, все ли враги убиты."""
        return self.kills >= total

    def elapsed_seconds(self):
        """Возвращает время прохождения в секундах."""
        if self.start_time is None:
            return 0

        return int(time.time() - self.start_time)
