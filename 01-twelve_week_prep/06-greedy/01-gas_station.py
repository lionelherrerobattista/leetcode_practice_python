from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # verify if a solution exists:
        if sum(gas) < sum(cost):
            return -1 
        total = 0
        answer = 0 # starting position
        # iterate over every position
        for i in range(len(gas)):
            # check the difference
            total += (gas[i] - cost[i])

            if total < 0: # greedy, if < 0 position will not work
                total = 0
                answer = i + 1
        return answer


    # brute force O(n^2)
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     gas_tank = 0
    #     starting_station = 0
    #     total_stations = len(gas)

    #     if len(gas) == 1 or len(cost) == 1:
    #         if gas[0] >= cost[0]:
    #             return 0
    #         else:
    #             return -1

    #     # check rout cost
    #     while starting_station < total_stations:
            
    #         # fill gas
    #         gas_tank = gas[starting_station]

    #         for next_station_index in range(starting_station + 1, len(cost)):
    #             # travel to the other station
    #             gas_tank -= cost[next_station_index - 1] # cost in i - 1
    #             # check if enough gas
    #             if gas_tank < 0:
    #                 break
    #             # if enough gas, fill tank
    #             gas_tank += gas[next_station_index]

    #         # cover rest of circle
    #         if next_station_index == len(cost) - 1 or starting_station == len(cost) - 1:
    #             for next_station_index in range(0, starting_station + 1): # include starting
    #                 # travel to the other station
    #                 gas_tank -= cost[next_station_index - 1]  # cost in i - 1
    #                 # check if enough gas
    #                 if gas_tank < 0:
    #                     break
    #                 # if enough gas, fill tank
    #                 gas_tank += gas[next_station_index]

    #         if next_station_index == starting_station and gas_tank - cost[starting_station] > 0: # check gas difference
    #             return starting_station
    #         # try next station
    #         starting_station += 1
    #     return -1
    
solution = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(solution.canCompleteCircuit(gas, cost))
gas = [2,3,4]
cost = [3,4,3]
print(solution.canCompleteCircuit(gas, cost))
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(solution.canCompleteCircuit(gas, cost))
