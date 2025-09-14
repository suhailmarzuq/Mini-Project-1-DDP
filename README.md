# Mini Project 1 DDP - Text Based RPG

### Biodata
Nama: Suhail Marzuq
<br> Nim: 2509116071
<br> Kelas: B
<br> Tema: Text Based RPG Menggunakan CRUD dan Pengulangan
<br> 
<br> 
<br> 
## Kata Pengantar
Kepada yang membaca, selamat pagi, siang, sore maupun malam. Semoga kita selalu diberi kesehatan dan dilancarkan segala urusannya. Saya, Suhail Marzuq dengan Nim 2509116071 ingin membagikan Text Based RPG saya yang menggunakan Create, Read, Update, Delete, Conditional Statement (if-elif-else), Variable List dan Variable Tuple.
<br> 
<br> 
## Flowchart
<img width="2842" height="1958" alt="FLowchart Text Based RPG2 drawio" src="https://github.com/user-attachments/assets/6b3cdc83-ddda-4289-936a-76683a55c0bc" />
Saya akan memberi penjelasan singkat apa yang terjadi pada flowchart. Selebihnya akan saya jelaskan pada penjelasan kode.
<br> 
<br> Pertama, melalui start program akan menampilkan sambutan. Kalian akan diminta mengkonfirmasi apakah akan melanjutkan program atau tidak. Jika tidak, pesan perpisahan akan ditampilkan dan program berakhir. Jika iya, maka program akan meminta untuk menginput nama. Setelah menginput nama, status pengguna sebagai pemain akan ditampilkan dan dibalik layar nilai variable quest diubah menjadi True. Variable ini yang akan membolehkan kalian untuk mengisi input selanjutnya.
<br> 
<br>  Berikutnya ada pemilihan quest. Pengguna diminta untuk memasukkan "A" atau "B". Jika memasukkan selain itu, program akan melakukan looping menggunakan variable quest yang nilainya diubah menjadi True sebelumnya. Apabila pengguna memasukkan "A", maka program akan menjalankan ke cabang Quest A. Apabila pengguna memasukkan "B", program akan menjalankan ke cabang Quest B. jika pengguna memasukkan selain kedua hal itu, progam akan menampilkan pesan yang meminta pengguna untuk memasukkan input dengan benar lalu looping kepada input pemilihan quest terjadi.
<br>
<br> Jika pengguna memilih Quest A, program akan menampilkan dialog pembuka, mengubah nilai variable battle menjadi True untuk memulai looping pertarungan. Pertarungan akan terjadi hingga salah satu dari pengguna atau monster kalah. Dalam bagian ini, pengguna juga dapat menggunakan item yang dapat menambah health dan menghapus item yang digunakan dari list. Jika pengguna kalah nilai variable game_status akan menjadi "Lose", sedangkan jika pengguna menang nilai game_status akan menjadi "Win". Lalu nilai variable battle dan quest_a diubah menjadi False untuk menghentikan pengulangan. Jika pengguna memilih Quest B, akan ada dialog singkat dari pengguna dan pemilik ladang sebelum akhirnya nilai variable game_status diubah menjadi "Win". Karena tidak ada kondisi kalah, Quest B dijamin menang.
<br> 
<br> Apabila game_status bernilai "Win", program akan menampilkan pesan yang menyebut nama pengguna dan memberitahukan bahwa pengguna menang. Jika game_status bernilai "Lose", pengguna kalah dan langsung menampilkan GAME OVER.
<br> 
<br> 

## Penjelasan Program
Pada bagian ini saya akan menjelaskan bagaimana program saya berjalan. Mulai dari awal, percabangannya hingga akhir.

### Deklarasi Variable
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4846998e-8587-4fbe-b240-09ae480f0518" />
<br> Terdapat beberapa variable yang saya deklarasikan. Pertama ada c_name, variable berbentuk tuple dan menyimpan nama-nama yang akan digunakan dalam program sebagai nama karakter. Kedua ada variable list monster yang menyimpan status dari monster, mulai dari nama yang diambil dari tuple sebelumnya, health, max health dan serangan. Ketiga ada list item yang berisi Sword dan Heal Potion.
<br>
<br> Di bawahnya terdapat variable battle yang selanjutnya menentukan apakah loop battle akan dimulai atau tidak. Variable game_status akan digunakan untuk menentukan apakah pengguna menang atau kalah. Variable quest akan menentukan apakah pengguna dapat mengambil quest, lalu variable quest_a atau quest_b digunakan untuk menjalankan program berdasarkan quest A atau B yang dipilih. take_quest akan membantu quest_a dan quest_b dalam menjalankan programnya.

### Kalimat Sambutan dan Menolak Pertanyaan Konfirmasi
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d52d92ba-1319-4ed2-8405-143a906b8799" />

<br> Program akan memberi kalimat sambutan, lalu akan ada input dari pertanyaan apakah pengguna ingin Start The Game atau tidak yang akan diisi ke dalam variable play. Jika pengguna menjawab "N" atau yang lainnya, program akan menjalankan percabangan else yang menampilkan kalimat perpisahan dari NPC Atda dan permainan berakhir. Jika pengguna menginput "Y", kita lanjutkan dengan subjudul selanjutnya.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3debad6d-11f1-48da-aa68-470a1a5d4d42" />

