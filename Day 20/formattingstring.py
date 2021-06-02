from decimal import Decimal
print(f'{17.456 : .2f}')
print(f'{17 : d}')
print(f'{	118:c}')
print(f'{"hello":s} {7} ')


print(f'{ Decimal("100000000.0"):.3f}')
print(f'{ Decimal("100000000.0"):.3e}')
# field width and alignment

print(f'[{ 27:10d}]')
print(f'[{ 2.7:10f}]')

print(f'[{ 27:<10d}]')
print(f'[{ 27:>10d}]')
print(f'[{ 27:^10d}]')

# Numerical formating
print(f'[{ 27:+10d}]')
print(f'[{ 27:+010d}]')
print(f'{27:d}\n{27:d}\n{-27:d}')


# grouping digits

print(f'{ 2712424325:,d}')
print(f'{ 2712424325:,.3f}')


# format method

a = "{:.2f}".format(23432.454765)
print(a)
b = '{} {}'.format("Hari", "geeta")
print(b)
c = '{} {} {} {}'.format("Hari", "geeta", 'Nita', "Rita")
print(c)

ac = '{0} {1} {0} {0}'.format("Hari", "geeta", 'Nita', "Rita")
print(ac)
e = '{first} {last}'.format(first="Hari", last="Sharma")
print(e)
