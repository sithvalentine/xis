# app.py
import streamlit as st
import plotly.express as px
import pandas as pd


def main():
    st.set_page_config(
        page_title="Xanadu Investment System",
        page_icon="📈",
        layout="wide"
    )

    st.title("Xanadu Investment System")

    # Sidebar
    st.sidebar.title("Investment Parameters")
    initial_investment = st.sidebar.number_input(
        "Initial Investment ($)",
        min_value=1000,
        max_value=1000000,
        value=50000
    )

    # Main content
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Portfolio Value",
            value=f"${initial_investment:,}",
            delta="Target: $1M"
        )

    with col2:
        # Sample data for pie chart
        data = {
            'Asset': ['Stocks', 'Bonds', 'Real Estate', 'Cash'],
            'Allocation': [60, 20, 15, 5]
        }
        fig = px.pie(data, values='Allocation', names='Asset')
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()