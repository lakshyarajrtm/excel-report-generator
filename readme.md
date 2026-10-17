# CSV Sales Report Generator

A Python automation tool that converts raw sales data from a CSV file into a clean PDF report. It validates and cleans the input data, calculates useful business metrics, creates charts, and records rows that could not be processed.

This is a personal portfolio project designed to demonstrate practical skills in Python scripting, data processing, validation, visualization, and PDF generation.

## Features

- Loads sales data from a CSV file
- Normalizes and maps common alternative column names
- Detects missing required columns
- Cleans invalid dates and numeric values
- Calculates revenue when it is not provided
- Produces sales totals and product-level summaries
- Creates revenue charts using Matplotlib
- Generates a professional PDF report
- Saves cleaned data and rejected rows separately
- Provides clear error messages for invalid input

## Expected Input

The input CSV should contain the following information:

| Field | Description | Accepted examples |
|---|---|---|
| Date | Date of the sale | `Date`, `Sale Date`, `Order Date` |
| Product | Product or item name | `Product`, `Product Name`, `Item` |
| Quantity | Number of units sold | `Quantity`, `Qty`, `Units` |
| Unit Price | Price of one unit | `Unit Price`, `Price`, `Rate` |
| Revenue | Total sale amount; optional if quantity and unit price are present | `Revenue`, `Sales`, `Amount`, `Total` |

Example:

```csv
Date,Product,Quantity,Unit Price,Revenue
2026-10-01,Laptop,2,60000,120000
2026-10-02,Mouse,10,1500,15000
2026-10-03,Keyboard,5,4000,20000
```

The program normalizes column names before processing them. For example, `Order Date`, `Item`, `Qty`, and `Amount` can be mapped to the standard internal fields.

## Generated Report

The PDF report includes:

- Reporting period
- Total revenue
- Total units sold
- Number of transactions
- Average transaction value
- Best-selling product
- Highest-revenue product
- Product summary table
- Revenue by product chart
- Revenue over time chart
- Data-quality summary

## Output Files

Each run creates files similar to the following:

```text
output/
├── sales_report.pdf
├── cleaned_sales.csv
├── rejected_rows.csv
├── revenue_by_product.png
└── revenue_over_time.png
```

Invalid records are not silently discarded. They are written to `rejected_rows.csv` with a reason so they can be reviewed and corrected.


## Requirements

- Python 3.10 or newer
- pandas
- matplotlib
- reportlab

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/your-username/csv-sales-report.git
cd csv-sales-report
```

Create and activate a virtual environment:

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the report generator with a CSV file:

```bash
python generate_report.py sample_data/sales.csv
```

Choose a different output directory:

```bash
python generate_report.py sample_data/sales.csv --output output/
```

Display command-line help:

```bash
python generate_report.py --help
```

## Data Validation

The program checks for:

- Empty input files
- Missing required columns
- Unrecognized column names
- Missing products or dates
- Invalid dates
- Non-numeric quantities, prices, or revenue
- Negative quantities or monetary values
- Revenue values that do not match `quantity × unit price`
- Files with no valid rows remaining

Example error:

```text
Error: A product column could not be found.
Accepted names: product, product_name, item
```

## Possible Future Improvements

- Support Excel `.xlsx` files
- Add a graphical file-selection interface
- Allow users to map unknown columns manually
- Add expense and inventory report templates
- Support custom branding and company logos
- Package the application as a Windows executable

## Privacy

The tool processes files locally. It does not upload sales data to an external service.

## Author

Lakshyaraj Singh Rathore  
Python Automation and Applied AI Developer

## License

This project is available under the MIT License.
