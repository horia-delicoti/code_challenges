#  How to implement a queue in specific languages.

from collections import deque
from typing import List

def execute(program: List[str]) -> List[int]:
    # initialize a deque representing a queue
    queue = deque()

    for instruction in program:
        if instruction == "peek":
            # print out the first itme in queue if it is not empty
            if queue:
                print(queue[0])
            else:
                print("Queue is empty!")
        elif instruction == "pop":
            # check if queue is empty
            if queue:
                # pop the first item in queue
                queue.popleft()
            else:
                # print message if queue is empty
                print("Queue is empty!")
        else:
            # get the data in the "push" instruction
            data = int(instruction[5:])
            # push data to the end of queue
            queue.append(data)
    
    return queue

if __name__ == '__main__':
    program = [input() for _ in range(int(input()))]
    res = execute(program)
    print(' '.join(map(str, res)))