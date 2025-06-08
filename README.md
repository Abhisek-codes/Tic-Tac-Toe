# 🎮 Tic Tac Toe Game with Smart AI (PyQt5 + Minimax)

This is a fully-featured Tic Tac Toe game written in Python using a clean **3-tier architecture**:
- **Data Layer (`dal.py`)** – board state management
- **Business Logic Layer (`bll.py`)** – game rules and Minimax AI
- **UI Layer (`ui.py`)** – graphical interface built with PyQt5

---

## ✨ Features

- ✅ Player vs Player & Player vs AI modes
- 🧠 Smart AI using Minimax algorithm (unbeatable)
- 🎯 Score tracking for both players
- 🖼️ GUI with icons (❌ / ⭕)
- 🛠️ Reset & Quit buttons
- 📁 Cleanly separated into logical components

---

## 🧠 AI: Minimax Strategy

The AI evaluates every possible outcome using the Minimax algorithm:
- Maximizes its own winning chances (`+1`)
- Minimizes the human's chance of winning (`-1`)
- Ensures a draw if it can’t win (`0`)

---

## 📦 Requirements

- Python 3.7+
- PyQt5

Install:
```bash
pip install PyQt5

## 🚀 Run Locally

```bash

python ui.py