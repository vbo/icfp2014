World description
========
The state of the world is encoded as follows:

1. The map;
    See info in map.md
2. the status of Lambda-Man;
      1. Lambda-Man's vitality (power pill effect);
      2. Lambda-Man's current location, as an (x,y) pair;
      3. Lambda-Man's current direction;
      4. Lambda-Man's remaining number of lives;
      5. Lambda-Man's current score.
3. the status of all the ghosts;
      1. the ghost's vitality
          * 0: standard;
          * 1: fright mode;
          * 2: invisible.
      2. the ghost's current location, as an (x,y) pair
      3. the ghost's current direction
4. the status of fruit at the fruit location.
  * 0: no fruit present;
  * n > 0: fruit present: the number of game ticks remaining while the
           fruit will will be present.

Direction
  * 0: up;
  * 1: right;
  * 2: down;
  * 3: left.


World state (
(
    (
        0,          //vitality
        (
            (1, 1), //location
            (2,     //direction down
                (3, //remaining number of lives
                0)  //current score
            )
        )
     ),
     (
        0, //empty array of ghosts
        0 //empty array of fruits
     )
)
