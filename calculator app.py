def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def main():
  first_number = float(input("Enter the first number: "))
  second_number = float(input("Enter the second number: "))

  print("Select an operation:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")

  operation = int(input("Enter your choice: "))

  if operation == 1:
    print(first_number, "+", second_number, "=", add(first_number, second_number))
  elif operation == 2:
    print(first_number, "-", second_number, "=", subtract(first_number, second_number))
  elif operation == 3:
    print(first_number, "*", second_number, "=", multiply(first_number, second_number))
  elif operation == 4:
    print(first_number, "/", second_number, "=", divide(first_number, second_number))
  else:
    print("Invalid operation")

if __name__ == "__main__":
  main()
