# Capture Olin - Turn-Based Game

This is a pygame implementation of a two-player turn-based game using the
Model-Controller-View framework. The game is designed to be played on a single
computer, with each player taking turns to make their moves.

## Getting Started

These instructions will get you up and running with a local version of the game.

### Prerequisites

- Python 3.12 or higher
- Pygame You can install the prerequisites using pip:

```bash
pip install pygame
```

Clone the repository to your local machine:

```bash
git clone https://github.com/olincollege/Turn-Based
```

### Running the Game

To run the game, run the following command in your terminal:

```bash
python Game.py
```

### Game Controls

Instructions for the game are displayed on the start screen help section, but
here is a quick summary of the controls:

- Use a mouse or your trackpad to select which Olin building you want to send
  Oliners to and from.
- Use the number keys to select the number of Oliners you want to send(1-9).
- Use the space bar to confirm your selection and send the Oliners.
- Use the escape key to exit the game at any time.

### Game Rules

The game is played on a grid representing Olin buildings. Players take turns
sending Oliners between buildings. Both players will make their choices in how
and where they move their Oliners before the actions of both players occur. This
simultaneous game-dynamic ensures that players have to make predictive moves
based on their opponent. The goal is to control the opponent's home-base
building by sending Oliners to it. Each player has a home-base building that
they begin in and must protect.

Players can send Oliners from one building to another by selecting the source
and destination buildings and specifying the number of Oliners to send. It is
only possible to send Oliners from one building to another if both buildings are
connected. Players can send a maximum of 9 Oliners per round to make sure
players do not stack Oliners and send a massive wave at the end. The game ends
one or both players control each other's home-bases as well as when the time
runs out.

For each controlled building, players get more Oliners to send in the next turn.
These extra Oliners will be spawned in the controlled building at the start of
the next turn.

Every turn, each controlled building of each player will spawn an additional
Oliner. This number will not change throughout the course of the game.

The control of a building is determined by the number of Oliners present in that
building. If a player has more Oliners than the opponent in a building, they
control it. If both players have the same number of Oliners, the building's
possession is decided by who was on the offensive.

There is an overall time limit of 5 minutes for the game. If the time runs out,
the game ends in a draw.

### Running PyTests

To run unit tests, execute the following command in your terminal:

```bash
pytest
```

### Running Pylint

To run Pylint, execute the following command in your terminal:

```bash
./lint_all.sh
```

For the sake of test accuracy, there are some Pylint errors that are ignored.
They are configured to not appear within the .pylintrc file.
