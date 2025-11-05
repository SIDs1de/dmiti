from src.natural import Natural

def main():
    print("=== Демонстрация работы с натуральными числами ===")

    a = Natural([1, 2])
    b = Natural([9])  # 9

    print(f"a = {a}, b = {b}")
    print(f"Сравнение: {a.COM_NN_D(b)}")
    # print(f"a + 1 = {a.add_1n_n()}")


if __name__ == "__main__":
    main()