### Pengguna Mengisi Nama dan Menampilkan Status
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/04beec35-ca78-47e6-a06e-130fb7646e09" />
<br> Pada input sebelumnya dalam variable play, jika pengguna memasukkan "Y" maka program akan memberikan pengguna input selanjutnya untuk mengisi nama dari pengguna ke dalam variable player_name. Setelah pengguna mengisi nama, program akan menampilkan status pengguna. Mulai dari nama, health, max health, serangan dan item yang dimilki. Nama di sini akan menampilkan string yang sebelumnya sudah pengguna input pada variable player_name. Selanjutnya, pengguna akan diberi pilihan untuk mengambil quest.

### Pengambilan Quest dan Quest B
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/afb08290-eee0-4096-a48b-a45b8f96eb28" />
<br> Pertama, kita akan memilih Quest B yang lebih pendek terlebih dahulu. Nilai dari variable quest diubah menjadi True untuk memberi izin kepada program untuk menjalankan percabangan untuk memilih quest apa yang akan diambil. Pengguna memasukkan input untuk memilih quest ke dalam take_quest dengan mengisikan "A" atau "B". Jika pengguna memasukkan pilihan selain itu, loop akan berjalan dan setelah menampilkan pesan yang memberitahu pengguna untuk memasukkan input yang benar, program akan mengulang ke bagian memasukkan input.
<br>
<br> Jika memilih Quest B, setelah menampilkan ucapan selamat menjalankan dari Atda, variable quest_b diubah menjadi True. Variable ini menjalankan program yang menampilkan dialog pendek antara pengguna dan pemilik ladang Aris. Setelah itu variable game_status diubah nilainya menjadi "Win". kemudian program mmenjalankan break untuk menghentikan pengulangan pemilihan quest.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/29868a8e-a6cb-4905-b966-0657411ab7e7" />

### Quest A - Mengambil dan Memulai Quest
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8173ae3f-ed25-465b-a197-80d49e59be42" />
<br> Sama seperti sebelumnya, program akan menjalankan print yang menampilkan kalimat selamat menjalankan quest dari Atda dan variable quest_a diubah menjadi True untuk menjalankan percabangan. Setelah dialog singkat, Quest A berjalan. Selanjutnya program akan menampilkan status dari pengguna dan monster dengan struktur yang sudah disebutkan sebelumnya. Hanya saja, sebelum menjalankan perintah untuk menampilkan status, percabangan Quest A mengubah nilai variable battle menjadi True yang mengakibatkan sebuah pengulangan aktif. Ini adalah pengulangan yang digunakan untuk melakukan battle.

### Quest A - Battle System
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b3128159-2779-46bb-9735-e5e41268866d" />
<br> Pengguna dapat memasukkan aksi ke dalam input. Dengan memasukkan input "A" atau "Sword", pengguna mengurangi variable monster[1] yang berisi health dengan player[3] pengurangan dan monster akan membalas dengan hal serupa. Hal ini akan terus berlangsung hingga salah satu health dari keduanya habis.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e5f0c18a-7f2b-496d-a79c-f0529f5647dc" />

### Quest A - No Moving
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fcc9be72-99fe-466e-af2c-4aee83d3b166" />
<br> Apabila pengguna memasukkan input action yang tidak valid, pengguna kehilangan gilirannya.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5cfa6fa7-144c-4709-af4e-ff33aff39cbb" />
<br> Begitu juga apabila pengguna menggunakan item yang telah habis. Hal yang sama akan terjadi.

### Quest A - Heal Potion
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c286d4c3-0cfa-4e62-9107-0f9602083b98" />
<br> Jika pengguna memasukkan input "Heal Potion" pada variable action, maka health pengguna pada player[1] akan diberi 10 nilai tambahan. Namun, apabila melewati max health, program akan mengubahnya dan menyesuaikan dengan max health yang pengguna punya. Lalu, item "Heal Potion" dihapus dari list item.
### Quest A - Win and Lose
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7a2a3e45-9369-46f8-bec8-61b88472da94" />
<br> Sistem akan mengecek jika health monster berada di bawah 0, akan ada dialog pendek dari NPC bernama Lily dan nilai variable game_status diubah menjadi Win. variable battle dan quest_a diubah menjadi False untuk menghentikan looping.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/122fdf05-0c98-4dbd-8eb2-fbf88d4ae9c2" />
<br> Jika health pengguna yang berada di bawah 0, pesan bahwa pengguna kalah akan ditampilkan dan nilai variable game_status diubah menjadi lose. Variable battle dan quest_a tetap diubah menjadi False untuk menghentikan looping.
### End The Game
<br> Baik "Win" atau "Lose", program akan mengecek isi dari game_status dan melakukan break. Tujuannya adalah untuk menghentikan pengulangan pemilihan quest dan lanjut ke tahap selanjutnya, yaitu menampilkan kemenangan dan kekalahan.

**Kemenangan**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3392eeb8-dd48-44b6-bf7c-fa3d980bc32e" />
<br> Jika variable game_status adalah "Win", program akan menampilkan nama pengguna diikuti kalimat WIN yang berarti menang dan pengguna telah berhasil menyelesaikan permainan.
**Kekalahan**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/31a2197c-abbe-467d-acbc-5ce7344c7cf4" />
<br> Jika variable game_status adalah "Lose", pengguna mengalami kekalahan dan program langsung menampilkan tulisan "GAME OVER" setelah teks sebelumnya dan program selesai.

## Penutup
<br> Itu saja penjelasan saya untuk Mini Project kali ini. Sekian dan terima kasih sudah membaca.
