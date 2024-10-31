def calculate_new_position(position, instruction):
    x, y, facing = position
    if instruction in "LR":
        # Format: (current_direction, instruction).
        direction_change = {
            ("N", "L"): "W",
            ("N", "R"): "E",
            ("W", "L"): "S",
            ("W", "R"): "N",
            ("S", "L"): "E",
            ("S", "R"): "W",
            ("E", "L"): "N",
            ("E", "R"): "S",
        }

        return x, y, direction_change[facing, instruction]
    else:  # instruction == "M"
        if facing == "N":
            y += 1
        elif facing == "W":
            x += 1
        elif facing == "S":
            y -= 1
        else:  # "E"
            x -= 1

    return x, y, facing


def do_cycle(start, instructions):
    changes_direction = False
    moves = False
    position = start

    for instruction in instructions:
        if changes_direction == False and instruction in "LR":
            changes_direction = True

        if moves == False and instruction == "G":
            moves = True

        position = calculate_new_position(position, instruction)

    return position, moves, changes_direction


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """

        # Check if returned to origin after 2 cycles.
        # => If the robot has returned to start, then it's True.
        # If not, do 2 more, then if he's at the beginning it's True, else False.
        origin = (0, 0, "N")

        (
            new_position,
            moves,
            changes_direction,
        ) = do_cycle(origin, instructions)

        if not moves:
            return True
        elif not changes_direction:
            return False

        for _ in range(3):
            (
                new_position,
                moves,
                changes_direction,
            ) = do_cycle(new_position, instructions)

            if new_position == origin:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    sol.isRobotBounded("GGLLGG")
