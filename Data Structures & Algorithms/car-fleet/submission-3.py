class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = []
        stack = []

        for pos, vel in cars:
            times.append(((target - pos) / vel))
        
        for time in times:
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
        