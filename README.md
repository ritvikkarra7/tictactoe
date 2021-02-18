# tictactoe
An imperfect AI that plays Tic-Tac-Toe with a player


There is no GUI as of yet. The play is conducted in a 2-D list of dimensions 3x3. Each cell is represented by a number from 1-9. This is pictorially represented below :

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
 
So 1 is mapped to board[0][0], 2 is mapped to [0][1], 3: [0][2], 4: [1][0]... and so on.



The computer's move is determined by a set of rules. The following is the hierarchy of move choices for the computer: 
1. If the computer has a winning move, it picks that move 
2. If the player has winning move, it blocks the player from making this move
3. It plays in the center if the center is available (chooses 5)
4. It randomly picks a corner to play in if a corner is available (chooses between 1, 3, 7, and 9)
5. It randomly picks an edge to play in if an edge is available (chooses between 2, 4, 6, 8)
