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
  The variable 'winner' is used to store the name of the player who won the game, but 
