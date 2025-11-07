from src.natural import Natural

def main():
    # умножение на цифру
    a = Natural([1, 2, 3])
    print(f"\nИсходное число a = {a}")

    for d in [0, 1, 3, 9]:
        result = a.MUL_ND_N(d)
        print(f"{a} * {d} = {result}")

    print("\n--- Умножение на 10^k ---")
    b = Natural([4, 5, 6])  

    for k in [0, 1, 2, 4]:
        result = b.MUL_Nk_N(k)
        print(f"{b} * 10^{k} = {result}")

    print("\n--- Граничные случаи ---")
    zero = Natural([0])
    print(f"0 * 7 = {zero.MUL_ND_N(7)}")
    print(f"0 * 10^3 = {zero.MUL_Nk_N(3)}")


if __name__ == "__main__":
    main()