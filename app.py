import base64
from pathlib import Path

import streamlit as st

IMAGE_DIR = Path(__file__).parent / "assets" / "images"

SECTIONS = [
    "Beranda",
    "Tentang Saya",
    "Pengalaman",
    "Skill",
    "Capstone",
    "Tugas Akhir",
    "System Machine Learning",
    "Asisten Laboratorium",
    "Mari Terhubung",
]

SKILL_GROUPS = [
    [
        ("power-bi.png", "Power BI"),
        ("word.png", "Microsoft Word"),
        ("excel.png", "Microsoft Excel"),
        ("microsoft.png", "Microsoft"),
        ("powerpoint.png", "Microsoft PowerPoint"),
        ("access.png", "Microsoft Access"),
        ("sql-server-management.png", "SQL Server Management"),
        ("vs-code.png", "Visual Studio Code"),
    ],
    [
        ("google.png", "Google"),
        ("google-docs.png", "Google Docs"),
        ("google-sheets.png", "Google Sheets"),
        ("google-slides.png", "Google Slides"),
        ("google-forms.png", "Google Forms"),
        ("colab.png", "Google Colab"),
        ("looker.png", "Looker"),
    ],
    [
        ("database.png", "Database"),
        ("postgresql.png", "PostgreSQL"),
        ("python.png", "Python"),
        ("github.png", "GitHub"),
        ("docker.png", "Docker"),
    ],
]

EXPERIENCES = [
    {
        "organisasi": "Asah led by Dicoding X Accenture",
        "periode": "Agustus 2025 – Januari 2026",
        "detail": ["Machine Learning"],
    },
    {
        "organisasi": "Laboratorium Sistem Informasi – Universitas Gunadarma",
        "periode": "2025 - 2026",
        "detail": ["Ketua dan Asisten Praktikum"],
    },
    {
        "organisasi": "Sharia Economic Forum (SEF) Universitas Gunadarma",
        "periode": "2024 - 2025",
        "detail": [
            "Staf Divisi Media, Komunikasi, dan Informasi (Medkominfo) — 2024/2025",
            "Staf Hubungan Masyarakat (Public Relations) – Gunadarma Sharia Economic Forum (GSENT) 2025",
            "Koordinator Acara – SEF Super Mentor (SSM) 2025",
            "Koordinator Divisi Konsumsi – Diklat Ekonomi Islam (DEI) 2024",
            "Bendahara – Gunadarma Sharia Economic Forum (GSENT) 2024",
        ],
    },
]

CLUSTER_TABLE = [
    ("Digital Rendah", ["10", "9", "9", "9", "13"]),
    ("Digital Menengah", ["19", "20", "20", "20", "16"]),
    ("Digital Maju", ["4", "4", "4", "4", "4"]),
    ("Digital Spesialis Non-Tunai", ["1", "1", "1", "1", "1"]),
]

CONTACTS = [
    ("Telepon", "+62 895 370 314 457", None),
    ("GitHub", "github.com/ekasandyaulia-lgtm", "https://github.com/ekasandyaulia-lgtm"),
    ("Email", "ekasandyaulia@gmail.com", "mailto:ekasandyaulia@gmail.com"),
    (
        "LinkedIn",
        "linkedin.com/in/ekasandyauliapuspitasari/",
        "https://www.linkedin.com/in/ekasandyauliapuspitasari/",
    ),
]

STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,700;1,900&family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
    --green: #598556;
    --green-deep: #234022;
    --cream: #FFFBDB;
    --paper: #FFFFFF;
    --ink: #2F3E2E;
    --hairline: rgba(89, 133, 86, 0.35);
}

html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

.stApp { background-color: var(--paper); }

.block-container {
    padding-top: 2.4rem;
    padding-bottom: 4rem;
    max-width: 1180px;
}

header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer, div[data-testid="stToolbar"], div[data-testid="stDecoration"],
div[data-testid="stStatusWidget"] { display: none; }

