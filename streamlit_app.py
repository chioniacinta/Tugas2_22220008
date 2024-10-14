import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Diabetes Dataset")
st.write("Data Overview")

# Membaca dataset diabetes
df_diabetes = pd.read_csv("./diabetes.csv", encoding="iso-8859-1")

# Menampilkan kolom untuk lebih memahami data
st.write("Dataset Columns: ", df_diabetes.columns.tolist())

# Memfilter dataset berdasarkan kelas 'Outcome' (0 = Tidak Diabetes, 1 = Diabetes)
df_filtered = df_diabetes[df_diabetes['Outcome'].isin([0, 1])]

# Menghitung jumlah kemunculan tiap kelas pada kolom 'Outcome'
outcome_counts = df_filtered['Outcome'].value_counts()

# Membuat DataFrame untuk visualisasi dan tabel
df_outcome_counts = pd.DataFrame(outcome_counts).reset_index()
df_outcome_counts.columns = ['Outcome', 'Count']

# Mengubah nilai 'Outcome' menjadi lebih deskriptif (0 -> Non-Diabetic, 1 -> Diabetic)
df_outcome_counts['Outcome'] = df_outcome_counts['Outcome'].replace({0: 'Non-Diabetic', 1: 'Diabetic'})

# Menampilkan tabel jumlah tiap kelas 'Outcome'
st.write("Class Counts Table")
st.dataframe(df_outcome_counts)

# Menampilkan dataset yang telah difilter
st.write("Filtered Dataset")
st.dataframe(df_filtere

#
# Bar Chart untuk Outcome
#
st.title("Bar Chart of Diabetes Outcome Classes")
st.bar_chart(df_outcome_counts.set_index('Outcome'))

st.markdown("---")