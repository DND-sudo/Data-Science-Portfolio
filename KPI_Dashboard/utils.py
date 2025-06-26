def compute_kpis(df):
    revenue = df["Revenue"].sum()
    sales_count = len(df)
    avg_order_value = revenue / sales_count if sales_count > 0 else 0
    return {
        "revenue": revenue,
        "sales_count": sales_count,
        "avg_order_value": avg_order_value
    }

def filter_data(df, selected_categories, date_range):
    filtered = df[
        (df['Category'].isin(selected_categories)) &
        (df['Date'] >= pd.to_datetime(date_range[0])) &
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    return filtered

