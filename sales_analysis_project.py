
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv", encoding='ISO-8859-1')

# Basic cleaning
df.dropna(subset=['Description', 'CustomerID'], inplace=True)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Add TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# --- 1. Top 10 Selling Products ---
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("Top 10 Selling Products:")
print(top_products)

# Plot Top 10 Products
top_products.plot(kind='barh', title='Top 10 Selling Products', figsize=(10,6), color='skyblue')
plt.xlabel('Quantity Sold')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# --- 2. Sales by Country ---
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Countries by Sales:")
print(country_sales)

country_sales.plot(kind='bar', title='Sales by Country', figsize=(10,6), color='orange')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_country.png")
plt.show()

# --- 3. Monthly Sales Trend ---
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend', figsize=(12,6), color='green')
plt.ylabel('Total Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# --- 4. Customer Spending Distribution ---
customer_spend = df.groupby('CustomerID')['TotalPrice'].sum()
print("\nTop 10 Customers by Spending:")
print(customer_spend.sort_values(ascending=False).head(10))

plt.figure(figsize=(8,6))
plt.hist(customer_spend, bins=100, color='purple')
plt.title('Customer Spending Distribution')
plt.xlabel('Total Spend')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig("customer_spending.png")
plt.show()
