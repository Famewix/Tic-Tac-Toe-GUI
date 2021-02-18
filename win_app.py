import subprocess
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class WinnerMessageApp(App):
    # width and height = 500x400
    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '400')
    # fixed window size
    Config.set('graphics', 'resizable', False)

    # to restart game
    def restart_click(self, index):
        self.get_running_app().stop()
        subprocess.Popen(['python', 'main.py'])

    def build(self):
        layout = BoxLayout()
        layout.orientation = 'vertical'

        layout.spacing = 15
        layout.padding = 15
        # reading file for the winner (Player1 or Player 2)
        with open('winner_player.txt', 'r') as f:
            txt = f.read()
        text = Label(text=txt, font_size=20)
        layout.add_widget(text)

        restart = Button(text='Restart', on_press=self.restart_click, pos_hint={'center_x': 0.5}, size_hint=(.7, .5), font_size=15)
        layout.add_widget(restart)

        exit_btn = Button(text='Exit', on_press=lambda index: quit(), pos_hint={'center_x': 0.5}, size_hint=(.7, .5), font_size=15)
        layout.add_widget(exit_btn)

        return layout


if __name__ == "__main__":
    WinnerMessageApp(title="Winner").run()