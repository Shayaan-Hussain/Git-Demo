while True:
  try:
    i=float(input('Enter 1st number : '))
    j=float(input('Enter 2nd number : '))
  except:
    print('Input data can not be typecasted to float')
  else:
    break
print(f'Sum = {i+j}\nDifference = {i-j}\nProduct = {i*j}\nQuotient = {i/j}\n')
