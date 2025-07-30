import random
import time

print("Welcome to the Love Percentage Calculator \n")

your_name = input("Enter your name: ")
crush_name = input("Enter your crush's name: ")

print("\nCalculating your love percentage", end="")
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)

love_score = random.randint(40,100)
print(f"\n\n{your_name}❤️{crush_name} = {love_score}% love match!!")
