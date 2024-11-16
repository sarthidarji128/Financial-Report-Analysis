# Financial Report Analysis

This Python project calculates and visualizes key financial ratios for a sample company across multiple years. The project aims to provide insights into the profitability and leverage of the company. Specifically, it computes the following financial ratios:

- **Leverage Ratio**: The ratio of total assets to net profit.
- **Profit Margin**: The percentage of revenue that turns into profit.
- **Return on Assets (ROA)**: The percentage of profit generated from total assets.
- **Return on Equity (ROE)**: The percentage of profit generated from equity.

These financial ratios are calculated and visualized in the form of line plots for each year in the sample dataset.

## Project Overview

### Goal
To analyze the financial performance of a sample company using key financial ratios and provide insights into profitability and leverage over a period of five years.

### Key Features
- Calculation of key financial ratios:
  - **Leverage Ratio**
  - **Profit Margin**
  - **Return on Assets (ROA)**
  - **Return on Equity (ROE)**
- Visualization of these ratios using `matplotlib` to better understand the financial performance.

---

## Libraries Used

This project uses the following Python libraries:

- **pandas**: For data manipulation, including creating DataFrames and performing calculations.
- **matplotlib**: For generating visualizations, such as line plots for financial ratios.

To install these libraries, use the following command:

```bash
pip install pandas matplotlib
```

---

## How to Run the Project

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/sarthidarji128/financial-report-analysis.git
cd financial-report-analysis
```

### 2. Install the Required Libraries

Once you've cloned the repository, install the required Python libraries by running:

```bash
pip install pandas matplotlib
```

### 3. Running the Python Script

After installing the necessary libraries, run the Python script to generate financial ratio calculations and visualizations:

```bash
python financial_report.py
```

### 4. Output

The script will display a table showing the financial ratios and generate four line plots for each of the financial ratios:

- **Leverage Ratio**
- **Profit Margin (%)**
- **Return on Assets (%)**
- **Return on Equity (%)**

These graphs will help in visualizing the performance over a period of time (from 2018 to 2022 in this example).

---

## Example Output

### Financial Ratios Table

| Year | Revenue (INR Lakhs) | Net Profit (INR Lakhs) | Total Assets (INR Lakhs) | Leverage Ratio | Profit Margin (%) | Return on Assets (%) | Return on Equity (%) |
|------|---------------------|------------------------|--------------------------|----------------|-------------------|----------------------|----------------------|
| 2018 | 500                 | 50                     | 2000                     | 40             | 10.00             | 2.50                 | 10.00                |
| 2019 | 800                 | 70                     | 2500                     | 35.71          | 8.75              | 2.80                 | 8.75                 |
| 2020 | 1200                | 150                    | 3000                     | 20             | 12.50             | 5.00                 | 12.50                |
| 2021 | 1500                | 200                    | 3500                     | 17.5           | 13.33             | 5.71                 | 13.33                |
| 2022 | 1800                | 250                    | 4000                     | 16             | 13.89             | 6.25                 | 13.89                |

### Example Plots

- **Leverage Ratio**: Shows the relationship between total assets and net profit over the years.
- **Profit Margin (%)**: Displays the percentage of revenue that is converted into profit.
- **Return on Assets**: Displays how effectively the company uses its assets to generate profit.
- **Return on Equity**: Shows the return generated from the equity invested in the company.

---

## Example Screenshot of Output

Here is the screenshot showing the output of the financial analysis and visualizations:

![Output Screenshot](https://github.com/user-attachments/assets/3784dcc2-e19e-4487-a123-786b7e31c903)

---

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---
