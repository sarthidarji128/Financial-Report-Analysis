import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": ["2018", "2019", "2020", "2021", "2022"],
    "Revenue (INR Lakhs)": [500, 800, 1200, 1500, 1800],
    "Net Profit (INR Lakhs)": [50, 70, 150, 200, 250],
    "Total Assets (INR Lakhs)": [2000, 2500, 3000, 3500, 4000]
}

df = pd.DataFrame(data)
df["Leverage Ratio"] = df["Total Assets (INR Lakhs)"] / df["Net Profit (INR Lakhs)"]
df["Profit Margin (%)"] = (df["Net Profit (INR Lakhs)"] / df["Revenue (INR Lakhs)"]) * 100
df["Return on Assets (%)"] = (df["Net Profit (INR Lakhs)"] / df["Total Assets (INR Lakhs)"]) * 100
df["Return on Equity (%)"] = (df["Net Profit (INR Lakhs)"] / df["Revenue (INR Lakhs)"]) * 100
print(df)

fig, ax = plt.subplots(2, 2, figsize=(12, 10))
ax[0, 0].plot(df["Year"], df["Leverage Ratio"], marker='o', color='b', label='Leverage Ratio')
ax[0, 0].set_title('Leverage Ratio')
ax[0, 0].set_xlabel('Year')
ax[0, 0].set_ylabel('Leverage Ratio')
ax[0, 0].grid(True)
ax[0, 1].plot(df["Year"], df["Profit Margin (%)"], marker='o', color='g', label='Profit Margin')
ax[0, 1].set_title('Profit Margin (%)')
ax[0, 1].set_xlabel('Year')
ax[0, 1].set_ylabel('Profit Margin (%)')
ax[0, 1].grid(True)
ax[1, 0].plot(df["Year"], df["Return on Assets (%)"], marker='o', color='r', label='Return on Assets')
ax[1, 0].set_title('Return on Assets (%)')
ax[1, 0].set_xlabel('Year')
ax[1, 0].set_ylabel('Return on Assets (%)')
ax[1, 0].grid(True)
ax[1, 1].plot(df["Year"], df["Return on Equity (%)"], marker='o', color='purple', label='Return on Equity')
ax[1, 1].set_title('Return on Equity (%)')
ax[1, 1].set_xlabel('Year')
ax[1, 1].set_ylabel('Return on Equity (%)')
ax[1, 1].grid(True)
plt.tight_layout()
plt.show()
