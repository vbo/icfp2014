World description
========
The state of the world is encoded as follows:

A 4-tuple consisting of

1. The map;
    See info in map.md
2. the status of Lambda-Man;
      1. Lambda-Man's vitality;
      2. Lambda-Man's current location, as an (x,y) pair;
      3. Lambda-Man's current direction;
      4. Lambda-Man's remaining number of lives;
      5. Lambda-Man's current score.
3. the status of all the ghosts;
4. the status of fruit at the fruit location.

Direction
  * 0: up;
  * 1: right;
  * 2: down;
  * 3: left.

Ghosts' vitality:
  * 0: standard;
  * 1: fright mode;
  * 2: invisible.