section[data-testid="stSidebar"] { background-color: var(--green); }
section[data-testid="stSidebar"] * { color: var(--cream) !important; }
section[data-testid="stSidebar"] .sidebar-name {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 700;
    font-size: 1.45rem;
    line-height: 1.2;
    margin-bottom: 0.15rem;
}
section[data-testid="stSidebar"] .sidebar-meta {
    font-size: 0.78rem;
    letter-spacing: 0.16em;
    opacity: 0.85;
    margin-bottom: 1.6rem;
}
section[data-testid="stSidebar"] div[role="radiogroup"] { gap: 0; }
section[data-testid="stSidebar"] label[data-testid="stRadioOption"] {
    display: block;
    padding: 0.55rem 0.9rem;
    border-radius: 8px;
    margin-bottom: 0.1rem;
    cursor: pointer;
    transition: background 0.15s ease;
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"] > div > div > div:not([data-testid="stMarkdownContainer"]) {
    display: none;
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"] p {
    font-size: 0.95rem;
    font-weight: 400;
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"]:hover {
    background: rgba(255, 251, 219, 0.14);
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"][data-selected="true"] {
    background: rgba(255, 251, 219, 0.24);
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"][data-selected="true"] p {
    font-weight: 600;
}
section[data-testid="stSidebar"] .sidebar-foot {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(255, 251, 219, 0.35);
    font-size: 0.78rem;
    line-height: 1.7;
    opacity: 0.9;
}

.page-rule {
    display: flex;
    align-items: center;
    justify-content: center;
    border-top: 1px solid var(--hairline);
    border-bottom: 1px solid var(--hairline);
    padding: 0.45rem 0;
    letter-spacing: 0.34em;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--green-deep);
    margin-bottom: 2.2rem;
}

.display-title {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 900;
    color: var(--green-deep);
    font-size: clamp(2.1rem, 4.6vw, 3.4rem);
    line-height: 1.08;
    margin: 0 0 1.4rem 0;
}

.section-label {
    display: inline-block;
    background: var(--green);
    color: var(--cream);
    border-radius: 999px;
    padding: 0.45rem 1.5rem;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.22em;
    margin-bottom: 1rem;
}

.subheading {
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--green-deep);
    text-transform: uppercase;
    margin: 2.2rem 0 0.7rem 0;
}

.body-text {
    font-size: 1rem;
    line-height: 1.85;
    color: var(--ink);
    max-width: 68ch;
    text-align: justify;
}

.body-text strong { color: var(--green-deep); font-weight: 600; }

.cover {
    background: var(--green);
    border-radius: 18px;
    padding: clamp(2.5rem, 7vw, 5rem) clamp(1.6rem, 5vw, 4rem);
    color: var(--cream);
    min-height: 68vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.cover-year { letter-spacing: 0.3em; font-size: 0.85rem; opacity: 0.9; }
.cover-title {
    font-weight: 700;
    font-size: clamp(2.8rem, 10vw, 6rem);
    letter-spacing: 0.02em;
    line-height: 1;
    margin: 0.6rem 0 1.2rem 0;
}
.cover-sub { font-size: 1.02rem; line-height: 1.8; max-width: 60ch; }

.intro-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 2.6rem;
    align-items: start;
}
.intro-photo {
    width: 100%;
    border-radius: 14px;
    display: block;
}

.timeline { border-left: 2px solid var(--hairline); padding-left: 1.6rem; }
.timeline-item { position: relative; padding-bottom: 2.2rem; }
.timeline-item:last-child { padding-bottom: 0; }
.timeline-item::before {
    content: "";
    position: absolute;
    left: -2.08rem;
    top: 0.45rem;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--green);
}
.timeline-head {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 0.4rem;
    align-items: baseline;
}
.timeline-org { font-weight: 600; color: var(--green-deep); font-size: 1.05rem; }
.timeline-period {
    font-weight: 600;
    font-size: 0.86rem;
    letter-spacing: 0.06em;
    color: var(--green);
}
.timeline-list { margin: 0.6rem 0 0 1.1rem; padding: 0; color: var(--ink); }
.timeline-list li { margin-bottom: 0.4rem; line-height: 1.7; }

