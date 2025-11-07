from src.natural import Natural

def trace_mul(a: Natural, b: Natural):
    print(f"{a} ({a.digits}) * {b} ({b.digits})")
    result = Natural([0])
    shift = 0
    step = 0
    for d in reversed(b.digits):
        step += 1
        print(f"\nШаг {step}: берем цифру {d} (разряд {shift})")
        if d == 0:
            partial = Natural([0])
        else:
            partial = a.MUL_ND_N(d)
        print(f"  Частичное (без сдвига): {partial} ({partial.digits})")
        if shift > 0:
            partial = partial.MUL_Nk_N(shift)
            print(f"  После сдвига на 10^{shift}: {partial} ({partial.digits})")
        result = result.ADD_NN_N(partial)
        print(f"  Накопленный результат: {result} ({result.digits})")
        shift += 1
    print(f"\nИтог: {a} * {b} = {result} ({result.digits})\n")
    return result

def main():
    a = Natural([1,2,3])   # 123
    b = Natural([4,5])     # 45
    trace_mul(a, b)

    trace_mul(Natural([9,9,9]), Natural([9]))
    trace_mul(Natural([1,0,0,0]), Natural([0]))  # умножение на ноль

if __name__ == "__main__":
    main()
