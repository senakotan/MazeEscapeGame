
# 🧩 Maze Exploration Game 🎮

This is a text-based maze exploration game developed in Python, where the player navigates through a maze from a starting point to an endpoint while encountering various obstacles and collecting bonuses. The player aims to collect the highest score while avoiding obstacles and completing the maze.

## Game Description

The game takes place on a 2D character matrix (15x15) that represents the structure of the maze. The player starts at the point marked 'B' and must navigate to the endpoint marked 'E'. Along the way, the player will encounter walls, mines, and other obstacles, which can be bypassed using specific bonuses.

## Features

- *Maze Representation*: The maze is represented by a 2D grid where each character in the matrix has a special meaning.
- *Movement*: Players can move up, down, left, or right, but cannot move diagonally or in other ways.
- *Bonuses*: Collect bonuses to assist in navigating obstacles and reducing moves.
- *Obstacles*: Encounter walls and mines which require specific bonuses to bypass.
- *Dynamic Maze*: Every 5 steps, the bonuses and mines move randomly, adding an element of unpredictability to the game.

## Maze Layout

The maze is represented by a 15x15 matrix, with each character indicating different elements of the maze:

- \# : Wall (Impassable, unless removed with 'R' bonus)
- . : Path (Passable)
- ! : Mine (Explodes unless defused with 'F' bonus)
- T : Teleportation bonus (Allows the player to teleport to a previously visited path)
- R : Bonus to remove a wall at the current location
- H : Bonus to reduce the number of moves
- F : Bonus to defuse a mine

## Player Commands

The player can move through the maze using the following commands:

- W : Move Up
- A : Move Left
- S : Move Down
- D : Move Right

The player cannot move diagonally or in any other way. If a move is invalid (e.g., trying to move through a wall without the 'R' bonus), the game will notify the player.

## Obstacles

### Walls (#)

- If the player encounters a wall, they need the 'R' bonus to remove it. Without the 'R' bonus, the player cannot pass.

### Mines (!)

- If the player encounters a mine, they need the 'F' bonus to defuse it. If the player doesn't have the 'F' bonus, the mine explodes, turning into a path (.), and the player loses 5 moves.

## Bonuses

The game has four types of bonuses that the player can collect and use:

1. *Teleportation Bonus (T)*: Allows the player to teleport to a previously visited (x, y) coordinate, as long as the location is not a wall (#) or a mine (!).
2. *Remove Obstacle Bonus (R)*: Allows the player to remove a wall (#) at their current location and continue moving.
3. *Move Reduction Bonus (H)*: Reduces the number of moves by 2 (but cannot go negative).
4. *Mine Defusing Bonus (F)*: Allows the player to defuse a mine (!) and pass through that location.

## Game Logic

### 1. Maze Setup

The maze is predefined in a 15x15 grid. The player starts at a point marked 'B' and the goal is to reach the endpoint marked 'E'. The maze structure cannot be modified, and the player must navigate through it while collecting bonuses and avoiding obstacles.

### 2. Bonus and Mine Movement

Every 5 steps, all bonuses and mines in the maze will move to new, random positions. These items will not be placed where there are walls (#) or mines (! for bonuses) and will not overlap with other bonuses or mines.

### 3. Game Loop

- The game loop continues until the player reaches the endpoint E or the game ends due to a failure (e.g., stepping into an explosive mine or running out of moves).
- After every step, the game will display the current state of the maze, along with the player's remaining moves, collected bonuses, and any encountered obstacles.

### 4. User Interface

The player will be prompted to input a move (W, A, S, D) at each step. The game will check the player's input and provide feedback if the move is valid or if an obstacle is encountered.

---


## How to Play

1. Start by pressing Enter to begin the game.
2. Use the following commands to move:
   - W : Move Up
   - A : Move Left
   - S : Move Down
   - D : Move Right
3. Keep an eye on the bonuses and obstacles.
4. Try to reach the endpoint E while avoiding mines and walls.
5. Enjoy the adventure and try to collect the highest score!



---
