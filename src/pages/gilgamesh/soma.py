from statistics import mean, stdev

a = [934.473493,
890.133794,
957.458256,
859.674555,
930.828698,
952.641627,
715.691032,
991.219752,
876.340718,
973.085708
]
b = [33917.2297,
37207.2528,
38682.1697,
35895.9093,
38239.3152,
37705.1204,
36677.4702,
36299.6260,
38447.8665,
36705.4322
]

c = [124121.198,
126031.817,
120833.456,
128456.864,
128306.981,
130564.667,
129032.405,
119880.437,
132065.011,
130738.463
]

d=[456238.144,
450559.441,
448121.127,
449980.191,
448115.514,
441273.656,
439026.139,
443736.324,
449573.290,
456608.980]



print("\n")
print(f"{mean(a):.3f}")
print(f"{min(a):.2f}")
print(f"{stdev(a):.2f}")

print("\n")
print(f"{mean(b):.2f}")
print(f"{min(b):.2f}")
print(f"{stdev(b):.2f}")

print("\n")
print(f"{mean(c):.2f}")
print(f"{min(c):.2f}")
print(f"{stdev(c):.2f}")

print("\n")
print(f"{mean(d):.2f}")
print(f"{min(d):.2f}")
print(f"{stdev(d):.2f}")

# print("\n\n")
# print(mean(b))
# print(min(b))
# print(stdev(b))

# print("\n\n")
# print(mean(c))
# print(min(c))
# print(stdev(c))

# print("\n\n")
# print(mean(d))
# print(min(d))
# print(stdev(d))
