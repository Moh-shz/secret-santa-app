# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import platform
import os

if platform.system() == "Windows":
    import winsound


class SecretSantaGUI:
    """Manages the UI and the Secret Santa draw logic."""
    def __init__(self, root):
        self.root = root
        self.root.title("Secret Santa 🎁")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        IMAGE_PATH = os.path.join(BASE_DIR, "assets", "images", "background.png")
        self.image_name = IMAGE_PATH
        
        if not self.load_background():
            return

        self.content_frame = tk.Frame(root, bg='white') 
        self.canvas.create_window(590, 300, window=self.content_frame, width=380, height=320)

        self.setup_ui()

    def load_background(self):
        """Loads and scales the background image to the canvas."""
        try:
            self.bg_image = Image.open(self.image_name)
            self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            
            self.canvas = tk.Canvas(self.root, width=800, height=600, highlightthickness=0)
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
            return True
        except Exception:
            messagebox.showerror("Error", f"Image file '{self.image_name}' not found!")
            self.root.destroy()
            return False

    def setup_ui(self):
        """Initialises labels, entry fields, and action buttons."""
        # 1. Title
        tk.Label(self.content_frame, text="🎄 Friends and Good Vibes 🎄", 
                 font=("Arial", 18, "bold"), bg='white', fg='#d63031').pack(pady=10)
        
        # 2. Instruction Hint
        self.hint_label = tk.Label(self.content_frame, text="Enter names (separated by commas):", 
                 font=("Arial", 11), bg='white')
        self.hint_label.pack(pady=2)
        
        # 3. Entry Box
        self.entry = tk.Text(self.content_frame, width=35, height=3, font=("Arial", 12), 
                             bd=1, relief="solid", padx=10, pady=10)
        self.entry.pack(pady=10)
        self.entry.insert("1.0", "Moh, Alexia, Jay, Rakesh")

        # 4. Start Button
        self.start_btn = tk.Button(self.content_frame, text="Start the Draw", 
                                  command=self.prepare_draw, font=("Arial", 11, "bold"),
                                  bg='#f1c40f', padx=20)
        self.start_btn.pack(pady=15)

        # 5. Status Label (for results and countdown)
        self.status_label = tk.Label(self.content_frame, text="", 
                                    font=("Arial", 14, "bold"), bg='white', 
                                    wraplength=370, justify="center")
        self.status_label.pack(pady=10)

        # 6. Action Button (Ready?)
        self.action_btn = tk.Button(self.content_frame, text="Yes, I'm Ready! 👋", 
                                   command=self.start_countdown, font=("Arial", 12, "bold"))

    def play_beep(self):
        """Plays a notification sound based on the operating system."""
        current_os = platform.system()
        
        try:
            if current_os == "Windows":
                winsound.Beep(1000, 300)
            elif current_os == "Darwin":
                os.system('afplay /System/Library/Sounds/Glass.aiff &')
        except Exception:
            pass

    def prepare_draw(self):
        """Validates input and shuffles names ensuring no self-picks."""
        names = [n.strip() for n in self.entry.get("1.0", "end-1c").split(',') if n.strip()]
        if len(names) < 2:
            messagebox.showwarning("Error", "Please enter at least 2 names!")
            return
        
        receivers = names.copy()
        while True:
            random.shuffle(receivers)
            if all(names[i] != receivers[i] for i in range(len(names))):
                break
        
        self.pairs = list(zip(names, receivers))
        self.current_index = 0
        
        # UI Cleanup to focus on the draw results
        self.start_btn.pack_forget()
        self.entry.pack_forget()
        self.hint_label.pack_forget()
        self.next_person()

    def save_results(self):
        """Logs the final pairs into a text file for record-keeping."""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "secret_santa_results.txt")
            with open(file_path, "w") as f:
                f.write("--- Secret Santa Results ---\n")
                for giver, receiver in self.pairs:
                    f.write(f"{giver} -> {receiver}\n")
            messagebox.showinfo("Saved", "Results saved to 'secret_santa_results.txt'")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save results: {e}")

    def next_person(self):
        """Handles the transition between different participants."""
        if self.current_index < len(self.pairs):
            giver = self.pairs[self.current_index][0]
            self.status_label.config(text=f"Turn: {giver}\nAre you ready to see your person?", fg="#2d3436")
            self.action_btn.pack(pady=10)
        else:
            self.save_results()
            self.status_label.config(text="🎉 Draw Complete! Merry Christmas ✨", fg="#27ae60", font=("Arial", 18))
            self.action_btn.pack_forget()

    def start_countdown(self, count=5):
        """Brief delay to allow the current user to prepare (Privacy measure)."""
        self.action_btn.pack_forget()
        if count > 0:
            self.status_label.config(text=f"Get Ready... {count}", fg="#e17055", font=("Arial", 30, "bold"))
            self.root.after(1000, self.start_countdown, count - 1)
        else:
            self.show_result()

    def show_result(self):
        """Displays the assignment for the current participant."""
        giver, receiver = self.pairs[self.current_index]

        self.status_label.config(font=("Arial", 18, "bold"), 
                                text=f"🎅 {giver}, you are buying for: '{receiver}'! ✨", 
                                fg="#00b894")
        # Auto-advance to the next person after 5 seconds
        self.root.after(5000, self.auto_next)

    def auto_next(self):
        """Logic to increment the index and trigger the next turn."""
        self.play_beep()
        self.action_btn.pack_forget()
        self.current_index += 1
        self.next_person()

if __name__ == "__main__":
    root = tk.Tk()
    app = SecretSantaGUI(root)
    root.mainloop()