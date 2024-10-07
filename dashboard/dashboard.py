import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
data = pd.read_csv(r"D:\belajar program\submission\data\all_data_bike.csv")

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

total_bike_usage = daily_bike_usage_df['bike_usage_count'].sum()
average_daily_usage = daily_bike_usage_df['bike_usage_count'].mean()

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Pengguna Sepeda", total_bike_usage)
with col2:
    st.metric("Rata-rata Pemakaian Harian", round(average_daily_usage, 2))

# Additional visualizations
# 1. Penggunaan Sepeda Berdasarkan Musim
season_usage_df = filtered_data.groupby('season').agg({
    "cnt_x": "sum"
}).reset_index()
season_usage_df.rename(columns={"cnt_x": "bike_usage_count"}, inplace=True)

st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="season", y="bike_usage_count", data=season_usage_df, palette="coolwarm", ax=ax)
ax.set_title("Penggunaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# 2. Penggunaan Sepeda Berdasarkan Hari dalam Seminggu
filtered_data['day_of_week'] = filtered_data['dteday'].dt.day_name()
day_usage_df = filtered_data.groupby('day_of_week').agg({
    "cnt_x": "sum"
}).reset_index()
day_usage_df.rename(columns={"cnt_x": "bike_usage_count"}, inplace=True)

st.subheader('Penggunaan Sepeda Berdasarkan Hari dalam Seminggu')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="day_of_week", y="bike_usage_count", data=day_usage_df, palette="magma", ax=ax)
ax.set_title("Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")
st.pyplot(fig)

# 3. Penggunaan Sepeda dan Suhu
st.subheader('Penggunaan Sepeda dan Suhu')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x="temp_x", y="cnt_x", data=filtered_data, hue="weathersit_x", palette="coolwarm", ax=ax)
ax.set_title("Penggunaan Sepeda dan Suhu")
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Penggunaan Sepeda")
st.pyplot(fig)

# 4. Penggunaan Sepeda Berdasarkan Bulan
filtered_data['month'] = filtered_data['dteday'].dt.month
month_usage_df = filtered_data.groupby('month').agg({
    "cnt_x": "sum"
}).reset_index()
month_usage_df.rename(columns={"cnt_x": "bike_usage_count"}, inplace=True)

st.subheader('Penggunaan Sepeda Berdasarkan Bulan')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x="month", y="bike_usage_count", data=month_usage_df, marker="o", ax=ax)
ax.set_title("Penggunaan Sepeda Berdasarkan Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penggunaan Sepeda")
st.pyplot(fig)