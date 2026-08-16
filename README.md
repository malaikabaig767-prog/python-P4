# 🧠 General Knowledge Quiz

**DecodeLabs Industrial Training Kit — Project 4 (Optional Mastery Phase)**

A command-line quiz game that asks the player 3 general knowledge
questions, tracks their score, and reports the result at the end.
Built to demonstrate **Control Flow** — directing a program's logic
based on user input.

---

## 📋 Overview

The player is asked 3 questions one at a time. For each question,
their typed answer is captured, sanitized, and compared against a
reference answer. A running score is incremented for every correct
answer, and the final score is printed once all questions have been
asked.

This project is intentionally simple on the surface, but under the
hood it models a small **decision engine**: raw human input is
chaotic (inconsistent casing, stray whitespace), so the program must
sanitize it before making a reliable comparison.

## ✨ Features

- **3-question quiz loop** — iterates through a list of question
  dictionaries, asking each one in turn.
- **Input sanitization pipeline** — every answer is passed through
  `.strip().lower()` before comparison, so `"Paris"`, `" paris "`,
  and `"PARIS"` are all accepted as correct.
- **State management** — a single `score` variable (the "score
  vault") persists across the whole quiz. It's only incremented on a
  correct answer; a wrong answer leaves it untouched rather than
  resetting it.
- **Control flow via if/else** — each answer is routed through a
  logic gate that decides whether to increment the score and what
  feedback to print.
- **Clean f-string output** — the final score is displayed with
  aligned formatting (e.g. ` 2/3`).
- **End-of-quiz feedback** — a short message (Perfect / Good effort /
  Better luck next time) based on the final score.

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies — only the Python standard library

## 🚀 Usage

Run the script from the command line:

```bash
python3 quiz_game.py
```

You'll be asked 3 questions in sequence. Type your answer and press
Enter after each prompt. Capitalization and extra spaces don't
matter — the program normalizes your input before checking it.

## 📸 Example

**Input:**

![Input example](screenshots/input.png)

**Output:**

![Output example](screenshots/output.png)

## 🧠 How It Works

The program follows the **Input → Process → Output → Storage (IPOS)**
architecture, repeated once per question:

1. **Ask & Capture (Input)** — `input()` prompts the player and
   captures their raw answer as a string.
2. **Sanitize (Process)** — the raw answer is cleaned with
   `.strip().lower()` to remove accidental whitespace and normalize
   case, so the comparison is case-insensitive and typo-tolerant for
   formatting quirks.
3. **Evaluate (Process)** — the sanitized answer is compared against
   the reference answer using `==`, producing a boolean.
4. **Execute (Output/Storage)** — an `if / else` gate routes the
   boolean result: on `True`, the score vault is incremented
   (`score += 1`) and a success message is printed; on `False`, the
   score is left unchanged and the correct answer is revealed.

After all 3 questions, the final score is printed using an f-string
(`f"{score:>2}/{total}"`) for clean, aligned CLI output.

## 📁 Project Structure

```
General-Knowledge-Quiz/
│
├── quiz_game.py             # Main script
├── README.md                 # This file
└── screenshots/
    ├── input.png              # Example of the input prompts
    └── output.png             # Example of the final results
```

## 🔮 Possible Extensions

- Load questions from an external file (JSON/CSV) instead of a
  hardcoded list
- Add a timer per question
- Support multiple acceptable answers per question (e.g. synonyms)
- Shuffle question order each run
- Track and display a leaderboard across multiple play sessions

---

*Built as part of the DecodeLabs Python Programming Industrial Training Kit (Batch 2026).*
