#!/usr/bin/python3

def canUnlockAll(boxes):
    # Create a list to keep track of which boxes are open.
    # Initialize it with the first box (box 0) being open.
    open_boxes = [False] * len(boxes)
    open_boxes[0] = True

    # Create a stack to perform DFS.
    stack = [0]

    while stack:
        current_box = stack.pop()
        
        # Check the keys in the current box.
        for key in boxes[current_box]:
            if not open_boxes[key]:
                # If the key opens a new box, mark it as open and add it to the stack.
                open_boxes[key] = True
                stack.append(key)

    # If all boxes are open, return True; otherwise, return False.
    return all(open_boxes)
