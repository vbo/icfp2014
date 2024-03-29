var MAX_NUM = 100;

function step(ai_state, player_pos) {
    var dir = start_map_walk(player_pos);
    return [dir, ai_state]
}

function start_map_walk(pos) {
    var neighs = get_neighbors(pos);
    var dir0 = 0;
    var dir1 = 0;
    var dir2 = 0;
    var dir3 = 0;
    function store_dir_profit(dir, profit) { // DONE
        if (dir == 0) dir0 += profit;
        if (dir == 1) dir1 += profit;
        if (dir == 2) dir2 += profit;
        if (dir == 3) dir3 += profit;
    }
    function get_max_profit_dir() {
        if (dir0 > dir1) {          //DONE
            if (dir0 > dir2) {          //DONE
                if (dir0 > dir3) {          //DONE
                    return 0;          //DONE
                } else {          //DONE
                    return 3;          //DONE
                }          //DONE
            } else {          //DONE
                if (dir2 > dir3) {          //DONE
                    return 2;          //DONE
                } else {          //DONE
                    return 3;          //DONE
                }          //DONE
            }          //DONE
        } else {          //DONE
            if (dir1 > dir2) {          //DONE
                if (dir1 > dir3) {          //DONE
                    return 1;          //DONE
                } else {          //DONE
                    return 3;          //DONE
                }          //DONE
            } else {          //DONE
                if (dir2 > dir3) {          //DONE
                    return 2;          //DONE
                } else {          //DONE
                    return 3;          //DONE
                }          //DONE
            }          //DONE
        }          //DONE
    }          //DONE
    function determine_neighs_profit(neigh) {
        var profit = get_profit(neigh);
        store_dir_profit(neigh['dir'], profit);
    }

    function map_walk(neighs, wave_num, total_visited) {
        neighs = filter_walkable(neighs); //DONE
        foreach(neighs, determine_neighs_profit); //DONE
        if (total_visited > MAX_NUM) { //DONE
            return; //DONE
        } else { // DONE
            var new_neighs, counter = get_neighbors_of_neighbors(neighs); //DONE
            if (counter > 0) {
                map_walk(new_neighs, wave_num + 1, counter + total_visited); //DONE
            }
        }
    }

    map_walk(neighs, 0); // DONE
    return get_max_profit_dir();
    //TODO: equal profits
}

function filter_walkable(neighs) {

}

step(1, {});

function foreach (list, fn) {

}

function get_profit(neigh) {

}






//function step(ai_state, world) {
//    return most_val_dir(
//        map_walk(
//            world,
//            get_neighbors(world.player.position),
//            0
//        )
//    )
//}

//function map_walk(world, neighbors, num) {
//    var next_wave = get_neighbors_of_neighbors(neighbors);
//    var profits = map_walk(world, next_wave);
//
//
//    var this_dirs = get_neighbors_value(neighbors);
//    if (num > MAX_NUM) return [];
//}

function step(ai_state, world) {
    var point = world['player']['location'];
    var neighbors = get_neighbors(world, point);
    var values = map(neighbors, get_calc_point_value(world, 0));
    // choose most valuable neighbor and go there
}

function get_calc_point_value(world, wave_num) {
    return function (point) { return calc_point_value(world, wave_num); }
}

function calc_point_value(world, point, wave_num) {
    var neighbor_values = [];
    if (wave_num < MAX_NUM) {
        neighbor_values = map(
            get_neighbors(world, point),
            get_calc_point_value(world, wave_num + 1)
        );
    }
    var this_value = get_value(world, point);
    return this_value + sum_values(neighbor_values);
}

function get_neighbors(pos) {
    // pass
}

function get_value(world, point) {
    // pass
}

function sum_values(values) {
    // pass
}

function get_neighbors_value(neighbors) {

}

function get_neighbors_of_neighbors(pos) {
    // pass
}

function most_val_dir(dirs) {
    return reduce(dirs, Math.max, -100500);
}

function reduce(list, fn, acc) {

}

function map(list, fn) {

}

function concat() {

}







