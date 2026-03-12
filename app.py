# -------------------------------------------------
# Import Libraries
# -------------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(page_title="YouTube Social Media Dashboard", layout="wide")

st.title("📊 YouTube Social Media Analytics Dashboard")

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\YouTube_Social_Media_Anlytics_Project\data\raw\youtube_data.csv")

    # Fix datatype issues
    df = df.convert_dtypes()

    # Convert date column
    df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")

    return df

df = load_data()

# -------------------------------------------------
# Dataset Overview
# -------------------------------------------------
st.header("Dataset Overview")

col1, col2 = st.columns(2)

col1.metric("Total Videos", len(df))
col2.metric("Total Channels", df["channel"].nunique())

st.write(df)

# -------------------------------------------------
# GRAPH 1: Videos per Channel
# -------------------------------------------------
st.header("Top Active Channels")

channel_counts = df["channel"].value_counts().head(10)

fig1, ax1 = plt.subplots()

sns.barplot(x=channel_counts.values, y=channel_counts.index, ax=ax1)

ax1.set_xlabel("Number of Videos")
ax1.set_ylabel("Channel")

st.pyplot(fig1)

# -------------------------------------------------
# GRAPH 2: Videos Published Per Year
# -------------------------------------------------
st.header("Videos Published Per Year")

df["year"] = df["published_at"].dt.year

year_counts = df["year"].value_counts().sort_index()

fig2, ax2 = plt.subplots()

year_counts.plot(kind="bar", ax=ax2)

ax2.set_xlabel("Year")
ax2.set_ylabel("Number of Videos")

st.pyplot(fig2)

# -------------------------------------------------
# GRAPH 3: Channel Distribution
# -------------------------------------------------
st.header("Channel Distribution")

fig3, ax3 = plt.subplots()

df["channel"].value_counts().head(5).plot(kind="pie", autopct="%1.1f%%", ax=ax3)

ax3.set_ylabel("")

st.pyplot(fig3)

# -------------------------------------------------
# GRAPH 4: Monthly Upload Trend
# -------------------------------------------------
st.header("Monthly Upload Trend")

df["month"] = df["published_at"].dt.month

fig4, ax4 = plt.subplots()

sns.countplot(x="month", data=df, ax=ax4)

ax4.set_xlabel("Month")
ax4.set_ylabel("Number of Videos")

st.pyplot(fig4)

# -------------------------------------------------
# Channel Filter
# -------------------------------------------------
st.header("Filter Videos by Channel")

selected_channel = st.selectbox("Select Channel", df["channel"].unique())

filtered_data = df[df["channel"] == selected_channel]

st.write("Filtered Videos")

st.write(filtered_data)