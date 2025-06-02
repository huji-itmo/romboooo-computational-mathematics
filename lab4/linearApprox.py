import numpy as np

def linealApprox(x,y) -> dict[str,float]:
    print("")
    print("--- Линейная ---")
    n = len(x)
    sumX = sum(x)
    sumY = sum(y)
    sumX2 = sum(X**2 for X in x)
    sumXY = sum(X * Y for X, Y in zip(x, y))
    A = np.array([[sumX2, sumX], [sumX, n]])
    B = np.array([sumXY, sumY])
    try:
        solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Система уравнений вырождена, решение не существует")
        return None
    if solution is not None:
        a0, a1 = solution
    else:
        print("ошибка в вычислении матрицы")

    def polinomModel(a0, a1, x):
        return a0*x + a1
    
    fi = []
    ei = []
    S = 0
    fiAverage = 0
    for i in range(n):
        fi.append(polinomModel(a0, a1, x[i]))
        ei.append(fi[i] - y[i])
        S += ei[i] ** 2
        fiAverage += fi[i]
    delta = np.sqrt(S / n)
    fiAverage = 1 / n * sum(fi)
    ss_total = sum((yi - fiAverage)**2 for yi in y)
    R2 = 1 - (S / ss_total)
    x_mean = sumX / n
    y_mean = sumY / n
    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denominator = np.sqrt(sum((xi - x_mean)**2 for xi in x) * sum((yi - y_mean)**2 for yi in y))
    r = numerator / denominator

    print(f"Формула: y = {a0:.6f}x + {a1:.6f}")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: 𝜹 = {delta:.6f}")
    print(f"Достоверность аппроксимации: R² = {R2:.6f}")
    print(f"Коэффицент корреляции: r = {r:.6f}")

    if R2 >= 0.95:
        print("R2 >= 0.95 -> Высокая точность аппроксимации, модель хорошо описывает явление")
    elif 0.75 <= R2 < 0.95:
        print("0.75 <= R2 < 0.95 -> Удовлетворительная аппроксимация, модель в целом адекватно описывает явление")
    elif 0.5 <= R2 < 0.75:
        print("0.5 <= R2 < 0.75 -> Слабая аппроксимация, модель слабо описывает явление")
    elif 0.5 > R2:
        print("0.5 > R2 -> Точность аппроксимации недостаточна и модель требует изменения")

    if r == 0:
        print("r = 0 -> Cвязь между переменными отсутствует")
    elif abs(r) < 0.3:
        print("|r| < 0.3 -> Cвязь между переменными слабая")
    elif 0.5 > abs(r) >= 0.3:
        print("0.5 > |r| >= 0.3 -> Cвязь между переменными умеренная")
    elif 0.7 > abs(r) >= 0.5:
        print("0.7 > |r| >= 0.5 -> Cвязь между переменными заметная")
    elif 0.9 > abs(r) >= 0.7:
        print("0.9 > |r| >= 0.5 -> Cвязь между переменными высокая")
    elif 1 > abs(r) >= 0.9:
        print("1 > |r| >= 0.9 -> Cвязь между переменными весьма высокая")
    elif abs(r) == 1:
        print("r = +-1 -> Cтрогая линейная функциональная зависимость в зависимости от знака коэффициента a")
    return {
        "a0": a0,
        "a1": a1,
        "S": S,
        "delta": delta,
        "R2": R2,
        "r": r
    }