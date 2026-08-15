# Thiranex Virtual Internship – Task 01

## Data Cleaning & Visualization Project

This project is completed as part of my **Virtual Internship at Thiranex**.

The objective of this task is to work with a raw marketing campaign dataset, clean and preprocess the data, analyze customer behavior, and create visualizations to identify useful insights.

---

## Internship

**Organization:** Thiranex  
**Program:** Virtual Internship  
**Task:** Task 01  
**Project:** Data Cleaning & Visualization

---

## Project Objective

The main objective of this project is to understand the process of preparing raw data for analysis and presenting meaningful insights through visualizations.

The project focuses on:

- Loading a raw dataset
- Understanding the structure of the data
- Handling missing values
- Identifying and removing duplicate records
- Detecting and handling outliers
- Creating new useful features
- Performing exploratory data analysis
- Creating meaningful visualizations
- Identifying key findings from the dataset
- Saving the cleaned dataset

---

## Dataset

The project uses a **Marketing Campaign dataset** containing information about customers, their demographics, purchasing behavior, product spending, and responses to marketing campaigns.

The dataset includes information such as:

- Customer ID
- Year of Birth
- Education
- Marital Status
- Income
- Number of Children
- Product Purchases
- Website Purchases
- Store Purchases
- Catalog Purchases
- Marketing Campaign Responses

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

---

## Data Cleaning

The following preprocessing steps were performed:

### 1. Missing Values

Missing values in the `Income` column were identified and replaced using the median income value.

### 2. Duplicate Records

Duplicate rows were checked and removed where necessary.

### 3. Invalid Values

Invalid values such as negative income values were identified and removed.

### 4. Age Cleaning

Customer age was calculated from the birth year.

Unrealistic ages were removed from the dataset.

### 5. Outlier Detection

The Interquartile Range (IQR) method was used to identify outliers.

Outliers in income were handled using IQR-based capping.

---

## Feature Engineering

New columns were created to make the analysis more meaningful.

### Age

Customer age was calculated using the year of birth.

### Total Children

The number of children and teenagers in the household were combined.

### Total Spending

Spending across different product categories was combined into one column.

### Total Purchases

Purchases made through web, catalog, and store channels were combined.

---

## Data Visualization

Several visualizations were created using Matplotlib and Seaborn.

The project includes:

1. Customer Age Distribution
2. Customer Income Distribution
3. Total Spending by Product Category
4. Purchases by Sales Channel
5. Income vs Total Spending
6. Average Spending by Education Level
7. Average Spending by Marital Status
8. Average Spending by Number of Children
9. Marketing Campaign Response
10. Correlation Heatmap

These visualizations help understand customer behavior and marketing performance.

---

## Key Analysis

The analysis helps answer questions such as:

- What is the age distribution of customers?
- What is the income distribution?
- Which product category has the highest spending?
- Which purchasing channel is most popular?
- Does income have a relationship with customer spending?
- How does education level affect spending?
- How does marital status relate to spending?
- Does the number of children affect customer spending?
- What percentage of customers responded to the marketing campaign?
- Which numerical variables have strong correlations?

---

## Project Structure

```text
TASK 01/
│
├── TASK_001.py
├── README.md
├── archive/
│   └── marketing_campaign.csv
│
├── cleaned_marketing_campaign.csv
│
└── visualizations/
    ├── 01_age_distribution.png
    ├── 02_income_distribution.png
    ├── 03_product_spending.png
    ├── 04_purchase_channels.png
    ├── 05_income_vs_spending.png
    ├── 06_spending_by_education.png
    ├── 07_spending_by_marital_status.png
    ├── 08_spending_by_children.png
    ├── 09_campaign_response.png
    └── 10_correlation_heatmap.png
