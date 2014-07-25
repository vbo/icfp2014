World description
========
The state of the world is encoded as follows:

1. The map;
    See info in map.md
2. the status of Lambda-Man;
      1. Lambda-Man's vitality;
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


World state example (incl. 22x24 map):
[
    [0,
        [
            [0, 2],
            [ [2, 255], 0]
        ]
    ],
    [
        [
            [0, [
                [0, 0],
                [
                    [2, 255],
                    0
                ]
            ]],
            [
                [0, [
                    [0, 1],
                    [
                        [2, 0],
                        0
                    ]
                ]],
                [
                    [0, [
                        [0, 2],
                        [
                            [2, 255],
                            0
                        ]
                    ]],
                    [
                        [1, [
                            [0, 2],
                            0
                        ]],
                        [
                            [12, [7, [
                                [1, 2],
                                [
                                    [0, 0],
                                    0
                                ]
                            ]]],
                            [
                                [0, [
                                    [0, 0],
                                    [
                                        [1, 2],
                                        0
                                    ]
                                ]],
                                [
                                    [0, [
                                        [0, 1],
                                        [
                                            [0, 2],
                                            0
                                        ]
                                    ]],
                                    [
                                        [10, [3, [
                                            [0, 2],
                                            [
                                                [2, 3],
                                                0
                                            ]
                                        ]]],
                                        [
                                            [0, [
                                                [0, 0],
                                                [
                                                    [0, 1],
                                                    0
                                                ]
                                            ]],
                                            [
                                                [13, [0, 0]],
                                                [
                                                    [13, [3, 0]],
                                                    [
                                                        [13, [6, 0]],
                                                        [
                                                            [1, [
                                                                [1, 1],
                                                                0
                                                            ]],
                                                            [
                                                                [14, 0],
                                                                0
                                                            ]
                                                        ]
                                                    ]
                                                ]
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ]
                ]
            ]
        ],
        [
            [
                [0, [
                    [0, 0],
                    [
                        [2, 255],
                        0
                    ]
                ]],
                [
                    [0, [
                        [0, 1],
                        [
                            [2, 0],
                            0
                        ]
                    ]],
                    [
                        [0, [
                            [0, 2],
                            [
                                [2, 255],
                                0
                            ]
                        ]],
                        [
                            [1, [
                                [0, 2],
                                0
                            ]],
                            [
                                [12, [7, [
                                    [1, 2],
                                    [
                                        [0, 0],
                                        0
                                    ]
                                ]]],
                                [
                                    [0, [
                                        [0, 0],
                                        [
                                            [1, 2],
                                            0
                                        ]
                                    ]],
                                    [
                                        [0, [
                                            [0, 1],
                                            [
                                                [0, 2],
                                                0
                                            ]
                                        ]],
                                        [
                                            [10, [3, [
                                                [0, 2],
                                                [
                                                    [2, 3],
                                                    0
                                                ]
                                            ]]],
                                            [
                                                [0, [
                                                    [0, 0],
                                                    [
                                                        [0, 1],
                                                        0
                                                    ]
                                                ]],
                                                [
                                                    [13, [0, 0]],
                                                    [
                                                        [13, [3, 0]],
                                                        [
                                                            [13, [6, 0]],
                                                            [
                                                                [1, [
                                                                    [1, 1],
                                                                    0
                                                                ]],
                                                                [
                                                                    [14, 0],
                                                                    0
                                                                ]
                                                            ]
                                                        ]
                                                    ]
                                                ]
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ]
                ]
            ],
            [
                [
                    [0, [
                        [0, 0],
                        [
                            [2, 255],
                            0
                        ]
                    ]],
                    [
                        [0, [
                            [0, 1],
                            [
                                [2, 0],
                                0
                            ]
                        ]],
                        [
                            [0, [
                                [0, 2],
                                [
                                    [2, 255],
                                    0
                                ]
                            ]],
                            [
                                [1, [
                                    [0, 2],
                                    0
                                ]],
                                [
                                    [12, [7, [
                                        [1, 2],
                                        [
                                            [0, 0],
                                            0
                                        ]
                                    ]]],
                                    [
                                        [0, [
                                            [0, 0],
                                            [
                                                [1, 2],
                                                0
                                            ]
                                        ]],
                                        [
                                            [0, [
                                                [0, 1],
                                                [
                                                    [0, 2],
                                                    0
                                                ]
                                            ]],
                                            [
                                                [10, [3, [
                                                    [0, 2],
                                                    [
                                                        [2, 3],
                                                        0
                                                    ]
                                                ]]],
                                                [
                                                    [0, [
                                                        [0, 0],
                                                        [
                                                            [0, 1],
                                                            0
                                                        ]
                                                    ]],
                                                    [
                                                        [13, [0, 0]],
                                                        [
                                                            [13, [3, 0]],
                                                            [
                                                                [13, [6, 0]],
                                                                [
                                                                    [1, [
                                                                        [1, 1],
                                                                        0
                                                                    ]],
                                                                    [
                                                                        [14, 0],
                                                                        0
                                                                    ]
                                                                ]
                                                            ]
                                                        ]
                                                    ]
                                                ]
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ]
                ],
                0
            ]
        ]
    ]
]
