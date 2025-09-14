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
