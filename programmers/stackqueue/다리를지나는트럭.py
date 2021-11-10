from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait_trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    arrived = []
    bridge_truck_count = 0
    bridge_weight_sum = 0
    while True:
        if bridge_truck_count < bridge_length and wait_trucks and bridge_weight_sum + wait_trucks[0] <= weight:            
            bridge[-1] = wait_trucks.popleft()
            bridge_truck_count += 1
            bridge_weight_sum += bridge[-1]
        if bridge[0] != 0:
            bridge_weight_sum -= bridge[0]
            bridge_truck_count -= 1
            arrived.append(bridge.popleft())
            bridge.append(0)
        else:
            bridge.popleft()
            bridge.append(0)
        answer +=1
        if arrived == truck_weights: break
    return answer + 1

print(solution(2,	10,	[7,4,5,6]))
print(solution(100,	100,	[10]))
print(solution(100,	100,	[10,10,10,10,10,10,10,10,10,10]))