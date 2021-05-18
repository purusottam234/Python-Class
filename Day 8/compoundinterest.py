# a= p(1+r)n
from decimal import Decimal
principal = Decimal('5000.00')
rate = Decimal("0.05")
for year in range(1, 11):
    amount = principal * (1+rate)**year
    print(f'{year:>2}{amount:>10.3f}')
