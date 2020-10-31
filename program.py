from math import factorial

t_work = 10
t_recovery = 0.1
N = 2

problem_intensity = 1/t_work
recovery_intensity = 1/t_recovery

probabilities = []
probabilities.append(1)
for i in range(N):
    probabilities[0] += (factorial(N)/factorial(N-(i+1))*problem_intensity**(i+1)) / (factorial(i+1)*recovery_intensity**(i+1))
probabilities[0] = 1 / probabilities[0]

for i in range(N):
    probabilities.append(probabilities[0] * (problem_intensity**(i+1)*factorial(N)/factorial(N-(i+1))) / (factorial(i+1) * recovery_intensity**(i+1)))
