import tkinter as tk
from tkinter import ttk
from character import Warrior, Mage, Dice


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Warrior")

        self.character_1 = Warrior("Tom", 20, 8, 3, Dice(6))
        self.character_2 = Mage("Helen", 20, 8, 3, Dice(6))

        self.character_frame_1 = ttk.Frame(root)
        self.character_frame_1.pack(side=tk.LEFT, padx=10, pady=10)
        self.character_frame_2 = ttk.Frame(root)
        self.character_frame_2.pack(side=tk.RIGHT, padx=10, pady=10)

        self.label_1 = ttk.Label(self.character_frame_1,
                                 text=f"{self.character_1.get_name()} (Warrior)")
        self.label_1.pack()
        self.label_2 = ttk.Label(self.character_frame_2,
                                 text=f"{self.character_2.get_name()} (Mage)")
        self.label_2.pack()

        self.health_bar_1 = ttk.Progressbar(
            self.character_frame_1, length=150, mode="determinate", maximum=self.character_1._max_health)
        self.health_bar_1.pack()
        self.health_bar_2 = ttk.Progressbar(
            self.character_frame_2, length=150, mode="determinate", maximum=self.character_2._max_health)
        self.health_bar_2.pack()

        self.message_text = tk.Text(root, height=10, width=40)
        self.message_text.pack()

        self.update_labels()
        self.bottom_frame = ttk.Frame(root)
        self.bottom_frame.pack(side=tk.BOTTOM, pady=10)

        self.attack_button = ttk.Button(
            self.bottom_frame, text="Attaquer", command=self.attack)
        self.attack_button.pack(side=tk.LEFT, padx=10)
        self.quit_button = ttk.Button(
            self.bottom_frame, text="Quitter", command=root.quit)
        self.quit_button.pack(side=tk.RIGHT, padx=10)

    def check_game_over(self):
        if not self.character_1.is_alive() or not self.character_2.is_alive():
            self.attack_button.config(state=tk.DISABLED)
            if not self.character_1.is_alive():
                winner = self.character_2.get_name()
            else:
                winner = self.character_1.get_name()
            self.message_text.insert(
                tk.END, f"Le jeu est terminé, {winner} a gagné !")

    def attack(self):
        self.character_1.attack(self.character_2)
        self.character_2.attack(self.character_1)
        self.update_labels()
        self.check_game_over()

    def update_labels(self):
        self.health_bar_1['value'] = self.character_1._health
        self.health_bar_2['value'] = self.character_2._health
        self.message_text.delete("1.0", tk.END)
        if self.character_1._health < self.character_1._max_health or self.character_2._health < self.character_2._max_health:
            self.message_text.insert(tk.END, f"{self.character_1.get_name()} attaque {
                self.character_2.get_name()}!\n")
        self.message_text.insert(tk.END, f"{self.character_1.get_name()} a {
            self.character_1._health} hp\n")

        self.message_text.insert(tk.END, f"{self.character_2.get_name()} a {
            self.character_2._health} hp\n")


if __name__ == "__main__":
    root = tk.Tk()
    game = GUI(root)
    root.mainloop()
