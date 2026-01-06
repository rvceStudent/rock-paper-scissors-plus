Rock–Paper–Scissors–Plus – AI Game Referee

Overview
This project implements a minimal AI referee for a Rock–Paper–Scissors–Plus game.
The chatbot enforces game rules, validates user actions, tracks game state across
turns, and automatically ends the game after three rounds.

The system is designed to act as a referee rather than a player, ensuring correctness
and rule enforcement throughout the game.

Game Rules Summary
- Best of 3 rounds
- Valid moves: rock, paper, scissors, bomb
- Bomb can be used only once per player
- Bomb beats all other moves
- Invalid input wastes the round
- Game ends automatically after 3 rounds

State Model
The game state is stored in an in-memory dictionary containing:
- Current round number
- User score and bot score
- Bomb usage flags for both players
- (Optionally) round history for display

State persists across turns and is updated only through explicit functions, ensuring
that critical game logic does not live only in the prompt or UI layer.

Agent and Tool Design
The solution separates responsibilities clearly:

- Intent Understanding:
  User actions are captured through UI interactions and mapped to game moves.

- Game Logic:
  Dedicated functions handle move validation, round resolution, and rule enforcement
  (including bomb usage constraints and draw conditions).

- State Management:
  Game state updates (round count, scores, bomb usage) are handled through explicit
  update functions to maintain correctness and clarity.

This separation makes the system easy to reason about and extend.

Tradeoffs
To keep the implementation minimal and focused on state management and rule
enforcement, the bot’s move selection is randomized rather than strategy-based.

Future Improvements
With additional time, the following improvements could be made:
- Smarter bot strategies based on game history
- Unit tests for game logic and state transitions
- Support for multiple consecutive games
- Enhanced UI animations and feedback

Note
An optional Streamlit-based UI was created separately for demonstration purposes.
The submitted version strictly follows the assignment constraints.