.skill-panel {
    border: 1px solid var(--hairline);
    border-radius: 16px;
    padding: 1.6rem 1.3rem 1.2rem 1.3rem;
    margin-bottom: 1.4rem;
    background: var(--paper);
}
.skill-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    gap: 1.4rem 1rem;
}
.skill-item { text-align: center; }
.skill-item img { height: 48px; width: auto; max-width: 100%; object-fit: contain; }
.skill-item span {
    display: block;
    margin-top: 0.55rem;
    font-size: 0.8rem;
    color: var(--ink);
    line-height: 1.4;
}

.figure-grid {
    display: grid;
    gap: 1.6rem;
    margin-top: 1.2rem;
    align-items: start;
}
.figure-grid[data-columns="1"] { grid-template-columns: minmax(0, 1fr); max-width: 780px; }
.figure-grid[data-columns="2"] { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.figure-grid[data-columns="3"] { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.figure {
    display: flex;
    flex-direction: column;
    border: 1px solid var(--hairline);
    border-radius: 12px;
    overflow: hidden;
    background: var(--paper);
}
.figure img {
    width: 100%;
    display: block;
    max-height: 680px;
    object-fit: contain;
}
.figure figcaption {
    margin-top: auto;
    padding: 0.7rem 1rem;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    color: var(--green-deep);
    background: var(--cream);
}

.note-card {
    background: var(--cream);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-top: 1.2rem;
}
.note-card .subheading { margin-top: 0; }
.note-card .body-text { text-align: left; }

.data-table { width: 100%; border-collapse: collapse; margin-top: 1rem; font-size: 0.92rem; }
.data-table th, .data-table td {
    border: 1px solid var(--hairline);
    padding: 0.65rem 0.8rem;
    text-align: center;
    color: var(--ink);
}
.data-table thead th { background: var(--green); color: var(--cream); font-weight: 600; }
.data-table tbody th { text-align: left; font-weight: 500; color: var(--green-deep); }

.contact-panel {
    background: var(--green);
    border-radius: 18px;
    padding: clamp(1.8rem, 4vw, 3.2rem);
}
.contact-panel .display-title { color: var(--cream); }
.contact-panel .intro-photo { border-radius: 12px; }
.contact-panel .contact-list li { border-bottom: 1px solid rgba(255, 251, 219, 0.35); }
.contact-panel .contact-label { color: rgba(255, 251, 219, 0.75); }
.contact-panel .contact-value,
.contact-panel .contact-value a { color: var(--cream); }
.contact-grid {
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    gap: 2.6rem;
    align-items: center;
}
.contact-list { list-style: none; margin: 0; padding: 0; }
.contact-list li {
    padding: 0.85rem 0;
    border-bottom: 1px solid var(--hairline);
}
.contact-label {
    display: block;
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    color: var(--green);
    font-weight: 600;
    margin-bottom: 0.2rem;
}
.contact-value { font-size: 1.02rem; color: var(--green-deep); }
.contact-value a { color: var(--green-deep); text-decoration: underline; }

@media (max-width: 900px) {
    .intro-grid, .contact-grid { grid-template-columns: 1fr; gap: 1.8rem; }
    .body-text { text-align: left; }
    .figure-grid[data-columns] { grid-template-columns: minmax(0, 1fr); }
    .skill-item img { height: 40px; }
}
</style>
"""


@st.cache_data(show_spinner=False)
def encode_image(filename):
    path = IMAGE_DIR / filename
    suffix = "jpeg" if path.suffix.lower() in (".jpg", ".jpeg") else "png"
    return f"data:image/{suffix};base64," + base64.b64encode(path.read_bytes()).decode()


def figure(filename, caption=None):
    label = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (
        f'<figure class="figure"><img src="{encode_image(filename)}" alt="{caption or ""}">'
        f"{label}</figure>"
    )


def figure_grid(items, columns=1):
    body = "".join(figure(name, caption) for name, caption in items)
    st.markdown(
        f'<div class="figure-grid" data-columns="{columns}">{body}</div>',
        unsafe_allow_html=True,
    )


def page_rule():
    st.markdown('<div class="page-rule">2026</div>', unsafe_allow_html=True)


def display_title(text):
    st.markdown(f'<h1 class="display-title">{text}</h1>', unsafe_allow_html=True)


def section_label(text):
    st.markdown(f'<span class="section-label">{text}</span>', unsafe_allow_html=True)


def subheading(text):
    st.markdown(f'<p class="subheading">{text}</p>', unsafe_allow_html=True)


def body_text(text):
    st.markdown(f'<p class="body-text">{text}</p>', unsafe_allow_html=True)


def render_beranda():
    st.markdown(
        f"""
        <div class="cover">
            <div class="cover-year">2026</div>
            <div class="cover-title">PORTOFOLIO</div>
            <div class="cover-sub">Eka Sandy Aulia Puspitasari</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_tentang():
    page_rule()
    st.markdown(
        f"""
        <div class="intro-grid">
            <div>
                <h1 class="display-title">Halo, saya Eka Sandy<br>Aulia puspitasari</h1>
                <p class="body-text">Saya selalu penasaran bagaimana sebuah <strong>masalah</strong>
                dapat <strong>dipahami</strong> dan <strong>dipecahkan</strong> melalui
                <strong>data</strong> dan <strong>teknologi</strong>. Ketertarikan tersebut membentuk
                cara saya bekerja, mulai dari mengolah dan memastikan ketelitian data hingga mencari
                solusi dengan memanfaatkan tools dan teknologi yang terus berkembang.</p>
                <p class="body-text">Sebagai lulusan Sistem Informasi, saya memiliki pengalaman selama
                <strong>2 tahun</strong> sebagai <strong>Asisten Laboratorium</strong>,
                <strong>2 tahun</strong> dalam <strong>organisasi</strong>, serta mengikuti
                <strong>program pelatihan Asah by Dicoding × Accenture</strong>. Berbagai pengalaman
                tersebut membantu saya mengembangkan kemampuan dalam data, problem solving,
                komunikasi, koordinasi, dan bekerja secara terstruktur.</p>
            </div>
            <div><img class="intro-photo" src="{encode_image('profile.jpg')}" alt="Eka Sandy Aulia Puspitasari"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_pengalaman():
    page_rule()
    display_title("Pengalaman")
    items = []
    for experience in EXPERIENCES:
        bullets = "".join(f"<li>{detail}</li>" for detail in experience["detail"])
        items.append(
            '<div class="timeline-item">'
            '<div class="timeline-head">'
            f'<span class="timeline-org">{experience["organisasi"]}</span>'
            f'<span class="timeline-period">{experience["periode"]}</span>'
            "</div>"
            f'<ul class="timeline-list">{bullets}</ul>'
            "</div>"
        )
    st.markdown(f'<div class="timeline">{"".join(items)}</div>', unsafe_allow_html=True)


def render_skill():
    page_rule()
    display_title("Skill")
    for group in SKILL_GROUPS:
        cells = "".join(
            f'<div class="skill-item"><img src="{encode_image("logos/" + filename)}" alt="{name}">'
            f"<span>{name}</span></div>"
            for filename, name in group
        )
        st.markdown(
            f'<div class="skill-panel"><div class="skill-grid">{cells}</div></div>',
            unsafe_allow_html=True,
        )


def render_capstone():
    section_label("CAPSTONE 01")
    display_title("Website Mining Value Chain Pertambangan Batubara")
    body_text(
        "Mengembangkan website berbasis AI untuk mendukung digitalisasi dan pengambilan keputusan "
        "berbasis data di industri pertambangan, melalui prediksi produksi, optimasi pengiriman, "
        "dan AI chatbot."
    )
    figure_grid(
        [
            ("capstone01-dashboard-admin.png", "Dashboard Admin"),
            ("capstone01-user-management.png", "User Management"),
            ("capstone01-shipping-page.png", "Shipping Page"),
            ("capstone01-mining-page.png", "Mining Page"),
        ],
        columns=2,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    section_label("CAPSTONE 02")
    display_title("Machine Learning Engineer")

    subheading("Logika Pemrosesan Data")
    body_text(
        "Membangun logic pemrosesan data operasional tambang menggunakan Python, terintegrasi "
        "dengan database untuk mendukung dashboard monitoring."
    )
    figure_grid([("capstone02-logika-pemrosesan.png", None)])

    subheading("Logika Status Armada & Pengiriman")
    body_text(
        "Menentukan status armada & pengiriman berdasarkan kondisi cuaca dan kapasitas "
        "menggunakan Python."
    )
    figure_grid([("capstone02-logika-status.png", None)])

    subheading("Hasil Data Akhir PostgreSQL")
    body_text(
        "Mengolah dan menyimpan hasil pemrosesan logic Python ke PostgreSQL sebagai data final "
        "untuk kebutuhan dashboard monitoring."
    )
    figure_grid([("capstone02-postgresql.png", None)])


def render_tugas_akhir():
    section_label("TUGAS AKHIR | PYTHON · K-MEANS · STREAMLIT")
    display_title("Klasterisasi Provinsi Indonesia")
    figure_grid([("klasterisasi-dashboard.png", "Klasterisasi Adopsi Transaksi Digital")])

    subheading("Pemrosesan Data")
    figure_grid([("klasterisasi-pemrosesan.png", None)])

    subheading("Evaluasi Model K-Means")
    figure_grid([("klasterisasi-elbow.png", None)])

    subheading("Hasil Klasterisasi")
    rows = "".join(
        f"<tr><th>{cluster}</th>" + "".join(f"<td>{value}</td>" for value in values) + "</tr>"
        for cluster, values in CLUSTER_TABLE
    )
    st.markdown(
        f"""
        <table class="data-table">
            <thead>
                <tr><th>Klaster</th><th colspan="5">Jumlah Provinsi per Tahun</th></tr>
                <tr><th></th><th>2021</th><th>2022</th><th>2023</th><th>2024</th><th>2025</th></tr>
            </thead>
            <tbody>{rows}</tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )


def render_sml():
    section_label("SML 01")
    display_title("System Machine Learning")

    subheading("Melakukan Eksperimen Terhadap Dataset")
    figure_grid(
        [
            ("sml01-eksperimen.png", None),
            ("sml01-preprocessing.png", None),
            ("sml01-split.png", None),
        ],
        columns=3,
    )

    subheading("Membuat Automasi Prapemrosesan Data")
    figure_grid([("sml01-automasi.png", None)])
    body_text(
        "Melakukan preprocessing data untuk menangani missing values, duplikasi, scaling, outlier, "
        "dan encoding. Mengembangkan kode otomatisasi preprocessing menggunakan Python agar tahapan "
        "pengolahan data dapat dilakukan secara terstruktur. Menghasilkan data yang telah diproses "
        "dan membaginya menjadi data training dan testing untuk kebutuhan machine learning."
    )

    st.markdown("<br>", unsafe_allow_html=True)
    section_label("SML 02")
    display_title("System Machine Learning")

    subheading("Proses Training Model")
    figure_grid([("sml02-training.png", None)])

    subheading("Hasil / Artefak Model")
    figure_grid([("sml02-artefak.png", None)])
    body_text(
        "Melatih dan mengoptimalkan model machine learning menggunakan MLflow dengan manual "
        "logging, hyperparameter tuning, serta menyimpan metrik dan artefak tambahan untuk "
        "mendokumentasikan hasil eksperimen."
    )

    st.markdown("<br>", unsafe_allow_html=True)
    section_label("SML 03")
    display_title("System Machine Learning")

    subheading("Membuat Sistem Monitoring dan Logging")
    figure_grid(
        [
            ("sml03-prometheus.png", "Prometheus Monitoring"),
            ("sml03-alerting.png", "Grafana Alerting Rule"),
            ("sml03-dashboard.png", "Grafana Dashboard"),
            ("sml03-email-alert.png", "Grafana Dashboard"),
        ],
        columns=2,
    )


def render_laboratorium():
    section_label("LAB 01")
    display_title("Asisten Laboratorium")

    subheading("Modul Praktikum")
    body_text(
        "Menyiapkan modul dan materi pembelajaran untuk mendukung pelaksanaan praktikum mahasiswa."
    )
    figure_grid([("lab01-modul.png", None), ("lab01-silabus.png", None)], columns=2)

    subheading("Pelaksanaan Praktikum")
    body_text(
        "Mendampingi mahasiswa selama praktikum serta membantu menjelaskan penggunaan software "
        "dan menyelesaikan kendala teknis."
    )
    figure_grid([("lab01-praktikum-1.png", None), ("lab01-praktikum-2.png", None)], columns=2)

    st.markdown("<br>", unsafe_allow_html=True)
    section_label("LAB 02")

    subheading("Absensi & Nilai Praktikan")
    body_text(
        "Merekap kehadiran dan memasukkan nilai praktikan sebagai bagian dari administrasi "
        "kegiatan praktikum."
    )
    figure_grid([("lab02-absensi-nilai.png", None)])

    subheading("Validasi Absensi Asisten")
    body_text(
        "Melakukan validasi kehadiran asisten untuk memastikan data absensi tercatat dengan sesuai."
    )
    figure_grid([("lab02-validasi-absensi.png", None)])

    subheading("Reimbursement")
    body_text(
        "Mengelola dokumentasi reimbursement terkait kebutuhan operasional kegiatan praktikum."
    )
    figure_grid([("lab02-reimbursement.png", None)])

    subheading("Pengelolaan Laboratorium")
    body_text(
        "Mendukung pengecekan software, perangkat, dan fasilitas laboratorium untuk memastikan "
        "kegiatan praktikum berjalan dengan baik."
    )
    figure_grid([("lab02-pengelolaan.png", None)])


def render_kontak():
    page_rule()
    entries = []
    for label, value, url in CONTACTS:
        shown = f'<a href="{url}" target="_blank">{value}</a>' if url else value
        entries.append(
            f'<li><span class="contact-label">{label}</span>'
            f'<span class="contact-value">{shown}</span></li>'
        )
    st.markdown(
        f"""
        <div class="contact-panel">
            <div class="contact-grid">
                <div><img class="intro-photo" src="{encode_image('profile.jpg')}" alt="Eka Sandy Aulia Puspitasari"></div>
                <div>
                    <h1 class="display-title">Mari<br>Terhubung</h1>
                    <ul class="contact-list">{"".join(entries)}</ul>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


RENDERERS = {
    "Beranda": render_beranda,
    "Tentang Saya": render_tentang,
    "Pengalaman": render_pengalaman,
    "Skill": render_skill,
    "Capstone": render_capstone,
    "Tugas Akhir": render_tugas_akhir,
    "System Machine Learning": render_sml,
    "Asisten Laboratorium": render_laboratorium,
    "Mari Terhubung": render_kontak,
}


def main():
    st.set_page_config(
        page_title="Portofolio — Eka Sandy Aulia Puspitasari",
        page_icon="assets/images/profile.jpg",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(STYLES, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown(
            '<div class="sidebar-name">Eka Sandy Aulia Puspitasari</div>'
            '<div class="sidebar-meta">PORTOFOLIO 2026</div>',
            unsafe_allow_html=True,
        )
        selected = st.radio("Navigasi", SECTIONS, label_visibility="collapsed")
        st.markdown(
            '<div class="sidebar-foot">ekasandyaulia@gmail.com<br>'
            "+62 895 370 314 457</div>",
            unsafe_allow_html=True,
        )

    RENDERERS[selected]()


if __name__ == "__main__":
    main()
