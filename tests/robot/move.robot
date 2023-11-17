*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.\n\nhttps://github.com/level-up-program/team-11-super7-e904776a/blob/main/tests/robot/images/20231117_085027.jpg?raw=true
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     4             4             1                     NORTH         4           3           2
Move North on the board (bounce)    1             1             5                     NORTH         1           0           6
Move East on the board (bounce)     9             5             6                     EAST          9           5           7
Move South on the board (bounce)    3             9             20                    SOUTH         3           9          21
Move West on the board (bounce)     0             5             8                     WEST          0           5           9
Move North on the board             2             2             3                     NORTH         2           1           4           
Move East on the board              3             5             8                     EAST          4           5           9
Move South on the board             7             8            10                     SOUTH         7           9           11
Move West on the board              2             6             3                     WEST          1           6           4   

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}