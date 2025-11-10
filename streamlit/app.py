import streamlit as st
import pandas as pd

st.set_page_config(page_title="Análise de Vendas", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("vendas_produtos_limpo.csv")
    df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
    return df

df = load_data()

st.title("Análise de Vendas — Atividade Prática")

# Indicadores simples
col1, col2, col3 = st.columns(3)
col1.metric("Qtd vendida", int(df["quantidade"].sum()))
col2.metric("Faturamento (R$)", f"{df['valor_total'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col3.metric("Ticket médio (R$)", f"{df['valor_total'].mean():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Gráficos
st.subheader("Faturamento por categoria (R$)")
fat_cat = df.groupby("categoria")["valor_total"].sum().reset_index().sort_values("valor_total", ascending=False)
st.bar_chart(fat_cat.set_index("categoria"))

st.subheader("Evolução do faturamento por data (R$)")
fat_dia = df.groupby("data_venda")["valor_total"].sum().reset_index().sort_values("data_venda")
st.line_chart(fat_dia.set_index("data_venda"))
