from math import factorial

print(
    "Условие: \n "
    "Написать программу оценивающую надежностные характеристики компьютерной системы. Система состоит из \n"
    "N одинаковых и работающих параллельно компьютеров. Известны входные параметры программы: среднее время \n"
    "безотказной работы каждого компьютера t, среднее время восстановления одного компьютера t_в. Требуется \n"
    "расчитать надежность системы: вероятности выхода из строя от 1 до N компьютеров и вероятность \n"
    "безотказной работы. Введите ниже входные параметры."
    )
N = int(input('Введите количество компьютеров N: '))
t_work = float(input('Введите среднее время безотказной работы каждого компьютера t: '))
t_recovery = float(input('Введите среднее время восстановления одного компьютера t_в: '))

problem_intensity = 1 / t_work
recovery_intensity = 1 / t_recovery

probabilities = []
probabilities.append(1)

for idx in range(N):
    probabilities[0] += (factorial(N) / factorial(N - (idx + 1)) * problem_intensity ** (idx + 1)) / (
            factorial(idx + 1) * recovery_intensity ** (idx + 1))
probabilities[0] = 1 / probabilities[0]

for idx in range(N):
    probabilities.append(probabilities[0] * (problem_intensity ** (idx + 1) * factorial(N) / factorial(N - (idx + 1))) / (
            factorial(idx + 1) * recovery_intensity ** (idx + 1)))

print('Результаты расчета надежности системы:')
for idx, value in enumerate(probabilities):
    if idx == 0:
        print('Вероятность безотказной работы: ')
        print(str(value) + '\n')
    elif idx < (N + 1):
        if (str(idx).endswith(str(11)) != 1) and str(idx).endswith(str(1)):
            print('Вероятность выхода из строя ' + str(idx) + ' компьютера: ')
        else:
            print('Вероятность выхода из строя ' + str(idx) + ' компьютеров: ')
        print(str(value) + '\n')
