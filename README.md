# Portofolio — Eka Sandy Aulia Puspitasari

Versi website dari portofolio PDF, dibangun dengan Python dan Streamlit.

## Menjalankan secara lokal

Pastikan Python 3.9 atau lebih baru sudah terpasang.

```bash
git clone <url-repository>
cd portfolio

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

Aplikasi akan terbuka di `http://localhost:8501`.

## Struktur project

```
portfolio/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
└── assets/
    └── images/
        └── logos/
```

Seluruh gambar dipanggil dengan relative path, sehingga project dapat dipindahkan atau
di-deploy tanpa penyesuaian konfigurasi.

## Deploy ke Streamlit Community Cloud

1. Push seluruh isi folder `portfolio/` ke sebuah repository GitHub (sertakan folder `assets/`).
2. Buka https://share.streamlit.io lalu masuk menggunakan akun GitHub.
3. Pilih **Create app** → **Deploy a public app from GitHub**.
4. Isi konfigurasi berikut:
   - Repository: repository yang baru dibuat
   - Branch: `main`
   - Main file path: `app.py` (gunakan `portfolio/app.py` jika folder tidak berada di root repository)
5. Klik **Deploy**. Streamlit akan memasang dependency dari `requirements.txt` secara otomatis.
6. Website dapat diakses melalui URL `https://<nama-app>.streamlit.app`.

Setiap perubahan yang di-push ke branch tersebut akan otomatis diperbarui di aplikasi.
