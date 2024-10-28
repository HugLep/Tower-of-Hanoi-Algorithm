# [IN PROGRESS] Algorithm that solves the Tower of Hanoi

## Progression 
- [X] Allows you to use the game in the terminal, choose the height of the tower and move it as you want while respecting the rules (from the largest to the smallest on each base)
- [ ] Render the graphic visual using Tkinter
- [ ] Create an algorithm that solves the tower without any prior movement from the player
- [ ] Adapt the algorithm so that it is able to solve the tower after the player moves
- [ ] FINISH?

## How the Tower of Hanoi works
![Image of the Tower of Hanoi](https://cdn.kastatic.org/ka-perseus-images/5b5fb2670c9a185b2666637461e40c805fcc9ea5.png)

The Tower of Hanoi is a mathematical logic game invented by French mathematician Édouard Lucas in 1883. The goal is to move a stack of disks, each with a unique diameter, from a starting base to an intermediate base, while respecting certain precise rules. This puzzle is often used to teach the principles of recursion in computer science and problem-solving strategies.

### Rules of the Game

**Three bases and several disks:**
- The starting configuration has three bases or rods, and several disks stacked from largest to smallest on the starting base.

**But:**
- Move the entire stack of disks from the starting base to the destination base.

**Constraints:**
- Only one disk can be moved at a time.
- No disk can be placed on a smaller disk.

### Recursion Principle

Solving the Tower of Hanoi relies on recursion, a method where a complete solution is constructed by solving several similar subproblems. Here is how it works: Splitting the problem: Consider moving 𝑛 n disks from the starting base to the destination base.

Recursive steps:
- Move the 𝑛 − 1 disks from the starting base to the intermediate base.
- Move the largest disk directly to the destination base.
- Move the 𝑛 − 1 disks from the intermediate base to the destination base.

### Solving Strategy

The number of moves needed to solve a Tower of Hanoi with 𝑛 disks is 2^𝑛 − 1. For example, for three disks, it will take at least 7 moves. This formula highlights the rapid growth of the complexity of the game with the increase in the number of disks, each addition of disk doubling the number of moves required.

### Applications and Uses

Beyond entertainment, the Tower of Hanoi is used in computer science to illustrate concepts such as recursion and algorithmic complexity. It also serves as a model for understanding data structures and process management, especially in situations requiring strict ordering.

## Project Progress

### October 28, 2024
- [X] Allows you to use the game in the terminal, choose the height of the tower and move it as you want while respecting the rules (from the largest to the smallest on each base)

![Image of program usage](https://github.com/user-attachments/assets/6fbe7d8d-ab3d-4f7c-840b-6dc976da570e)
