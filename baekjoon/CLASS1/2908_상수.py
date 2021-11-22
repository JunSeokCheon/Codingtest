a, b = input().split()

a_reverse = a[::-1]      # reverse 하는방법 | slicing
b_reverse = b[::-1]

if a_reverse > b_reverse:
  print(a_reverse)
else:
  print(b_reverse)