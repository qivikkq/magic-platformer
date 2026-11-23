from game.ui.popup import Popup


class RulesPopup(Popup):
    def __init__(self):
        title = 'Правила'

        text_lines = [
            'Двигайся с помощью клавиш управления',
            'Прыгай, чтобы преодолевать препятствия',
            'Стреляй во врагов',
            'Цель: убей всех врагов!'
        ]

        button_text = 'ИГРАТЬ'

        super().__init__(title, text_lines, button_text)