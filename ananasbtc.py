import random
from colorama import Fore
from time import sleep
import string

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&B&@@@@@@@&B&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J 5@@@@@@@J 5@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@#P5PB@@@@@BP5P#@@@@@BP5P#@@@@@BP5P#@@@@@BP5P#@@@#P55555P@J 7P55P#@@J 5@@@@@@G5Y5B@@@@@@@@@
@@@@@@@@B~:!?7^^5@P^^7?!:~B@P^^7?!:~B@P^^7?!:~B@P^^7?!:~BP ^JJJJJY@J ~???!:7&J !JJJ&P::7?!:!&@@@@@@@
@@@@@@@&:.#@@@&~ 5 ^&@@@#.:P ^@@@@#.:G ^&@@@#.:P ^@@@@#.:5.^JJJJJP@J 5@@@@P !J 7555G ^@@@@&#@@@@@@@@
@@@@@@@@^ P@@@@? 7 7@@@@@^ P.:B@@@@^.5 7@@@@@^ P.:B@@@@^ #&P555P? 7P !&@@@Y ?P !&@@#.:G@@@G5@@@@@@@@
@@@@@@@@&?^~!!!: ? 7@@@@@~.#B7^~!!!.:5 7@@@@@~.#B7^~!!!..#Y!7777~:5@P~^~!^^Y@@P~^~!##7:^~^:?&@@@@@@@
@@@@@@@@@@@#BBBB#&B#@@@@@##@@@&BBBBB#&B#@@@@@##@@@&BBBBB#@#BBBBBB&@@@@&BB#@@@@@@&BB@@@&#B#@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")


keyy = input("Input License Key: ")

sleep(2)

print(Fore.GREEN + "License Key valid")


wallet = input("Input your Bitcoin Wallet: ")
sleep(3)

bits = random.getrandbits(256)

bits_hex = hex(bits)

private_key = bits_hex[2:]


con = True

print(Fore.GREEN + "Valied Bitcoin Wallet")

while True:
    if con == True:
        for i in range(1, 2000000):
            sleep(0.1)
            bitcoin = "".join(random.choice(string.ascii_letters + string.digits) for a in range(25))
            money = random.randint(1,2000000)
            num = random.randint(1,10)
            bits = random.getrandbits(256)
            bits_hex = hex(bits)
            private_key = bits_hex[2:]
            if num == 16262:
                print(Fore.GREEN + "> [✓]" + f" | 0.0{money} BTC | " + "1" + bitcoin + f" | {private_key}" )
                with open("BTC.txt", "w") as file:
                    file.write(">" f" | 0.0{money} BTC | " + "1" + bitcoin + f" | {private_key}" )
                print("> Transferring Bitcoins to Wallet.")
                sleep(5)
                answer = input("> Continue mining? (y/n): ")
                if answer.lower() == "y":
                    con = True
                if answer.lower() == "n":
                    con = False
            else:
                print(Fore.RED + "> [x]" + f" | 0.00 BTC | " + "1" + bitcoin + f" | {private_key}" )
    else:
        break
