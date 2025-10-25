# ⏳ Countdown Timer

A simple and interactive Python project that counts down to a user-specified time.  
The program allows the user to input the countdown duration in hours, minutes, and seconds — and displays the timer in a digital-clock format until it reaches **"Time up!"**

---

## 🚀 Features
- Accepts user input in the format `HH MM SS`
- Displays the countdown in a digital style (e.g., `00:05:12`)
- Automatically shows **"Time up!"** when the countdown finishes
- Beginner-friendly and written in pure Python

---

## 🛠️ Built With
- **Language:** Python 🐍
- **IDE:** PyCharm 

---

## 💻 How to Run the Project
Since GitHub doesn’t execute Python code directly, follow these steps to run the countdown timer on your local machine:

1. Make sure you have **Python** installed.  
   You can check by running:
   ```bash
   python --version
2. Download or clone this repository.
3. Open the project in PyCharm or VS Code.
4. Run the Python file


🧩 How It Works

1. The program prompts the user to enter a time in the format:

HH MM SS


Example:

0 1 30 or 00 01 30

(which means 1 minute and 30 seconds)
📝 Note:
No matter how you enter the time — for example, 00 01 30 or simply 0 1 30 —
the program automatically converts it to a digital format like 00:01:30.

2. The countdown begins immediately after input, displaying the remaining time in a digital style until it reaches zero.

3. Once the countdown finishes, the program displays:

Time up!

🧠 Challenges Faced and Solutions
🕐 Challenge 1: Displaying the timer in a digital clock format

Problem: The countdown initially didn’t look like a digital timer.
Solution: After researching, I discovered the use of the Python format() function with the {:02d} format specifier, which ensures each number is displayed as two digits (e.g., 05 instead of 5).

⌨️ Challenge 2: Getting all time inputs on a single line

Problem: Initially, I was taking inputs for hours, minutes, and seconds separately.
Solution: I learned about the split() function and tuple unpacking. Using them together allowed me to take all three inputs in one line


👩🏽‍💻 Author

Sonia-Chima

⭐ Acknowledgments

Thanks to the Python documentation and online resources for helping me solve formatting and input-handling challenges.
