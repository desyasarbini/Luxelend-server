1. clone repository
   `git clone https://github.com/desyasarbini/Luxelend-server.git`

2. masuk ke directory yang baru saja diclone
   install package manager
   `pip3 install poetry`

3. install depencies yang akan digunakan menggunakan poetry
   `poetry install`

4. Structure Folder Description
   connectors : untuk connect ke database, fetch data .env
   controller : controller, untk model seperti (untuk get product, create product, etc)
   models : untuk menyamakan data tabel yang ada disupabase, beserta typenya
   routes : route api dan method yang digunakan
   utils : settingan api_response awal

5. [Documentasi Luxelend API](https://documenter.getpostman.com/view/32144902/2sA3e1AV8d)
