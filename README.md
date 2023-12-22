# Terminal based Chess in Python.
#### Video Demo:  <URL HERE>
#### Description:
  I represented the chessboard as a list of lists (each sublist represents each line of the chessboard). 
Each element of a sublist is a dictionary that represents a square in the chessboard.
The dictionary contains the piece in the square (if there is not a piece in the square, it's represented as 'NONE'),
the player the piece belongs to (if there isn't a piece in the square, it's also represented as 'NONE') and
if the piece was moved or not (only for pawns, as a pawn's behavior changes depending on whether it had already been moved or not).

  To move a piece from position X to position Y you only need to digit 'X Y' when the program prompts you with the message 'Your move: '.
The spaces in your input are ignored, so digiting 'XY' and 'X          Y' have no difference whatsoever.
A position in the chessboard is represented as a combination of a letter (A - H) and a number (1 - 8).
I coded it to consider both letter-number and number-letter as correct, so A1 is equal to 1A
(there's also no difference between uppercase and lowercase letters, so A1 = 1A = 1a = a1).
I wanted to let the users free to use whichever way they think it's better to use.

  A vast majority of the code is just the program checking if the user's move is invalid
(this all is needed to ensure the move was a valid one).
I coded a function for every type of piece, because they all have different behaviors.
Every function named as a type of piece is used to check the validity of a move made by this specific type of piece
(so a function named 'rook' checks the validity of a move made by a rook).
Obviously, only one of these function is used every turn for each player
(the queen function actually uses the rook or the bishop function because the behavior of a queen is equal to the behavior of a rook or a bishop).

  The chessboard outputed in the terminal is always colored. I created a funtion 'colorize' to be able to color strings with every color I wanted.
The chessboard is colored as a black and white grid (not actually black and white, but a dark and light color).
I made a function to return if, given the coordinates of a square (its i and j), it needs to be colored with a light color
(it will return false if it needs to be colored with a dark color).
At beggining, I wanted to put the corresponding color as an element of the square dictionary, 
but, when a piece moves, the program switches the dictionary of the piece and the dictionary of the destined position
(if the destined position has a piece from the enemy, the program switches the dictionary of the piece and an empty dictionary, because the enemy's piece was eaten).
Because of this, I thought it was better to code the color system as a separated part from the square dictionary.

  The main game happens in a while loop in the main function. The while loops always checks the variable 'winner' to see if someone won.
The variable 'winner' is used to store the name of the player who won the game, but while there's no winer, the variable is set as 'NONE'.
Each iteration checks if the variable is different than 'NONE' and, if so, it ends the game and announces the winner.

  In the actual game, it is not possible to actually eat the opponent's king, only putting it at checkmate.
It also is not possible to move your king to a position in which the king is in check.
I didn't get attached to these kind of strict rules of actual chess, so the game simply ends when the king of one of the players gets eaten.
I didn't implement checkmate, as it would be a very complicated mechanic to implement, and, 
althrough a very iconic part of the game, it wouldn't affect too much the gameplay
(as for one to be able to eat the opponent's king, it usually means that the king was already in check).

  It would also be a good ideia to prompt first for the piece the player wants to move, calculate all the possible square this specific piece may move to, 
show them to the players, and, only after that, prompt the player for the square the piece is to be moved to.
With this method, it would be a tad easier to implement checkmate (for checkmate, it would need to analyse all the possible movements of each of the opponent's pieces)
and it would also be more user-friendly for people that don't know very much the movements of each piece.
I just choose my method to prioritize the quickness of the game.

  Also, it's important to note that, at one point, I used the new match case statement that was introduced in Python 3.10.
If you have a version of python prior to 3.10, you may change this part of the code to an if else statement and it will work just fine
(happily, the match case statement I used was very small and simple, I just wanted to test it out).
