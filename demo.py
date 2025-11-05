from src.natural.base import BaseNatural
from src.natural.add_1n_n import ADD_1N_N

examples = [
    [1, 2, 3],     # обычное число
    [1, 2, 9],     # с переносом
    [9, 9, 9],     # 999 + 1
    [0],           # ноль
]

for num in examples:
    a = BaseNatural(num)
    res = ADD_1N_N.ADD_1N_N(a)
    print(f"{num} + 1 = {res.digits}")
