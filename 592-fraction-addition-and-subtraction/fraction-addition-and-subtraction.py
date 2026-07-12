class Solution:
    def fractionAddition(self, expression: str) -> str:
        i = 0
        num, den = 0, 1  # Current result

        while i < len(expression):
            # Read sign
            sign = 1
            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            # Read numerator
            n = 0
            while expression[i].isdigit():
                n = n * 10 + int(expression[i])
                i += 1
            n *= sign

            i += 1  # Skip '/'

            # Read denominator
            d = 0
            while i < len(expression) and expression[i].isdigit():
                d = d * 10 + int(expression[i])
                i += 1

            # Add fractions
            num = num * d + n * den
            den *= d

            # Reduce fraction
            g = gcd(abs(num), den)
            num //= g
            den //= g

        return f"{num}/{den}"