'''
made by Famewix
github: https://github.com/Famewix
date: 2/18/2021
'''

import subprocess
import os
import sys
import runpy
try:
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.config import Config
    from kivy.lang import Builder
    from kivy.properties import ObjectProperty
    from kivy.properties import NumericProperty
    from kivy.properties import ListProperty
except ImportError:
    os.system('pip3 install kivy')
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.config import Config
    from kivy.lang import Builder
    from kivy.properties import ObjectProperty
    from kivy.properties import NumericProperty
    from kivy.properties import ListProperty

Builder.load_file('main.kv')
val = 0
class TttGridLayout(Widget):

    one = ObjectProperty(None)
    size_of_font = ObjectProperty(None)
    two = ObjectProperty(None)
    three = ObjectProperty(None)
    four = ObjectProperty(None)
    five = ObjectProperty(None)
    six = ObjectProperty(None)
    seven = ObjectProperty(None)
    eight = ObjectProperty(None)
    nine = ObjectProperty(None)

    # setting the windows size to 600x600
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '600')
    # sets fixed size window
    Config.set('graphics', 'resizable', False)
    # for determining x or o (1 ,2)
    def check_win_lose(self):
        dict_ = {
            11:{
            1: self.one, 2: self.two, 3: self.three
            },
            22:{
            1: self.four, 2: self.five, 3: self.six
            },
            33:{
            1: self.seven, 2: self.eight, 3: self.nine
            }
        }
        all_places = [self.one.text, self.two.text, self.three.text,
                      self.four.text, self.five.text, self.six.text,
                      self.seven.text, self.eight.text, self.nine.text
                      ]
        key_words = [11, 22, 33]
        if '' in all_places:
            # checks row
            for i in key_words:
                if dict_[i][1].text == dict_[i][2].text == dict_[i][3].text :
                    return dict_[i][1].text
            # checks columns
            for index in range(1, 4):
                if dict_[11][index].text == dict_[22][index].text == dict_[33][index].text :
                    return dict_[11][index].text
            # checks corner to corner
            if dict_[11][1].text == dict_[22][2].text == dict_[33][3].text or dict_[11][3].text == dict_[22][2].text == dict_[33][1].text:
                return dict_[11][1].text
        else:
            return 'Draw'

    def return_result(self):
        winner_char = self.check_win_lose()
        with open('winner_player.txt', 'w') as f:
            if winner_char == 'X':
                f.write('Player 1 has won!')
                # subprocess.call("win_app.py", shell=True)
                subprocess.Popen(['python', 'win_app.py'])
                App.get_running_app().stop()
            elif winner_char == 'O':
                f.write('Player 2 has won!')
                subprocess.Popen(['python', 'win_app.py'])
                App.get_running_app().stop()
            elif winner_char == 'Draw':
                f.write("It's a Draw")
                subprocess.Popen(['python', 'win_app.py'])
                App.get_running_app().stop()

    def click(self, index):
        global val
        dict_ = {
            1: self.one, 2: self.two, 3: self.three,
            4: self.four, 5: self.five, 6: self.six,
            7: self.seven, 8: self.eight, 9: self.nine
        }
        pos = dict_[index]
        if pos.text == "":
            val += 1
            if val % 2 != 0:
                turn = 'X'
            elif val % 2 == 0:
                turn = 'O'

            pos.text = turn

            self.return_result()
        else:
            pass


class TTTApp(App):

    fontSize = NumericProperty(80)
    back_color = ListProperty((68/200, 82/200, 97/200, 1))

    # char_color = ListProperty((210/255, 77/255, 87/255, 1))
    # char_color = ListProperty((171/255, 75/255, 112/255, 1))
        

    def build(self):
        layout = TttGridLayout()
        return layout

if __name__ == "__main__":
    TTTApp(title="Tic Tac Toe").run()
