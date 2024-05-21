class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # TODO solve it again
        # Sort the cars based on their starting position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []

        for pos, spd in cars:
            # Calculate the time it takes for each car to reach the target
            time_to_target = (target - pos) / float(spd)
            # Add this car's time to the stack
            stack.append(time_to_target)
            # If the last car in the stack takes less or equal time than the second last, they form a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
