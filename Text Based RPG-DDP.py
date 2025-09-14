### Note : print() dengan isi kosong digunakan untuk menambahkan spasi agar kemudahan membaca terminal

## Pengaturan Dasar

# Tuple Nama-Nama Karakter
c_name = ("Atda", "Lily", "Goblin", "Aris")

# Status Musuh
monster = [c_name[2], 10, 10, 5]

# List Nama-Nama Item
item = ["Sword", "Heal Potion"]

## Battle
battle = False

## Game Status (Win/Lose)
game_status = ""

# Variable yang Digunakan untuk Mengecek Apakah Sudah Saatnya Mengambil Quest
quest = False
quest_a = False
quest_b =False

# Quest yang Diambil
take_quest = ""


## Main Program
# Sambutan
print()
print(f"{c_name[0]} : Selamat datang! Apakah anda ingin mengambil quest?")
print()

# Pertanyaan Konfirmasi
play = input("Start the game? [Y/N] : ")
print()

# Pengguna Mengambil Quest
if play == "Y":

    # Pengguna Mengisi Nama
    print(f"{c_name[0]} : Baiklah! Silahkan isi namamu! ")
    player_name = input("Nama : ")
    print()
    

    # Status karakter
    # Nama - Health - Max Health - Serangan
    player = [player_name, 20, 20, 2]
    print(f"{c_name[0]} : Baik. Kepada petualang:")
    print("Nama : ", player[0])
    print(f"HP : {player[1]} / {player[2]}")
    print("Serangan : ", player[3])
    print("Item : ", item)
    print()



    # Pengguna diizinkan mengambil Quest
    quest = True

# Pengguna Tidak Mengambil Quest (Program Selesai)
else:
    print()
    print(f"{c_name[0]} : Begitu? Terima kasih. Silahkan datang kembali!")
    print()


# Pengguna Memilih Quest
while quest == True:
    # Memilih Quest A atau B
    print(f"{c_name[0]} : Quest apa yang ingin anda ambil?")
    take_quest = input("[A] Berburu Goblin [B] Membersihkan Ladang [A/B] : ")
    print()

    # Pengguna Mengambil Quest A
    if take_quest == "A":
        print(f"{c_name[0]} : Quest A tersedia! Selamat menjalankan!")

        # Quest A akan berjalan
        quest_a = True


    ## Pengguna Mengambil Quest B
    elif take_quest == "B":
        print(f"{c_name[0]} : Quest B tersedia! Selamat menjalankan!")
        quest_b = True

    else:
        print(f"{c_name[0]} : Haha, tolong pilih quest dengan benar ^^")

    ## Menjalankan Quest A
    while quest_a == True:
        print()
        print(f"{player[0]} berjalan ke dalam hutan dan bertemu dengan goblin yang sedang menyerang seorang gadis. {player[0]} maju dan menyerang goblin itu.")
        print()
        battle = True


        ## Battle
        while battle == True:
            print()
        
            # Status Player
            print("Nama : ", player[0])
            print(f"HP : {player[1]} / { player[2]}")
            print("Serangan : ", player[3])
            print("Item : ", item)
            print()

            # Status Monster
            print("Nama : ", monster[0])
            print(f"HP : {monster[1]} / {monster[2]}")
            print("Serangan : ", monster[3])
            print()


            ## Pengguna Melakukan Aksi
            # Mengecek Apakah Pengguna Masih Mempunyai HP
            if player[1] > 0:
                print("[A] Menyerang menggunakan Pedang [Nama Item] Menggunakan item")
                action = input("Aksi : ")
                print()

                # Pengguna Menyerang atau Menggunakan Pedang
                if action == "A" or action == "Sword":
                    # Mengurangi Health Musuh
                    monster[1] -= player[3]

                    # Menampilkan Update
                    print(f"{player[0]} menyerang {monster[0]} dan memberikan 2 serangan!")

                # Pengguna Menggunakan Heal
                elif action == "Heal Potion" and "Heal Potion" in item:

                    # Menambah 10 Health Kepada Karakter
                    player[1] += 10


                    # Mengecek Apakah Health Melewati Max Health
                    if player[1] > player[2]:

                    # Menetapkan Health Pengguna Sesuai Max Health
                        player[1] = 20
                    
                    # Menampilkan output
                    print(f"{player[0]} menggunakan Heal Potion dan menyembuhkan diri! HP menjadi {player[1]}!")

                    # Menghapus Item Heal Potion dari List Item
                    item.remove("Heal Potion")

                # Giliran Pengguna Dilewati
                else:
                    print(f"{player[0]} hanya terdiam.")



            # Mengecek Apakah Pengguna Kehabisan HP
            elif player[1] <= 0:

                # Menampilkan Pesan Kekalahkan
                print()
                print(f"{player[0]} Kalah!")

                # Status Permainan Menjadi Kalah
                game_status = "Lose"
                
                
                # Mengentikan Loop Battle
                battle = False

                # Menghentikan Loop Quest A
                quest_a = False

            # Mengecek Apakah Monster Masih Memiliki HP
            if monster[1] > 0:
                # Monster Menyerang Balik
                # Mengurangi Health Pengguna
                player[1] -= monster[3]
                
                # Menampilkan Update
                print(f"{monster[0]} menyerang {player[0]} dan memberikan 5 serangan!")

            # Mengecek Apakah Monster Kehabisan HP
            elif monster[1] <= 0:

                # Dialog Pendek
                print()
                print(f"{c_name[1]} : Namaku Lily. Terima Kasih Telah Membantu!")

                #  Status Permainan Menjadi menang
                game_status = "Win"

                # Mengentikan Loop Battle
                battle = False

                # Menghentikan Loop Quest A
                quest_a = False


    ## Menjalankan Quest B
    if quest_b == True:
        # Dialog
        print()
        print(f"{player[0]} pergi ke ladang untuk membersihkannya. Pemilik ladang datang untuk berterima kasih.")
        print()
        print(f"{c_name[3]} : Terima kasih {player[0]} telah membantu. Hari sudah mulai sore, anakku {c_name[1]} belum juga pulang. Aku harus mencarinya!")
        print()
        print(f"{player[0]} mengangguk dan meninggalkan ladang tersebut.")

        #  Status Permainan Menjadi menang
        game_status = "Win"

    # Menghentikan Loop  Pemiihan Quest
    if game_status == "Lose" or "Win":
        break






# Jika Menang Menampilkan {player[0]} WIN, Jika Kalah Menampilkan GAME OVER
if game_status == "Win":
    print()
    print(f"{player[0]} WIN")

elif game_status == "Lose":
    print()
    print("GAME OVER")


print()
