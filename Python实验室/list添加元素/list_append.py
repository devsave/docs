# a = [1, 2]
# b = [1, 2]

# print('The id of a: %d' % id(a) )
# a += [3]
# print('The id of a: %d' % id(a) )
# print('a = %s' % str(a))

# print('The id of b: %d' % id(b) )
# b = b + [3]
# print('The id of b: %d' % id(b) )
# print('b = %s' % str(b))


# b = (1, 2)
# c = b

# print('Before calculation')
# print('The id of b: %d' % id(b))
# print('The id of c: %d' % id(c))
# b += (3, )
# print('After calculation')
# print('The id of b: %d' % id(b) )
# print('The id of c: %d' % id(c))
# print('b = %s' % str(b))
# print('c = %s' % str(c))

b = (1, 2)
c = b

print('Before calculation')
print('The id of b: %d' % id(b))
print('The id of c: %d' % id(c))
print('b = %s' % str(b))
print('c = %s' % str(c))
b += (3, )
print()
print('After calculation')
print('The id of b: %d' % id(b) )
print('The id of c: %d' % id(c))
print('b = %s' % str(b))
print('c = %s' % str(c))