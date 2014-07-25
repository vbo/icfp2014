function main(world, undocumented) {
    // frame size = 2
    // DUM(world.size)
    // push world to data stack
    var get_step = function () {
        // frame size = world.size
        var step = function (last_ai_state, world) {
            // frame size = 2, parent frame size = world.size
            // update world on parent frame using ST
            var new_ai_state = do_ai(last_ai_state, world);
            var move = determine_move(last_ai_state, world);
            return [new_ai_state, move]
        }
    }
    var ai_state = {};
    return [ai_state, step];
}
