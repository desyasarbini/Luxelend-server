1. clone repository
   `git clone https://github.com/desyasarbini/Luxelend-server.git`

2. masuk ke directory yang baru saja diclone
   install package manager
   `pip3 install poetry`

3. install depencies yang akan digunakan menggunakan poetry
   `poetry install`

4. Folder Description
   connectors : untuk connect ke database, fetch data .env
   models : untuk menyamakan data tabel yang ada disupabase, beserta typenya
   route : route api dan method yang digunakan
   controller : controller, untk model seperti (untuk get product, create product, etc)
   utils : settingan api_response awal
