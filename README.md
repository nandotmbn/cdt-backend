# DNN SERVER FOR INTENSIFY

Pengembangan Deep Neural Network untuk aplikasi web Intensify menggunakan teknologi, diantaranya:

1. Programming Language : Python
2. Framework RESTAPI : Flask
3. Framework Machine Learning : Tensorflow

## How to run

### Windows

> Requirements:
>
> 1. Python
> 2. Flask
> 3. TensorFlow
> 4. Open-CV

#### Installing Python

Menginstall python caranya sangat mudah, yaitu diantaranya:

1. Mengunjungi [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Klik tombol **Download Python 3.x.x**
   ![alt text for screen readers](/tutorials/img/1.png "Text to show on mouseover")
3. Tunggu hingga selesai terdownload
4. Jalankan file yang terdownload
5. Akan muncul jendela instalasi, centang semua pilihan yang ada di sisi bawah jendela
   ![alt text for screen readers](/tutorials/img/2.png "Text to show on mouseover")
   * Use admin priviledges when installing py.exe
   * Add python.exe to PATH
6. Klik Install Now
7. Tunggu hingga proses instalasi selesai
8. Jika proses instalasi selesai, buka CMD (Anda dapat mencari aplikasi CMD di bilah pencarian windows)
9. Ketikkan command `python --version`

   ```bash
   PS D:\> python --version
   ```

10. Jika hasil command adalah `Python 3.x.x`, maka python berhasil diinstall.

  ```bash
   PS D:\> python --version
   Python 3.9.12
  ```

#### Installing Flask, OpenCV and TensorFlow

Jika python sudah terinstall, maka Flask, OpenCV dan TensorFlow akan mudah untuk diinstall.

1. Buka CMD (Command Prompt)
2. Ketikkan command `py -m pip install numpy opencv-python flask flask-cors tensorflow`
3. Tunggu hingga proses selesai
4. Setelah selesai, cari di bilah pencarian 'env', maka akan muncul seperti gambar dibawah ini
   ![alt text for screen readers](/tutorials/img/3.png "Text to show on mouseover")
5. Klik Open
6. Lalu akan muncul jendela System Properties
7. Klik **Environment Variables**
   ![alt text for screen readers](/tutorials/img/4.png "Text to show on mouseover")
8. Lalu akan muncul jendela Environment Variables
9. Klik tombol **New** pada User Variable (yellow highlighted)
    ![alt text for screen readers](/tutorials/img/5.png "Text to show on mouseover")
10. Isi seperti gambar dibawah
    ![alt text for screen readers](/tutorials/img/6.png "Text to show on mouseover")
11. Buat lagi dengan isian seperti gambar dibawah
    ![alt text for screen readers](/tutorials/img/7.png "Text to show on mouseover")
12. Selesai
  
#### Run DNN Server in your system

1. Buka repository
2. Buka Command Prompt atau Windows PowerShell
3. Arahkan menuju repository
4. Ketikkan `py -m flask run`
5. Jika jendela command prompt atau powershell menghasilkan pesan seperti ini, maka DNN Server berhasil dijalankan

   ```bash
    * Serving Flask app 'app.py' (lazy loading)
    * Environment: development
    * Debug mode: on
   2022-12-29 21:15:42.275862: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
   To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 130-907-334
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   2022-12-29 21:15:46.527509: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
   To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
   ```

6. Selesai
