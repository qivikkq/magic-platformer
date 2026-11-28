from game.ui.popup import Popup


class ResultPopup(Popup):
    """Окно с результатами прохождения уровня."""

    def __init__(self, kills, mushrooms, seconds):
        title = 'Результаты'

        minutes = seconds // 60
        remaining_seconds = seconds % 60

        text_lines = [
            f'Убито врагов: {kills}',
            f'Собрано грибов: {mushrooms}',
            f'Время прохождения: {minutes:02}:{remaining_seconds:02}'
        ]

        button_text = 'ВЫХОД'

        super().__init__(title, text_lines, button_text)