# Raspberry Pi Haar Classifier
Program dibagi menjadi 2, untuk Windows dan Raspbian OS

<br>

## Software yang dibutuhkan
* [python >= 3.8](https://www.python.org/downloads/)
* [Cascade Trainer GUI](https://amin-ahmadi.com/cascade-trainer-gui/)

<br>

## Penggunaan di Windows
1. Mengaktifkan virtuan environtment
2. Menginstall dependency yang dibutuhkan
```
pip install -r requirements.txt
```
3. Percobaan pertama bisa digunakan `test.py`
```
python test.py
```
<br>
Haar Cascade Classifier digunakan untuk melakukan klasifikasi pada sebuah benda. Untuk membuat model Haar Cascade Classifier, kita harus menyiapkan dataset yang berupa dataset negatif dan dataset positif. Contoh dataset ada pada folder `dataset_sample`.
<br>
<br>
Lalu dengan menggunakan software Cascade Trainer GUI, bisa dilakukan train data Haar Cascade Classifier. File model Haar diexspresikan dalam bentuk *.xml seperti pada folder `dataset_sample/classifier`.
<br>
<br>

4. Untuk melakukan pengambilan dataset dengan menggunakan kamera, dapat dilakukan dengan menjalankan file `createNegative.py` dan `createTest.py`