# filenames = ["1.doc", "1.report", "1.presentation"]

# filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

# print(filenames)

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
    
#     total = float(value / total_value * 100)
    
#     print(f'That is {total}')

# except:
#     print("You need to enter a number. Run the program again.")


# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
    
#     total = value / total_value
    
#     print(f'That is {total}')

# except ZeroDivisionError:
#     print("Your total value cannot be zero.")


# colors = [11, 34, 98, 43, 45, 54, 54]

# color = [col > 50 for col in colors]
# print(color)

# def get_average():
#     print("Hi")
#     x = "hello"
    
# print(get_average())

def calculate_time(g=9.80665, h):
    t = (2 * h / g) ** 0.5
    return t
    
  
time = calculate_time(100)
print(time)

        
