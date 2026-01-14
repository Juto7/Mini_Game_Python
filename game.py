import random
class Player:
    def __init__(self, nm):
        self.nama = nm
        self.darah = 100
        self.exp = 0
        self.level = 1
        self.damage = 5

    def attack(self, bot):
        print(f"{self.nama} menyerang {bot.nama}")
        bot.defend(self.damage)
        self.exp += 12
        self.CekLevel()
    
    def defend(self, damage):
        self.darah -= damage
        print(f"{self.nama} terkena serangan, Darah berkurang {damage} ")

    def CekLevel(self):
        if self.exp >= 100:
            self.level +=1
            self.exp = 0
            self.darah +=20
            self.damage += 10
            print(f"{self.nama} naik ke level {self.level}")
            print(f"Damage Kamu Bertambah Menjadi  {self.damage}")
    
    def status(self):
        print(input(f"siap mas {self.nama}, print status akun..."))
        print(f"Darah : {self.darah}\nEXP : {self.exp}\nLevel : {self.level}\nDamage : {self.damage}")

nama = input("buat nickname kamu : ")
input("berhasil membuat nickname")
p = Player(nama)
bot= Player("Jagoan")
opsi = {
    "1": "gunting",
    "2": "batu",
    "3": "kertas"

} 
while p.darah > 0 and bot.darah > 0:
    print("=================================================")
    print("      SELAMAT DATANG DI PERMAINAN GABUT          ")
    print("=================================================")
    print("1. Gunting")
    print("2. Batu")
    print("3. Kertas")
    print("4. Cek Level Player")
    print("5. Cek Level Musuh")

    menu = int(input("pilih yang mana bos : "))
    bot_Menu = random.randint(1,3)

    if menu in [1,2,3]:
        if menu == bot_Menu:
            print("DRAW BOS")
        elif (
            (menu == 1 and bot_Menu == 3) or
            (menu == 2 and bot_Menu == 1) or
            (menu == 3 and bot_Menu == 2)
        ):
            print(f"{p.nama} WIN")
            p.attack(bot)
        else:
            print(f"{bot.nama} WIN")
            bot.attack(p)
    elif menu == 4:
        p.status()
    elif menu == 5:
        bot.status()
    else:
        print("NOT FOUND")

if p.darah <= 0:
    print(f"{p.nama} kalah, cemen lu")
else:
    print(f"{p.nama} WIN KELAZZZZZ")

    # if menu == 1:
    #     if bot_Menu == 1:
    #         print("draw")
    #     elif bot_Menu == 2:
    #         print(f"{bot.nama} win")
    #         bot.attack()
    #         p.defend()
    #     elif bot_Menu == 3:
    #         print(f"{p.nama} win, seneng yee")
    #         p.attack()
    #         bot.defend()
    #     else:
    #         print("not found")
    # elif menu == 2:
    #     if bot_Menu == 1:
    #         print(f"{p.nama} win, seneng yee")
    #         p.attack()
    #         bot.defend()
    #     elif bot_Menu == 2:
    #         print("draw")
    #     elif bot_Menu == 3:
    #         print(f"{bot.nama} win")
    #         bot.attack()
    #         p.defend()
    #     else:
    #         print("not found")
    # elif menu == 3:
    #     if bot_Menu == 1:
    #         print(f"{bot.nama} win")
    #         bot.attack()
    #         p.defend()
    #     elif bot_Menu == 2:
    #         print(f"{p.nama} win, seneng yee")
    #         p.attack()
    #         bot.defend()
    #     elif bot_Menu == 3:
    #         print("draw")
    # elif menu == 4:
    #     print(p.status())
    #     print("=============================")
    # elif menu == 5:
    #     input("print out")
    #     print("=====================================================")
    #     print(f"darah : {bot.darah}\nLevel : {bot.level}\nEXP : {bot.exp}")
    # else:
    #     print("masukan yang benar bos")


    


# pr
# remake code lebih rapih
# tambahin damage, setiap bertambah level tambah damage += 7
# kalau naik level, darah bertambah 20


