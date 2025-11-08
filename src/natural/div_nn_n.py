from .base import BaseNatural


class DIV_NN_N:
    def DIV_NN_N(self: BaseNatural, second: BaseNatural) -> BaseNatural:
        """
        Автор: Viktor Permitin
        Неполное частное от деления первого
        натурального числа на второе с
        остатком (делитель отличен от нуля)
        """
        if len(second.digits) == 1 and second.digits[0] == 0:
            raise ValueError("division by zero")
    
        cmp_result = self.COM_NN_D(second)
        if cmp_result == 1:
            return BaseNatural([0])
        
        if cmp_result == 0:
            return BaseNatural([1])
        
        k_max = len(self.digits) - len(second.digits)
        
        remainder = self.copy()
        result_digits = []
        
        for k in range(k_max, -1, -1):
            digit = remainder.DIV_NN_DK(second, k)
            
            if digit > 0:
                shifted = second.MUL_Nk_N(k)
                product = shifted.MUL_ND_N(digit)
                remainder = remainder.SUB_NN_N(product)
            
            if len(result_digits) == 0 and digit == 0:
                continue
            
            result_digits.append(digit)
        
        while len(result_digits) > 1 and result_digits[0] == 0:
            result_digits.pop(0)
        
        return BaseNatural(result_digits)