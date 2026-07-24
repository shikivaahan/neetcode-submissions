class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_needed = [-1] * len(position)

        for i, pos in enumerate(position):
            time_needed[i] = (target - pos) / speed[i]

        for i in range(len(position)):
            min_idx = i

            for j in range(i + 1, len(position)):

                if position[j] < position[min_idx]:
                    min_idx = j
            position[i], position[min_idx] = position[min_idx], position[i]
            time_needed[i], time_needed[min_idx] = time_needed[min_idx], time_needed[i]

        current_fleet_time = 0
        groups = 0
        
        for i in range(len(position) - 1, -1, -1):
            
            if time_needed[i] > current_fleet_time:
                groups += 1
                current_fleet_time = time_needed[i]
        
        return groups



        