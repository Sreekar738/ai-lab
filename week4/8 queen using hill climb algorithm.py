import random

def calculate_cost(state):
   
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_best_neighbor(state):
  
    n = len(state)
    best_state = list(state)
    best_cost = calculate_cost(state)
    
    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row == original_row:
                continue
            
            neighbor = list(state)
            neighbor[col] = row
            cost = calculate_cost(neighbor)
            
            if cost < best_cost:
                best_cost = cost
                best_state = neighbor
                
    return best_state, best_cost

def hill_climbing_8_queens():
    
    restarts = 0
    steps = 0
    
    current_state = [random.randint(0, 7) for _ in range(8)]
    current_cost = calculate_cost(current_state)
    
    while current_cost > 0:
        steps += 1
        neighbor_state, neighbor_cost = get_best_neighbor(current_state)
        
        if neighbor_cost >= current_cost:
            restarts += 1
            current_state = [random.randint(0, 7) for _ in range(8)]
            current_cost = calculate_cost(current_state)
        else:
            current_state = neighbor_state
            current_cost = neighbor_cost
            
    return current_state, restarts, steps

def print_board(state):
  
    n = len(state)
    for r in range(n):
        row_str = ""
        for c in range(n):
            if state[c] == r:
                row_str += " Q "
            else:
                row_str += " . "
        print(row_str)
    print()

if __name__ == "__main__":
    print("Solving 8 Queens Problem using Hill Climbing...")
    solution, restarts, steps = hill_climbing_8_queens()
    
    print(f"\nSolution Found!")
    print(f"State (Column-to-Row mapping): {solution}")
    print(f"Total Restarts: {restarts}")
    print(f"Total Steps: {steps}\n")
    
    print("Chessboard Visualization:")
    print_board(solution)
