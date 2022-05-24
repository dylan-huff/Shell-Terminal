# Shell-Terminal
The purpose of this program was to learn about the command line and bash commands by creating some of the commands and a mock terminal
ourselves. I, Dylan Huff, worked with a classmate, Jordan Bennett, on this project. The list of commands we were instructed to implement
is as follows: cat, cd, chmod, cp, grep, head, history, less, ls, mkdir, mv, pwd, rm, rmdir, sort, tail, wc, who. We also implemented some
flags with these commands, which you can see inside of the function for each command. Because this project was for a class, we only implemented
the commands and flags required by the professor. To immulate a terminal, we used a getch function to capture the key strokes of the user, and 
then used a parser function to break up and interpret the commands and determine if flags were used or not. At the moment, the only required
functionality that is not finished is redirect and pipe.
