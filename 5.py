def prime_factors(n):
  factors = []
  temp = n

  for x in range(2, n):
    if (temp % x == 0):
      factors.append(x)
      temp /= x
    if (temp == 1):
      break

  if (len(factors) == 0):
    return [n]

  return factors

def divisible():
  


def main():
  print(prime_factors(21))

if __name__ == "__main__":
  main()