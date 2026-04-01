import time
import sys

from caesar_art import run_matrix

# ------------------- COLORS -------------------

GREEN = "\033[92m"
RED = "\033[91m"
WHITE = "\033[97m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# ------------------- TYPE EFFECT -------------------

def type_text(text, color=GREEN, speed=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print(RESET)

# ------------------- VALIDATION FUNCTIONS -------------------

def get_direction():
    while True:
        direction = input(GREEN + "encode / decode > " + RESET).strip().lower()

        if direction == "":
            type_text("[ ERROR: EMPTY INPUT ]", RED)
        elif direction in ["encode", "decode"]:
            return direction
        else:
            type_text("[ ERROR: TYPE 'encode' OR 'decode' ]", RED)


def get_text():
    while True:
        text = input(GREEN + "input text      > " + RESET).strip().lower()

        if text == "":
            type_text("[ ERROR: TEXT CANNOT BE EMPTY ]", RED)
        else:
            return text


def get_shift():
    while True:
        shift_input = input(GREEN + "shift value     > " + RESET).strip()

        if shift_input == "":
            type_text("[ ERROR: SHIFT CANNOT BE EMPTY ]", RED)
            continue

        if not shift_input.isdigit():
            type_text("[ ERROR: ENTER A VALID NUMBER ]", RED)
            continue

        shift = int(shift_input)

        if shift < 0:
            type_text("[ ERROR: SHIFT MUST BE POSITIVE ]", RED)
        else:
            return shift % 26   # keeps shift in range


def get_yes_no(prompt):
    while True:
        ans = input(YELLOW + prompt + RESET).strip().lower()

        if ans in ["yes", "y"]:
            return "yes"
        elif ans in ["no", "n"]:
            return "no"
        else:
            type_text("[ ERROR: TYPE yes OR no ]", RED)

# ------------------- STARTUP -------------------

run_matrix("ACCESS GRANTED", 4)

type_text("\n[ SYSTEM ONLINE ]", GREEN, 0.05)
type_text("[ Loading Cipher Module... ]\n", CYAN, 0.04)

# ------------------- FUNCTIONS -------------------

def encrypt(text, shift):
    result = ""
    for letter in text:
        if letter in alphabets:
            result += alphabets[(alphabets.index(letter) + shift) % 26]
        else:
            result += letter

    type_text("\n[ ENCRYPTING DATA... ]", YELLOW, 0.04)
    time.sleep(0.5)
    type_text(">>> " + result, WHITE, 0.02)


def decrypt(text, shift):
    result = ""
    for letter in text:
        if letter in alphabets:
            result += alphabets[(alphabets.index(letter) - shift) % 26]
        else:
            result += letter

    type_text("\n[ DECRYPTING DATA... ]", CYAN, 0.04)
    time.sleep(0.5)
    type_text(">>> " + result, WHITE, 0.02)

# ------------------- MAIN LOOP -------------------

while True:
    type_text("\n----------------------------------------", GREEN, 0.002)

    direction = get_direction()
    text = get_text()
    shift = get_shift()

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

    again = get_yes_no("\nrun again? (yes/no) > ")

    if again == "no":
        type_text("\n[ SYSTEM SHUTDOWN... ]", GREEN, 0.05)
        break