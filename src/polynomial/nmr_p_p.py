from typing import Self

class NMR_P_P:
    def NMR_P_P(self: Self) -> Self:
        """
        Преобразование многочлена - кратные корни в простые
        Автор: Карпов Андрей, гр. 4382
        Возвращает многочлен с простыми корнями
        """
        # Нулевой многочлен остается нулевым
        if self.is_zero():
            return self.copy()
            
        # Находим производную
        derivative = self.DER_P_P()
        
        # Если производная нулевая - это константа, возвращаем константу
        if derivative.is_zero():
            return self.copy()
        
        # Находим НОД многочлена и его производной
        gcd_polynomial = self.GCF_PP_P(derivative)
        
        # Делим исходный многочлен на НОД
        result = self.DIV_PP_P(gcd_polynomial)
        
        return result