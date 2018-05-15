import tkinter
import random
from collections import namedtuple



class SimonGame:

    Button = namedtuple("Button", "color alt_color x y")
    BUTTONS_DATA = [Button("yellow", "yellow3", 50, 70),
                    Button("blue", "medium blue", 145, 70),
                    Button("red", "red3", 50, 165),
                    Button("green", "dark green", 145, 165)]

    def __init__ (self, buttons_data=BUTTONS_DATA ):


        self.base = tkinter.Tk()
        self.frame = tkinter.Frame(self.base, bg="black", width="300", height="325")


        self.score = 0
        self.score_label = self.place_label(50, 35, "Score:")
        self.score_val = self.place_label(90, 35, self.score)

        self.best = 0
        self.best_label = self.place_label(175, 35, "Best:")
        self.best_val = self.place_label(208, 35, self.best)

        self.start = tkinter.Button(self.base, bd="0", text="Start and Level up!", command=self.show_sequence)
        self.start.place(x=125, y=35)

        self.sequence = []
        self.user_sequence = []

        self.buttons_data = buttons_data
        self.buttons = [self.create_button(*button) for button in self.buttons_data]

        self.frame.pack()
        self.base.resizable(False, False)
        self.base.mainloop()



    def place_label(self, x, y, text, fg="white", bg="orange"):
        label = tkinter.Label(self.base, bg=bg, fg=fg, text=text)
        label.place(x=x, y=y)
        return label

    def click_factory(self, button, color, alt_color):
        def click():
            button.configure(activebackground=alt_color)
            button.after(500, lambda: button.configure(activebackground=color))
            self.user_sequence.append(color)
            self.check_sequence()
        return click

    def create_button(self, color, alt_color, x, y):
        button = tkinter.Button(self.base, bd="0", highlightthickness="0",
                           width="14", height="7", activebackground=color,
                           bg=alt_color)
        button['command'] = self.click_factory(button, color, alt_color)
        button.place(x=x, y=y)
        return button

    def show_sequence(self):
        self.reset_gui()
        for _ in range(self.score + 1):
            i = random.randrange(len(self.buttons))
            button = self.buttons[i]
            button_data = self.buttons_data[i]
            button.configure(bg=button_data.color)
            button.after(750, lambda: button.configure(bg=button_data.alt_color))
            self.sequence.append(button_data.color)
        print (self.sequence)

    def check_sequence(self):
        if self.sequence == self.user_sequence:
            self.score += 1
            self.best = max(self.best, self.score)
            self.reset_gui()
        elif not self.sequence[:len(self.user_sequence)] == self.user_sequence:
            self.score = 0
            self.reset_gui()

    def reset_gui(self):
        self.sequence = []
        self.user_sequence = []
        for button, data in zip(self.buttons, self.buttons_data):
            button.configure(bg=data.alt_color, activebackground=data.color)
        self.best_val.configure(text=self.best)
        self.score_val.configure(text=self.score)

if __name__ == "__main__":
    game = SimonGame()
