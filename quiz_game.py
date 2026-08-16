"""
General Knowledge Quiz
------------------------
DecodeLabs Industrial Training Kit - Project 4 (Optional Mastery Phase)

Asks the player 3 general knowledge questions, keeps a running score,
and reports the final result. Built to demonstrate Control Flow
(if/elif/else), state management (an accumulator variable), and
input sanitization.

Key concepts demonstrated:
    - if / elif / else branching (Control Flow)
    - State management with a persistent "score vault" variable
    - Input sanitization pipeline: .strip().lower()
    - f-string output formatting
"""

# Each question is a dictionary containing the prompt and the
# sanitized reference answer to compare against.
QUESTIONS = [
    {
        "prompt": "What is the capital of France?",
        "answer": "paris",
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "answer": "mars",
    },
    {
        "prompt": "What is the largest ocean on Earth?",
        "answer": "pacific ocean",
    },
]


def sanitize(raw_input: str) -> str:
    """
    Step 2: Sanitize
    Applies the filter pipeline: .strip().lower()
    Removes leading/trailing whitespace and normalizes case so that
    "Paris", " paris ", and "PARIS" are all treated as equivalent.
    """
    return raw_input.strip().lower()


def ask_question(question_number: int, question: dict) -> bool:
    """
    Step 1: Ask & Capture, Step 3: Evaluate
    Prompts the user with a single question, sanitizes their answer,
    and returns True if it matches the reference answer.
    """
    print(f"\nQuestion {question_number}: {question['prompt']}")
    raw_answer = input("Your answer: ")
    user_answer = sanitize(raw_answer)

    return user_answer == question["answer"]


def run_quiz() -> int:
    """
    The Repeatable Question Block, run once per question.
    Step 4: Execute — routes through an if/else gate to trigger the
    score increment (or not) and print feedback for each question.

    Returns the final score (state is only updated on success; a
    wrong answer leaves the score vault untouched).
    """
    score = 0  # State Initialization — the "score vault"

    for i, question in enumerate(QUESTIONS, start=1):
        is_correct = ask_question(i, question)

        # The Logic Gate: routes execution based on a boolean check
        if is_correct:
            score += 1  # Increment only on success
            print("Correct! ✅")
        else:
            # Failure case: no operation on score — state is
            # intentionally maintained, not reset.
            print(f"Incorrect. The correct answer was '{question['answer'].title()}'. ❌")

    return score


def main():
    print("=" * 50)
    print("   DecodeLabs General Knowledge Quiz")
    print("=" * 50)
    print(f"You will be asked {len(QUESTIONS)} questions. Good luck!")

    score = run_quiz()
    total = len(QUESTIONS)

    print("\n" + "=" * 50)
    print(f"Quiz complete! Your final score: {score:>2}/{total}")

    # Simple feedback branching based on the final score
    if score == total:
        print("Perfect score!")
    elif score >= total / 2:
        print("Good effort!")
    else:
        print("Better luck next time!")
    print("=" * 50)


if __name__ == "__main__":
    main()
