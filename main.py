import math


def input_number(text, minimum, maximum, is_integer=False):
    while True:
        try:
            user_input = input(text).replace(",", ".")

            if is_integer:
                number = int(user_input)
            else:
                number = float(user_input)

        except ValueError:
            print("Ошибка: введите число в правильном формате.")
            continue

        if minimum <= number <= maximum:
            return number
        else:
            print(f"Ошибка: введите число от {minimum} до {maximum}.")


def calculate(V, D, z, Sz, t):
    n = 1000 * V / (math.pi * D)
    Smin = Sz * z * n
    MRR = t * (D / 2) * Smin / 1000
    return n, Smin, MRR


print("Выберите материал:")
print("1 — сталь")
print("2 — алюминий")
print("3 — чугун")

choice = ""

while choice not in ("1", "2", "3"):
    choice = input("Введите 1, 2 или 3: ")

    if choice not in ("1", "2", "3"):
        print("Ошибка: выберите 1, 2 или 3.")


match choice:
    case "1":
        material = "сталь"
        V = 80
    case "2":
        material = "алюминий"
        V = 250
    case "3":
        material = "чугун"
        V = 60


D = input_number("Диаметр фрезы D, мм (5–200): ", 5, 200)
z = input_number("Число зубьев z (1–20): ", 1, 20, True)
Sz = input_number("Подача на зуб Sz, мм/зуб (0.01–0.5): ", 0.01, 0.5)
t = input_number("Глубина резания t, мм (0.1–10): ", 0.1, 10)

n, Smin, MRR = calculate(V, D, z, Sz, t)

if t < 1:
    processing_type = "чистовая"
elif t <= 3:
    processing_type = "получистовая"
else:
    processing_type = "черновая"

print("\nРезультаты:")
print(f"Материал: {material}")
print(f"Скорость резания: {V} м/мин")
print(f"Частота вращения: {n:.2f} об/мин")
print(f"Минутная подача: {Smin:.2f} мм/мин")
print(f"Производительность: {MRR:.2f} см³/мин")
print(f"Тип обработки: {processing_type}")