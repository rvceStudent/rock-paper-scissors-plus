import tkinter as tk
import random

# -----------------------------
# GAME STATE
# -----------------------------
def init_state():
    return {
        "round": 1,
        "user_score": 0,
        "bot_score": 0,
        "user_bomb_used": False,
        "bot_bomb_used": False
    }

game_state = init_state()

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

# -----------------------------
# LOGIC TOOLS
# -----------------------------
def validate_move(move):
    if move not in VALID_MOVES:
        return False, "Invalid move ❌"
    if move == "bomb" and game_state["user_bomb_used"]:
        return False, "Bomb already used 💣"
    return True, move

def bot_choose_move():
    if not game_state["bot_bomb_used"]:
        return random.choice(VALID_MOVES)
    return random.choice(["rock", "paper", "scissors"])

def resolve_round(user, bot):
    if user == bot:
        return "draw"
    if user == "bomb":
        return "user"
    if bot == "bomb":
        return "bot"

    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    return "user" if rules[user] == bot else "bot"

def update_state(winner, user_move, bot_move):
    if user_move == "bomb":
        game_state["user_bomb_used"] = True
        bomb_btn.config(state=tk.DISABLED)

    if bot_move == "bomb":
        game_state["bot_bomb_used"] = True

    if winner == "user":
        game_state["user_score"] += 1
    elif winner == "bot":
        game_state["bot_score"] += 1

    game_state["round"] += 1

# -----------------------------
# UI HELPERS
# -----------------------------
def round_progress():
    filled = "● " * (game_state["round"] - 1)
    empty = "○ " * (3 - (game_state["round"] - 1))
    progress_label.config(text=f"Round Progress: {filled}{empty}")

def emoji_result(winner):
    return {
        "user": "🎉 You win this round!",
        "bot": "🤖 Bot wins this round!",
        "draw": "🤝 It's a draw!"
    }[winner]

# -----------------------------
# GAME HANDLER
# -----------------------------
def play(move):
    if game_state["round"] > 3:
        return

    valid, result = validate_move(move)
    if not valid:
        output.set(result + " (Round wasted)")
        game_state["round"] += 1
        round_progress()
        check_game_end()
        return

    bot_move = bot_choose_move()
    winner = resolve_round(move, bot_move)
    update_state(winner, move, bot_move)

    text = f"""
Round {game_state['round'] - 1}
You played: {move}
Bot played: {bot_move}

{emoji_result(winner)}

Score → You: {game_state['user_score']} | Bot: {game_state['bot_score']}
"""
    output.set(text)

    round_progress()
    check_game_end()

def check_game_end():
    if game_state["round"] > 3:
        if game_state["user_score"] > game_state["bot_score"]:
            final = "🏆 FINAL RESULT: YOU WIN!"
        elif game_state["bot_score"] > game_state["user_score"]:
            final = "🤖 FINAL RESULT: BOT WINS!"
        else:
            final = "⚖ FINAL RESULT: DRAW!"

        output.set(output.get() + f"\n\n{final}")
        for btn in buttons:
            btn.config(state=tk.DISABLED)

# -----------------------------
# RESTART GAME
# -----------------------------
def restart_game():
    global game_state
    game_state = init_state()

    output.set("New game started! Make your move 🎮")
    bomb_btn.config(state=tk.NORMAL)

    for btn in buttons:
        btn.config(state=tk.NORMAL)

    round_progress()

# -----------------------------
# UI SETUP
# -----------------------------
root = tk.Tk()
root.title("Rock–Paper–Scissors–Plus")
root.geometry("440x480")
root.resizable(False, False)

tk.Label(root, text="🎮 Rock–Paper–Scissors–Plus",
         font=("Helvetica", 16, "bold")).pack(pady=8)

tk.Label(root, text="Best of 3 | Bomb usable once",
         font=("Helvetica", 10)).pack()

progress_label = tk.Label(root, font=("Helvetica", 10))
progress_label.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

buttons = []

for move in ["rock", "paper", "scissors"]:
    btn = tk.Button(
        frame,
        text=move.capitalize(),
        width=10,
        command=lambda m=move: play(m)
    )
    btn.pack(side=tk.LEFT, padx=5)
    buttons.append(btn)

bomb_btn = tk.Button(
    root,
    text="💣 Bomb",
    width=18,
    bg="red",
    fg="white",
    command=lambda: play("bomb")
)
bomb_btn.pack(pady=5)
buttons.append(bomb_btn)

restart_btn = tk.Button(
    root,
    text="🔄 Restart Game",
    width=18,
    command=restart_game
)
restart_btn.pack(pady=5)

output = tk.StringVar()
output.set("Click a move to start the game 🎯")

tk.Label(
    root,
    textvariable=output,
    justify="left",
    font=("Courier", 10),
    wraplength=400
).pack(pady=10)

round_progress()
root.mainloop()
