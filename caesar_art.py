import os
import random
import time

def run_matrix(hidden_text, duration=5):
    try:
        width = os.get_terminal_size().columns
        height = os.get_terminal_size().lines
    except:
        width, height = 80, 24

    drops = [0 for _ in range(width)]
    hidden_pos = width // 2 - len(hidden_text) // 2

    start_time = time.time()

    while time.time() - start_time < duration:
        os.system('cls' if os.name == 'nt' else 'clear')  # CLEAR SCREEN

        for i in range(height):
            line = ""
            for j in range(width):
                if i == drops[j]:
                    line += str(random.randint(0, 9))
                elif i < drops[j] and random.random() > 0.9:
                    line += str(random.randint(0, 9))
                else:
                    line += " "
            print("\033[92m" + line)   # GREEN COLOR

        # print hidden text AFTER matrix
        middle_row = height // 2
        print("\n" * (middle_row - height//2), end="")
        print(" " * hidden_pos + "\033[97m" + hidden_text)

        # update drops
        for i in range(len(drops)):
            if drops[i] > height and random.random() > 0.975:
                drops[i] = 0
            drops[i] += 1

        time.sleep(0.05)