import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# URL dataset dari GitHub (pastikan URL adalah versi raw file)
url = 'https://raw.githubusercontent.com/ilhamhaikal/file/main/all_data_bike.csv'

# Load data langsung dari URL
data = pd.read_csv(url)

# Convert 'dteday' to datetime
data['dteday'] = pd.to_datetime(data['dteday'])

# Menyiapkan rentang waktu
min_date = data['dteday'].min()
max_date = data['dteday'].max()

# Sidebar untuk filter tanggal
with st.sidebar:
    st.header('Select Date Range')
    start_date, end_date = st.date_input(
        label="Select Date Range",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data sesuai rentang waktu
filtered_data = data[(data['dteday'] >= pd.to_datetime(start_date)) & (data['dteday'] <= pd.to_datetime(end_date))]

# Mapping nama cuaca dan musim
weather_mapping = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain'}
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}

# Mengganti nilai angka dengan nama di kolom cuaca dan musim
filtered_data['weathersit_x'] = filtered_data['weathersit_x'].map(weather_mapping)
filtered_data['season'] = filtered_data['season'].map(season_mapping)

# Daily Bike Users
def create_daily_bike_usage_df(df):
    daily_bike_usage_df = df.resample(rule='D', on='dteday').agg({
        "cnt_x": "sum"
    }).reset_index()
    daily_bike_usage_df.rename(columns={
        "cnt_x": "bike_usage_count"
    }, inplace=True)
    return daily_bike_usage_df

daily_bike_usage_df = create_daily_bike_usage_df(filtered_data)

# Visualisasi Pengguna Sepeda Setiap Hari
st.header('Pengguna Sepeda Setiap Hari')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(daily_bike_usage_df['dteday'], daily_bike_usage_df['bike_usage_count'], marker='o', linewidth=2, color="#90CAF9")
ax.set_xlabel('Tanggal')
ax.set_ylabel('Total Penggunaan Sepeda')
ax.set_title('Total Penggunaan Sepeda dari Waktu ke Waktu')
st.pyplot(fig)

# Pengelompokan Berdasarkan Kondisi Cuaca
weather_usage_df = filtered_data.groupby('weathersit_x').agg({
    "cnt_x": "sum"
}).reset_index()
weather_usage_df.rename(columns={"cnt_x": "bike_usage_count"}, inplace=True)

# Visualisasi Cuaca dan Penggunaan Sepeda
st.subheader('Penggunaan Sepeda Berdasarkan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="weathersit_x", y="bike_usage_count", data=weather_usage_df, palette="Blues_d", ax=ax)
ax.set_title("Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

# Penggunaan Sepeda Berdasarkan Musim
season_usage_df = filtered_data.groupby('season').agg({
    "cnt_x": "sum"
}).reset_index()
season_usage_df.rename(columns={"cnt_x": "bike_usage_count"}, inplace=True)

st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="season", y="bike_usage_count", data=season_usage_df, palette="coolwarm", ax=ax)
ax.set_title("Penggunaan Sepeda Berdasarkan Musim")
st.pyplot(fig)
