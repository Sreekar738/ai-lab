import random
import math

def objective(x):
    return x ** 2


def simulated_annealing(x, temperature, cooling_rate):
    current = x
    best = x
    iteration = 0

    while temperature > 0.1:
        iteration += 1

        # Generate a neighboring solution
        neighbor = current + random.uniform(-1, 1)

        # Calculate change in objective value
        delta = objective(neighbor) - objective(current)

        # Accept a better solution
        if delta < 0:
            current = neighbor

        else:
            # Probability of accepting a worse solution
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current = neighbor

        # Update the best solution
        if objective(current) < objective(best):
            best = current

        # Reduce temperature
        temperature *= cooling_rate

    print("Iterations:", iteration)
    print("Best solution:", round(best, 4))
    print("Minimum value:", round(objective(best), 6))


x = float(input("Enter initial value of x: "))
temperature = float(input("Enter initial temperature: "))
cooling_rate = float(input("Enter cooling rate (0 to 1): "))

if temperature <= 0.1 or not 0 < cooling_rate < 1:
    print("Invalid temperature or cooling rate")
else:
    simulated_annealing(x, temperature, cooling_rate)
