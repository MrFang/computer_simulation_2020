from math import factorial
from decimal import localcontext, Decimal
repeated = True
bb = True

while repeated:

    if bb != 0:
        print(
            "Условие:\n"
            "Написать программу оценивающую надежностные характеристики компьютерной системы. Система состоит из\n"
            "N одинаковых и работающих параллельно компьютеров. Известны входные параметры программы: среднее время\n"
            "безотказной работы каждого компьютера t, среднее время восстановления одного компьютера t_в. Требуется\n"
            "расчитать надежность системы: вероятности выхода из строя от 1 до N компьютеров и вероятность\n"
            "безотказной работы. Введите ниже входные параметры."
            )
        N = int(input('Введите количество компьютеров N: '))
        t_work = float(input('Введите среднее время безотказной работы каждого компьютера t: '))
        t_recovery = float(input('Введите среднее время восстановления одного компьютера t_в: '))

        problem_intensity = 1 / t_work
        recovery_intensity = 1 / t_recovery

        probabilities = []
        probabilities.append(1)

        """
            Считаем вероятность P_1
        """
        for i in range(N):
            with localcontext() as ctx:
                ctx.prec = 32
                a = ctx.multiply(
                    ctx.divide(
                        factorial(N),
                        factorial(N - (i + 1))
                    ),
                    ctx.power(
                        Decimal(problem_intensity),
                        i+1
                    )
                )
                b = ctx.multiply(
                    factorial(i+1),
                    ctx.power(
                        Decimal(recovery_intensity),
                        i + 1
                    )
                )
                probabilities[0] += ctx.divide(a, b)

        probabilities[0] = 1 / probabilities[0]

        """
            Считаем вероятности P_2 ... P_(N+1)
        """
        for i in range(N):
            with localcontext() as ctx:
                ctx.prec = 32
                a = ctx.multiply(
                    ctx.power(
                        Decimal(problem_intensity),
                        i+1
                    ),
                    ctx.divide(
                        factorial(N),
                        factorial(N - (i + 1))
                    )
                )
                b = ctx.multiply(
                    factorial(i+1),
                    ctx.power(
                        Decimal(recovery_intensity),
                        i + 1
                    )
                )
                probabilities.append(probabilities[0] * ctx.divide(a, b))

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

        print('Введите 0 - если хотите выйти или любую другую цифру для продолжения')
        bb = int(input())
    else:
        break
