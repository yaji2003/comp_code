def can_complete_circuit(gas, cost):
    n = len(gas)
    
    total_gas = 0
    current_gas = 0
    start_station = 0

    for i in range(n):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        # If we run out of gas at station i, reset the starting station to the next station
        if current_gas < 0:
            current_gas = 0
            start_station = i + 1

    # If the total gas is non-negative, a solution exists
    if total_gas >= 0:
        return start_station
    else:
        return -1

gas=[]
cost=[]
n=int(input("enter the number station"))
for i in range(n):
    g=int(input("gas :"))
    gas.append(g)
for i in range(n):
    c=int(input("cost :"))
    cost.append(c)


start_index = can_complete_circuit(gas, cost)

if start_index != -1:
    print(f"You can start from station {start_index} to complete the circular tour.")
else:
    print("No solution exists.")
