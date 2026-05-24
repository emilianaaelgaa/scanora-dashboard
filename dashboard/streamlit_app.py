import os
import base64
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

# PAGE CONFIG
st.set_page_config(
    page_title="Scanora Dashboard",
    page_icon="🍊",
    layout="wide"
)

# CUSTOM CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #FFFDF5 0%, #F4FAEE 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .main-header {
        background: linear-gradient(135deg, #FFF7D6 0%, #EAF7D6 55%, #FFF2E1 100%);
        padding: 36px 46px;
        border-radius: 28px;
        border: 2px solid #E5F2C9;
        box-shadow: 0 10px 28px rgba(85, 130, 45, 0.10);
        margin-bottom: 26px;
    }

    .title {
        font-size: 44px;
        font-weight: 900;
        color: #2F6B24;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }

    .subtitle {
        font-size: 19px;
        font-weight: 800;
        color: #F5A623;
        margin-top: 0;
        margin-bottom: 12px;
    }

    .desc {
        font-size: 16px;
        color: #52645A;
        line-height: 1.75;
        max-width: 100%;
        text-align: justify;
        text-justify: inter-word;
        margin-right: 4px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 900;
        color: #2F6B24;
        margin-top: 34px;
        margin-bottom: 6px;
    }

    .section-subtitle {
        font-size: 15px;
        color: #6B7B70;
        margin-bottom: 18px;
        line-height: 1.6;
    }

    .context-card {
        background: linear-gradient(135deg, #FFF4E8 0%, #FFF8EF 100%);
        padding: 24px 28px;
        border-radius: 24px;
        border: 1.5px solid #F6D9B8;
        box-shadow: 0 8px 20px rgba(222, 146, 74, 0.10);
        margin-top: 10px;
        margin-bottom: 18px;
    }

    .context-text {
        font-size: 15.5px;
        color: #4F5D57;
        line-height: 1.75;
        text-align: justify;
        margin: 0;
    }

    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 18px 18px;
        border-radius: 22px;
        border: 1.5px solid #E8F3D8;
        box-shadow: 0 8px 22px rgba(75, 120, 55, 0.08);
    }

    div[data-testid="stMetricLabel"] {
        font-size: 14px;
        color: #6B7B70;
        font-weight: 700;
    }

    div[data-testid="stMetricValue"] {
        font-size: 28px;
        color: #2F6B24;
        font-weight: 900;
    }

    .highlight-box {
        background: linear-gradient(135deg, #FFF7D6 0%, #FFFFFF 100%);
        padding: 18px 22px;
        border-radius: 20px;
        border-left: 7px solid #F5A623;
        box-shadow: 0 6px 18px rgba(245, 166, 35, 0.12);
        margin-top: 14px;
        margin-bottom: 20px;
        color: #39483F;
        font-size: 15px;
        line-height: 1.6;
    }

    .insight-card {
        background: #FFFFFF;
        padding: 20px 22px;
        border-radius: 22px;
        border: 1.5px solid #E8F3D8;
        box-shadow: 0 8px 22px rgba(75, 120, 55, 0.08);
        margin-bottom: 14px;
        min-height: 130px;
    }

    .insight-icon {
        font-size: 26px;
        margin-right: 8px;
    }

    .insight-title {
        font-size: 17px;
        font-weight: 900;
        color: #2F6B24;
        margin-bottom: 7px;
    }

    .insight-text {
        font-size: 15px;
        color: #4B5B52;
        line-height: 1.55;
    }

    .small-note {
        color: #6B7280;
        font-size: 14px;
        line-height: 1.5;
    }

    .preview-title {
        font-size: 22px;
        font-weight: 900;
        color: #2B2D3A;
        margin-top: 4px;
        margin-bottom: 18px;
    }

    .image-card {
        background: #FFFFFF;
        border: 1.5px solid #E8F3D8;
        border-radius: 22px;
        padding: 18px 16px 16px 16px;
        box-shadow: 0 8px 22px rgba(75, 120, 55, 0.10);
        margin-bottom: 24px;
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        min-height: 315px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .image-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(75, 120, 55, 0.16);
    }

    .image-wrapper {
        width: 100%;
        height: 190px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 12px;
    }

    .image-wrapper img {
        max-width: 190px;
        max-height: 180px;
        width: auto;
        height: auto;
        object-fit: contain;
        border-radius: 16px;
    }

    .image-caption {
        font-size: 14px;
        font-weight: 900;
        color: #2B2D3A;
        margin-top: 4px;
        margin-bottom: 10px;
    }

    .image-badge {
        display: inline-block;
        font-size: 12px;
        font-weight: 900;
        padding: 5px 12px;
        border-radius: 999px;
        margin: 0 auto;
        width: fit-content;
    }

    .badge-unripe {
        background-color: #FFF4D8;
        color: #B87900;
    }

    .badge-ripe {
        background-color: #EAF7D6;
        color: #2F6B24;
    }

    .badge-rotten {
        background-color: #FFE9DF;
        color: #C94F2D;
    }

    section[data-testid="stSidebar"] {
        background-color: #F6FAEF;
        border-right: 1px solid #E3EFD4;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 10px 18px;
        border: 1px solid #E6F1D8;
        font-weight: 800;
    }

    .stTabs [aria-selected="true"] {
        background-color: #EAF7D6;
        color: #2F6B24;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# COLOR PALETTE
scanora_colors = [
    "#7CB342",
    "#F5A623",
    "#FF7043",
    "#4CAF50",
    "#FFD54F",
    "#66BB6A",
    "#FFA726",
    "#8BC34A"
]

scanora_green = "#7CB342"

condition_order = ["unripe", "ripe", "rotten"]

condition_colors = {
    "unripe": "#F5A623",
    "ripe": "#7CB342",
    "rotten": "#FF7043"
}

# LOAD DATA
@st.cache_data
def load_image_metadata():
    file_path = "metadata_processed.csv"

    if not os.path.exists(file_path):
        return None

    return pd.read_csv(file_path)


@st.cache_data
def load_consumption_summary():
    file_path = "fruit_consumption_summary.csv"

    if not os.path.exists(file_path):
        return None

    return pd.read_csv(file_path)


df_image = load_image_metadata()
df_consumption = load_consumption_summary()

# HELPER FUNCTIONS
def check_columns(df, required_cols):
    if df is None:
        return False

    return all(col in df.columns for col in required_cols)


def format_number(value):
    if value is None or pd.isna(value):
        return "-"

    if isinstance(value, float):
        return f"{value:.3f}"

    return f"{value:,}"


def format_gram(value):
    if value is None or pd.isna(value):
        return "-"

    gram_value = value * 1000
    return f"{gram_value:.0f} gram"


def get_value_by_name(df, name):
    if df is None or len(df) == 0:
        return None

    if not check_columns(df, ["komoditas_buah", "rata_rata_konsumsi"]):
        return None

    temp_df = df.copy()
    temp_df["komoditas_buah"] = temp_df["komoditas_buah"].astype(str).str.strip().str.lower()

    row = temp_df[temp_df["komoditas_buah"] == name.strip().lower()]

    if len(row) == 0:
        return None

    return row["rata_rata_konsumsi"].iloc[0]


def prepare_consumption_data(df):
    if df is None:
        return None, None

    if not check_columns(df, ["komoditas_buah", "rata_rata_konsumsi"]):
        return None, None

    data = df.copy()

    data["komoditas_buah"] = data["komoditas_buah"].astype(str).str.strip()
    data["rata_rata_konsumsi"] = pd.to_numeric(
        data["rata_rata_konsumsi"],
        errors="coerce"
    )

    data = data.dropna(subset=["rata_rata_konsumsi"])

    pisang = get_value_by_name(data, "Pisang")
    apel = get_value_by_name(data, "Apel")
    jeruk = get_value_by_name(data, "Jeruk")

    if pisang is None:
        pisang_ambon = get_value_by_name(data, "Pisang ambon")
        pisang_lainnya = get_value_by_name(data, "Pisang lainnya")

        total_pisang = 0
        ada_pisang = False

        if pisang_ambon is not None:
            total_pisang += pisang_ambon
            ada_pisang = True

        if pisang_lainnya is not None:
            total_pisang += pisang_lainnya
            ada_pisang = True

        if ada_pisang:
            pisang = total_pisang

    if jeruk is None:
        jeruk = get_value_by_name(data, "Jeruk, jeruk bali")

    target_rows = []

    if pisang is not None:
        target_rows.append({
            "komoditas_buah": "Pisang",
            "rata_rata_konsumsi": pisang
        })

    if apel is not None:
        target_rows.append({
            "komoditas_buah": "Apel",
            "rata_rata_konsumsi": apel
        })

    if jeruk is not None:
        target_rows.append({
            "komoditas_buah": "Jeruk",
            "rata_rata_konsumsi": jeruk
        })

    df_target = pd.DataFrame(target_rows)

    if len(df_target) > 0:
        df_target = df_target.sort_values(
            "rata_rata_konsumsi",
            ascending=False
        ).reset_index(drop=True)

    return data, df_target


def create_fruit_insight(fruit_count, selected_fruit, selected_condition):
    if len(fruit_count) == 0:
        return "Insight belum dapat ditampilkan karena data tidak tersedia."

    total = int(fruit_count["jumlah"].sum())

    if selected_fruit == "Semua" and selected_condition == "Semua":
        most_fruit = fruit_count.iloc[0]
        least_fruit = fruit_count.iloc[-1]
        return (
            f"Fruits image dataset paling banyak berisi gambar <b>{most_fruit['fruit']}</b> "
            f"sebanyak <b>{most_fruit['jumlah']:,}</b> gambar, sedangkan jumlah paling sedikit "
            f"terdapat pada <b>{least_fruit['fruit']}</b> sebanyak <b>{least_fruit['jumlah']:,}</b> gambar."
        )

    if selected_fruit != "Semua" and selected_condition == "Semua":
        return (
            f"Buah <b>{selected_fruit}</b> memiliki total <b>{total:,}</b> gambar "
            f"dalam fruits image dataset."
        )

    if selected_fruit == "Semua" and selected_condition != "Semua":
        most_fruit = fruit_count.iloc[0]
        return (
            f"Pada kondisi <b>{selected_condition}</b>, jenis buah dengan jumlah gambar terbanyak adalah "
            f"<b>{most_fruit['fruit']}</b> sebanyak <b>{most_fruit['jumlah']:,}</b> gambar."
        )

    return (
        f"Kombinasi <b>{selected_fruit}</b> dengan kondisi <b>{selected_condition}</b> "
        f"memiliki total <b>{total:,}</b> gambar dalam fruits image dataset."
    )


def create_condition_insight(condition_count, selected_fruit, selected_condition):
    if len(condition_count) == 0:
        return "Insight belum dapat ditampilkan karena data tidak tersedia."

    total = int(condition_count["jumlah"].sum())

    if selected_fruit == "Semua" and selected_condition == "Semua":
        most_condition = condition_count.iloc[0]
        least_condition = condition_count.iloc[-1]
        return (
            f"Kondisi <b>{most_condition['condition']}</b> memiliki jumlah gambar terbanyak "
            f"sebanyak <b>{most_condition['jumlah']:,}</b> gambar, sedangkan kondisi "
            f"<b>{least_condition['condition']}</b> memiliki jumlah paling sedikit sebanyak "
            f"<b>{least_condition['jumlah']:,}</b> gambar."
        )

    if selected_fruit != "Semua" and selected_condition == "Semua":
        most_condition = condition_count.iloc[0]
        return (
            f"Pada buah <b>{selected_fruit}</b>, kondisi <b>{most_condition['condition']}</b> "
            f"memiliki jumlah gambar terbanyak sebanyak <b>{most_condition['jumlah']:,}</b> gambar."
        )

    if selected_fruit == "Semua" and selected_condition != "Semua":
        return (
            f"Kondisi <b>{selected_condition}</b> memiliki total <b>{total:,}</b> gambar "
            f"dalam fruits image dataset."
        )

    return (
        f"Buah <b>{selected_fruit}</b> dengan kondisi <b>{selected_condition}</b> "
        f"memiliki total <b>{total:,}</b> gambar."
    )


def create_label_insight(label_count, selected_fruit, selected_condition):
    if len(label_count) == 0:
        return "Insight belum dapat ditampilkan karena data tidak tersedia."

    total = int(label_count["jumlah"].sum())

    if selected_fruit == "Semua" and selected_condition == "Semua":
        max_label = label_count.iloc[0]
        min_label = label_count.iloc[-1]
        return (
            f"Kombinasi kelas terbesar adalah <b>{max_label['label']}</b> sebanyak "
            f"<b>{max_label['jumlah']:,}</b> gambar, sedangkan kombinasi terkecil adalah "
            f"<b>{min_label['label']}</b> sebanyak <b>{min_label['jumlah']:,}</b> gambar."
        )

    if selected_fruit != "Semua" and selected_condition == "Semua":
        max_label = label_count.iloc[0]
        return (
            f"Pada buah <b>{selected_fruit}</b>, kombinasi kelas terbesar adalah "
            f"<b>{max_label['label']}</b> sebanyak <b>{max_label['jumlah']:,}</b> gambar."
        )

    if selected_fruit == "Semua" and selected_condition != "Semua":
        max_label = label_count.iloc[0]
        return (
            f"Pada kondisi <b>{selected_condition}</b>, kombinasi kelas terbesar adalah "
            f"<b>{max_label['label']}</b> sebanyak <b>{max_label['jumlah']:,}</b> gambar."
        )

    return (
        f"Kombinasi kelas <b>{selected_fruit}_{selected_condition}</b> memiliki total "
        f"<b>{total:,}</b> gambar."
    )


def get_preview_images(selected_fruit, selected_condition):
    image_dir = Path(__file__).parent / "image"

    fruits = ["apple", "banana", "orange"]
    conditions = condition_order
    image_numbers = [1, 2, 3]
    extensions = ["png", "jpg", "jpeg"]

    if selected_fruit != "Semua":
        fruits = [selected_fruit]

    if selected_condition != "Semua":
        conditions = [selected_condition]

    image_paths = []

    for fruit in fruits:
        for condition in conditions:
            for number in image_numbers:
                for ext in extensions:
                    image_path = image_dir / f"{fruit}_{condition}_{number}.{ext}"

                    if image_path.exists():
                        image_paths.append(image_path)
                        break

    return image_paths


def image_to_base64(image_path):
    suffix = image_path.suffix.lower().replace(".", "")

    if suffix == "jpg":
        suffix = "jpeg"

    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    return f"data:image/{suffix};base64,{encoded}"


def show_preview_images(image_paths):
    if len(image_paths) == 0:
        st.info("Gambar preview belum ditemukan. Pastikan file gambar sudah tersedia di folder `dashboard/image`.")
        return

    for start_idx in range(0, len(image_paths), 3):
        cols = st.columns(3)

        for col, image_path in zip(cols, image_paths[start_idx:start_idx + 3]):
            file_name = image_path.stem
            parts = file_name.split("_")

            if len(parts) >= 3:
                fruit = parts[0].title()
                condition = parts[1].lower()
                number = parts[2]

                caption = f"{fruit} #{number}"
                condition_label = condition.title()
                badge_class = f"badge-{condition}"
            else:
                caption = file_name.replace("_", " ").title()
                condition_label = "-"
                badge_class = "badge-ripe"

            with col:
                st.markdown(
                    f"""
                    <div class="image-card">
                        <div class="image-wrapper">
                            <img src="{image_to_base64(image_path)}" alt="{caption}">
                        </div>
                        <div class="image-caption">{caption}</div>
                        <div class="image-badge {badge_class}">{condition_label}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


df_consumption_plot, df_target_consumption = prepare_consumption_data(df_consumption)

# HEADER
st.markdown(
    """
    <div class="main-header">
        <div class="title">🍊 Scanora Dashboard</div>
        <div class="subtitle">Fruit Freshness & Consumption Insight</div>
        <div class="desc">
            Dashboard ini menampilkan hasil eksplorasi fruits image dataset dan fruits consumption dataset.
            Analisis ini digunakan untuk memahami distribusi data buah, kondisi kesegaran, komposisi kelas,
            serta melihat peluang pengembangan fitur deteksi kesegaran Scanora berdasarkan pola konsumsi buah.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# DATA WARNING
if df_image is None:
    st.warning("File `metadata_processed.csv` belum ditemukan di folder project.")

if df_consumption is None:
    st.warning("File `fruit_consumption_summary.csv` belum ditemukan di folder project.")

# SIDEBAR
st.sidebar.title("⚙️ Filter Dashboard")

st.sidebar.markdown("### Fruits Image Dataset")

if df_image is not None and check_columns(df_image, ["fruit", "condition", "label"]):
    fruit_options = ["Semua"] + sorted(df_image["fruit"].dropna().unique().tolist())

    available_conditions = df_image["condition"].dropna().unique().tolist()
    condition_options = ["Semua"] + [
        condition for condition in condition_order
        if condition in available_conditions
    ]

    selected_fruit = st.sidebar.selectbox("Pilih jenis buah", fruit_options)
    selected_condition = st.sidebar.selectbox("Pilih kondisi buah", condition_options)

    df_image_filtered = df_image.copy()

    if selected_fruit != "Semua":
        df_image_filtered = df_image_filtered[df_image_filtered["fruit"] == selected_fruit]

    if selected_condition != "Semua":
        df_image_filtered = df_image_filtered[df_image_filtered["condition"] == selected_condition]
else:
    selected_fruit = "Semua"
    selected_condition = "Semua"
    df_image_filtered = df_image


st.sidebar.markdown("### Fruits Consumption Dataset")

if df_consumption_plot is not None:
    top_n = st.sidebar.slider(
        "Jumlah komoditas buah teratas",
        min_value=5,
        max_value=20,
        value=10
    )
else:
    top_n = 10

# WHY THIS ANALYSIS MATTERS
st.markdown('<div class="section-title">Why This Analysis Matters?</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="context-card">
        <div class="context-text">
            Menilai kesegaran buah memang terlihat sederhana, tetapi pada praktiknya tidak selalu mudah. 
            Perbedaan warna kulit, tekstur, tingkat kematangan, hingga tanda kerusakan membuat penilaian visual sering kali tidak konsisten. 
            Scanora hadir untuk membantu proses tersebut melalui fitur deteksi kesegaran berbasis gambar. 
            Karena itu, analisis ini dilakukan untuk melihat sejauh mana fruits image dataset mampu merepresentasikan jenis buah, kondisi kesegaran, dan komposisi kelas yang dibutuhkan, sekaligus menempatkan buah target Scanora dalam konteks pola konsumsi masyarakat melalui fruits consumption dataset.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# KPI CARDS
st.markdown('<div class="section-title">Overview Dataset</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Sebelum masuk ke detail visualisasi, bagian ini memberikan gambaran cepat tentang cakupan data yang digunakan. Angka-angka berikut membantu melihat seberapa luas fruits image dataset dan bagaimana posisi konsumsi buah target Scanora dalam fruits consumption dataset.</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

if df_image_filtered is not None and check_columns(df_image_filtered, ["fruit", "condition", "label"]):
    col1.metric("Total Gambar", f"{len(df_image_filtered):,}")
    col2.metric("Jenis Buah", df_image_filtered["fruit"].nunique())
    col3.metric("Kondisi Buah", df_image_filtered["condition"].nunique())
    col4.metric("Kombinasi Kelas", df_image_filtered["label"].nunique())
else:
    col1.metric("Total Gambar", "-")
    col2.metric("Jenis Buah", "-")
    col3.metric("Kondisi Buah", "-")
    col4.metric("Kombinasi Kelas", "-")


if df_target_consumption is not None and len(df_target_consumption) > 0:
    st.markdown("")
    col5, col6, col7 = st.columns(3)

    pisang_value = get_value_by_name(df_target_consumption, "Pisang")
    apel_value = get_value_by_name(df_target_consumption, "Apel")
    jeruk_value = get_value_by_name(df_target_consumption, "Jeruk")

    col5.metric("🍌 Rata-Rata Konsumsi Pisang", format_gram(pisang_value), "per kapita/minggu")
    col6.metric("🍎 Rata-Rata Konsumsi Apel", format_gram(apel_value), "per kapita/minggu")
    col7.metric("🍊 Rata-Rata Konsumsi Jeruk", format_gram(jeruk_value), "per kapita/minggu")

    st.markdown(
        """
        <p class="small-note">
        Nilai konsumsi ditampilkan dalam gram per kapita per minggu agar lebih mudah dibaca.
        Data konsumsi mengacu pada fruits consumption dataset BPS 2025.
        </p>
        """,
        unsafe_allow_html=True
    )

# DATASET GAMBAR
st.markdown('<div class="section-title">Fruits Image Dataset</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Setelah mengetahui cakupan data secara umum, bagian ini melihat isi fruits image dataset lebih dekat: bagaimana gambar tersebar berdasarkan jenis buah, kondisi kesegaran, dan kombinasi kelas.</div>',
    unsafe_allow_html=True
)

if df_image_filtered is not None and check_columns(df_image_filtered, ["fruit", "condition", "label"]):

    tab1, tab2, tab3, tab_preview = st.tabs(
        [
            "Distribusi Jenis Buah",
            "Distribusi Kondisi Buah",
            "Kombinasi Kelas",
            "Image Preview"
        ]
    )

    with tab1:
        fruit_count = (
            df_image_filtered["fruit"]
            .value_counts()
            .reset_index()
        )
        fruit_count.columns = ["fruit", "jumlah"]

        col_bar, col_pie = st.columns([1.2, 1])

        with col_bar:
            fig_fruit = px.bar(
                fruit_count,
                x="fruit",
                y="jumlah",
                text="jumlah",
                title="Distribusi Jumlah Gambar Berdasarkan Jenis Buah",
                labels={
                    "fruit": "Jenis Buah",
                    "jumlah": "Jumlah Gambar"
                }
            )

            fig_fruit.update_traces(
                marker_color=scanora_green,
                textposition="outside",
                hovertemplate="<b>Jenis Buah</b> = %{x}<br><b>Jumlah Gambar</b> = %{y:,}<extra></extra>"
            )

            fig_fruit.update_layout(
                height=460,
                showlegend=False,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig_fruit, use_container_width=True)

        with col_pie:
            fig_fruit_pie = px.pie(
                fruit_count,
                names="fruit",
                values="jumlah",
                title="Proporsi Dataset Berdasarkan Jenis Buah",
                hole=0.45,
                color_discrete_sequence=scanora_colors
            )

            fig_fruit_pie.update_traces(
                hovertemplate="<b>Jenis Buah</b> = %{label}<br><b>Jumlah Gambar</b> = %{value:,}<extra></extra>"
            )

            fig_fruit_pie.update_layout(
                height=460,
                paper_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig_fruit_pie, use_container_width=True)

        if len(fruit_count) > 0:
            insight_text = create_fruit_insight(fruit_count, selected_fruit, selected_condition)

            st.markdown(
                f"""
                <div class="highlight-box">
                    <b>Insight:</b> {insight_text}
                </div>
                """,
                unsafe_allow_html=True
            )

    with tab2:
        condition_count = (
            df_image_filtered["condition"]
            .value_counts()
            .reset_index()
        )
        condition_count.columns = ["condition", "jumlah"]

        condition_count["condition"] = pd.Categorical(
            condition_count["condition"],
            categories=condition_order,
            ordered=True
        )
        condition_count = condition_count.sort_values("condition")

        col_a, col_b = st.columns([1.2, 1])

        with col_a:
            fig_condition_bar = px.bar(
                condition_count,
                x="condition",
                y="jumlah",
                text="jumlah",
                title="Distribusi Jumlah Gambar Berdasarkan Kondisi Buah",
                labels={
                    "condition": "Kondisi Buah",
                    "jumlah": "Jumlah Gambar"
                }
            )

            fig_condition_bar.update_traces(
                marker_color=scanora_green,
                textposition="outside",
                hovertemplate="<b>Kondisi Buah</b> = %{x}<br><b>Jumlah Gambar</b> = %{y:,}<extra></extra>"
            )

            fig_condition_bar.update_layout(
                height=460,
                showlegend=False,
                xaxis={"categoryorder": "array", "categoryarray": condition_order},
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig_condition_bar, use_container_width=True)

        with col_b:
            fig_condition_pie = px.pie(
                condition_count,
                names="condition",
                values="jumlah",
                title="Proporsi Kondisi Buah",
                hole=0.45,
                color_discrete_sequence=scanora_colors
            )

            fig_condition_pie.update_traces(
                hovertemplate="<b>Kondisi Buah</b> = %{label}<br><b>Jumlah Gambar</b> = %{value:,}<extra></extra>"
            )

            fig_condition_pie.update_layout(
                height=460,
                paper_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig_condition_pie, use_container_width=True)

        if len(condition_count) > 0:
            insight_text = create_condition_insight(condition_count, selected_fruit, selected_condition)

            st.markdown(
                f"""
                <div class="highlight-box">
                    <b>Insight:</b> {insight_text}
                </div>
                """,
                unsafe_allow_html=True
            )

    with tab3:
        label_count = (
            df_image_filtered["label"]
            .value_counts()
            .reset_index()
        )
        label_count.columns = ["label", "jumlah"]

        fig_label = px.bar(
            label_count,
            x="label",
            y="jumlah",
            text="jumlah",
            title="Distribusi Jumlah Gambar Berdasarkan Kombinasi Kelas",
            labels={
                "label": "Kombinasi Kelas",
                "jumlah": "Jumlah Gambar"
            }
        )

        fig_label.update_traces(
            marker_color=scanora_green,
            textposition="outside",
            hovertemplate="<b>Kombinasi Kelas</b> = %{x}<br><b>Jumlah Gambar</b> = %{y:,}<extra></extra>"
        )

        fig_label.update_layout(
            height=500,
            showlegend=False,
            xaxis_tickangle=-35,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig_label, use_container_width=True)

        col_stacked, col_heatmap = st.columns([1.25, 1])

        with col_stacked:
            stacked_data = (
                df_image_filtered
                .groupby(["fruit", "condition"])
                .size()
                .reset_index(name="jumlah")
            )

            stacked_data["condition"] = pd.Categorical(
                stacked_data["condition"],
                categories=condition_order,
                ordered=True
            )
            stacked_data = stacked_data.sort_values(["fruit", "condition"])

            fig_stacked = px.bar(
                stacked_data,
                x="fruit",
                y="jumlah",
                color="condition",
                title="Distribusi Kondisi Kesegaran pada Setiap Jenis Buah",
                labels={
                    "fruit": "Jenis Buah",
                    "condition": "Kondisi Buah",
                    "jumlah": "Jumlah Gambar"
                },
                color_discrete_map=condition_colors,
                category_orders={"condition": condition_order}
            )

            fig_stacked.update_traces(
                hovertemplate="<b>Jenis Buah</b> = %{x}<br><b>Kondisi Buah</b> = %{fullData.name}<br><b>Jumlah Gambar</b> = %{y:,}<extra></extra>"
            )

            fig_stacked.update_layout(
                barmode="stack",
                height=500,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                legend_title_text="Kondisi Buah"
            )

            st.plotly_chart(fig_stacked, use_container_width=True)

        with col_heatmap:
            heatmap_data = pd.crosstab(
                df_image_filtered["fruit"],
                df_image_filtered["condition"]
            )

            heatmap_data = heatmap_data.reindex(
                columns=[col for col in condition_order if col in heatmap_data.columns]
            )

            fig_heatmap = px.imshow(
                heatmap_data,
                text_auto=True,
                title="Heatmap Jenis Buah dan Kondisi",
                labels=dict(
                    x="Kondisi Buah",
                    y="Jenis Buah",
                    color="Jumlah Gambar"
                ),
                color_continuous_scale=["#FFF7D6", "#F5A623", "#7CB342"]
            )

            fig_heatmap.update_traces(
                hovertemplate="<b>Jenis Buah</b> = %{y}<br><b>Kondisi Buah</b> = %{x}<br><b>Jumlah Gambar</b> = %{z:,}<extra></extra>"
            )

            fig_heatmap.update_layout(
                height=500,
                paper_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig_heatmap, use_container_width=True)

        if len(label_count) > 0:
            insight_text = create_label_insight(label_count, selected_fruit, selected_condition)

            st.markdown(
                f"""
                <div class="highlight-box">
                    <b>Insight:</b> {insight_text}
                </div>
                """,
                unsafe_allow_html=True
            )

    with tab_preview:
        preview_images = get_preview_images(selected_fruit, selected_condition)

        st.markdown(
            '<div class="preview-title">Sample Image Preview</div>',
            unsafe_allow_html=True
        )

        show_preview_images(preview_images)

else:
    st.info("Dataset gambar belum tersedia atau kolom `fruit`, `condition`, dan `label` belum ditemukan.")

# DATA KONSUMSI BUAH
st.markdown('<div class="section-title">Fruits Consumption Dataset</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Setelah memahami komposisi fruits image dataset, analisis dilanjutkan dengan melihat konteks konsumsi buah. Fruits consumption dataset membantu menunjukkan posisi pisang, apel, dan jeruk dibandingkan komoditas buah lainnya, sehingga pengembangan Scanora dapat dikaitkan dengan pola konsumsi masyarakat.</div>',
    unsafe_allow_html=True
)

if df_consumption_plot is not None and check_columns(df_consumption_plot, ["komoditas_buah", "rata_rata_konsumsi"]):

    col_c, col_d = st.columns([1, 1.2])

    with col_c:
        if df_target_consumption is not None and len(df_target_consumption) > 0:
            fig_target = px.bar(
                df_target_consumption,
                x="komoditas_buah",
                y="rata_rata_konsumsi",
                text="rata_rata_konsumsi",
                title="Rata-Rata Konsumsi Buah Target Scanora",
                labels={
                    "komoditas_buah": "Komoditas Buah",
                    "rata_rata_konsumsi": "Rata-Rata Konsumsi (Kg)"
                }
            )

            fig_target.update_traces(
                marker_color=scanora_green,
                texttemplate="%{text:.3f}",
                textposition="outside",
                hovertemplate="<b>Komoditas Buah</b> = %{x}<br><b>Rata-Rata Konsumsi</b> = %{y:.3f} kg/kapita/minggu<extra></extra>"
            )

            fig_target.update_layout(
                height=460,
                showlegend=False,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig_target, use_container_width=True)
        else:
            st.info("Data konsumsi Pisang, Apel, atau Jeruk belum ditemukan.")

    with col_d:
        top_consumption = (
            df_consumption_plot
            .sort_values("rata_rata_konsumsi", ascending=False)
            .head(top_n)
        )

        fig_top = px.bar(
            top_consumption,
            x="rata_rata_konsumsi",
            y="komoditas_buah",
            orientation="h",
            text="rata_rata_konsumsi",
            title=f"Top {top_n} Komoditas Buah Berdasarkan Rata-rata Konsumsi",
            labels={
                "komoditas_buah": "Komoditas Buah",
                "rata_rata_konsumsi": "Rata-Rata Konsumsi (Kg)"
            },
            color="rata_rata_konsumsi",
            color_continuous_scale=["#FFF7D6", "#F5A623", "#7CB342"]
        )

        fig_top.update_traces(
            texttemplate="%{text:.3f}",
            textposition="outside",
            hovertemplate="<b>Komoditas Buah</b> = %{y}<br><b>Rata-Rata Konsumsi</b> = %{x:.3f} kg/kapita/minggu<extra></extra>"
        )

        fig_top.update_layout(
            height=460,
            yaxis={"categoryorder": "total ascending"},
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            coloraxis_colorbar=dict(
                title="Rata-Rata Konsumsi (Kg)"
            )
        )

        st.plotly_chart(fig_top, use_container_width=True)

    if df_target_consumption is not None and len(df_target_consumption) > 0:
        highest_target = df_target_consumption.iloc[0]

        st.markdown(
            f"""
            <div class="highlight-box">
                <b>Insight:</b> Di antara buah target Scanora, rata-rata konsumsi tertinggi terdapat pada 
                <b>{highest_target['komoditas_buah']}</b> dengan nilai rata-rata 
                <b>{highest_target['rata_rata_konsumsi']:.3f} kg/kapita/minggu</b>. 
                Hasil ini menunjukkan bahwa buah tersebut memiliki relevansi kuat sebagai salah satu fokus 
                pengembangan fitur deteksi kesegaran.
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.info("Dataset konsumsi buah belum tersedia atau kolom `komoditas_buah` dan `rata_rata_konsumsi` belum ditemukan.")

# KEY INSIGHTS
st.markdown('<div class="section-title">Key Insights</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Bagian ini merangkum temuan utama dari analisis data gambar dan data konsumsi agar insight yang paling penting lebih mudah ditangkap.</div>',
    unsafe_allow_html=True
)

insight_cards = []

if df_image is not None and check_columns(df_image, ["fruit", "condition", "label"]):
    fruit_all = df_image["fruit"].value_counts()
    condition_all = df_image["condition"].value_counts()
    label_all = df_image["label"].value_counts()

    if len(fruit_all) > 0:
        insight_cards.append({
            "icon": "🍎",
            "title": "Jenis Buah Paling Dominan",
            "text": f"Fruits image dataset paling banyak berisi buah {fruit_all.index[0]} dengan {fruit_all.iloc[0]:,} gambar."
        })

    if len(condition_all) > 0:
        insight_cards.append({
            "icon": "🌱",
            "title": "Kondisi Buah Paling Dominan",
            "text": f"Kondisi buah yang paling dominan adalah {condition_all.index[0]} dengan {condition_all.iloc[0]:,} gambar."
        })

    if len(label_all) > 0:
        insight_cards.append({
            "icon": "📊",
            "title": "Kombinasi Kelas Dataset",
            "text": f"Kombinasi kelas terbesar adalah {label_all.index[0]}, sedangkan kombinasi terkecil adalah {label_all.index[-1]}."
        })

if df_consumption_plot is not None and check_columns(df_consumption_plot, ["komoditas_buah", "rata_rata_konsumsi"]):
    df_rank = df_consumption_plot.sort_values(
        "rata_rata_konsumsi",
        ascending=False
    )

    if len(df_rank) > 0:
        insight_cards.append({
            "icon": "🏆",
            "title": "Komoditas Konsumsi Tertinggi",
            "text": f"Komoditas buah dengan rata-rata konsumsi tertinggi adalah {df_rank.iloc[0]['komoditas_buah']}."
        })

    if df_target_consumption is not None and len(df_target_consumption) > 0:
        insight_cards.append({
            "icon": "🍌",
            "title": "Buah Target Scanora",
            "text": f"Di antara buah target Scanora, konsumsi tertinggi terdapat pada {df_target_consumption.iloc[0]['komoditas_buah']}."
        })

if len(insight_cards) > 0:
    cols = st.columns(2)

    for idx, item in enumerate(insight_cards):
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="insight-card">
                    <div class="insight-title">
                        <span class="insight-icon">{item['icon']}</span>{item['title']}
                    </div>
                    <div class="insight-text">{item['text']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.info("Insight belum dapat ditampilkan karena data belum lengkap.")

# FOOTER
st.markdown("---")
st.markdown(
    """
    <p class="small-note">
    Dashboard ini dibuat untuk mendukung proses analisis Scanora. 
    Fruits image dataset digunakan untuk memahami karakteristik data model, sedangkan fruits consumption dataset digunakan sebagai konteks tambahan dalam menentukan relevansi dan peluang pengembangan fitur.
    </p>
    """,
    unsafe_allow_html=True
)
