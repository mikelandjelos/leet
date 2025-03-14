from collections import deque


class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        ready_boxes = deque()
        available_boxes = set()
        extra_keys = set()
        candies_collected = 0

        for box in initialBoxes:
            if status[box] == 1:
                ready_boxes.append(box)
            else:
                available_boxes.add(box)

        while ready_boxes:
            box = ready_boxes.pop()
            candy, new_boxes, new_keys = candies[box], containedBoxes[box], keys[box]

            candies_collected += candy
            extra_keys.update(new_keys)

            # For each new box:
            # if open => processing queue;
            # if closed => store for later;
            for new_box in new_boxes:
                if status[new_box] == 1:
                    ready_boxes.append(new_box)
                else:
                    available_boxes.add(new_box)

            newly_opened_boxes = extra_keys & available_boxes
            for newly_opened_box in newly_opened_boxes:
                ready_boxes.append(newly_opened_box)

            available_boxes -= newly_opened_boxes
            extra_keys -= newly_opened_boxes

        return candies_collected
