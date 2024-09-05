# Chess.com X Discord event 2024
# 1 month Free Diamond subscription code generator (without validation)
# Written by XyrenChess on 5th Sep 2024

import string, random

chars = string.ascii_uppercase + string.digits

def scrap(time: int) -> None:
    try:
        for i in range(int(time)):
            code = ''.join(random.choices(chars, k=5))
            print(f"DISCORD124-{code}")
        print("! Redeem at https://www.chess.com/special\n\n-----Session ended-----")
    except:
        print("Please specify value for code generation.")

while True:
    t = input("Enter generation value (How many codes do you want to generate?):\n>>> ")
    scrap(t)
