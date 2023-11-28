add_integer = __import__('0-add_integer').add_integer

f = __import__("0-add_integer").add_integer.__doc__
print(len(f) > 1)


print(add_integer(-1, -2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(1, 2, 3))
except Exception as e:
    print(e)
try:
    print(add_integer(True, 1))
except Exception as e:
    print(e)
