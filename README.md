# 🎅🏼 Secret Santa GUI Generator

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey)
![GUI](https://img.shields.io/badge/UI-Tkinter-green)

A desktop application built with Python and Tkinter to automate your Secret Santa lucky draw. It features a clean user interface, privacy-focused countdowns, and automated pair generation.

---

## ✨ Features

- **Smart Matching:** Automatically ensures that no one is assigned to themselves.

- **Privacy Guard:** Includes a 5-second countdown between turns to allow participants to switch places privately.

- **Cross-Platform Audio:** Plays notification sounds on Windows and macOS when a turn is complete.

- **Results Logging:** Automatically exports the final pairings to a `.txt` file for the organiser.

- **Custom UI:** Supports a custom background image for a festive holiday feel.

---

## 📸 Preview

![App Screenshot](assets/images/screenshot.png)

---

## 🛠 Requirements

* **Python:** 3.9 or higher
* **External Libraries:** `Pillow` (tested on 10.2.0)
* **OS:** macOS, Windows
---

## 🚀 Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/Moh-shz/secret-santa-app.git
cd secret-santa-app
```

2. Install the required dependency:
```bash
pip install Pillow
```

3. Run the Application:
```bash
python src/SecretSanta.py
```

---

## 📝 How to Use

1. Enter Names: Type all participant names separated by commas.

2. Start Draw: Click "Start the Draw" to shuffle the names.

3. Reveal: Participants take turns at the computer. Each person clicks "Ready," waits for the countdown, and sees their assigned recipient for 5 seconds.

4. Save: Once finished, the pairings are saved to `secret_santa_results.txt.

---

## 🛠️ Project Structure

```
Secret-Santa-App/
├── assets/
│   ├── images/
│   │   ├── background.png		# UI Background image 
│   │   ├── screenshot.jpg
│   │   └── icon.ico
│   └── demo/
│       └── secret_santa_results.txt	# Demo 
├── src/
│   └── SecretSanta.py			# The main Python script 
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📦 Download for macOS
You can download the standalone **Application Bundle** for macOS (Apple Silicon) from the Releases page:

➡️ https://github.com/Moh-shz/secret-santa-app/releases

---

## 👤 Author

**Mohammad Sharzehei**
Data Science
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/msharzehei) 
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat&logo=Kaggle&logoColor=white)](https://www.kaggle.com/mohammadsharzehei)