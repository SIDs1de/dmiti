from src.natural import Natural

def main():
    print("=== Демонстрация работы с натуральными числами ===")

    # Примеры чисел
    a = Natural([1, 2, 3])   # 123
    b = Natural([9, 9, 9])   # 999

    print(f"a = {a}, b = {b}")

    # === Проверка сравнения (COM_NN_D) ===
    print("\n--- Сравнение ---")
    print(f"a ? b → {a.COM_NN_D(b)} (0 — равно, 1 — меньше, 2 — больше)")

    # === Проверка умножения на цифру (MUL_ND_N) ===
    print("\n--- Умножение на цифру ---")
    print(f"{a} * 0 = {a.MUL_ND_N(0)}")
    print(f"{a} * 1 = {a.MUL_ND_N(1)}")
    print(f"{a} * 3 = {a.MUL_ND_N(3)}")
    print(f"{b} * 9 = {b.MUL_ND_N(9)}")

    # Попробуем пограничные случаи
    print("\n--- Пограничные случаи ---")
    zero = Natural([0])
    print(f"{zero} * 5 = {zero.MUL_ND_N(5)}")
    one = Natural([1])
    print(f"{one} * 9 = {one.MUL_ND_N(9)}")

    # Проверка, что возвращается новый объект, а не тот же самый
    print("\n--- Проверка копирования ---")
    result = a.MUL_ND_N(2)
    print(f"id(a) = {id(a)}, id(result) = {id(result)}")
    print("Ожидаем разные id, т.е. возвращается новый объект")

if __name__ == "__main__":
    main()
